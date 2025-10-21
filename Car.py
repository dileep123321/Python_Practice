class Car:
    def __init__(self, Brand, Model, Year):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year

    def get_Car_Brand(self):
        return f"Car Brand is {self.Brand}"

    def get_Car_Model(self):
        return f"Car Model is {self.Model}"

    def get_Car_Year(self):
        return f"Car Year is {self.Year}"

    def get_Car_Details(self):
        return f"Car Details: {self.Brand} {self.Model} {self.Year}"


Car_obj1 = Car("Toyota", "GR Supra", 2019)
Car_obj2 = Car("Ford", "Mustang", 2021)

print(Car_obj1.get_Car_Brand())
print(Car_obj1.get_Car_Model())
print(Car_obj1.get_Car_Year())
print(Car_obj1.get_Car_Details())

print(Car_obj2.get_Car_Brand())
print(Car_obj2.get_Car_Model())
print(Car_obj2.get_Car_Year())
print(Car_obj2.get_Car_Details())