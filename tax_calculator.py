def calculate_tax_2025(income, sd):
    slab = [[400000, 0], [400000, 5], [400000, 10], [400000, 15], [400000, 20], [400000, 25], [0, 30]]

    if income <= 1200000.00 + sd:
        return 0.00
    else:
        income -= sd
        tax = 0.00
        index = 0
        amount = 0.00
        while amount < income:
            if amount + slab[index][0] >= income:
                taxable_amount = income - amount
                amount = income
            else:
                amount += slab[index][0]
                taxable_amount = slab[index][0]
                
            tax += (slab[index][1]*taxable_amount)/100
            
            if index < len(slab) - 1:
                index += 1
            else:
                taxable_amount = income - amount
                tax += (slab[index][1]*taxable_amount)/100
                return tax
            # print(amount, taxable_amount, income, tax)
        return tax           
            
def calculate_tax_2024_new_regime(income, sd):
    slab = [[300000, 0], [400000, 5], [300000, 10], [200000, 15], [300000, 20], [0, 30]]

    if income <= 700000.00 + sd:
        return 0.00
    else:
        income -= sd
        tax = 0.00
        index = 0
        amount = 0.00
        while amount < income:
            if amount + slab[index][0] >= income:
                taxable_amount = income - amount
                amount = income
            else:
                amount += slab[index][0]
                taxable_amount = slab[index][0]
                
            tax += (slab[index][1]*taxable_amount)/100
            
            if index < len(slab) - 1:
                index += 1
            else:
                taxable_amount = income - amount
                tax += (slab[index][1]*taxable_amount)/100
                return tax
            # print(amount, taxable_amount, income, tax)
        return tax   
# output = calculate_tax(1300000.00, 75000.00)
print("Income Tax Calculator\nChoose Year and Regime:\n1. 2025 New Regime\n2. 2024 New Regime")
choice = int(input('Input Choice: '))
annual_income = float(input("Enter annual income: "))
if choice == 1:
    output = calculate_tax_2025(annual_income, 75000.00)
elif choice == 2:
    output = calculate_tax_2024_new_regime(annual_income, 75000.00)
print(output)