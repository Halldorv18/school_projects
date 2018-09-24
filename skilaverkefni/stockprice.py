#User inputs the number of shares.
#User inputs the price per share in Dollars and a float < 0.
#After the calculation of the total price of all the shares the user gets to choose to continue or quit.



choice = "y"
while choice == "y":
    try:
        number_of_shares = int(input("Enter number of shares: "))
    except Exception:
        print("Invalid number!")
        continue
    pp_share = input("Enter the price (dollars, numerator, denominator): ")
    new_pp = pp_share.replace(" ", "")
    if new_pp.isdigit() == True:
        dollars = new_pp[:-2]
        numerator = new_pp[-2]
        denominator = new_pp[-1]
        print(dollars, numerator, denominator)
        try:
            brot = int(numerator)/int(denominator)
            total_price = (int(dollars)+ brot) * number_of_shares
            brot_str = dollars + " " + numerator + "/" + denominator
            print("{} shares with market price {} have value {:.2f}".format(number_of_shares, brot_str, total_price ))
        except ValueError:
            print("Invalid price!")

    else:
        print("Invalid price!")

    go_on = input("Continue: ")
    choice = go_on.lower()

    
        

