import os
import sympy
import math

def mod_inverse(x, y):
	modular_inverse = sympy.mod_inverse(x, y)
	return modular_inverse


def main():
	total = 23
	rowL = 3
	print(total / 3)
	print(total % rowL)
	print(mod_inverse(3, 2))
	print(pow(3, -1 ,2))
	

if __name__ == "__main__":
	main()
