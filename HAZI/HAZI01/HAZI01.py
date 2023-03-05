numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def subset(input_list, start_index, end_index):

    output_list = []
    for i in range(start_index, end_index):
        output_list.append(input_list[i])
    return output_list


print("subset")
print(subset(numbers, 2, 6))
print(subset([1, 2, 3, 4, 5], 1, 4))


def every_nth(input_list, step_size):
    output_list = []
    if len(input_list) > 0:
        output_list.append(input_list[0])
    for i in range(1, len(input_list)):
        if i % step_size == 0:
            output_list.append(input_list[i])
    return output_list


print("every_nth")
print(every_nth(numbers, 2))
print(every_nth([], 1))
print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))


def unique(input_list):
    uniques = []
    for i in input_list:
        if uniques.__contains__(i):
            return False
        else:
            uniques.append(i)
    return True


print("unique")
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


print("flatten")
print(flatten(nested_numbers))
print(flatten([]))


def merge_lists(*args):
    output_list = []
    for i in args:
        for j in i:
            output_list.append(j)
    return output_list


print("merege_lists")
print(merge_lists(nested_numbers, numbers))
print(merge_lists(numbers, numbers, numbers))
print(merge_lists([]))
tuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 0)]


def reverse_tuples(input_list):
    output_list = []
    for i in input_list:
        output_list.append((i[1], i[0]))
    return output_list


print("reverse_tuples")
print(reverse_tuples(tuples))
print(reverse_tuples([]))


def remove_duplicates(input_list):
    output_list = []
    for i in range(0, len(input_list)):
        if not (output_list.__contains__(i)):
            output_list.append(i)
    return output_list


print("remove duplicates")
print(remove_duplicates([0, 1, 4, 5, 0, 2, 4, 1, 23, 12, 123, 0]))


def transpose(input_list):
    output_list = []
    for i in range(0, len(input_list)):
        output_list.append([])
        for j in range(0, len(input_list[i])):
            output_list[i].append(input_list[j][i])
    return output_list


print("array")
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
print("transpose")
print(transpose(arr))


def split_into_chunks(input_list, chunk_size):
    output_list = []
    current_chunk = 0
    chunk_number = -1
    for i in range(len(input_list)):
        if current_chunk == 0:
            output_list.append([])
            chunk_number += 1
        output_list[chunk_number].append(input_list[i])
        current_chunk += 1
        if current_chunk == chunk_size:
            current_chunk = 0

    return output_list


print("split_into_chunks")
print(split_into_chunks([1, 2, 3, 4, 5, 6, 7, 8], 3))


def merge_dicts(*args):
    output_dict = {}
    for i in args:
        for key, value in i.items():
            output_dict[key] = value
    return output_dict


print('merge_dicts')
print(merge_dicts({'one': 1, 'two': 2}, {'four': 4, 'three': 3}))


def by_parity(input_list):
    output_dict = {'even': [], 'odd': []}
    for i in input_list:
        if i % 2 == 0:
            output_dict['even'].append(i)
        else:
            output_dict['odd'].append(i)
    return output_dict


print("by_parity")
print(by_parity([1, 2, 3, 4, 5, 6]))


def mean_key_value(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        count = len(input_dict[key])
        sum = 0
        for i in input_dict[key]:
            sum += i
        mean = sum/count
        output_dict[key] = mean
    return output_dict

print("mean key value")
print(mean_key_value({"some_key":[1, 2, 3, 4], "another_key":[1, 2, 3, 4]}))
