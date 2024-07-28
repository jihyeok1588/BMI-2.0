# Enter your height in meters e.g., 1.55
height = float(input("what is your height?: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("what is your weight?: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height ** 2)
BMI_round = round(BMI, 1)
if BMI < 18.5:
  print(f"Your BMI is {BMI_round}, " + "you are under weight.")
elif BMI < 25:
  print(f"Your BMI is {BMI_round}, " +"you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI_round}, " +"you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI_round}, " +"you are obese.")
else:
  print(f"Your BMI is {BMI_round}, " +"you are clinically obese.")
