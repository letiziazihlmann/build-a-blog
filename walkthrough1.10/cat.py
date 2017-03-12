#verbs are going to become methods
#A cat has-a
    #Tail lenght - float/in
    #Color - string*
    #Fur/fur lenght - float/int
    #smell - string
    #name - string*
    #breed - string
    #number of legs - int
    #isMale - boolean*
    #meow - string*
    #position - point (user-defined type)
    #age - int

#Cat can-do
    #jump(height)
    #sleep(duration)*
    #run(distance)
    #hunt(prey)*
    #play(toy)
    #purr()
    #meow()*
    #eat(food)
    #age(age)

class Cat:

    def __init__(self, name, color, meow, isMale):
        self.color = color
        self.name = name
        self.meow = meow
        self.isMale = isMale
        self.age = 0

    def sleep(self, duration):
        print(self.name + "slept for " + str(duration) + " minutes!")

    def getOlder(self):
        self.age += 1

    def makeMeow(self):
        print(self.name + " says " +self.meow)

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName
        print(self.name)

franklin = Cat("franklin", "orange", "meeeoww", True)
franklin.sleep(60)
franklin.makeMeow()
sally = Cat("Sally", "blue", "moeoawy", False)
sally.makeMeow()
sally.setName('sammy')
nori = Cat("Nori", "grey", "meeoooooooow", True)
nori.makeMeow()
