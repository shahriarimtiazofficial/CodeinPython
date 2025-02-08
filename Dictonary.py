
age_dict = {
    "Imtiaz": 23,
    "Shahriar": 24,
    "Md": 35
}
name = input("Enter a name to find their age: ")
if name in age_dict:
    print(f"{name}'s age is: {age_dict[name]}")
else:
    print("Sorry, that name is not in the dictionary.")
