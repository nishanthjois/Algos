# Each order is represented by an "order id" (an integer).

# We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

# def merge_list(my_list, alice_list):
# 	len_merged_list = len(my_list)+len(alice_list)
# 	index_my_list = 0
# 	index_alice_list=0
# 	index_merged_list = 0
# 	merged_list = len_merged_list*[None]



# 	while index_merged_list < len_merged_list:
# 		exhausted_my_list = index_my_list>=len(my_list)
# 		exhausted_alice_list = index_alice_list>=len(alice_list)

# 		if not exhausted_my_list and ((my_list[index_my_list]<alice_list[index_alice_list]) or exhausted_alice_list):
# 			merged_list[index_merged_list]=my_list[index_my_list]
# 			index_my_list+=1

# 		else:
# 			merged_list[index_my_list]=my_list[index_alice_list]
# 			index_alice_list+=1

# 		index_merged_list+=1

# 	return merged_list


def merge_lists(my_list, alices_list):

    # set up our merged_list
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0

    while current_index_merged < merged_list_size:

        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alices_list_exhausted = current_index_alices >= len(alices_list)

        # case: next comes from my list
        # my list must not be exhausted, and EITHER:
        # 1) Alice's list IS exhausted, or
        # 2) the current element in my list is less
        #    than the current element in Alice's list
        if not is_my_list_exhausted and (is_alices_list_exhausted or \
                (my_list[current_index_mine] < alices_list[current_index_alices])):

            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1

        # case: next comes from Alice's list
        else:
            merged_list[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1

        current_index_merged += 1

    return merged_list

print (merge_lists([2,4,7],[1,3,5]))
