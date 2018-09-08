loan = float(input("Input the cost of the item in $: "))
debt = loan
month = 0
total_interest = 0.0
default_payment = 50.0


if loan < 2500.0:


    if loan <= 1000.0:
        rate = 0.015
    else:
        rate = 0.02


    while debt > 0.0:
        interest= debt * rate
        if debt < default_payment:
            payment = interest + debt 
        else: 
            payment = default_payment

        principal_payment = payment - interest 
        debt = debt - principal_payment 
        month += 1
        total_interest += interest

        print("Month:",month, 
        "Payment:" ,round(payment,2), 
        "Interest paid:" ,round(interest,2), 
        "Remaining debt:",round(debt,2),)

    else:
        print("Number of months:" ,month,)
        print("Total interest paid:",round(total_interest,2))
else:
    print("Input invalid, it must be < 2500")
    
