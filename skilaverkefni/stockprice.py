def stock_calc(dollars, float_of, shares):
    dollars_str = str(dollars)
    float_str = str(float_of)
    value_of_each = dollars_str + float_str
    total_value = float_of * dollars
    print("{} shares with the market price {} have value {}".format(shares, value_of_each, total_value))



def info_split(share_info):
    try:
        counter = 0
        stipped_info = share_info.replace(" ", "")
        if stripped_info.digit() == True:
            for index, letter in enumerate(share_info):
                if letter == " " and counter == 0:
                    dollars = int(share_info[0: index])
                    dollars_stop = index
                    counter += 1
                elif letter == " " and counter == 1:
                    counter += 1
                    numerator = int(share_info[dollars_stop + 1: index + 2 ])
                elif letter == " " and counter == 2:
                    denomintor = int(share_info[index + 1: index + 2])
            
                float_of_nd = numerator/denominator
        else:
            print("Invalid price!")
    except Exception:
        Exception
            
    return dollars, float_of_nd


      
        
def keep_going():
    yes_or_no = input("Continue?: ")
    answer_str = yes_or_no.lower()
    
        
    
keep_going = "y"
while keep_going == "y":
    shares = int(input("Enter number of shares:"))
    share_info = input("Enter price: (dollars, numerator, denominator): ")
    dollars, float_of_nd = info_split(share_info)
    keep_going()