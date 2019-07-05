def subArray(arr, n, k):
	ans = []
	for i in range(0, n-k+1):
		subAr = []
		for j in range(i, i+k):
		    subAr.append(arr[j])
		ans.append(subAr)
	return ans

def Larger(X, Y):
    for i in range(len(X)):
        x = X[i]
        y = Y[i]
        if x > y:
            return X
        if y > x:
            return Y

def Largest(arr):
    for i in range(len(arr)-1):
        X = arr[i]
        Y = arr[i+1]
        largest = Larger(X, Y)
    return largest;

if __name__ == '__main__':
	n, k = input().split()
	arr = [int(x) for x in input().split()]
	subArr = subArray(arr, int(n), int(k))
	print(Largest(subArr))
	  