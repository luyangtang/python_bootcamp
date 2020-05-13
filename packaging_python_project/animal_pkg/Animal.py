class PetException(Exception):
    
    pass


class Animal(object):

    def __init__(self, _type, _colour, _sound, _isPet = False):

        self.type = _type
        self.colour = _colour
        self.sound = _sound
        self.isPet = _isPet

        self.adopted = False
    

    def adopt(self, name = None):

        if not self.isPet:

            raise PetException

        else:

            self.name = name
            self.adopted = True

            print('%s is adopted' % (self.name if self.name else self.type))

