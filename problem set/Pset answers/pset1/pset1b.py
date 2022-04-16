
    # Get info from the user
    
a = input("Enter your annual salary: ")
b = input("Enter the percent of your salary to save, as a decimal: ")
c = input("Enter the cost of your dream home: ")

    # inputted variables are in str so they should be converted to ints
    
annual_salary = float(a)
portion_to_save = float(b)
total_cost =  float(c)

current_savings = 0
x = 0
r = 0.04

portion_down_payment = (25/100) * total_cost  # Down payment
portion_saved  =  (portion_to_save / 10) * annual_salary #Saved amount annually

x = portion_saved + current_savings

y = (current_savings * (r / 12)) 
        
days = 0
month = 0
while (x <= portion_down_payment):
        days += 1
     
        if(days == 30):
            days = 0
            month += 1
        
        
print("Number of months: ", int(month))

print(portion_down_payment)
print(saved_from_salary)
print(r)
print(current_savings)
