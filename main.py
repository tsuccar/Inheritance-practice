from turtle import Turtle, Screen
from random import randint, choice
from time import sleep

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class Car(Turtle):
	def __init__(self, speed):
		# This line creates a turtle and assigns it to "self"!
		#   almost as if you had written self = Turtle()
		super().__init__()
		self.pu()
		self.shape("square")
		self.resizemode("user")
		self.shapesize(stretch_len=2)
		self.setheading(180)
		self.color(choice(COLORS))
		# self.goto(randint(300, 1300),randint(-250, 250))
		self.setx(randint(300, 1300))
		self.sety(randint(-250, 250))
		self.move_distance = speed
	
	def move(self):
		self.fd(self.move_distance)


screen = Screen()
screen.setup(width=600, height=600)

# create the car objects
car_1 = Car(20)
car_2 = Car(30)


# move the cars
while True:
	sleep(0.6)
	car_1.move()
	car_2.move()
	print(car_1.position())

# # create 20 car objects
# screen.tracer(0)
# cars = []
# for _ in range(20):
# 	cars.append(Car(randint(10, 30)))
#
# # move the cars
# while True:
# 	screen.update()
# 	sleep(0.2)
# 	for car in cars:
# 		car.move()
#
#############################################################
# With Call manager - managing the turtle inheritance objects
#############################################################
# class CarManager:
# 	def __init__(self):
# 		self.cars = []
#
# 	def create_cars(self, quantity):
# 		for _ in range(quantity):
# 			new_car = Car(randint(10, 30))   # Turtle inherited Class created this object
# #         new_car = Turtle()               # not <<this< the actual Turtle() class
# 			self.cars.append(new_car)
#
# 	def move_cars(self):
# 		for car in self.cars:
# 			car.move()
#
#
# screen = Screen()
# screen.setup(width=600, height=600)
#
# screen.tracer(0)
# car_manager = CarManager()
# car_manager.create_cars(20)
#
# # # move the cars
# while True:
# 	screen.update()
# 	sleep(0.2)
# 	car_manager.move_cars()
