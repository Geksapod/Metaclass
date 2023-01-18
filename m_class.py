

file_name = "Metaclass_and_fields.txt"


class MetaClassUse(type):

    def __new__(typeclass, classname, supers, classdict):

        with open(file_name, "r+") as f:
            if classname not in f:
                f.write(f"Class name = {classname}, ")
                f.write(str([key for key in classdict]))
                f.write("\n")

        return type.__new__(typeclass, classname, supers, classdict)


class Person(metaclass=MetaClassUse):

    def __init__(self, surname, name, id_number):

        self.surname = surname
        self.name = name
        self.id_number = id_number

    def __str__(self):

        return f"{self.surname} {self.name}"



