import numpy as np

with open('Piworks.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

array=[]
for i in range(0,len(content)):
    k=content[i].split(" ")
    array.append(k)

my_array = np.array(array,dtype=list)

def primenumber(number):
    global word
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "is not a prime number")
                return 0
    else:
        print(number, "is a prime number")
        return 1

length_triangle = len(my_array)
array_last = []

MainMatrix=np.zeros((length_triangle, length_triangle))
print(MainMatrix)

for ilkan in range (length_triangle):
    newarr = my_array[ilkan]
    for t in range (ilkan+1):
        newarr[t] = int(newarr[t])
        result = primenumber(newarr[t])
        MainMatrix[ilkan][t] =newarr[t]
        if result == 0:
            continue
        else:
            if ilkan == 0:
                continue
            else:
                 MainMatrix[ilkan][t] = 0
            print("yo")

print(MainMatrix)



def toplama(Path, m, n):

	# loop for bottom-up calculation 
	for i in range(m-1, -1, -1): 
		for j in range(i+1):
			if (Path[i+1][j] > Path[i+1][j+1]):
				Path[i][j] += Path[i+1][j]
			else: 
				Path[i][j] += Path[i+1][j+1]
	return Path[0][0]

print(toplama(MainMatrix, length_triangle-1, length_triangle-1))

