weight = input("Enter your weight(kg)? ")
height = input("Enter your height(cm)? ")

height_to_meter = int(height) / 100
bmi = round(float(weight) / float(height_to_meter) ** 2, 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinical obese.")
