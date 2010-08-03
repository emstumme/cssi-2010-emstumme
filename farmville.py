# farmville

class Animal(object):
    """describes an animal"""

    def __init__(self, name, sound):
        """every animal has a name"""
        self.name = name
        self.sound = sound

    def __str__(self):
        """print the name for the animal"""
        return self.name

    def get_name(self):
        """return the animal's name"""
        return self.name
    
    def get_sound(self):
        """return the sound the animal makes"""
        return self.sound

class Cow(Animal):
    """cows are animals"""

    def __init__(self, name, milk):
        """every cow has a name"""
        super(Cow, self).__init__(name, "mooooo")
        self.milk - milk

    def get_milk(self):
        return self.milk

class Spider(Animal):
    """spiders are animals too"""

    def __init__(self, name, message):
        """every spider has a name and a message"""
        super(Spider,self).__init__(name, "tchk tchk")
        self.message = message

        def get_message(self)
            return self.message
        
        

