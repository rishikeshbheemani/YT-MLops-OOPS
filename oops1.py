#initialize a class
class Employee:
    #constructor
    def __init__(self):
        print("Started execting attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("this travle method was called manually ")
        print(f"Employee is travelling to {destination}")

#create an object/instance of the class
sam = Employee()
#print sam id
print(sam.id)
sam.travel("Kerala")