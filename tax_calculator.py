def calculate_tax_2025_new_regime(income, sd=75000):
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
            
def calculate_tax_2024_new_regime(income, sd=75000):
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

def calculate_tax_old_regime(income, age,deduction=0):
    tax = 0
    income -= deduction
    
    # Tax Slabs for Old Regime based on age
    if age < 60:  # Below 60 years
        if income <= 250000:
            tax = 0
        elif income <= 500000:
            tax = 0.05 * (income - 250000)
        elif income <= 1000000:
            tax = 0.20 * (income - 500000) + 12500
        else:
            tax = 0.30 * (income - 1000000) + 112500
    elif 60 <= age < 80:  # Between 60 and 80 years (Senior Citizens)
        if income <= 300000:
            tax = 0
        elif income <= 500000:
            tax = 0.05 * (income - 300000)
        elif income <= 1000000:
            tax = 0.20 * (income - 500000) + 10000
        else:
            tax = 0.30 * (income - 1000000) + 120000
    else:  # Above 80 years (Super Senior Citizens)
        if income <= 500000:
            tax = 0
        elif income <= 1000000:
            tax = 0.20 * (income - 500000)
        else:
            tax = 0.30 * (income - 1000000) + 100000

    # Apply cess (4%)
    cess = 0.04 * tax
    total_tax = tax + cess
    return total_tax

# Calculate tax based on choice
def calculate_tax(annual_income, fy, age, deduction=0):
    old_regime, new_regime = 0, 0
    sd = 75000.00  # standard deduction for new regimes

    if fy == 1:
        old_regime = calculate_tax_old_regime(annual_income, age, deduction)
        new_regime = calculate_tax_2024_new_regime(annual_income, sd)
    elif fy == 2:
        old_regime = calculate_tax_old_regime(annual_income, age, deduction)
        new_regime = calculate_tax_2025_new_regime(annual_income, sd)
    
    return old_regime, new_regime

# User input section
print("Income Tax Calculator\nChoose Fiscal Year :\n1. 2024-25\n2. 2025-26")
fy = int(input('Input Choice: ')) 
annual_income = float(input("Enter annual income: ")) 
age = int(input("Enter your age: ")) 
deduction = float(input("Enter annual Deductions: ")) 


# Calculate tax for both regimes
old_regime, new_regime = calculate_tax(annual_income, fy, age, deduction)

# Display results
print("\nTax Calculation Results:")
print(f"Tax under New Regime: ₹{new_regime:.2f}")
print(f"Tax under Old Tax Regime: ₹{old_regime:.2f}")

# Calculate savings and verdict
if new_regime < old_regime:
    savings = old_regime - new_regime
    print(f"\nYou save ₹{savings:.2f} by choosing the New Regime.")
    print("Verdict: New Regime is better for you.")
else:
    savings = old_regime - new_regime
    print(f"\nYou save ₹{savings:.2f} by choosing the Old Tax Regime.")
    print("Verdict: Old Tax Regime is better for you.")