#task1
def palindromes():
    word = input('Enter the word:')
    reversed_word = word[::-1]
    if word == reversed_word:
        print('+')
    else:
        print('-')

palindromes()

#task2
def word_in_sentence():
    sentence = input('Enter the sentence:')
    word  = input('Enter the word:')
    if word in sentence.split(' '):
        print('Yes')
    else:
        print('No')

word_in_sentence()

#task3
def email_check():
    email = input('Enter your email: ')
    if email.__contains__('@') and email.__contains__('.'):
        print('YES')
    else:
        print('NO')

email_check()

#task4
def three_last_element():
    text = input('Enter text:')
    print(text.split(' ')[-3:])

three_last_element()
