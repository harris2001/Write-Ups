# Problem Description:
We were provided with 64 encoded messages and the sourcecode used to generate them. The task was to siply decrypt the communication by knowing the first random number used (r0) which was given in the problem statement. 

## Difficulty:
This was a medium-diffuculty Crypto challenge solved by 45/665 teams

## The code:
```python
def get_seed(l):
	seed = 0
	rand = random.getrandbits(l)
	raw = list()
	
	while rand > 0:
		rand = rand >> 1
		seed += rand
		raw.append(rand)
	
	if len(raw) == l:
		return raw, seed
	else:
		return get_seed(l)

def encrypt(m):
	l = len(m)

	raw, seed = get_seed(l)
	random.seed(seed)

	with open('encrypted.txt', 'w') as f:	
		for i in range(l):
			r = random.randint(1, 2**512)
			if i == 0:
				print("r0 =",r)
			encoded = hex(r ^ m[i] ^ raw[i])[2:]
			f.write(f"F{i}:  {encoded}\n")
```
