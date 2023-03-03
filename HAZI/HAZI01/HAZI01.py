numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def subset(input_list, start_index, end_index):

    output_list = []
    for i in range(start_index, end_index):
        output_list.append(input_list[i])
    return output_list


print(subset(numbers, 2, 6))


def every_nth(input_list, step_size):
    output_list = []
    for i in input_list:
        if i % step_size == 0:
            output_list.append(input_list[i])
    return output_list


print(every_nth(numbers, 2))
print(every_nth([], 1))


def unique(input_list):
    uniques = []
    for i in input_list:
        if uniques.__contains__(i):
            return False
        else:
            uniques.append(i)
    return True


print(unique(numbers))
print(unique([0, 1, 4, 5, 0, 2, 4, 1, 23, 12, 123, 0]))
print(unique([]))
nested_numbers = [[1, 0], [2, 9], [3, 8], [4, 7], [5, 6]]


def flatten(input_list):
    output_list = []
    for i in input_list:
        for j in i:
            output_list.append(j)
    return output_list


print(flatten(nested_numbers))
print(flatten([]))


def merge_lists(*args):
    output_list = []
    for i in args:
        for j in i:
            output_list.append(j)
    return output_list


print(merge_lists(nested_numbers, numbers))
print(merge_lists(numbers, numbers, numbers))
print(merge_lists([]))
tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0)]


def reverse_tuples(input_list):
    output_list = []
    for i in input_list:
        output_list.append((i[1], i[0]))
    return output_list


print(reverse_tuples(tuples))
print(reverse_tuples([]))


def remove_tuplicates(input_list):
    output_list = []
    for i in input_list:
        if ~(output_list.__contains__(i)):
            output_list.append(i)
    return output_list


print(remove_tuplicates([0, 1, 4, 5, 0, 2, 4, 1, 23, 12, 123, 0]))


#def transpose(input_list):
#    output_list = []
#    for i in range(0,len(input_list)):
#        for j in range(0,len(input_list[i])):
#            output_list[j][i].append(input_list[i][j])
#    return output_list


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
#print(transpose(arr))
