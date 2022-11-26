# TODO: Students' score:
# Grade A (100-80),
# Grade B (79-60),
# Grade C (59-50),
# Fail(lower than 50)

print("FAIL OR PASS")
student = input("What is your name?: ")
scores = int(input("What is your score?: "))
A = 'A',
B = 'B',
C = 'C',
F = 'FAIL'
resultPass = student, "You grade is"
resultFail = student, "You have", F
# elif = known as else if
if  scores >= 80:
    print(resultPass, A)
elif 79 > scores >= 60:
    print(resultPass, B)
elif 59 > scores >= 50:
    print(resultPass, C)
else:
    print(resultFail)
