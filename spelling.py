word = input('write a word: ').lower()


if 'c' in word and 'ei' in word:
    ei_pos = word.index('ei')
    c_pos = word.index('c')
    if c_pos < ei_pos:
        print('pass')
elif 'ei' in word:
    print('fail')
elif 'ie' in word:
    print('pass')


