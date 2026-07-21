#Python Compound Interest Calculator

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero") 
    else:
       break

while True:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero")
    else:
     break

while True:
    time = int(input("Enter the time amount: "))
    if time <= 0:
        print("time can't be less than or equal to zero")
    else:
        break
 
print(principle)
print(rate)
print(time)

total = principle*pow((1+rate/100), time)
print(f"Balance after {time} year/s : ${total:.2f}")
