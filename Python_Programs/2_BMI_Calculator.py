# 2) BMI with elif

weight = float(input("Enter your weight in KG :"))
height = float(input("Enter your height in meter :"))

bmi = weight/height**2
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are Obese")
else:
    print(f"Your BMI is {bmi} and you are clinically Obese")