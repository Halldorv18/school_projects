def make_new_row(new_row):
    next_row = []
    if new_row == []:
        return [1]
    elif new_row == [1]:
        return [1, 1]
    else:
        next_row.append(1)
        for index in range(1, len(new_row)):
            next_row.append(new_row[index] + new_row[index - 1])
            
        next_row.append(1)
    return next_row

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)
