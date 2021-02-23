#!/usr/bin/env python3
import random
import binascii
import string

def get_seed(l):
	seed = 0
	rand = 8926184294774128254*2
	raw = list()
	
	while rand > 0:
		rand = rand >> 1
		seed += rand
		raw.append(rand)
	
	if len(raw) == l:
		return raw, seed
	else:
		return get_seed(l)

testing = []

def decrypt():
	l = 64
	solution = ""
	raw, seed = get_seed(l)
	print(raw,seed)
	random.seed(seed)

	for i in range(0,64):	
		r = random.randint(1, 2**512)
		print("r"+str(i)+ "=",r)
		b = 1
		for m in string.printable:
			encoded = hex(r ^ ord(m) ^ raw[i])[2:]
			if(encoded==testing[i]):
				solution += m
				b=0
		if(b==1):
			print(i)
	print(solution)

with open('encrypted.txt', 'r') as f:
	lines = f.readlines()
	i=0
	here = "0123456789abcdef"
	for line in lines:
		r = random.randint(1, 2**512)
		s=line.split(":")[1][2:][:128]
		if(s[127] in here):
			testing.append(s)
		else:
			s=s[:127]
			testing.append(s)
		i += 1

decrypt()
#darkCON{user_W4rm4ch1ne68_pass_W4RM4CH1N3R0X_t0ny_h4cked_4g41n!}
