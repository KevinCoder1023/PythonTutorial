# Create simple function that return value
def printWord(): print("HALO")


printWord()


# Create simple function that pass in props/parameters and return it
def showUser(name, age):
    if age >= 18:
        print("Hello " + str(name), "you are old")
    else:
        print("Hello " + str(name), "you are young")


showUser('Joel', 12)
