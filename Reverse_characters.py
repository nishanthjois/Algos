def reverse_characters(message_list, front_index, back_index):

    # walk towards the middle, from both sides

    while front_index < back_index:

        # swap the front char and back char
        message_list[front_index], message_list[back_index] = message_list[back_index], message_list[front_index]

        front_index += 1
        back_index  -= 1

    return message_list


msg = "the ind world"
msg = list (msg)
print (reverse_characters(msg, 0, len(msg)-1))



