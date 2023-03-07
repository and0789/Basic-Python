weight = input("Enter your weight(kg)? ")
height = input("Enter your height(cm)? ")

height_to_meter = int(height) / 100
bmi = int(weight) / float(height_to_meter) ** 2
bmi_as_int = int(bmi)
print(f"your bmi is {bmi_as_int}")
