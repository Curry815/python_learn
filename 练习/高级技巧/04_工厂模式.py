from multiprocessing.pool import worker


class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class PersonFactory:
    def create_person(self,type):
        if type == 'w':
            return Worker()
        elif type == 's':
            return Student()
        else:
            return Teacher()

pf = PersonFactory()
worker = pf.create_person("w")
stu = pf.create_person("s")
teacher = pf.create_person("t")