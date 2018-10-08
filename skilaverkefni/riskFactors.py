index_tuple = (1, 5, 7, 11, 13)
data_list = []
heart = []
motorVD =[]
tbr = []
smoking = []
obese = []
float_list = []
sjukd = []
try:
    filename = input("Enter filename containing csv data: ")
except:
    print("")

print("{:<33}{:<21}{:<15}".format("Indicator","Min","Max"))
print("-"*87)

with open(filename, "r", encoding = "utf-8") as file_contents:
    for line in file_contents:
        line = line.strip().split(",")
        data_list.append(line)
    

for data in data_list[0]:
    sjukd.append(data)
sjukd.pop(0)
data_list.pop(0)
states = []
for data in data_list:
    states.append(data[0])
states.pop(0)
sjuk_counter = 0
for index in index_tuple:
    if index == 1:
        list_at_index = heart
    elif index == 5:
        list_at_index = motorVD
    elif index == 7:
        list_at_index = tbr
    elif index == 11:
        list_at_index  = smoking
    elif index == 13:
        list_at_index = obese
    for data in data_list:
        list_at_index.append(data[index])
    list_at_index.pop(0)
    
    for stuff in list_at_index:
        if stuff[-1] == "%":
            list_at_index = [float(x[:-1]) for x in list_at_index]
        else:
            list_at_index = [float(x) for x in list_at_index]
        break
    max_of = max(list_at_index)
    min_of = min(list_at_index)
    index_of_max = list_at_index.index(max_of)
    index_of_min = list_at_index.index(min_of)
    print("{:<33}{:<21}{:<6}{}{:<15}{:<6}".format(sjukd[sjuk_counter], states[index_of_min], min_of, " "*6 ,states[index_of_max], max_of))
    sjuk_counter += 1
    

   





    
  
        
    #print("{}{}{}{}{}".format(sjukd[sjuk_counter], states[index_of_max], max_of ,states[index_of_min], min_of))
   