## Inputs we need from the user
# Total Rent
# Total food ordered
# Electricity Units
# Charge per unit
# Persons living in room/flat

# Output
## Total amount have to pay by each person

rent= int(input("Enter total rent amount= "))
food= int(input("Enter total food expense= "))
electricity= int(input("Enter total electricity spend= "))
charge_per_unit= int(input("Enter charge per unit= "))
persons= int(input("Enter the number of persons living in room/flat= "))
total_bill= electricity*charge_per_unit
output=(food+rent+total_bill)//persons
print("Each person will pay= ",output)