
input_list = input("Enter a list of integers: ")
int_list = input_list.split()


largest = int(int_list[0])
for num in int_list:
    if int(num) > largest:
        largest = int(num)
print("The largest element is:", largest)
