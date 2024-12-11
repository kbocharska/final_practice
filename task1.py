import argparse

parser = argparse.ArgumentParser("Cars in the garage")

parser.add_argument("-add",
                    nargs = 3,
                    metavar = ("license_plate", "make", "year"),
                    help = "Enter the licence plate, mark and year of production of the car")

parser.add_argument("-view",
                    nargs = 1,
                    metavar = "license_plate",
                    help = "Enter the licence plate of the car that you want to find")



args = parser.parse_args()



class Car:
    def __init__(self, licence, make, year):
        self.l_plate = licence
        self.make = make
        self.year = int(year)


class Garage:
    def __init__(self):
        self.cars = {}

    def add_car(self, license_plate, make, year):
        self.cars[license_plate] = Car(license_plate, make, year)
        print(f"Car with license plate {license_plate} added/updated successfully.")

    def view_car(self, licence_plate):
        if licence_plate in self.cars:
            print(f"{self.cars[licence_plate].make} ({self.cars[licence_plate].year})")
        else:
            print("there's no such car")

garage = Garage()

if args.add:
        garage.add_car(args.add[0], args.add[1], args.add[2])
elif args.view:
        garage.view_car(args.view[0])




