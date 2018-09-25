#User inputs the number of shares.
#User inputs the price per share in Dollars and a float < 0.
#After the calculation of the total price of all the shares the user gets to choose to continue or quit.

def brot_str(price):
    check = True
    while check == True:
        try:
            int(price.replace(" ", ""))
            check = False
        except ValueError:
            break
    
        counter = 0
        for index, letter in enumerate(price):
            
            if letter == " " and counter == 0:
                dollars = price[0:index]
                dollar_index = index + 1
                counter += 1
            elif letter == " " and counter == 1:
                numerator = price[dollar_index : index]
                numerator_index = index + 1
                counter += 1
            elif counter == 2:
                denominator = price[numerator_index : ]
        dollars_int = int(dollars)
        numerator_int = int(numerator)
        denominator_int = int(denominator)
        pp_share_int = dollars_int + numerator_int/denominator_int
        pp_share_str = dollars + " " + numerator + "/" + denominator
        return pp_share_str, pp_share_int
    
def user_input(number_of_shares):
    try:
        int(number_of_shares)
    except ValueError:
        print("Invalid number!")

def value_check():
    
    invalid_number = True
    while invalid_number == True:
        pp_share = input("Enter price (dollars, numerator, denominator): ")
    
        try:
            pp_share_str, pp_share_int = brot_str(pp_share)
            return pp_share_str, pp_share_int
        except Exception:
            print("Invalid price!")
            continue
    
choice = "y"
while choice == "y":
    try:
        number_of_shares = int(input("Enter number of shares: "))
    except ValueError:
        print("Invalid number!")
        continue

    pp_share_str, pp_share_int = value_check()

    total_price = number_of_shares * pp_share_int
    print("{} shares with market price {} have value {}{:.2f}".format(number_of_shares, pp_share_str, "$", total_price ))
    go_on = input("Continue: ")
    choice = go_on.lower()
    

    
    




    
        

