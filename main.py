import m_class as ms

if __name__ == "__main__":

    class A(metaclass=ms.MetaClassUse):
        pass

    person_1 = ms.Person("Petrenko", "Petro", 112233)

    print(person_1)
    print(ms.Person.__dict__.keys())
    print(ms.MetaClassUse.__dict__.keys())