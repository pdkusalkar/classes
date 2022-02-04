class Employee:
    def __init__(self,name,number,address):
        self.ename=name
        self.eno=number
        self.eadd=address

    def __str__(self):
        return f'{self.ename},{self.eno},{self.eadd}'

e=Employee("Pandit",11,"Pune")
e1=Employee("Pratiksha",12,"Pune1")
print(e)
print(e1)