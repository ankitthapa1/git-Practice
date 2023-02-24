prices = [7,1,5,3,6,4]
max = min = prices[0]
for a,x in enumerate(prices):
    if x < min: min = x
    print(min)
    if a > prices.index(min):
        if x > max:
            max = x 
    print()

print(max)

    