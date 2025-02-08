def process_list():
    ui = input("Enter a list of integers: ")
   
    int_list = [int(x) for x in ui.split()]

    
    int_list = list(set(int_list))
    print("List after removing duplicates:", int_list)

    int_list.sort(reverse=True)
    print("List after sorting in descending order:", int_list)

    new_list = []
    for num in int_list:
        if num % 3 != 0:
            new_list.append(num)
           
    return new_list

modified_list = process_list()
print("Final New Modified List:", modified_list) 
