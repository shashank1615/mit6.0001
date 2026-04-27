total_cost = float(input("Enter the cost of the house:"))
portion_saved = float(input("Enter the portion saved for the DP:"))
annual_salary = float(input("Enter your annual salary:"))

portion_down_payment = 0.25
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04
months = 0
down_payment = portion_down_payment * total_cost
monthly_saved = portion_saved * monthly_salary

while current_savings < down_payment:
    investment_return = current_savings * r / 12
    current_savings += investment_return + monthly_saved
    months += 1

print("No of Months taken:", months)