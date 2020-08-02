n = int(input("How many elements do you want to sort?"))
a = []
for i in range(n):
	a.append(int(input("Enter Element No " + str(i+1) + ":" )))

def bubble_sort(a):

	while True:
		x = 0

		for i in range(1, len(a)):
			if a[i-1] > a[i]:
				temp = a[i-1]
				a[i-1] = a[i]
				a[i] = temp
				x = 1

		if x == 0:		
			break

	print("Sorted Array: ")
	for x in range(len(a)):
		print(a[x])

bubble_sort(a)
