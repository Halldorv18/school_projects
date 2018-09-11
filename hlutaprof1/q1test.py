month = input("Month: ")
day = input("Day: ")
holiday = month.capitalize() + " " + day

if holiday == "January 1":
    holiday1 = "New year's day"
    print(holiday1)
elif holiday == "June 17":
    holiday1 = "National holiday"
    print(holiday1)
elif holiday == "December 25":
    holiday2 = "Christmas day"
    print(holiday2)

else:
    print("Not a holiday")
    print(holiday)
    

