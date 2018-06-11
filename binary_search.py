'''  
binary  search algo
 '''
x = input()
y = list(input())
def bisect_search(e,l):	
	if l==[]:
		return False
		#setting base case for recursion
	elif len(l)==1:
		return l[0]==e
		#setting base case
	else:
		half =len(l)//2
		if l[half]>e:
			return bisect_search(e,l[:half])
		else:
			return bisect_search(e,l[half:])

print(bisect_search(x,y))


