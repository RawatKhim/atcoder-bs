# atcoder beginners selection abc081a

s = input()
num = int(s)
count_1 = 0

while num > 0:
    if num%10 == 1:
        count_1 += 1
    num = num // 10

print(count_1)
