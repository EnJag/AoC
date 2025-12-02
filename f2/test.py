b = '156545425'
l = len(b)
div = [d for d in range(1, l+1) if l%d==0]
print(div)
# liste = [for d in div]
g = 3
lb = [b[i:i+g] for i in range(0, len(b), g)]
print(lb)
# a='82-103'
# for i in range (int(a.split('-')[0]), int(a.split('-')[1])+1):
#     print(len(str(i))%2)
#     if len(str(i))%2 == 1:
#         continue
#     print(i)