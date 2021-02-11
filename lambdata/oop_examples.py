import pandas as pd 
import numpy as np 

class BareMinimumClass:
	pass
	# __init__(self, X, Y):
	# self.x = X
	# self.y = Y

class Complex:
	def __init__(self, realpart, imaginarypart):
		"""
			Constructor for complex numbers,
			Part real and part imaginary
		"""
		self.r = realpart
		self.i = imaginarypart

	def add(self, other_complex):
		self.r += other_complex.r
		self.i += other_complex.i

	def __repr__(self):
		return '({}, i{})'.format(self.r, self.i)

class SocialMediaUser:
	def __init__(self, name, location, upvotes = 0):
		self.name = name
		self.location = location
		self.upvotes = upvotes

	def receive_upvotes(self, num_upvotes=100):
		self.upvotes += num_upvotes

	def is_popular(self):
		return self.upvotes > 100

	def __repr__(self):
		return "Here's {} and they're at {}".format(self.name, self.location)


class Animal:
	def __init__(self, name, weight, location, diet_type, poisonous):
		self.name = name
		self.weight = weight
		self.location = location
		self.diet_type = diet_type
		self.poisonous = poisonous

	def run(self, pace):
		return 'Going at speed ' + str(pace)

	def eat(self, food):
		return 'Delicious ' + str(food)



class Sloth(Animal):
	def __init__(self, name, weight, locaiton='Earth', diet_type='berries', poisonous=True, naps):
		super().__init__(name, weight, locaiton, diet_type, poisonous)
		self.naps = naps


	def say_something(self):
		return "This is a sloth of typing"


	def run(self):
		return "I'm slow as shit"

if __name__ == "__main__":
	user1 = SocialMediaUser('Carl', 'Benin', 58)
	user2 = SocialMediaUser('Benny', 'California', 67)
	user3 = SocialMediaUser('Dolly', 'Atlanta', 167)
	user4 = SocialMediaUser('George', 'Djibouti', 16)

	print("name: {}, is popular: {}, location: {}".format(user1.name, user1.is_popular(), user1.location))
	user1.receive_upvotes(101)
	print("name: {}, is popular: {}, location: {}".format(user1.name, user1.is_popular(), user1.location))


