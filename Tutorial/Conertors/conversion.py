birth_year = input("Enter your birth year: ")
year = 2022
# Due to input() only and always return string,
# Hence we will need to some conversion to int to do calculation
age = year - int(birth_year)
print(age)

# Other converters:
# String:str()
print(str(age)+' string value') # Convert and return you a string value
# Decimal: float()
print(float(year),' decimal value') # Convert and return a decimal value