a = 1.; eps = 1.; b = a + eps
while a != b:
	eps /= 2
	b = a + eps
print(eps)