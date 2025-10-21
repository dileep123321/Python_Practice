#basic class example
class Name:
    Name = "Dileep"
obj = Name()
print(obj.Name)

#basic class with method example
class MyFrnd:
    MyFrnd = "Bahar"
    
    def frnd_name(self):
        print(self.MyFrnd)
        print("is my best friend")
obj1 = MyFrnd()
obj1.frnd_name()

#using __init_ method
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
student1 = Student("Dileep", 23, "A")

#Accessing attributes and methods
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def get_movie_info(self):
        return f"{self.title} directed by {self.director} released in {self.year}"
    
movie1 = Movie("Inception", "Christopher Nolan", 2010)
print(movie1.get_movie_info())