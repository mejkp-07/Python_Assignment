# -*- coding: utf-8 -*-
"""
Created on Mon May  1 12:41:39 2023

@author: Jay Kumar
"""
def check(groups, planes, n, m, min_time) :
	
	temp = 0
	count = 0

	while (count < m) :
		j = 0
		while (j < min_time and temp < n and
					planes[count] >= groups[temp] ):
			temp +=1
			j += 2

		count += 1

	if (temp == n) :
		return True

	return False


def result(groups, planes, n, m) :

	groups.sort();
	planes.sort();

	low_bound = 0
	high_bound = 2 * n

	min_time = 0

	while (low_bound <= high_bound) :
		mid = (low_bound + high_bound) // 2

		if (check(groups, planes, n, m, mid)) :
			min_time = mid
			high_bound = mid - 1
	
		else :
			
			low_bound = mid + 1

	return min_time



groups = [ 8, 1, 6, 9]
planes = [ 7, 3, 2 ]

'''Unable to transport peaople with these input !!'''

n = len(groups)
m = len(planes)

res = result(groups, planes, n, m)
if(res > 0):
    print(res)
else:
    print("Sorry, we can't trasport them")