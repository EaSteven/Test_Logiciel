import math
import sympy

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
def derivee(float_list,h):
	if len(float_list) <= 1:
		return -1
	if h <= 0:
		return -1

	float_list_derivee = []
	for i in range (len(float_list)-1):
		float_list_derivee.append((float_list[i+1] - float_list[i])/h)
	return float_list_derivee

def derivee_seconde(float_list,h):
	float_list_derivee = derivee(float_list,h)
	if float_list_derivee == -1:
		return -1
	float_list_derivee_seconde = (derivee(float_list_derivee,h))
	return float_list_derivee_seconde


def approx_derivee(fonction,point,ordre_de_grandeur): 
	if (point == 0):
		if(input("dérivée en 0. Avez vous demandé une dérivée en 0? : [y/n]") == 'y'):
			return False
	
	try:
		h = 0.001
		val_approx = (fonction(point+h)-fonction(point))/h 
	except(ZeroDivisionError,ValueError):
		return False	
	
	arrondi =round(val_approx,ordre_de_grandeur)
	return arrondi
