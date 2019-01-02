def DP(i):
	if i == 0:
		return 1
	if i < 0: 
		return 0
	return DP(i-3) + DP(i-2) + DP(i-1)

n = 5
x = DP(n)
print(x)