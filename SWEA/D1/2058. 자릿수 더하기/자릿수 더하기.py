N = int(input())
arr = []

while N >= 10:
    arr.append(N % 10) 
    N = N // 10
    
arr.append(N)
       
sum = 0

for a in arr:
    sum += a    

print(sum)