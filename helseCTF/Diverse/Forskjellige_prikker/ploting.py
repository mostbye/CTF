import matplotlib
import matplotlib.pyplot as plt
import numpy as np



def main():
	with open('prikker', 'r') as infile:
		dots = infile.readlines()
	dots_arr = []
	x = []
	y = []
	zero = []
	one = []
	two = []
	three = []
	four = []
	five = []
	six = []
	for item in dots:
		dots_arr.append(item.strip().split(" "))
		first = item.strip().split(" ")[0]
		#print(first)
		second = item.strip().split(" ")[1]
		#print(second)
		x.append(first)
		y.append(second)
		if second == "0":
			zero.append(first)
		if second == "1":
			one.append(first)
		if second == "2":
			two.append(first)
		if second == "3":
			three.append(first)
		if second == "4":
			four.append(first)
		if second == "5":
			five.append(first)
		if second == "6":
			six.append(first)
	
	#print(dots_arr)
	
	
	x_sorted = sorted(x)
	y_sorted = sorted(y)
	#plt.scatter(x_sorted, y_sorted)
	plt.scatter(x, y)
	plt.show()
	
	#print(zero)
	#print(one)
	#print(two)
	#print(three)
	#print(four)
	#print(five)
	#print(six)

if __name__ == "__main__":
	main()
