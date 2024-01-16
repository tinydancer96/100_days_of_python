# a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It will tell the user the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

while True:
    try:
        height = float(input("Your height in metres: "))
        weight = int(input("Your weight in kilograms: "))
        bmi = weight / (height * height)
        break
    except ValueError:
        print("Please enter valid number")


if bmi >= 35:
  print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif bmi >= 30:
  print(f"Your BMI is {round(bmi)}, you are obese.")
elif bmi >= 25:
  print(f"Your BMI is {round(bmi)}, you are sligtly overweight.")
elif bmi >= 18.5:
  print(f"Your BMI is {round(bmi)}, you have a normal weight.")
else:
  print(f"Your BMI is {round(bmi)}, you are underweight.")
