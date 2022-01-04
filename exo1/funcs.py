def get_mean(tab_int=[]):
	tab_sum=0
	for value in tab_int:
		tab_sum +=value
	return tab_sum//len(tab_int)