class Student:

    def __init__(self):
        self.name="Pandit"
        self.rollno=19
        self.address="Pune"

    def __str__(self):
        return f'{self.name},{self.rollno},{self.address}'

    def talk(self):
        print("Hello I am:",self.name)
        print("my rollno:",self.rollno)
        print("and address is:",self.address)

s=Student()
print(s.name)
print(s.__str__())
s.talk()
