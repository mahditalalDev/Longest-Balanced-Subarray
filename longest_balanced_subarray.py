
def find_longest_balanced_subarray(list):                           #O(1)
    counter_of_ones = 0                                             #O(1) 
    for i in range (len(list)):                                     #O(1) since len of list Constant  
        if list[i]==1:                                              #O(1)
            counter_of_ones +=list[i]                               #O(1)  
    # Compare the count of ones to the count of zeros
    if counter_of_ones > len(list)-counter_of_ones:                 #O(1)
            # Return the length of the zeros (balanced length)
            return( (len(list) - counter_of_ones ) %len(list)*2)      #O(1)
    elif counter_of_ones < len(list)-counter_of_ones:               #O(1)
            # Return the length of the zeros (balanced length)
            return (len(list) % (len(list) - counter_of_ones)*2)      #O(1)
    else:                                                           #O(1)
            return counter_of_ones*2                                  #O(1)

print(find_longest_balanced_subarray([1,1,0,0,0,0,1]))                    #O(1)






# def second_solution(list):
#         zeros_counter=0
#         onces_counter=0
#         for i in range (len(list)):
#                 if list[i]==0:
#                         zeros_counter+=1
#                 else:
#                         onces_counter+=1
#         return (min(zeros_counter,onces_counter)*2)
                
# print(second_solution([1,1,1,0,0,0,0,1,0]))