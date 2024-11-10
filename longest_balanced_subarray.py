def read_lists_from_user():
        """function to read list of 0s and 1s

        Returns:
            list: list of zeros and onces
        """
        user_list = input("Enter an list of (0s and 1s) separated by a space: ")
        user_list = list(map(int,user_list.split()))
        return user_list




def subarray_length(binary_list):
        MAX_COUNTER=0
        COUNTER=0
        for num in range (len(binary_list) - 1):
                if binary_list[num] != binary_list[num + 1]:
                        COUNTER+=1
                        if COUNTER > MAX_COUNTER:
                                MAX_COUNTER = COUNTER
                else:
                        COUNTER = 0
        return MAX_COUNTER + 1

BINARY_LIST = read_lists_from_user()
SUB_LIST = subarray_length(BINARY_LIST)
print(SUB_LIST)







# def find_longest_balanced_subarray(list):
#         """function that return longest balanced array of zeros and onces

#         Args:
#             list (): list of zeros and onces

#         Returns:
#             list: balanced sub array of zeros and onces
#         """
#         counter_of_ones = 0                                         
#         for i in range (len(list)):                                   
#                 if list[i]==1:                                       
#                         counter_of_ones +=list[i]                    
#         # Compare the count of ones to the count of zeros
#         if counter_of_ones > len(list)-counter_of_ones:              
#                 # Return the length of the zeros (balanced length)
#                 return( (len(list) - counter_of_ones ) %len(list)*2) 
#         elif counter_of_ones < len(list)-counter_of_ones:            
#                 # Return the length of the zeros (balanced length)
#                 return (len(list) % (len(list) - counter_of_ones)*2) 
#         else:                                                        
#                 return counter_of_ones*2                             


# user_list=read_lists_from_user()
# print(find_longest_balanced_subarray(user_list))

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