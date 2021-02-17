#ABC087B Coins

a = int(input())
b = int(input())
c = int(input())
x = int(input())
nu_combination = 0
for n500 in range(0,a+1):
    for n100 in range(0,b+1):
        for n50 in range(0,c+1):
            amount = n500*500+n100*100+n50*50

            if amount == x :
                #print(n500, n100, n50, amount)
                num_combination += 1


print (num_combination)
