import math

def power(a, b, p):
	return a**b%p
	
def gcd(a,b):
	while b:
		a, b = b, a%b;
	
	return a
	
def d_h(p, g):
	a, b = 4, 3
	print("The value of p :", p)
	print("The value of g :", g)
	print("The private key a for Alice : ", a)
	print("The private key b for Bob : ", b)
	x = power(g, a, p)
	y = power(g, b, p)
	ka = power(y, a, p)
	kb = power(x, b, p)
	print("Secret key for Alice is : ", ka)
	print("Secret key for Bob is : ", kb)

def rsa(p, q):
	n = p*q
	phi = (p-1)*(q-1)
	e = 7
	
	while gcd(e, phi) != 1:
		e += 1
		
	d = pow(e, -1, phi)
	message = 11
	c = pow(message, e, n)
	m = pow(c, d, n)
	print("Original Message = ", message)
	print("p = ", p)
	print("q = ", q)
	print("n = pq = ", n)
	print("phi = ", phi)
	print("e = ", e)
	print("d = ", d)
	print("Encrypted message = ", c)
	print("Decrypted message = ", m)
	
if __name__ == "__main__":
	p, q = 13, 11
	print("RSA Algorithm: ")
	rsa(p, q)
	print("\n\n Diffie Hellman Algorithm: ")
	d_h(p, q)
