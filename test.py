N, K = map(int, input().split())

arr = []
arr2 = []
result = 0

for _ in range(N): # 보석 개수 
    M, V = map(int, input().split()) # 무게, 가격
    arr.append([M, V])
    
arr.sort(key= lambda x: (x[1], x[0]), reverse=True)

for _ in range(K): # 가방 개수 
    C = int(input()) # 가방 최대 무게 
    arr2.append(C)

for x, y in arr:
    for i in arr2:
        if (x <= i):
            result += y
            print("x,",x," i", i, "== y",y,"re",result)
            
print(result)