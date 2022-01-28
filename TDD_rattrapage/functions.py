
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
	if len(float_list) <= 1:
		return -1
	float_list_derivee = []
	for i in range (len(float_list)-1):
		float_list_derivee.append(float_list[i+1] - float_list[i])
	return float_list_derivee

def derivee_seconde(float_list):
	float_list_derivee = derivee(float_list)
	if float_list_derivee == -1:
		return -1
	float_list_derivee_seconde = (derivee(float_list_derivee))
	return float_list_derivee_seconde