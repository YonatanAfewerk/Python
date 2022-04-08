height = input("Enter Your Height pls (meters 1.00 format): ")
x = float(height)

if x >= 1.88:
    print("Sorry your too tall. good for the ladies tho")
elif x >= 1.55 and x <= 1.87:
    print ("Have a great time.")
elif x > 0 and x <= 1.54:
    print("Sorry to short. mayabe read those books")
else:
    print("No service") 