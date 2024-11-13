def remove_all(xs, item_to_remove):
    # while item_to_remove in xs:
    #     xs.remove(item_to_remove)

    # return None
    


    if item_to_remove in xs:
        first_occurence = xs.index(item_to_remove)
        repeatedness_length = 0

        for i in range(first_occurence, len(xs)):
            if xs[i] == item_to_remove:
                repeatedness_length += 1
            else:
                del xs[first_occurence:first_occurence+repeatedness_length]
                break
                
        


    index = 0
    while item_to_remove in xs:
        if xs[index] == item_to_remove:
            xs.pop(index)
            if index != 0:
                index -= 1
        else:
            index += 1


lst = [1, 3, 1]
remove_all(lst, 1)
print(lst)


# def remove_all(xs, item_to_remove):
#     write_index = 0  # Initialize the write_index to 0

#     # Traverse through each element in xs
#     for i in range(len(xs)):
#         if xs[i] != item_to_remove:
#             # If the current element is not the item to remove, write it at write_index
#             xs[write_index] = xs[i]
#             write_index += 1

#     # Remove elements from write_index onwards
#     del xs[write_index:]
