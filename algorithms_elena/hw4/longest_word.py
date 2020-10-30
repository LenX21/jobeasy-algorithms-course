"""
Enter a string of words separated by spaces. 
Find the longest word. (split / join methods)
"""
import string
import random
import timeit

def count_words(s):
    max_count, counter = 0, 0
    word, max_result = '', ''
    for i in range(len(s)):
        if not s[i].isalpha() or i == len(s)-1:
            if i == len(s) - 1 and s[i].isalpha():
                counter +=1
                word+=s[i]
            if max_count < counter:
                max_count = counter
                max_result = word
            counter = 0
            word = ''
            continue
        counter +=1
        word += s[i]

    return max_result, max_count


def count_split(s):
    w = s.split()
    word = max(w, key =lambda x: len(x))
    return word, len(word)


def random_sentence(word_size=15, irregular = False):
    if irregular:
        char_list = string.ascii_letters + ' '*40
    else:
        char_list = string.ascii_lowercase
    sentence = ' '
    while len(sentence) <= 50:
        word = ''.join(random.choice(char_list) for _ in range(random.randint(2, word_size)))
        sentence += word + ' '
    print(f'Random sentence: {sentence}')
    if irregular:
        return sentence.strip()
    else:
        return sentence


def time_it():
    print('--------------\nTime it:')
    stp= """
def count_words(s):
    max_count, counter = 0, 0
    word, max_result = '', ''
    for i in range(len(s)):
        if not s[i].isalpha() or i == len(s)-1:
            if i == len(s) - 1 and s[i].isalpha():
                counter +=1
                word+=s[i]
            if max_count < counter:
                max_count = counter
                max_result = word
            counter = 0
            word = ''
            continue
        counter +=1
        word += s[i]
    
    return max_result, max_count
    
    
def count_split(s):
    w = s.split()
    word = max(w, key =lambda x: len(x))
    return word, len(word)
"""
    print(timeit.timeit(setup = stp, stmt = 'count_split("a bb ccc dddd w")', number = 10000))
    print(timeit.timeit(setup = stp, stmt = 'count_words("a bb ccc dddd w")', number = 10000))


if __name__ == '__main__':
    if input('Would you like to use random sentence(y/n): ') == 'y':
        s = random_sentence()
    else:
        s = str(input('enter: '))
    print('Return last encountered word:')
    print(count_words(s))
    print('Return first encountered word:')
    print(count_split(s))
    s = 'a bb ccc dddd w'
    assert count_words(s) == ('dddd', 4), 'Error. Unexpected result!'
    assert count_split(s) == ('dddd', 4), 'Error. Unexpected result!'
    time_it()
