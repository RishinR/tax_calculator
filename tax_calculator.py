def calculate_tax(income, sd):
    slab = [0, 5, 10, 15, 20, 25, 30]
    if income <= 1200000.00 + sd:
        return 0.00
    else:
        income -= sd
        tax = 0.00
        index = 0
        amount = 0.00
        while amount < income:
            if amount + 400000.00 >= income:
                taxable_amount = income - amount
                amount = income
            else:
                amount += 400000.00
                taxable_amount = 400000.00
                
            tax += (slab[index]*taxable_amount)/100
            
            if index < len(slab) - 1:
                index += 1
            # print(amount, taxable_amount, income, tax)
        return tax            
            
# output = calculate_tax(1300000.00, 75000.00)
print("Income Tax Calculator: New Tax Regime 2025")
annual_income = float(input("Enter annual income: "))
output = calculate_tax(annual_income, 75000.00)
print(output)