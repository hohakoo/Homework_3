###################################################### Задание 1
my_list = [1, 15, 104, 43, 233, 98, 10, 700, 58, 307]
for number in my_list:
    if number > 100:
        print(number)
###################################################### Задание 2
my_list = [1, 15, 104, 43, 233, 98, 10, 700, 58, 307]
my_results = []
for number in my_list:
    if number > 100:
        my_results.append(number)
print(my_results)
###################################################### Задание 3
my_list = [1, 15, 104, 43, 233, 98, 10, 700, 58, 307]
my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[-1] + my_list[-2])
print(my_list)
