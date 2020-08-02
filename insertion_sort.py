n = int(input("Enter number of elements to insert:"))
a = []

for i in range(n):
	a.append(int(input("Enter Element")))

for i in range(1, len(a)):
	temp = a[i]
	j = i-1
	while(j>=0 and temp < a[j]):
		a[j+1] = a[j]
		j = j-1
	a[j+1] = temp

for i in range(len(a)):
	print(a[i])

