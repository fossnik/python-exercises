def is_armstrong(number):
	power = len(str(number))
	summ = 0

	for c in str(number):
		summ += pow(int(c), power)

	return summ == number