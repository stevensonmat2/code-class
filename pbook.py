phone_book = {'matt': 1234567890, 'joe': 9876543210}

def phonebook():
   while True:
       menu = input("""
                       1. Search
                       2. Add Entry
                       3. Change Entry
                       4. Delete Entry
                       5. Exit Program
                       6. Print Phonebook
                       Please choose from menu: """)
       if menu == "1":
           query = input('Enter name: ')
           try:
                entry = phone_book[query]
           except KeyError:
               print('not in phone book')
               continue
           print(query, phone_book[query])

       elif menu == "2":
           name = input("Enter a name to add to your phonebook: ")
           number = input("Enter their number: ")
           phone_book[name] = number
           print(name + " added to phonebook with the number: " + number)
           pass

       elif menu == "3":
           query = input('Enter a name to change: ')
           query_n = input('New number: ')
           del phone_book[query]
           phone_book[query] = query_n
           print(phone_book)
           pass

       elif menu == "4":
           query = input('Enter a name to delete: ')
           del phone_book[query]
           print(phone_book)
           pass

       elif menu == "5":
           quit()

       elif menu == "6":
           print(phone_book)

phonebook()
