## STARTER CODE
file = open('Day22_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
total = 0
for buyer in [int(i) for i in lines]:
    for i in range(2000):
        prod = buyer * 64
        buyer ^= prod
        buyer %= 16777216
        quot = buyer//32
        buyer ^= quot
        buyer %= 16777216
        prod = buyer * 2048
        buyer ^= prod
        buyer %= 16777216
    # print(buyer)
    total += buyer

print(f"Part 1: {total}")

# PART 2
for buyer in [int(i) for i in lines]:
    prices = [buyer%10]
    for i in range(9):
        prod = buyer * 64
        buyer ^= prod
        buyer %= 16777216
        quot = buyer//32
        buyer ^= quot
        buyer %= 16777216
        prod = buyer * 2048
        buyer ^= prod
        buyer %= 16777216
        prices.append(buyer%10)
    print(prices)
    break