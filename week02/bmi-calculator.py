#!/usr/bin/env python3

weight_kg = int(input())
height_cm = int(input())

h1 = height_cm / 100
bmi = weight_kg / (h1 ** 2)

if bmi < 18.5:
   category = "underweight"
elif 18.5 <= bmi < 25.0:
   category = "normal"
elif 25.0 <= bmi < 30.0:
   category = "overweight"
else:
   category = "obese"

print(f"{category}")
