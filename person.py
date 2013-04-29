# person.py

class Person:
    """ person super class """
    def __init__(self, pid, name):
        """ constructor for person """
        self.__pid = pid
        self.__name = name

    def get_pid(self):
        """ accessor for person id """
        return self.__pid

    def get_name(self):
        """ accessor for name """
        return self.__name

    def display(self):
        """ support/helper to show person info """
        print("ID:", self.__pid)
        print("Name:", self.__name)


class Student(Person):
    """ student subclass """
    def __init__(self, pid, name, classid):
        """ constructor for student """
        super().__init__(pid, name)
        self.__classid = classid

    def get_classid(self):
        """ accessor for student class """
        return self.__classid

    def set_classid(self, new_classid):
        """ modifier/mutator for student class """
        self.__classid = new_classid

    def display(self): # overriding
        """ support/helper to show student info """
        super().display()
        print("Class:", self.__classid)


class Staff(Person):
    """ staff subclass """
    
    def __init__(self, pid, name, department):
        """ constructor for staff """
        super().__init__(pid, name)
        self.__department = department

    def get_department(self):
        """ accessor for staff department """
        return self.__department

    def set_department(self, new_department):
        """ modifier/mutator for staff department """
        self.__department = new_department

    def display(self): # overriding
        """ support/helper to show staff info """
        super().display()
        print("Department:", self.__department)


# main
# instantiate student and staff objects
student1 = Student("S01", "Lim Ah Seng", "13Y5C23")
staff1 = Staff("A05", "Robert Yeo", "Computing")

person_list = []
person_list.append(student1)
person_list.append(staff1)
for person in person_list:
    person.display() # polymorphism


