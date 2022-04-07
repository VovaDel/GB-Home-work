my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length_of_list: int = (len(my_list))
store_id = id(my_list)
for _ in range(len(my_list)):
    elem = my_list.pop()
    if elem.isdigit():
        my_list.append(f'"{int(elem):02d}"')
    elif elem[0] == '+' and elem[1].isdigit():
        my_list.append(f'"+{int(elem):02d}"')
    else:
        my_list.append(elem)
print(my_list)
print(' '.join(my_list))


