def calculate_tax(income):
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

# Example: Calculating tax for ₹13,00,000 income
income = int(input('Enter your Net Income: '))
tax_payable = calculate_tax(income)

print(f"Total tax payable for an income of ₹{income}: ₹{tax_payable:.2f}")
