
input_list = input("Enter a list of integers: ")
int_list = input_list.split()
for i in range(len(int_list)):
    int_list[i] = int(int_list[i])

unique_list = []
for num in int_list:
    if num not in unique_list:
        unique_list.append(num)

unique_list.sort(reverse=True)
final_list = []
for num in unique_list:
    if num % 3 != 0:
        final_list.append(num)

print("Modified list:", final_list)


