#price = 1000000
#has_good_credit = True

#if has_good_credit:
    #down_payment = 0.1 * price
#else:
    #down_payment = 0.2 * price
    #print(f"Down Payment : ${down_payment}")

    has_high_income = True
    has_good_credit = True

    if has_high_income and not has_good_credit:
        print("Eligible for loan")