class Luhn(object):
	def __init__(self, card_num):
		self.card_num = card_num

	def is_valid(self):
		sum = 0
		odd = False
		for x in self.card_num[::-1]:
			if str.isdigit(x):
				if odd == False:
					odd = True
					sum += int(x)
				else:
					odd = False
					if int(x) * 2 > 9:
						sum += int(x) * 2 - 9
					else:
						sum += int(x) * 2
			elif x != " ":
				return False

		if sum == 0 and len(self.card_num) < 3:
			return False

		return sum % 10 == 0