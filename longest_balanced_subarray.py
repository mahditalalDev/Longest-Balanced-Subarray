def find_longest_balanced_subarray(list):                           #O(1)
    counter_of_ones = 0                                             #O(1) 
    for i in range (len(list)):                                     #O(1) since len of list Constant  
        if list[i]==1:                                              #O(1)
            counter_of_ones +=list[i]                               #O(1)  
    if counter_of_ones > len(list)-counter_of_ones:                 #O(1)
            return( (len(list) - counter_of_ones ) %len(list))      #O(1)
    elif counter_of_ones < len(list)-counter_of_ones:               #O(1)
            return (len(list) % (len(list) - counter_of_ones))      #O(1)
    else:                                                           #O(1)
            return counter_of_ones                                  #O(1)

print(find_longest_balanced_subarray([1,1,1,0]))                    #O(1)