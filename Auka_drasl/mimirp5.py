secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)
hours = secs_int // 3600# hours =
minutes = (secs_int % 3600) // 60# minutes =
seconds =  secs_int - (hours * 3600) - (minutes * 60)
print(hours,":",minutes,":",seconds) # do not change this line