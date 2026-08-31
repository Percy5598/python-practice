monthly_salary = float(input("Enter your monthly salary: "))
tax_rate = float(input("Enter tax rate (%): "))
annual_salary = monthly_salary * 12 * (1 - tax_rate / 100)
print("Your annual salary is:", annual_salary)

