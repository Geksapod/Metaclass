

file_name = "Metaclass_and_fields.txt"


class MetaClassUse(type):

    @classmethod
    def write_class(mcs, classname, classdict):

        with open(file_name, "a") as f:
            f.write(f"Class name = {classname}, ")
            f.write(f"List of fields = {[key for key in classdict]}")
            f.write("\n")

    def __new__(mcs, classname, supers, classdict):

        MetaClassUse.write_class(classname, classdict)

        return type.__new__(mcs, classname, supers, classdict)


class Person(metaclass=MetaClassUse):
    """
    This is a class to represent a person.


    """

    def __init__(self, surname, name, id_number):


        self.surname = surname
        self.name = name
        self.id_number = id_number

    def __str__(self):

        return f"{self.surname} {self.name}"
