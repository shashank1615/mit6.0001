total_cost = float(input("Enter the cost of the house:"))
portion_saved = float(input("Enter the portion saved for the DP:"))
annual_salary = float(input("Enter your semi annual salary:"))
salary_raised = float(input("Enter amount of salary raised:"))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 0
down_payment = portion_down_payment * total_cost

while current_savings < down_payment:
    monthly_salary = annual_salary / 12
    investment_return = current_savings * r / 12
    monthly_saved = portion_saved * monthly_salary
    
    current_savings += investment_return + monthly_saved
    months += 1

    if months % 6 == 0:
        annual_salary *= (1 + salary_raised)

print("No of Months taken:", months)