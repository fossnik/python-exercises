import random
import string


def namegenerate():
	letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
	digits = ''.join(random.choice(string.digits) for _ in range(3))
	return letters + digits


class Robot(object):
	name = ""

	def __init__(self):
		self.name = namegenerate()

	def getname(self):
		return self.name

	def reset(self):
		self.name = Robot().getname()
