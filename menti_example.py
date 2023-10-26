
def find_strings_containing_a(list_of_strings):
    output_list = []
    for single_string in list_of_strings:
        if 'a' in single_string:
            output_list.append(single_string)
    return output_list

full_list = ['the mouse', 'some cats', 'a dog', 'people']
another_list = ['the banana', 'some apples', 'a dog', 'people']
result = find_strings_containing_a(list_of_strings = full_list)
result = find_strings_containing_a(list_of_strings = another_list)
print(result)