# finance_calculator.py
# This script calculates monthly savings and projected annual savings with interest

# Prompt user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
projected_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")
