try:
    filename = input("Enter filename containing csv data:")
except:
    print("")
with open(filename, "r", encoding = "utf-8") as file_contents:
    data_list = []
    for line in file_contents:
        values =  line.split(",")
        data_list.append(values)

print(data_list)
