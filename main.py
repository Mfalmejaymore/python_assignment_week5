# for random prices
import random

# root class (main one)

class vahicle:
	_power = 300 # private
	wheels = 0
	cost = 20000

	def __init__(self,power,wheels):
		self._power = power
		self.wheels = wheels

class car(vahicle):
	make = "toyota"

	def __init__(self,make,hp):
		self.make = make;
		self._power = hp
		self.wheels = 4
		self.cost = random.randint(500000,1200000)

	def move(self):
		return "drive"

	def getpower(self):
		res = f"{self._power} HorsePower"
		return res

class bike(vahicle):
	make = "ducati"

	def __init__(self,make,cc):
		self.make = make
		self._power = cc
		self.wheels = 2
		self.cost = random.randint(120000,500000)

	def move(self):
		return "ride"

	def getpower(self):
		res = f"{self._power} CCs"
		return res

class plane(vahicle):
	make = "ducati"

	def __init__(self,make,thrust):
		self.make = make
		self._power = thrust
		self.wheels = 16
		self.cost = random.randint(50000000,120000000)

	def move(self):
		return "Fly"

	def getpower(self):
		res = f"{self._power} kiloNewtons of Thrust"
		return res

my_car = car("BMW",250);
my_bike = bike("Honda",200);
my_plane = plane("Cessna",89)

loopme = True
wanted = ""

# loop until a valid response is given
while loopme:
	wanted = input("you have a car, a bike and a plane. which one do you want information on (none to opt out)? ")

	if wanted == "car" or wanted == "bike" or wanted == "plane" or wanted == "none":
		loopme = False;
	else:
		print("invalid input, try again")


if wanted != "none":
	print(f"showing info on your {wanted}\n")

	if wanted == "car":
		my_ve = my_car
	elif wanted == "bike":
		my_ve = my_bike
	else:
		my_ve = my_plane

	lines = []
	lines.append(f"make: {my_ve.make}");
	lines.append(f"wheels: {my_ve.wheels}")
	lines.append(f"movement type: {my_ve.move()}")
	lines.append(f"power: {my_ve.getpower()}\n")
	lines.append(f"and you bought it for ksh {my_ve.cost:,}\n")

	outdata = "\n".join(lines)

	print(outdata)

	# practise with error handling and files
	saveinfo = input("would you like to save to the data file (Y/N): ");

	if saveinfo == "y" or saveinfo == "Y":
		try:
			fname = "savedinfo.txt"
			thefile = open(fname,"w")

			with thefile:
				thefile.write(outdata)

			print("data written successfully")
		except:
			print("error writing the file")

	print("okay, have a good day")
else:
	print("okay, have a good day though")
