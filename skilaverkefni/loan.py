loan_str = input("Input the cost of the item in $: ")
loan_float = float(loan_str)
og_loan = loan_float
min_monthly_payment = 50.0
over_thousand_interest = 0.02
under_thousand_interest = 0.015
counter = 0
sum_of_interest = 0
while loan_float > 0.0 and loan_float < 2500:
    if og_loan > 1000.0:
        deduced_loan = loan_float - min_monthly_payment + (over_thousand_interest * loan_float)
        interest = loan_float * over_thousand_interest
        loan_float = deduced_loan
        counter += 1
        sum_of_interest += interest
        if deduced_loan < 0:
            min_monthly_payment += round(deduced_loan, 2)
            deduced_loan = 0
        print("Month:", counter, "Payment:", round(min_monthly_payment,2), "Interest paid:", round(interest, 2), "Remaining debt:", round(deduced_loan, 2))

    else:
        deduced_loan = loan_float - min_monthly_payment + (under_thousand_interest * loan_float)
        interest = loan_float * under_thousand_interest
        loan_float = deduced_loan
        counter += 1
        sum_of_interest += interest
        if deduced_loan < 0:
            min_monthly_payment += round(deduced_loan, 2)
            deduced_loan = 0.0

    
            
                
        print("Month:", counter, "Payment:", round(min_monthly_payment, 2), "Interest paid:", round(interest,2), "Remaining debt:", round(deduced_loan,2))
print()
print("Number of months:", counter)
print("Total interest paid:", round(sum_of_interest, 2))