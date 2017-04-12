#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    #takes a file name and extra paramaters, basically renders the template we create
    def render_str(self, template , **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    # takes templates and calls the above function but wrapped in write so it actaully writes in the browser
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class BlogPosts(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add = True)

class MainHandler(Handler):

    def render_base(self):
        blogposts = db.GqlQuery("SELECT * FROM BlogPosts ORDER BY created DESC LIMIT 5")
        self.render('mainpage.html', blogposts=blogposts)

    def get(self):
        self.render_base()


class BlogHandler(Handler):

    def render_base(self, title="", body="", error=""):

        self.render('newpost.html', title=title, body=body, error=error)

    def get(self):
        self.render_base()

    def post(self):
        title = self.request.get('title')
        body = self.request.get('body')

        if title and body:
            b = BlogPosts(title=title, body=body)
            b.put()

            self.redirect('/blog')
        else:
            error = "Please enter both a title and body!"
            self.render_base(title, body, error)


app = webapp2.WSGIApplication([
    ('/blog', MainHandler),
    ('/newpost', BlogHandler)
], debug=True)
