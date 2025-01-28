rent=int(input("Enter monthly rent: "))
food=int(input("Total monthly food cost: "))
units=int(input("Total units spend: "))
charge=int(input("Charge per unit: "))
person=int(input("Enter no. of people: "))

sum=(rent+food+(units*charge))//person

print(f"Each person have to pay {int(sum)} amount.")
