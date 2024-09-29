name = input("Please enter your first and last name: ")
split_name = name.split()
for i in split_name:
    x = len(i)
    if x < 2:
        print("Sorry this name isn't long enough.")
    else:
        print(x)