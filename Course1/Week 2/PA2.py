
def merge_count(a, b):
	## assumes a and b are already sorted
	## count inversions in c
	c = []
	count = 0; i=0; j=0
	while i<len(a) and j<len(b):
		if (a[i] > b[j]):
			count = count + len(a)
			c.append(b.pop(0))	## size of b reduced by 1
		elif a[i] < b[j]:
			c.append(a.pop(0))
			
	## elements left in a, add to c
	## for 
	while(len(a)):
		c.append(a.pop(0))
	while(len(b)):
		c.append(b.pop(0))
	return count, c
  
def count_inv(a):
	if len(a) == 1:
		return 0, a
	else:
		x, b = count_inv(a[0:len(a)//2])
		y, c = count_inv(a[len(a)//2: ])
		z, a = merge_count(b, c)
	return (x+y+z), a
  
  
  with open("IntegerArray.txt", "r") as file:
	lines = file.readlines()
	a = []
	for l in lines:
		a.append(int(l.strip()))

c, a = count_inv(a)
print(c)
##a = [4, 12, 13, 16, 8, 3, 11, 6, 1, 9, 10, 5, 14, 15, 2, 7]
##c, a = count_inv(a)
##print(c)
###Output: 64
