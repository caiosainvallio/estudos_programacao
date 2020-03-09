def fizzbuzz(num):
	if num % 3 == 0 and num % 5 == 0:
		r = 'FizzBuzz'
	else:
		if num % 3 == 0:
			r = 'Fizz'
		else:
			if num % 5 == 0:
				r = 'Buzz'
			else:
				r = num
	return r



	



	



	
