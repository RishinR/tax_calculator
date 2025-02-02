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
    tax = 0
    cess = 0

    # If income is less than ₹7,00,000, no tax is applied
    if income <= 700000:
        tax = 0
        return tax
    else:
        # Tax Slabs for FY 2024-25 New Regime
        if income <= 300000:
            tax = 0
        elif income <= 700000:
            tax = 0.05 * (income - 300000)
        elif income <= 1000000:
            tax = 20000 + 0.10 * (income - 700000)
        elif income <= 1200000:
            tax = 50000 + 0.15 * (income - 1000000)
        elif income <= 1500000:
            tax = 80000 + 0.20 * (income - 1200000)
        else:
            tax = 140000 + 0.30 * (income - 1500000)

    # Calculating the cess (4% of total tax)
    cess = 0.04 * tax

    # Total tax payable including cess
    total_tax = tax + cess
    return total_tax  

def calculate_tax_old_regime(income, age):
    tax = 0
    # Tax Slabs for Old Regime
    if income <= 250000:
        tax = 0
    elif income <= 300000:
        tax = 0.05 * (income - 250000)
    elif income <= 500000:
        tax = 0.05 * (income - 250000)
    elif income <= 1000000:
        tax = 0.20 * (income - 500000) + 12500
    else:
        tax = 0.30 * (income - 1000000) + 112500
    
    # Apply cess (4%)
    cess = 0.04 * tax
    total_tax = tax + cess
    return total_tax

 
# output = calculate_tax(1300000.00, 75000.00)
print("Income Tax Calculator\nChoose Year and Regime:\n1. 2025 New Regime\n2. 2024 New Regime\n3. Old Tax Regime")
choice = int(input('Input Choice: '))
annual_income = float(input("Enter annual income: "))
age = int(input("Enter your age: "))

# Default standard deduction for new regimes
sd = 75000.00

# Calculate tax based on choice
if choice == 1:
    output_2025 = calculate_tax_2025(annual_income, sd)
    print(f"Tax under 2025 New Regime: ₹{output_2025:.2f}")
elif choice == 2:
    output_2024 = calculate_tax_2024_new_regime(annual_income, sd)
    print(f"Tax under 2024 New Regime: ₹{output_2024:.2f}")
elif choice == 3:
    output_old_regime = calculate_tax_old_regime(annual_income, age)
    print(f"Tax under Old Tax Regime: ₹{output_old_regime:.2f}")

# Tax difference calculation
if choice == 1:
    output_2024 = calculate_tax_2024_new_regime(annual_income, sd)
    output_old_regime = calculate_tax_old_regime(annual_income, age)
    print(f"\nTax under 2024 New Regime: ₹{output_2024:.2f}")
    print(f"Tax under Old Tax Regime: ₹{output_old_regime:.2f}")
    
    print(f"\nTax difference between 2025 New Regime and Old Tax Regime: ₹{output_2025 - output_old_regime:.2f}")
    print(f"Tax difference between 2024 New Regime and Old Tax Regime: ₹{output_2024 - output_old_regime:.2f}")
    
elif choice == 2:
    output_2025 = calculate_tax_2025(annual_income, sd)
    output_old_regime = calculate_tax_old_regime(annual_income, age)
    print(f"\nTax under 2025 New Regime: ₹{output_2025:.2f}")
    print(f"Tax under Old Tax Regime: ₹{output_old_regime:.2f}")
    
    print(f"\nTax difference between 2025 New Regime and Old Tax Regime: ₹{output_2025 - output_old_regime:.2f}")