
def mirror(str_input,nb):
	# check if nb is a integer
	if isinstance(nb,float):
		return -1

	# check if integer is not > to the str_input. 
	if (nb > len(str_input)):
		return -1

	#check if integer is not negatif
	if (nb < 0):
		return -1

	return_string = str_input[:nb+1]
	inverse_string = return_string
	
	while nb != 0:
		return_string += inverse_string[nb]
		nb -= 1
	#last iter for nb = 0
	return_string += inverse_string[nb]
	return return_string


#f'= [f(n+1) - f(n)]/h
#on fix l'interval h = 1
def derivee(float_list):
	return -1
