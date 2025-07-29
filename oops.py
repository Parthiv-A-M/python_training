"""
class person:
    def print_name(self,name):
        print("My name is "+name)
    def add(self,a,b):
        return a-b
person = person()
person.print_name("aarthi")
result = person.add(3,5)
print(result)"""
"""
class City:
    def addCityDetails(self,name,country):
        self.name = name 
        self.country = country
    def printCityDetails(self):
        print("City name:" + self.name)
        print("Country:" + self.country)
delhi = City()
delhi.addCityDetails("delhi","India")
delhi.printCityDetails()
mumbai = City()
mumbai.addCityDetails("mumbai","India")
mumbai.printCityDetails()
salem = City()
salem.addCityDetails("new york","India")
salem.printCityDetails()"""
class Person():
    CityName = "mumbai"
    def printName(self,name):
        print(name)
class Aarthi(Person):
    def printDetail(self):
        print("some message")
obj = Aarthi()
obj.cityName = "london"
obj.printName("Aarthi")