#no case statements in python

Grade = input("Enter Your Grade : ").upper()

if Grade == "A":
    print("Top Grade")
elif Grade in ("U", "F"):
    print("Fail")
elif Grade in ("B", "c", "D", "E"):
    print("pass")
else:
    print("Invalid Grade")