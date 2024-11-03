def find_longest_balanced_subarray(list):
    counter_of_ones = 0
    for i in range (len(list)):
        if list[i]==1:
            counter_of_ones +=list[i]
    if counter_of_ones > len(list)-counter_of_ones:
            return( (len(list) - counter_of_ones ) %len(list))
    elif counter_of_ones < len(list)-counter_of_ones:
            return (len(list) % (len(list) - counter_of_ones))
    else:
            return counter_of_ones

print(find_longest_balanced_subarray([1,1,1,0]))