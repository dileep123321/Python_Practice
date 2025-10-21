myage = list(range(18,26))
print(f"Myage is - {myage}")

while myage:
    print(f"Removing {myage[0]} from the list")
    del myage[0]
    print(myage)