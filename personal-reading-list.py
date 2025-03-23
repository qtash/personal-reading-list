# CAPSTONE PROJECT - QONITA SHOBRINA
# PERSONAL READING LIST

# ==================== DATA =======================

# owner nickname
owner = 'avid reader wannabe'

# initial data
titles = ["The World According to Anna", 'The Da Vinci Code' ,'Oliver Twist', 'Viper', 'The Mountain is You', 'Rebel Skies', 'Saltblood']
genres = ['PHYL', 'MYST', 'CLAS', 'FTSY', 'SLFG', 'FTSY', 'FICT']
total_pages = [240, 448, 660, 436, 245, 339, 337]
current_pages = [240, 448, 16, 436, 16, 182, 61]
index = [i for i in range(len(titles))]

# make DICTIONARY
library = {
    'Index'         : index,
    'Title'         : titles, 
    'Genre'         : genres, 
    'Total Pages'   : total_pages,
    'Current Page'  : current_pages
}


# ==================== FUNCTIONS ==========================

# 1. Menu
def menu():
    print("""\n> What's now lads?
        1. Show the reading list
        2. Update reading checkpoint 
        3. Add Book(s) to the reading list
        4. Delete Book(s) from the reading list
        5. Quit \n""")

# 2. SHOW/READ reading list
def reading_list():
    print("\n== Your Reading List ==\n")
            
    for key in library.keys():
        print(key, end="\t | ")
    print()

    for i in range(len(library["Index"])):
        # print(i)
        for k in library.keys():
            # print(k)
            print(library[k][i], end="\t | ")
        print()

# 3. UPDATE reading checkpoint --> current_page
def update_cp(index_up, cpage_up):
    # update value in list of current pages of the indexed book
    current_pages[index_up] = cpage_up
    # update values for 'current page' key
    library.update({"Current Page" : current_pages})

# 4. ADD book data
def add_book(title_add, genre_add, tpage_add, cpage_add):
    # add new index based on how many existing data (which index starts at 0)
    index_add = int(len(library["Index"]))

    # add new values to each key's list
    index.append(index_add)
    titles.append(title_add)
    genres.append(genre_add)
    total_pages.append(tpage_add)
    current_pages.append(cpage_add)

    # update dict with the updated list of values
    library.update({"Index" : index})
    library.update({"Title" : titles})
    library.update({"Genre" : genres})
    library.update({"Total Pages" : total_pages})
    library.update({"Current Page" : current_pages})

# 5. DELETE book data
def del_book(index_del):
    # delete book data on every key's list value
    titles.pop(index_del)
    genres.pop(index_del)
    total_pages.pop(index_del)
    current_pages.pop(index_del)

    # renew index (-1) & update dict data
    index = [i for i in range(len(titles))]

    # update dict with the updated list of values
    library.update({"Index" : index})
    library.update({"Title" : titles})
    library.update({"Genre" : genres})
    library.update({"Total Pages" : total_pages})
    library.update({"Current Page" : current_pages})


# ==================== PROGRAM ======================

# greeting
print(f'\nHeya {owner}!')

# PROGRAM'S LOOPING     
while True:
    menu()
    command = int(input("> Pick the number (1-5)! "))

    # 1. Show reading list -- READ
    if command == 1:
        reading_list()
        continue

    # 2. Update reading checkpoint  -- UPDATE
    elif command == 2:
        # show reading list to help user located the to-be-updated book's index
        reading_list()

        print("\n> Let's record your reading progress^^")

        # user input book's index & the new current page
        index_up = int(input("\nBook's index : "))
        cpage_up = int(input("The page you will continue later : "))

        # updating process
        update_cp(index_up, cpage_up)

        # show updated reading list 
        reading_list()

        # success prompt
        print(f"\n> Current page of '{titles[index_up]}' is up-to-date! I hope you enjoy what you've read^^")
        continue

    # 3. Add book   -- ADD
    elif command == 3:
        print("\n> New book? @.@ Again? xD")
        # show the current reading list
        reading_list()

        while True:
            # recheck prompt
            r3_command = input("\n> Are you sure it's not already on the list? (Y/N): ")

            if r3_command == "Y":
                print("OK! Let's add this fella in!")

                # fill value to parameters  
                title_add = input("\nBook Title : ")
                genre_add = input("Genre : ")
                tpage_add = int(input("Total Pages : "))
                cpage_add = int(input("The page you will continue at : "))

                # add book function
                add_book(title_add, genre_add, tpage_add, cpage_add)

                # show updated reading list 
                reading_list()

                # success prompt
                print(f"\n> '{title_add}' has been successfully added to your reading list! Good luck on finishing that <3")
                break

            elif r3_command == "N":
                print("\n> See? It's already there *^^*")
                break
            
            else: 
                print("\n> I don't understand your command =.=' I will ask again:")

        continue

    # 4. Delete book    -- DELETE
    elif command == 4:
        print("\n> You want to delete a book?? Why?! @.@!")
        print("> Anyway, OK. I shall do as you command ^-^")

        # show the current reading list
        reading_list()
        
        # user input index for the to-be deleted book
        index_del = int(input("\n> What's the Book's Index? "))  
    
        # save book title
        deleted_book = titles[index_del]

        while True: 
            r4_command = input(f"\n> Are you sure that you want to delete '{deleted_book}' data from your reading list? (Y/N): ")

            if r4_command == "Y":
                del_book(index_del)

                # show updated reading list 
                reading_list()

                # success prompt
                print(f"\n> '{deleted_book}' has been successfully deleted! I hope you will not regret it ^^")
                break

            elif r4_command == "N":
                print("\n> OK^^")
                break
                
            else: 
                print("\n> I don't understand your command =.=' I will ask again:")

        continue
    
    # if command = 5 --> QUIT LOOP 
    elif command == 5:
        break 

    # if else return error and let user to put the correct command (1-5)
    else:           
        print("\n> ERROR! Command not found. Try Again!")