import unittest
from animal_pkg.Animal import Animal, PetException


class AnimalTest(unittest.TestCase):

    def test_animal_adopt(self):

        tiger = Animal('Tiger', 'White', 'Roar')
        self.assertRaises(PetException, tiger.adopt)
    
        dog = Animal('Dog', 'Brown', 'Bark Bark', True)
        dog.adopt()
        self.assertTrue(dog.adopted)



if __name__ == '__main__':

    unittest.main()