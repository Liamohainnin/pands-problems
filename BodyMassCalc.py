# This Program calculates body mass  index

#  Input parameters
Height = float(input ("Enter Height in Centimetres : "))
Weight = float(input ("Enter weight in Kilos :"))

# Calculation
BMI = Weight / (Height/100 * Height/100)

# Output Results
print ("Your BMI ",round (BMI,2))