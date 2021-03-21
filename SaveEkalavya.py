def Digital(str):
	san = ["shun","ekam","dvee","trin","catv","panc","shat","sapt","asta","nava"]
	str+= " "
	for i in range(len(san)):
		count = 0
		for j in range(len(san[i])):
			for k in range(len(str)):
				if san[i][j] == str[k]:
					count+=1
					break
			if count < len(san[i]) and k == len(str)-1:
				break
			if count == len(san[i]):
				return i
def Tratru(nos):
	arr = list(map(int, str(nos)))
	mid = int(len(arr) // 2)
	iter = 0
	while True:
		iter+=1
		if(iter > 20):
			exit(0)
		paschima = arr[:mid]	
		poorva = arr[mid+1:]
		if sum(paschima) > sum(poorva):
			mid-=1
			continue
		elif sum(paschima) < sum(poorva):
			mid+=1
			continue
		else:
			break
	paschima.sort(reverse = True)
	poorva.sort(reverse = True)
	left = int("".join([str(k) for k in paschima]))
	right = int("".join([str(k) for k in poorva]))	
	return (left * arr[mid] * right)

if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		shuff = input().split()
		num = []
		for x in range(len(shuff)):
			num.append(Digital(shuff[x].lower()))
		print(Tratru(int("".join([str(k) for k in num]))))