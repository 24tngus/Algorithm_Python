str1 = input()
str2 = str1.split('-')

result = 0

if str1[0] == '-':
    result -= sum(map(int, str2[0].split('+')))
else :
    result += sum(map(int, str2[0].split('+')))

for i in str2[1 : ]:
    result -= sum(map(int, i.split('+')))

print(result)
