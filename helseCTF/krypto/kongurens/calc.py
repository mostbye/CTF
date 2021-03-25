import numpy as np
import sympy
import math

def mod_inverse(x, y):
	modular_inverse = sympy.mod_inverse(x, y)
	return modular_inverse



def solve_linear_congruence(a, b, m):
    """ Describe all solutions to ax = b  (mod m), or raise ValueError. """
    g = math.gcd(a, m)
    if b % g:
        raise ValueError("No solutions")
    a, b, m = a//g, b//g, m//g
    return pow(a, -1, m) * b % m, m


def main():
	# a*x ≡ 1 (mod p)
	# a*x = c
	# a = x_ * c
	p = 88619509055522082453204780866094153179701708680210152273575985657978607113243
	x = 38751234384983559040347094325349107850289644025269636239010846543908547616067


	#print(p)
	#print(x)
	#print(type(p))
	#print(type(x))
	#a = mod_inverse(x, p)
	# Python FTW
	x_ = pow(x, -1, p)
	print(x_)
	print(x_ * x)
	print(x_**2 % p)
	print(x_ * x % p)

	
	#res = solve_linear_congruence(x, 1 ,p)
	#print(res)
	

	

	

if __name__ == "__main__":
	main()
