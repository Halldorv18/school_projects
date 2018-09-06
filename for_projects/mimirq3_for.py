chess_slots = 64
sum_of_grain = 0
for grains in range(1,65):
    if grains == 1:
        sum_of_grain += 1
    else:
        sum_of_grain += 2**(grains - 1)
print(sum_of_grain)