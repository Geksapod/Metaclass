"""This module provide access to MetaClassUse and Person classes."""

file_name = "Metaclass_and_fields.txt"


class MetaClassUse(type):
    """This is the metaclass used to write name of class used this metaclass and its fields in txt file."""

    @staticmethod
    def write_class(classname, classdict):
        """
        Static method used to write name of class used this metaclass and its fields in txt file.

        :param classname: Name of the class used this metaclass.
        :param classdict: Dictionary of fields of the class used this metaclass.
        """

        with open(file_name, "a") as f:
            f.write(f"Class name = {classname}, ")
            f.write(f"List of fields = {[key for key in classdict]}")
            f.write("\n")

    def __new__(mcs, classname, supers, classdict):

        MetaClassUse.write_class(classname, classdict)
        return type.__new__(mcs, classname, supers, classdict)


class Person(metaclass=MetaClassUse):
    """This is a class to represent a person."""

    def __init__(self, surname, name, id_number):
        """Initialisation of the attributes of the class Person."""

        self.surname = surname
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"{self.surname} {self.name}"
