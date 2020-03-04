def dont_give_me_five_mine(start,end):
#    numberrange = range(start,end)
#    stringednumbers = ""
#    for i in numberrange:
#        stringednumbers += str(i) + " "
#    arrayednumbers = stringednumbers.split(" ")
#    for i in arrayednumbers:
#        if "5" in i:
#            arrayednumbers.pop(arrayednumbers.index(i))
#    print(arrayednumbers)
#    return print(len(arrayednumbers))
# array = [expression for value in array]
    my_array = len([str(i) for i in range(start,end+1) if '5' not in i])+1
    return print(my_array)
dont_give_me_five_mine(100,180)

def dont_give_me_five(start, end):
    return print(sum('5' not in str(i) for i in range(start, end + 1)))

dont_give_me_five(100,180)
