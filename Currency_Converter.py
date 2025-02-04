def rupees(amount):
    print("Pounds: ",amount*0.0093)
    print("Dollar: ",amount*(1/87.08))
    print("Euro: ",amount*0.011)
    print("Bitcoin: ",amount*0.0000001)
    
def Euro(amount):
    print("Pounds: ",amount*0.83)
    print("Dollar: ",amount*(1/.96))
    print("Inr: ",amount*89.7)
    print("Bitcoin: ",amount*0.00001)

def Pound(amount):
    print("Euro: ",amount*1.2)
    print("Dollar: ",amount*(1/.8))
    print("Inr: ",amount*108)
    print("Bitcoin: ",amount*0.000013)
    
def Dollar(amount):
    print("Euro: ",amount*0.96)
    print("Pound: ",amount*0.80)
    print("Inr: ",amount*87.08)
    print("Bitcoin: ",amount*0.00001)
    
def Bitcoin(amount):
    print("Euro: ",amount*96479.65)
    print("Dollar: ",amount*99327.73)
    print("Inr: ",amount*8645568)
    print("Pound: ",amount*80102.38)
          
print("Welcome to Currency Converter")
print("Here you can convert currencies of these countries: ")
print("1) Rupees\n2) Euro\n3) Pound\n4) Dollar\n5) Bitcoin")
print("Choose from which currency")

c=int(input("Enter the no.: "))
amount=float(input("Enter the amount: "))

if c == 1:
    print(rupees(amount))
elif c == 2:
    Euro(amount)
elif c == 3:
    Pound(amount)
elif c == 4:
    Dollar(amount)
elif c == 5:
    Bitcoin(amount)
else:
    raise ValueError("You entered a wrong input")