class Family:
    def __init__(self, mother, father, son, daughter, address, telephone_number):
        self.mother = mother
        self.father = father
        self.son = son
        self.daughter = daughter
        self.address = address
        self.telephone_number = telephone_number

    def getInfo(self):
            print "Mother:", self.mother, "\n", "Father:", self.father, "\n", "Son:", self.son, "\n", "Daughter:", self.daughter, "\n", "Address:", self.address, "Telephone:", self.telephone_number

    def pet(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

        print "Name:" , self.first_name, "\n", "Last name:", self.last_name, "\n", "Gender:", self.gender




class User(object):
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def displayInfo(self):
        print  "First name:", self.first_name ,"\n", "Last name:", self.last_name ,"\n", "Gender:" , self.gender


class Person(User):
    def __init__(self, first_name, last_name, gender):
        super(Person, self).__init__(first_name, last_name, gender)


class Pet(User):
        def __init__(self, first_name, last_name, gender):
             super(Pet, self).__init__(first_name, last_name, gender)








 def main():

family = Family("Anna", "Armen", "Karen", "Nina",  "Baghramyan", 354687)
family.getInfo()
pet = Pet ("..", "....", "......")




main()


