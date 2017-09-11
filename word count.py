import string
import operator

text_file = open('test.txt', "r", encoding="utf8")

text = text_file.read().lower()

new_string = ""

for letter in text:
    if letter not in string.punctuation:
        new_string += letter

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

# print(new_string)
word_list = list(word_count(text).items())
word_list_sorted = sorted(word_list, key=operator.itemgetter(1), reverse=True)[:10]
for x,y in word_list_sorted:
    print("{} - {}.".format(x,y))

# print(word_list)
# print(list)
#
# print(sorted(list))




# print( word_count(fff))



# print(new_string)

# print( word_count(fff))
#
# words = open('test.txt').read().lower().split()











