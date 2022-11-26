print("Pounds (lbs) vs Kilogram (kg)")
# to lbs needs multiple
# to kg needs divide
diff = 0.45
w = int(input("Weight?: "))
u = input("(K)g or (L)bs?: ")

if u.upper() == 'K':
    converted = w/diff
    print("Weight in Kg:", converted)
elif u.upper() == 'L':
    converted = w * diff
    print("Weight in Lbs:", converted)
else:
    print("Please enter the correct the value")