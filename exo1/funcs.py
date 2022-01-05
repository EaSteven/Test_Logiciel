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