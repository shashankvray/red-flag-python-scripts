N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(len(A)-1):
    if A[i] == A[i+1]:
        continue
    count += 1

print(count+1)

'''
You are given an array A of length N and can perform the following operation on the array:

Select a subarray from array A having the same value of elements and decrease the value of all the elements in that subarray by any positive integer x.
Find the minimum number of operations required to make all the elements of array A equal to zero.

Input format

The first line contains an integer N denoting the number of elements in the array.
The next line contains space-separated integers denoting the elements of array A.
Output format

Print the minimum number of operations required to make all the elements of array A equal to zero.

Sample Input
5
2 2 1 3 1

Output
4
'''