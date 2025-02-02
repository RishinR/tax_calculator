import React, { useState } from 'react';

const App = () => {
  const [fy, setFy] = useState(1); // Fiscal year (1 for 2024-25, 2 for 2025-26)
  const [annualIncome, setAnnualIncome] = useState('');
  const [age, setAge] = useState('');
  const [deduction, setDeduction] = useState('');
  const [oldTax, setOldTax] = useState(null);
  const [newTax, setNewTax] = useState(null);
  const [savings, setSavings] = useState(null);
  const [verdict, setVerdict] = useState('');

  // Tax Calculation for New Regime (2024-25)
  const calculateTax2024NewRegime = (income, sd = 75000) => {
    let tax = 0;
    if (income <= 700000) {
      tax = 0;
    } else {
      if (income <= 300000) {
        tax = 0;
      } else if (income <= 700000) {
        tax = 0.05 * (income - 300000);
      } else if (income <= 1000000) {
        tax = 20000 + 0.10 * (income - 700000);
      } else if (income <= 1200000) {
        tax = 50000 + 0.15 * (income - 1000000);
      } else if (income <= 1500000) {
        tax = 80000 + 0.20 * (income - 1200000);
      } else {
        tax = 140000 + 0.30 * (income - 1500000);
      }
    }
    let cess = 0.04 * tax;
    return tax + cess;
  };

  // Tax Calculation for New Regime (2025-26)
  const calculateTax2025NewRegime = (income, sd = 75000) => {
    let tax = 0;
    const slab = [
      [400000, 0],
      [400000, 5],
      [400000, 10],
      [400000, 15],
      [400000, 20],
      [400000, 25],
      [0, 30],
    ];
    if (income <= 1200000 + sd) {
      return 0;
    } else {
      income -= sd;
      let amount = 0;
      let index = 0;
      while (amount < income) {
        let taxableAmount = 0;
        if (amount + slab[index][0] >= income) {
          taxableAmount = income - amount;
          amount = income;
        } else {
          amount += slab[index][0];
          taxableAmount = slab[index][0];
        }
        tax += (slab[index][1] * taxableAmount) / 100;
        if (index < slab.length - 1) {
          index += 1;
        } else {
          taxableAmount = income - amount;
          tax += (slab[index][1] * taxableAmount) / 100;
          return tax;
        }
      }
    }
    return tax;
  };

  // Tax Calculation for Old Regime
  const calculateTaxOldRegime = (income, age, deduction = 0) => {
    income -= deduction;
    let tax = 0;

    if (age < 60) {
      if (income <= 250000) {
        tax = 0;
      } else if (income <= 500000) {
        tax = 0.05 * (income - 250000);
      } else if (income <= 1000000) {
        tax = 0.20 * (income - 500000) + 12500;
      } else {
        tax = 0.30 * (income - 1000000) + 112500;
      }
    } else if (age >= 60 && age < 80) {
      if (income <= 300000) {
        tax = 0;
      } else if (income <= 500000) {
        tax = 0.05 * (income - 300000);
      } else if (income <= 1000000) {
        tax = 0.20 * (income - 500000) + 10000;
      } else {
        tax = 0.30 * (income - 1000000) + 120000;
      }
    } else {
      if (income <= 500000) {
        tax = 0;
      } else if (income <= 1000000) {
        tax = 0.20 * (income - 500000);
      } else {
        tax = 0.30 * (income - 1000000) + 100000;
      }
    }

    let cess = 0.04 * tax;
    return tax + cess;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!annualIncome || !age) return;

    let oldTaxAmount = 0;
    let newTaxAmount = 0;

    if (fy === 1) {
      oldTaxAmount = calculateTaxOldRegime(annualIncome, age, deduction);
      newTaxAmount = calculateTax2024NewRegime(annualIncome);
    } else {
      oldTaxAmount = calculateTaxOldRegime(annualIncome, age, deduction);
      newTaxAmount = calculateTax2025NewRegime(annualIncome);
    }

    setOldTax(oldTaxAmount);
    setNewTax(newTaxAmount);

    let difference = Math.abs(oldTaxAmount - newTaxAmount);
    setSavings(difference);

    if (newTaxAmount < oldTaxAmount) {
      setVerdict("New Regime is better for you.");
    } else {
      setVerdict("Old Tax Regime is better for you.");
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 py-10">
      <h1 className="text-3xl font-bold mb-6">Income Tax Calculator</h1>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-lg w-96 space-y-4">
        <div>
          <label className="block text-sm font-semibold mb-2">Choose Fiscal Year:</label>
          <select
            value={fy}
            onChange={(e) => setFy(Number(e.target.value))}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            <option value="1">2024-25</option>
            <option value="2">2025-26</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-semibold mb-2">Enter Annual Income:</label>
          <input
            type="number"
            value={annualIncome}
            onChange={(e) => setAnnualIncome(Number(e.target.value))}
            required
            className="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div>
          <label className="block text-sm font-semibold mb-2">Enter Your Age:</label>
          <input
            type="number"
            value={age}
            onChange={(e) => setAge(Number(e.target.value))}
            required
            className="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <div>
          <label className="block text-sm font-semibold mb-2">Enter Deductions (if any):</label>
          <input
            type="number"
            value={deduction}
            onChange={(e) => setDeduction(Number(e.target.value))}
            className="w-full p-2 border border-gray-300 rounded-md"
          />
        </div>
        <button type="submit" className="w-full p-2 bg-blue-500 text-white rounded-md hover:bg-blue-600">
          Calculate
        </button>
      </form>

      {oldTax !== null && newTax !== null && (
        <div className="mt-6 bg-white p-6 rounded-lg shadow-lg w-96">
          <h2 className="text-xl font-semibold mb-4">Tax Calculation Results:</h2>
          <p className="mb-2">Tax under New Regime: ₹{newTax.toFixed(2)}</p>
          <p className="mb-2">Tax under Old Regime: ₹{oldTax.toFixed(2)}</p>
          <p className="mb-2">
            {savings && (
              <span>
                You save ₹{savings.toFixed(2)} by choosing the{" "}
                <span className='font-bold '>{newTax < oldTax ? "New Regime" : "Old Tax Regime"}</span>
                .
              </span>
            )}
          </p>
          <h3
            className={`text-lg font-semibold ${
              newTax < oldTax ? 'text-green-500' : 'text-red-500'
            }`}
          >
            {verdict}
          </h3>

        </div>
      )}
    </div>
  );
};

export default App;
