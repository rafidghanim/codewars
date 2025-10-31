def bmi(weight, height):
    #your code here
    return "Underweight" if weight / (height ** 2) <= 18.5 else "Normal" if weight / (height ** 2) <= 25 else "Overweight" if weight / (height ** 2) <= 30 else "Obese"
