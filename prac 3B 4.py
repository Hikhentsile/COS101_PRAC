# Initialize variables
salaries = []
month = 1
total_salary = 0

# Collect salaries for 6 months
while month <= 6:
    salary = float(input(f"Enter salary for month {month}: "))
    salaries.append(salary)
    total_salary += salary
    month += 1

# Calculate average salary
average_salary = total_salary / 6

# Determine tax rate
if average_salary > 30000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

# Calculate tax and net income
tax_amount = total_salary * tax_rate
net_income = total_salary - tax_amount

print()
# Display results
print("-------------------------------------------------")
print(f"Total salary over 6 months: R{total_salary:.2f}")
print(f"Average monthly salary: R{average_salary:.2f}")
print(f"Tax rate applied: {int(tax_rate * 100)}%")
print(f"Tax amount: R{tax_amount:.2f}")
print(f"Net income after tax: R{net_income:.2f}")
print("-------------------------------------------------")
