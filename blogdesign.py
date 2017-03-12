class Post():
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    def like(self):
        self.likes += 1

    def __str__(self):
        return self.title + " by " + self.author


class VideoPost(Post):
    def __init__(self, title, author, url):
        super().__init__(title, author, None)
        self.video_url = url
        self.plays = 0

    def play(self):
        self.plays += 1

    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + " URL: " + self.video_url + " Likes: " + str(self.likes) +" Play: " + str(self.plays)

class ImagePost(Post):
    def __init__(self, title, author, file_name):
        super().__init__(title, author, None)
        self.file_name = file_name

    def __str__(self):
        return "File Name: " + self.file_name

class LinkPost(Post):
    def __init__(self, title, author, url_linked):
        super().__init__(title, author, None)
        self.url_linked = url_linked
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def __str__(self):
        return "Clicks: " + str(self.clicks)

samplePost = Post("Dogs", "LZ", "Puppies")
print(samplePost)
sampleVideo = VideoPost("Dog Video", "LZ", "www.dogs.com")
print(sampleVideo)

samplePost.like()
sampleVideo.like()

print(sampleVideo)

sampleLinkPost = LinkPost('The Who', "LZ", "www.facebook.com")
sampleImagePost = ImagePost("Mountains", "LZ", "mountains.jpeg")

print(sampleLinkPost)
print(sampleImagePost)

plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")
pic_post = ImagePost("Cats in space", "Crystal Martin", "spacecats.gif")
url_post = LinkPost("LaunchCode's LC101", "LaunchCode Staff", "https://www.launchcode.org/lc101")

vid_post.play()
vid_post.play()
url_post.click()

print(vid_post)
print(plain_post)
print(url_post)
print(pic_post)
