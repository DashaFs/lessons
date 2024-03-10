# task1
def upper():
    list_of_names =["john", "marta", "james", "amanda", "marianna"]
    capitalized_names  = [name.capitalize() for name in list_of_names]
    print(capitalized_names)

upper()


# #task2
def snake_case():
    camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
    snake_case_list = []
    for name in camel_case_list:
        snake_case_chars = []
        for char in name:
            if char.isupper():
                snake_case_chars.append("_")
                snake_case_chars.append(char.lower())
            else:
                snake_case_chars.append(char)
        snake_case_list.append(''.join(snake_case_chars).strip('_'))
    print(snake_case_list)

snake_case()

# task3

programming_languages = {"Python": "Guido van Rossum",
                         "Java": "James Gosling",
                         "C++": "Bjarne Stroustrup",
                         "JavaScript": "Brendan Eich"}
for lang, creator in programming_languages.items():
    print("My favorite programming language is {}. It was created by {}.".format(lang, creator))
del programming_languages['C++']
print(programming_languages)

# task4
def name_print():
    names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
    for name in names:
        if not isinstance(name, str):
            continue
        print(name)

name_print()

#task5

types=[1, 1000, 2, 12, {'key': 'value'}]
for item in types:
    if isinstance(item , int):
        print(item)
    else:
        break
print(f"The loop is not working with {type(item)}")


# task6

def count_characters():
    string = 'abcdefgabc'
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count


output = ' '.join([f"{char},{count}" for char, count in count_characters().items()])
print(output)

