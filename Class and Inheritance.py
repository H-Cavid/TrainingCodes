class User:
    def __init__(self,firstname,surname):
        self.fname=firstname
        self.surname=surname
    def showData(self):
        print("My name is:",self.fname, "and my surname is:",self.surname,"and my gradition year is:",self.graditionyear)
class Student(User):
    def __init__(self,firstname,surname,year):
        super().__init__(firstname,surname)
        self.graditionyear=year
    def Welcome(self,):
        print("Welcome",self.fname,self.surname,"what is your gradition year?","My gradition year is:",self.graditionyear,end=" ")
x=Student("Cavid","Hesenov",2019)
print(x.Welcome())

