from flask import Flask, request, jsonify

app = Flask(__name__)

# Tax calculation function
def calculate_tax(income, standard_deduction):
    slab = [0, 5, 10, 15, 20, 25, 30]
    if income <= 1200000.00 + standard_deduction:
        return 0.00
    else:
        income -= standard_deduction
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
                
            tax += (slab[index] * taxable_amount) / 100
            
            if index < len(slab) - 1:
                index += 1
        return tax

# Flask route for the tax calculation
@app.route('/calculate_tax', methods=['POST'])
def calculate_tax_endpoint():
    # Get data from request JSON
    data = request.get_json()
    
    income = data.get('income')
    standard_deduction = data.get('standard_deduction', 75000.00)  # Default standard deduction value
    
    if income is None:
        return jsonify({"error": "Income is required"}), 400
    
    # Call the tax calculation function
    tax = calculate_tax(income, standard_deduction)
    
    return jsonify({
        "income": income,
        "taxable_income": income - standard_deduction,
        "tax": tax
    })

if __name__ == '__main__':
    app.run(debug=True)
