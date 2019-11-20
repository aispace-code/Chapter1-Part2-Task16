weight_earth = int(input())

for i in range(0, 15):
    weight_moon = weight_earth * 0.165
    weight_earth += 1
    print(weight_moon)