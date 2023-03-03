
greeting = 'Hello World!'
print(greeting)

def printer(to_print):
    for letter in to_print:
        print(letter)

printer(greeting)
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1
    numbers = [1, 2, 5, 2, 7, 3, 0]
    del numbers[0]
    numbers[2] = 12
    numbers.append(100)
    print(numbers)
    for value in person.values():
        print(value)

    odd_numbers = (1, 3, 5, 7)
    even_numbers = (2, 4, 6)
    all_numbers =(*odd_numbers, *even_numbers)
    print(all_numbers)


person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 25,
    'favorite_colors': ['blue','green'],
    'active' : True
}

main()

