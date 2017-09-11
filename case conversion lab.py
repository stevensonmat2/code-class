
word = input("Enter word: ")

def define_case():
   if '_' in word:
        print('you word is snake_case')

define_case()

def define_upp():

    if word[0].isupper():
        # if word[0:] in caps:
         print("your word is CamelCase")
    else:
        print('invalid')

define_upp()
