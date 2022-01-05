import statistics
def get_mean(tab_int=[]):
	tab_sum=0
	for value in tab_int:
		tab_sum +=value
	return tab_sum//len(tab_int)

def min_int(a,b):
	if a<b:
		return a
	else:
		return b

def get_mediane(tab_int):
	return statistics.median(tab_int)

def get_ecart_type(tab_int):
	return round(statistics.pstdev(tab_int),2)

def is_Arithm(tab_int):
	raison = tab_int[1]-tab_int[0]
	for i in range (len(tab_int)-1):
		if (tab_int[i+1]-tab_int[i] != raison):
			return False
	return True		

def is_Géo(tab_int):
	raison = tab_int[1]/tab_int[0]
	for i in range (len(tab_int)-1):
		if (tab_int[i+1]/tab_int[i] != raison):
			return False
	return True