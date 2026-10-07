# inputs we need from the user
# total rent
# total food ordered for snacking
# electricity unit bills
# charge per unit
# output
# total amount you have

#project code

rent = int(input("Enter your hostel/flat rent ="))
food = int(input("Enter the amount of food order ="))
electricity_spend = int(input("Enter the total of electricity spend ="))
charge_per_unit = int(input("Enter the charge per unit="))
persons = int(input("Enter the number of person living in room.flat ="))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons
print("Each person will pay =",output)

