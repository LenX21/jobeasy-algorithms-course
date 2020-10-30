"""
Enter an irregular string (that means it may have space at the beginning of a string, 
at the end of the string, and words may be separated by several spaces). 
Make the string regular (delete all spaces at the beginning and end of the string, 
leave one space separating words).
"""
import string
import random
import timeit, inspect


def remove_space_split(s):
    return ' '.join(s.split())

def remove_space(s):
    import string
    word = ''
    result = []
    for i in range(len(s)):
        ele = s[i]
        if ele.isalpha() or ele in string.punctuation:
            word += ele
            if i == len(s)-1:
                result.append(word)
            continue
        if word:
            result.append(word)
            word = ''
    return ' '.join(result)


def random_sentence(word_size=15, irregular = False):
    if irregular:
        char_list = string.ascii_letters + ' '*40
        space = ''
    else:
        char_list = string.ascii_lowercase
        space = ' '
    sentence = ' '
    while len(sentence) <= 50:
        word = ''.join(random.choice(char_list) for _ in range(random.randint(2, word_size)))
        sentence += word + space
    print(f'Random sentence: {sentence}')
    if irregular:
        return sentence.strip()
    else:
        return sentence

def time_it(func, params):
    stp = inspect.getsource(func)
    name = func.__name__
    stmt = f"{name}('{params}')"
    print(timeit.timeit(setup=stp, stmt=stmt, number=10000))


if __name__ == "__main__":
    if input('Would you like to have a random input for your test? (y/n): ') == 'y':
        s = random_sentence(irregular = True)
    else:
        s = str(input('please  enter a string: '))
    print('Remove spaces using split() and join() methods:')
    print(remove_space_split(s))
    print('Remove spaces using for loop:')
    print(remove_space(s))
    s = '   test how    it works   !'
    assert remove_space_split(s) == 'test how it works !', 'Error. Unexpected result'
    assert remove_space(s) == 'test how it works !', 'Error. Unexpected result'
    print('--------------\nTime it:')
    time_it(remove_space_split, s)
    time_it(remove_space, s)
