import os
import time
import sys
import datetime

os.system("mode con cols=150 lines=150") # Resize a console window ("DOS prompt") to 150 columns of 150 lines

# Create list-----------------------------------------------------------------------------------------------------------------------------------------------
acc_num = []
acc_ID = []
acc_name = []
acc_type = []
exp_date = []
acc_borrow = []

book_num = []
book_callnum = []
book_barcode = []
book_isbnnum = []
book_title = []
book_author = []
book_availability = []

chkout_num=[]
chkout_ID = []
chkout_barcode = []
chkout_strt = []
chkout_end = []

chkin_num=[]
chkin_ID = []
chkin_barcode = []
chkin_return = []

# Open text file--------------------------------------------------------------------------------------------------------------------------------------------
def OpenFile():
    acc_num.clear() # clear() empty the given list
    acc_ID.clear()
    acc_name.clear()
    acc_type.clear()
    exp_date.clear()
    acc_borrow.clear()

    book_num.clear()
    book_callnum.clear()
    book_barcode.clear()
    book_isbnnum.clear()
    book_title.clear()
    book_author.clear()
    book_availability.clear()

    chkout_num.clear()
    chkout_ID.clear()
    chkout_barcode.clear()
    chkout_strt.clear()
    chkout_end.clear()

    chkin_num.clear()
    chkin_ID.clear()
    chkin_barcode.clear()
    chkin_return.clear()

    count=0
  
    if os.access("accountlist.txt",os.F_OK): # Test existence of "accountlist.txt" text file
        with open("accountlist.txt", "r") as account_list: # Open "accountlist.txt" text file
            for account in account_list:
                acc = account[:-1].split("|")
                acc_num.append(acc[0])
                acc_ID.append(acc[1])
                acc_name.append(acc[2])
                acc_type.append(acc[3])
                exp_date.append(acc[4])
                acc_borrow.append(acc[5])
        account_list.close() # Close "accountlist.txt" text file
    else:
        print("\t\t\t\t\t\t\t\u001b[0mCould not open accountlist.txt file.") # \u001b[0m is to set console text colour back to white
        count += 1

    if os.access("booklist.txt",os.F_OK): # Test existence of "booklist.txt" text file    
        with open("booklist.txt", "r") as book_list: # Open "booklist.txt" text file
            for book in book_list:
                bk = book[:-1].split("|")
                book_num.append(bk[0])
                book_barcode.append(bk[1])
                book_callnum.append(bk[2])
                book_isbnnum.append(bk[3])
                book_title.append(bk[4])
                book_author.append(bk[5])
                book_availability.append(bk[6])
        book_list.close() # Close "booklist.txt" text file
    else:
        print("\t\t\t\t\t\t\t\u001b[0mCould not open booklist.txt file.") # \u001b[0m is to set console text colour back to white
        count += 1

    if os.access("checkout.txt",os.F_OK): # Test existence of "checkout.txt" text file
        with open("checkout.txt", "r") as checkout_list: # Open "checkout.txt" text file
            for checkout in checkout_list:
                chkout = checkout[:-1].split("|")
                chkout_num.append(chkout[0])
                chkout_ID.append(chkout[1])
                chkout_barcode.append(chkout[2])
                chkout_strt.append(chkout[3])
                chkout_end.append(chkout[4])
        checkout_list.close() # Close "checkout.txt" text file
    else:
        print("\t\t\t\t\t\t\t\u001b[0mCould not open checkout.txt file.") # \u001b[0m is to set console text colour back to white
        count += 1

    if os.access("checkin.txt",os.F_OK): # Test existence of "checkin.txt" text file
        with open("checkin.txt", "r") as checkin_list: # Open "checkin.txt" text file
            for checkin in checkin_list:
                chkin = checkin[:-1].split("|")
                chkin_num.append(chkin[0])
                chkin_ID.append(chkin[1])
                chkin_barcode.append(chkin[2])
                chkin_return.append(chkin[3])
        checkin_list.close() # Close "checkin.txt" text file
    else:
        print("\t\t\t\t\t\t\t\u001b[0mCould not open checkin.txt file.") # \u001b[0m is to set console text colour back to white
        count += 1

    if count>0:
        print("\t\t\t\t\tPlease make sure that the text file(s) exist along with the program")
        exit() # Exit the program

# Security access system for user---------------------------------------------------------------------------------------------------------------------------
def Security():
    username = input("\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tEnter Username: ") # Username as "system"
    password = input("\t\t\t\t\t\t\t\tEnter Password: ") # Password as "root"
    for x in range(0, 3): # Start at 0, increase by 1 and end at 3
        sys.stdout.write("\r\t\t\t\t\t\t\t\tLoading...")
        time.sleep(0.5) # Suspend execution for 0.5 seconds
        sys.stdout.write("\r\t\t\t\t\t\t\t\t          ")
        time.sleep(0.3) # Suspend execution for 0.3 seconds
    while username != "system" or password != "root":
        print("\n\n\t\t\t\t\t\t\t\tUsername or Password did not match!\n\t\t\t\t\t\t\t\tPlease try again.")
        time.sleep(1) # Suspend execution for 1 seconds
        os.system("cls") # Clear screen
        username = input("\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\tEnter Username: ")
        password = input("\t\t\t\t\t\t\t\tEnter Password: ")
        for x in range(0, 3):
            sys.stdout.write("\r\t\t\t\t\t\t\t\tLoading...")
            time.sleep(0.5) # Suspend execution for 0.5 seconds
            sys.stdout.write("\r\t\t\t\t\t\t\t\t          ")
            time.sleep(0.3) # Suspend execution for 0.3 seconds
    if username != "system" or password != "root":
        print("\n\n\t\t\t\t\t\t\t\tLogin successful!")
        time.sleep(1) # Suspend execution for 1 seconds

# Display Main menu ----------------------------------------------------------------------------------------------------------------------------------------
def MainMenu():
    os.system("cls") # Clear screen
    print("\n")
    print("\t\t\t\t\t\u001b[36m   __________________________________________________________________\n") # \u001b[36m is to set console text colour to cyan
    print("\t\t\t\t\t   __________________________________________________________________\n")
    print("\t\t\t\t\t  |                                                                |\n")
    print("\t\t\t\t\t  |                         Library System                         |\n")
    print("\t\t\t\t\t  |                         ''''''''''''''                         |\n")
    print("\t\t\t\t\t  |                                                                |\n")
    print("\t\t\t\t\t  |           >>1. Book List                                       |\n")
    print("\t\t\t\t\t  |           >>2. Search Book                                     |\n")
    print("\t\t\t\t\t  |           >>3. Check Out Book                                  |\n")
    print("\t\t\t\t\t  |           >>4. Check In Book                                   |\n")
    print("\t\t\t\t\t  |           >>5. Account & Membership Maintenance                |\n")
    print("\t\t\t\t\t  |           >>6. Book Management                                 |\n")
    print("\t\t\t\t\t  |           >>7. Record                                          |\n")
    print("\t\t\t\t\t  |           >>8. <COMING SOON> Fines and Penalties               |\n")
    print("\t\t\t\t\t  |           >>9. Exit                                            |\n")
    print("\t\t\t\t\t  |                                                                |\n")
    print("\t\t\t\t\t  |________________________________________________________________|\n")
    print("\t\t\t\t\t__________________________________________________________________\n\n")

# Book list-------------------------------------------------------------------------------------------------------------------------------------------------
def BookList():
    os.system("cls") # Clear screen
    repeat_booklist = True
    while repeat_booklist == True:
        os.system("cls") # Clear screen
        print("\u001b[33m\t\t\t\tNo.\t\t\t\tBook Title") # \u001b[33m is to set console text colour to yellow
        print("-"*150)
        for x in range(len(book_num)): 
            print("\t\t\t\t", book_num[x], "\t", book_title[x]) # Display book list(No. and book title)
        print("-"*150)
        print("\n\t\t\t\tTo view the details of the book, please enter the No..")
        bk_num = input("\t\t\t\tNo.(Press '0' if don't want to proceed): ") # Enter '0' to display ReturnExit()

        while bk_num != "0" and bk_num not in book_num:
            print("\t\t\t\tThe number is invalid, no book is found with the number. Please try again. ")
            bk_num = input("\t\t\t\tNo.(Press '0' if don't want to proceed): ") # Enter '0' to display ReturnExit()

        if bk_num != "0":
            for i in range(len(book_num)):
                if bk_num == book_num[i]: # Display information of book 
                    print("\n\n\t\t\t\tInformation of Book Selected\n")
                    print("\t\t\t\tBook Title\t\t\t\t\t: ", book_title[i])
                    print("\t\t\t\tBook Author\t\t\t\t\t: ", book_author[i])
                    print("\t\t\t\tBarcode\t\t\t\t\t\t: ", book_barcode[i])
                    print("\t\t\t\tCall Number\t\t\t\t\t: ", book_callnum[i])
                    print("\t\t\t\tISBN Number\t\t\t\t\t: ", book_isbnnum[i])
                    print("\t\t\t\tNumber of book(s) available to be borrowed\t: ", book_availability[i])
                    print() # For new line
                    os.system("pause") # Display a message 'Press any key to continue . . .'
        else:
            repeat_booklist = False # Display ReturnExit()

# Search book-----------------------------------------------------------------------------------------------------------------------------------------------
def SearchBook():
    repeat_search=True
    while repeat_search==True:
        os.system("cls") # Clear screen                            # Display search book menu 
        print("\n\n\t\t\t\t\t\t\t\t\u001b[35m1.Search by Barcode") # \u001b[35m is to set console text colour to magenta
        print("\t\t\t\t\t\t\t\t2.Search by Call number")
        print("\t\t\t\t\t\t\t\t3.Search by ISBN number")
        print("\t\t\t\t\t\t\t\t4.Search by Title")
        print("\t\t\t\t\t\t\t\t5.Search by Author")
        srch_opt = input("\n\t\t\t\t\t\tSelect your option[1-5] (Press '0' to back to Main Menu):") # Enter '0' to display ReturnExit()
        while srch_opt < "0" or srch_opt > "5":
            print("\t\t\t\t\t\tInvalid input!!")
            print("\t\t\t\t\t\tPlease enter valid option from '0' to '5'.")
            srch_opt = input("\t\t\t\t\t\tSelect your option:")

        if srch_opt =="0":
            break # Terminate the loop
        else:
            if srch_opt == "1": #Search by barcode
                repeat = "1"
                while repeat == "1":
                    srch = input("Enter barcode >>")
                    count = 0
                    num = 1
                    title_flag = True
                    for i in book_barcode:
                        if srch in i:
                            if title_flag == True:
                                print("\nNo.\t  Barcode\t  Call Number\t\t\t  ISBN Number\t\t\t\t\t Book Title")
                                title_flag = False # Show the title flag once
                            print(num, "\t", i, "\t", book_callnum[count], "\t\t", book_isbnnum[count], "\t\t", book_title[count])
                            num += 1
                            count += 1

                    if count == 0:
                        print("Error! There is no record. Please try again.")

                    repeat = input("\n\nDo you want to repeat search by barcode? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search
                    os.system("cls") # Clear screen

                    while repeat < "0" or repeat > "1":
                        print("Invalid input!!")
                        print("Please enter valid option from '0' to '1'.")
                        repeat = input("Do you want to repeat search by barcode? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search

            elif srch_opt == "2": # Search by call number
                repeat = "1"
                while repeat == "1":
                    srch = input("Enter Call no. >>")
                    count = 0
                    num = 1
                    title_flag = True
                    for i in book_callnum:
                        if srch in i:
                            if title_flag == True:
                                print("\nNo.\t  Barcode\t  Call Number\t\t\t  ISBN Number\t\t\t\t\t Book Title")
                                title_flag = False # Show the title flag once
                            print(num, "\t", book_barcode[count], "\t", i, "\t\t", book_isbnnum[count], "\t\t", book_title[count])
                            num += 1
                            count += 1

                    if count == 0:
                        print("Error! There is no record. Please try again.")
                    repeat = input("\n\nDo you want to repeat search by call number? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search
                    os.system("cls") # Clear screen

                    while repeat < "0" or repeat > "1":
                        print("Invalid input!!")
                        print("Please enter valid option from '0' to '1'.")
                        repeat = input("Do you want to repeat search by call number? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search

            elif srch_opt == "3": # Search by ISBN number
                repeat = "1"
                while repeat == "1":
                    srch = input("Enter ISBN no. >>")
                    count = 0
                    num = 1
                    title_flag = True
                    for i in book_isbnnum:
                        if srch in i:
                            if title_flag == True:
                                print("\nNo.\t  Barcode\t  Call Number\t\t\t  ISBN Number\t\t\t\t\t Book Title")
                                title_flag = False # Show the title flag once
                            print(num, "\t", book_barcode[count], "\t", book_callnum[count], "\t\t", i, "\t\t", book_title[count])
                            num += 1
                            count += 1

                    if count == 0:
                        print("Error! There is no record. Please try again.")
                    repeat = input("Do you want to repeat search by ISBN number? (0 - No / 1 - Yes) >>")  # Enter 0 return to search book menu, enter 1 will repeat search
                    os.system("cls") # Clear screen

                    while repeat < "0" or repeat > "1":
                        print("Invalid input!!")
                        print("Please enter valid option from '0' to '1'.")
                        repeat = input("Do you want to repeat search by ISBN number? (0 - No / 1 - Yes) >>")  # Enter 0 return to search book menu, enter 1 will repeat search

            elif srch_opt == "4": # Search by title
                repeat = "1"
                while repeat == "1":
                    srch = input("Enter book title >>")
                    count = 0
                    num = 1
                    title_flag = True
                    for i in book_title:
                        if srch.capitalize() in i: # capitalize() is to convert first character of a string to uppercase letter and lowercases all other characters, if any
                            if title_flag == True:
                                print("\nNo.\t  Barcode\t  Call Number\t\t\t  ISBN Number\t\t\t\t\t Book Title")
                                title_flag = False # Show the title flag once
                            print(num, "\t", book_barcode[count], "\t", book_callnum[count], "\t\t", book_isbnnum[count], "\t\t", i)
                            num += 1
                            count += 1

                    if count == 0:
                        print("Error! There is no record. Please try again.")
                    repeat = input("Do you want to repeat search by title? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search
                    os.system("cls") # Clear screen

                    while repeat < "0" or repeat > "1":
                        print("Invalid input!!")
                        print("Please enter valid option from '0' to '1'.")
                        repeat = input("Do you want to repeat search by title? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search

            else: # Search by author
                repeat = "1"
                while repeat == "1":
                    srch = input("Enter book author >>")
                    count = 0
                    num = 1
                    title_flag = True
                    longest_title = max(len(x) for x in book_title) # max() is to return the item with the highest value, or the item with the highest value in an iterable
                    for i in range(len(book_num)): # Arrange the book title to make the table nicer
                        if len(book_title[i])<longest_title:
                            book_title[i]=book_title[i]+" "*(longest_title-len(book_title[i]))
                    for i in book_author:
                        if srch.capitalize() in i: # capitalize() is to convert first character of a string to uppercase letter and lowercases all other characters, if any
                            if title_flag == True:
                                print("\nNo.\t  Barcode\t\t\tBook Title\t\t\t\t\t\t\t\tBook Author")
                                title_flag = False # Show the title flag once
                            print(num, "\t", book_barcode[count], "\t", book_title[count], "\t", i)
                            num += 1
                            count += 1
            
                    if count == 0:
                        print("Error! There is no record. Please try again.")
                    repeat = input("\n\nDo you want to repeat search by author? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search
                    os.system("cls") # Clear screen

                    while repeat < "0" or repeat > "1":
                        print("Invalid input!!")
                        print("Please enter valid option from '0' to '1'.")
                        repeat = input("Do you want to repeat search by author? (0 - No / 1 - Yes) >>") # Enter 0 return to search book menu, enter 1 will repeat search

# Check out book---------------------------------------------------------------------------------------------------------------------------------------------
def CheckOut():
    repeat_chkout = True
    while repeat_chkout == True:
        os.system("cls") # Clear screen
        id = input("\n\u001b[34mPlease enter Account ID (Press '0' to return to main menu): ") # \u001b[34m is to set console text colour to blue
                                                                                               # Enter '0' to display ReturnExit()
        if id == "0":
            break # Terminate the loop

        while id not in acc_ID:
            print("Invalid Student ID! Please try again.")
            id = input("Please enter Account ID (Press '0' to return to main menu): ") # Enter '0' to display ReturnExit()
        id_position = acc_ID.index(id)

        if int(acc_borrow[id_position]) >= 5:
            print("\nThis Student ID has reached the maximum number of books borrowed, Check Out can't be proceed.")
            time.sleep(2) # Suspend execution for 2 seconds

        else:
            for x in range(0, 3):
                sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                time.sleep(0.5) # Suspend execution for 0.5 seconds
                sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                time.sleep(0.3) # Suspend execution for 0.3 seconds

            while True:
                os.system('cls') # Clear screen
                print("\t\t\t\t Name: ", acc_name[id_position], "\t\tAccount ID: ", id,
                      "\t\tMax Book(s) to borrow: ", 5 - int(acc_borrow[id_position]))
                print("\n\n")
                print("No.\t  Barcode\t    Call no.\t\t   ISBN no.\t\t\t\tBook Title\t\t\t\t     Book Availability")
                print("-"*150)
                longest_title = max(len(x) for x in book_title) # max() is to return the item with the highest value, or the item with the highest value in an iterable
                for x in range(len(book_num)): # Arrange the book title to make the table nicer
                    if len(book_title[x])<longest_title:
                        book_title[x]=book_title[x]+" "*(longest_title-len(book_title[x]))
                    print(book_num[x], "\t", book_barcode[x], "\t", book_callnum[x], "\t",
                          book_isbnnum[x], "\t", book_title[x], "\t\t", book_availability[x])
                print()
                print("-"*150)
                print("\n")
                print("\t\t\t\tTo check out the book,please enter the No.")
                bk_num = input("\t\t\t\tNo.(0 - Back): ") # Enter 0 return to check out page

                while bk_num not in book_num and bk_num != "0":
                    print("\t\t\t\tThe number is invalid, no book is found with the number. Please try again. ")
                    bk_num = input("\t\t\t\tNo.(0 - Back): ") # Enter 0 return to check out page

                while book_availability[int(bk_num)-1] == "0" and bk_num != "0":
                    print("\t\t\t\tThe book is out of stock, it cannot be checked out.")
                    bk_num = input("\t\t\t\tNo.(0 - Back): ") # Enter 0 return to check out page

                if bk_num == "0": 
                    break # Terminate the loop
                else:
                    repeat_chkout = False
                    for i in range(len(book_num)):
                        if bk_num == book_num[i]:
                            print("\n\n\t\t\t\tInformation of Book Selected\n") # Display information of book
                            print("\t\t\t\tBook Title\t\t\t\t\t: ", book_title[i])
                            print("\t\t\t\tBook Author\t\t\t\t\t: ", book_author[i])
                            print("\t\t\t\tBarcode\t\t\t\t\t\t: ", book_barcode[i])
                            print("\t\t\t\tCall Number\t\t\t\t\t: ", book_callnum[i])
                            print("\t\t\t\tISBN Number\t\t\t\t\t: ", book_isbnnum[i])
                            print("\t\t\t\tNumber of book(s) available to be borrowed\t: ", book_availability[i])

                    print("\n\n\t\t\t\tDo you want to check out this book? (0 - No , 1 - Yes)")
                    ans = input("\t\t\t\tAnswer: ")

                    while ans != "0" and ans != "1":
                        print("\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                        ans = input("\t\t\t\tAnswer: ")

                    if ans == "1":
                        with open("booklist.txt", "w+") as book_list: # Open "booklist.txt" file for both writing and reading
                            book_list.seek(0) # set the current file position in a file stream
                            book_list.truncate() # truncates the file's size
                            book_availability[int(bk_num)-1] = str(int(book_availability[int(bk_num)-1])-1)
                            for i in range(len(book_num)):
                                book_list.write("%s|%s|%s|%s|%s|%s|%s\n" % (
                                    book_num[i], book_barcode[i], book_callnum[i], book_isbnnum[i], book_title[i], book_author[i], book_availability[i]))
                        book_list.close() # Close "booklist.txt" file

                        with open("checkout.txt", "a") as checkout_list: # Open "checkout.txt" file for appending
                            start_date = datetime.date.today() # Get the current local date
                            end_date = start_date + datetime.timedelta(days=14) # Calculate the date after 14 days
                            chkout_num.append(str(int(chkout_num[-1])+1))
                            checkout_list.write("%s|%s|%s|%s|%s\n" % (chkout_num[-1],id, book_barcode[int(bk_num)-1], start_date, end_date))
                        checkout_list.close() # Close "checkout_list" file

                        with open("accountlist.txt", "w+") as account_list:  # Open "accountlist.txt" file for both writing and reading
                            acc_borrow[id_position] = str(int(acc_borrow[id_position])+1)
                            for i in range(len(acc_num)):
                                account_list.write("%s|%s|%s|%s|%s|%s\n" % (acc_num[i], acc_ID[i],
                                                                            acc_name[i], acc_type[i], exp_date[i], acc_borrow[i]))
                        account_list.close() # Close "accountlist.txt" file

                        print("\n")
                        for x in range(0, 3):
                            sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                            time.sleep(0.5) # Suspend execution for 0.5 seconds
                            sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                            time.sleep(0.3) # Suspend execution for 0.3 seconds

                        print("\n\t\t\t\tCompleted! The book is successfully checked out.")
                        print("\n\t\t\t\tDo you want to check out another book? (0 - No , 1 - Yes)") # Enter 0 display ReturnExit(), enter 1 to check out book again
                        ans = input("\t\t\t\tAnswer: ")

                        while ans != "0" and ans != "1":
                            print("\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                            ans = input("\t\t\t\tAnswer: ")

                        if ans != "1":
                            break # Terminate the loop

# Check in book----------------------------------------------------------------------------------------------------------------------------------------------
def CheckIn():
    repeat_chkin = True
    while repeat_chkin == True:
        os.system("cls") # Clear screen
        id = input("\n\u001b[34mPlease enter Account ID (Press '0' to return to main menu): ") # \u001b[34m is to set console text colour to blue

        if id == "0":
            break # Terminate the loop

        while id not in acc_ID:
            print("Invalid Student ID! Please try again.")
            id = input("Please enter Account ID (Press '0' to return to main menu): ") # Enter '0' to display ReturnExit()
        id_position = acc_ID.index(id)

        for x in range(0, 3):
            sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
            time.sleep(0.5) # Suspend execution for 0.5 seconds
            sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
            time.sleep(0.3) # Suspend execution for 0.3 seconds

        while True:
            os.system('cls') # Clear screen
            if acc_borrow[id_position] == "0":
                print("This Student ID has nothing to check in.")
                os.system("pause") # Display a message 'Press any key to continue . . .'
                break
            else:
                print("\t\t\t\t Name: ", acc_name[id_position], "\t\tAccount ID: ", id, "\t\tNumber of book(s) borrowed: ", acc_borrow[id_position])
                print("\n\n")
                num = 1
                count = 0
                index_count = 0
                a = 0
                chkout_ID_position = []
                barcode_position = []
                temp_barcode = []
                temp_callnum = []
                temp_isbnnum = []
                temp_title = []
                temp_author = []

                print("\n\n")
                print("No.\t  Barcode\t     Call no.\t\t   ISBN no.\t\t\t\tBook Title")
                print("-"*150)

                for i in chkout_ID:
                    if i == id:
                        count += 1
                        if count > 1:
                            chkout_ID_position.append(chkout_ID.index(i, chkout_ID_position[a-1]+1))
                        else:
                            chkout_ID_position.append(chkout_ID.index(i))

                        for x in book_barcode:
                            if x == chkout_barcode[chkout_ID_position[a]]:
                                barcode_position.append(book_barcode.index(x))
                                temp_barcode.append(chkout_barcode[chkout_ID_position[a]])
                                temp_callnum.append(book_callnum[barcode_position[a]])
                                temp_isbnnum.append(book_isbnnum[barcode_position[a]])
                                temp_title.append(book_title[barcode_position[a]])
                                temp_author.append(book_author[barcode_position[a]])
                        print(num, "\t", temp_barcode[a], "\t", temp_callnum[a], "\t", temp_isbnnum[a], "\t\t", temp_title[a])
                        a += 1
                        num += 1
                print()
                print("-"*150)
                print("\n")
                print("\t\t\t\tTo check in the book,please enter the No.")
                bk_num = input("\t\t\t\tNo.(0 - Back): ")

                while int(bk_num) not in range(num) and bk_num != "0":
                    print("\t\t\t\tThe number is invalid, no book is found with the number. Please try again. ")
                    bk_num = input("\t\t\t\tNo.(0 - Back): ")

                if bk_num == "0":
                    break  # Terminate the loop
                else:
                    repeat_chkin = False
                    for i in range(num):
                        if int(bk_num) == i:
                            print("\n\n\t\t\t\tInformation of Book Selected\n") # Display information of book
                            print("\t\t\t\tBook Title\t\t\t\t\t: ", temp_title[int(bk_num)-1])
                            print("\t\t\t\tBook Author\t\t\t\t\t: ", temp_author[int(bk_num)-1])
                            print("\t\t\t\tBarcode\t\t\t\t\t\t: ", temp_barcode[int(bk_num)-1])
                            print("\t\t\t\tCall Number\t\t\t\t\t: ", temp_callnum[int(bk_num)-1])
                            print("\t\t\t\tISBN Number\t\t\t\t\t: ", temp_isbnnum[int(bk_num)-1])

                    print("\n\n\t\t\t\tDo you want to check in this book? (0 - No , 1 - Yes)")
                    ans = input("\t\t\t\tAnswer: ")

                    while ans != "0" and ans != "1":
                        print("\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                        ans = input("\t\t\t\tAnswer: ")

                    if ans == "1":
                        with open("checkin.txt", "a") as checkin_list:
                            return_date = datetime.date.today()
                            chkin_num.append(str(int(chkin_num[-1])+1))
                            checkin_list.write("%s|%s|%s|%s\n" % (chkin_num[-1],id, temp_barcode[int(bk_num)-1], return_date))
                        checkin_list.close()

                        with open("checkout.txt", "w+") as checkout_list:
                            checkout_list.seek(0)
                            checkout_list.truncate()
                            if len(chkout_ID_position)==1:
                                position1=chkout_ID_position[0]
                                
                            elif len(chkout_ID_position)==2:
                                position1=chkout_ID_position[0]
                                position2=chkout_ID_position[1]
                                
                            elif len(chkout_ID_position)==3:
                                position1=chkout_ID_position[0]
                                position2=chkout_ID_position[1]
                                position3=chkout_ID_position[2]
                                
                            elif len(chkout_ID_position)==4:
                                position1=chkout_ID_position[0]
                                position2=chkout_ID_position[1]
                                position3=chkout_ID_position[2]
                                position4=chkout_ID_position[3]
                                
                            elif len(chkout_ID_position)==5:
                                position1=chkout_ID_position[0]
                                position2=chkout_ID_position[1]
                                position3=chkout_ID_position[2]
                                position4=chkout_ID_position[3]
                                position5=chkout_ID_position[4]
                                

                            if temp_barcode[int(bk_num)-1] == chkout_barcode[position1]:
                                    index=position1
                            elif temp_barcode[int(bk_num)-1] == chkout_barcode[position2]:
                                    index=position2
                            elif temp_barcode[int(bk_num)-1] == chkout_barcode[position3]:
                                    index=position3
                            elif temp_barcode[int(bk_num)-1] == chkout_barcode[position4]:
                                    index=position4
                            elif temp_barcode[int(bk_num)-1] == chkout_barcode[position5]:
                                    index=position5
                            chkout_ID.pop(index)
                            chkout_barcode.pop(index)
                            chkout_strt.pop(index)
                            chkout_end.pop(index)
                            for i in range(len(chkout_ID)):
                                checkout_list.write("%d|%s|%s|%s|%s\n" % (i+1,chkout_ID[i], chkout_barcode[i], chkout_strt[i], chkout_end[i]))
                        checkout_list.close()

                        with open("accountlist.txt", "w+") as account_list:
                            acc_borrow[id_position] = str(int(acc_borrow[id_position])-1)
                            for i in range(len(acc_num)):
                                account_list.write("%s|%s|%s|%s|%s|%s\n" % (acc_num[i], acc_ID[i],acc_name[i], acc_type[i], exp_date[i], acc_borrow[i]))
                        account_list.close()

                        with open("booklist.txt", "w+") as book_list:
                            book_list.seek(0)
                            book_list.truncate()
                            for i in barcode_position:
                                if temp_barcode[int(bk_num)-1] == book_barcode[i]:
                                    book_availability[i] = str(int(book_availability[i])+1)
                            for i in range(len(book_num)):
                                book_list.write("%s|%s|%s|%s|%s|%s|%s\n" %(book_num[i], book_barcode[i], book_callnum[i], book_isbnnum[i], book_title[i], book_author[i], book_availability[i]))
                        book_list.close()

                        print("\n")
                        for x in range(0, 3):
                            sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                            time.sleep(0.5)
                            sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                            time.sleep(0.3)

                        print("\n\t\t\t\tCompleted! The book is successfully checked in.")
                        print("\n\t\t\t\tDo you want to check in another book? (0 - No , 1 - Yes)")
                        ans = input("\t\t\t\tAnswer: ")

                        while ans != "0" and ans != "1":
                            print("\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                            ans = input("\t\t\t\tAnswer: ")

                        if ans != "1":
                            break  # Terminate the loop

# Account & membership maintenance---------------------------------------------------------------------------------------------------------------------------
def AccountList():
    repeat_accountlist = True
    while repeat_accountlist == True:
        os.system("cls") # Clear screen
        print("\u001b[32m\n\n\t\t\t\t\t\t\t\t1. Account List\n\t\t\t\t\t\t\t\t2. Add Account\n\t\t\t\t\t\t\t\t3. Delete Account") # Display account & membership maintenance menu
        print("\n\n") # \u001b[32m is to set console text colour to green
        option=input(("\t\t\t\t\t\tOption[1-3](Press '0' to return to menu or exit program): "))
        while option < "0" or option > "3" or len(option) > 1:
            print("\t\t\t\t\t\tInvalid input!!")
            print("\t\t\t\t\t\tPlease enter valid option from '1' to '3'.")
            option = input("\t\t\t\t\t\tOption[1-3]:")
        if option =="0":
            repeat_accountlist=False
        else:
            OpenFile()
            if option=="1": # Display account list
                while True:
                    os.system("cls") # Clear screen
                    print("\t\t\t\tNo.\tAccount ID\t\tName") 
                    print("-"*150)
                    for x in range(len(acc_num)):
                        print("\t\t\t\t", acc_num[x], "\t", acc_ID[x], "\t", acc_name[x])
                    print("-"*150)
                    print("\n\t\t\t\tTo view the details of the account, please enter the account number.")
                    account_num = input("\t\t\t\tAccount Number(Press '0' if don't want to proceed): ")

                    while account_num != "0" and account_num not in acc_num:
                        print("\t\t\t\tThe number is invalid, no account is found with the number. Please try again. ")
                        account_num = input("\t\t\t\tAccount Number(Press '0' if don't want to proceed: ")

                    if account_num != "0":
                        for i in range(len(acc_num)):
                            if account_num == acc_num[i]:
                                print("\n\n\t\t\t\tInformation of Account Selected\n") # Display information of account
                                print("\t\t\t\tAccount ID\t\t\t: ", acc_ID[i])
                                print("\t\t\t\tName\t\t\t\t: ", acc_name[i])
                                print("\t\t\t\tMembership Type\t\t\t: ", acc_type[i])
                                print("\t\t\t\tExpiry Date\t\t\t: ", exp_date[i])
                                print()
                                os.system("pause") # Display a message 'Press any key to continue . . .'
                    else:
                        break # Terminate the loop

            elif option=="2": # Add account
                while True:
                    os.system("cls")
                    print("\t\t\t\t\t\t\t\tAdd Account")
                    id=input("\n\n\t\t\t\t\t\t\tAccount ID: ")
                    while len(id)!=7 or id.isalpha(): # isalpha() is to return True if all characters in the string are alphabets
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tAccount ID should only contain 7 digits.")
                        id = input("\t\t\t\t\t\t\tAccount ID:")

                    name=input("\t\t\t\t\t\t\tAccount Name: ")
                    while name.isnumeric(): # isnumeric() is to return True if all characters in a string are numeric characters.
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tAccount Name should only contain alphabets.")
                        name=input("\t\t\t\t\t\t\tAccount Name: ")

                    type=input("\t\t\t\t\t\t\tAccount Type(Student/Staff): ")
                    while type != "Student" and type !="Staff" and type !="student" and type !="staff":
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tThere are only 2 type of membership, which is 'Student' or 'Staff'.")
                        type=input("\t\t\t\t\t\t\tAccount Type(Student/Staff): ")
                    

                    print("\t\t\t\t\t\t\tExpire Date")
                    repeat_date=True
                    while repeat_date==True:
                        expire_year=input("\t\t\t\t\t\t\tYear: ")
                        while len(expire_year)>4 or len(expire_year)<4:
                            print("\t\t\t\t\t\t\tInvalid input!!")
                            print("\t\t\t\t\t\t\tYear only valid for 4 digits")
                            expire_year=input("\t\t\t\t\t\t\tYear: ")

                        leap_year = int(expire_year) % 4 == 0 and int(expire_year) % 100 == 0 and int(expire_year % 400) == 0
                        if leap_year:      
                            month_day=[31,29,31,30,31,30,31,31,30,31,30,31]
                        else:
                            month_day=[31,28,31,30,31,30,31,31,30,31,30,31]

                        expire_month=input("\t\t\t\t\t\t\tMonth: ")
                        while int(expire_month)<1 or int(expire_month)>12:
                            print("\t\t\t\t\t\t\tInvalid input!!")
                            print("\t\t\t\t\t\t\tMonth is only valid from '1' to '12'")
                            expire_month=input("\t\t\t\t\t\t\tMonth: ")

                        expire_day=input("\t\t\t\t\t\t\tDay: ")
                        while int(expire_day)<1 or int(expire_day)>31:
                            print("\t\t\t\t\t\t\tInvalid input!!")
                            print("\t\t\t\t\t\t\tDay is only valid from '1' to '31'")
                            expire_day=input("\t\t\t\t\t\t\tDay: ")
                    
   
                        if int(expire_day)>month_day[int(expire_month)-1]:
                            if int(expire_month)==2:
                                print("\t\t\t\t\t\t\tInvalid input!!")
                                if leap_year:
                                    print("\t\t\t\t\t\t\tThis month is only valid from '1' to '29'")
                                else:
                                    print("\t\t\t\t\t\t\tThis month is only valid from '1' to '28'")
                            else:
                                print("\t\t\t\t\t\t\tInvalid input!!")
                                print("\t\t\t\t\t\t\tThis month is only valid from '1' to '30'")
                            
                        else:
                            repeat_date=False

                    if len(expire_day)==1:
                        expire_day= "0" + expire_day

                    if len(expire_month)==1:
                        expire_month= "0" + expire_month
                    
                    expire_date = expire_year + "-" + expire_month + "-" + expire_day

                    for x in range(0, 3):
                        sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                        time.sleep(0.5)
                        sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                        time.sleep(0.3)

                    with open("accountlist.txt","a+") as account_list:
                        acc_num.append(str(int(acc_num[-1])+1))
                        account_list.write("%s|%s|%s|%s|%s|0\n"%(acc_num[-1],id,name,type.capitalize(),expire_date))
                    account_list.close()

                    print("\n\t\t\t\t\t\tCompleted! The account is successfully created.")
                    print("\n\t\t\t\t\t\tDo you want to add another account? (0 - No , 1 - Yes)")
                    ans = input("\t\t\t\t\t\tAnswer: ")

                    while ans != "0" and ans != "1":
                        print("\t\t\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                        ans = input("\t\t\t\t\t\t\tAnswer: ")

                    if ans != "1":
                        break

            elif option=="3": # Delete account
                while True:
                    os.system("cls")
                    print("\t\t\t\t\t\t\t\tDelete Account")
                    print("\n\t\t\t\tNo.\tAccount ID\t\t\tName")
                    print("-"*150)
                    for x in range(len(acc_num)):
                        print("\t\t\t\t", acc_num[x], "\t", acc_ID[x], "\t", acc_name[x])
                    print("-"*150)
                    print("\n\n")
                    print()
                    print("\t\t\t\t\t\tTo delete the account,please enter the No.")
                    ac_num = input("\t\t\t\t\t\tNo.(0 - Back): ")

                    while ac_num not in acc_num and ac_num != "0":
                        print("\t\t\t\t\t\tThe number is invalid, no account is found with the number. Please try again. ")
                        ac_num = input("\t\t\t\t\t\tNo.(0 - Back): ")
                    
                    if ac_num=="0":
                        repeat_accountlist = True
                        break
                    else:
                        repeat_accountlist = False
                        for i in range(len(acc_num)):
                            if ac_num == acc_num[i]:
                                print("\n\n\t\t\t\t\t\tInformation of Account Selected\n") # Display information of account
                                print("\t\t\t\t\t\tAccount ID\t\t\t: ", acc_ID[i])
                                print("\t\t\t\t\t\tName\t\t\t\t: ", acc_name[i])
                                print("\t\t\t\t\t\tMembership Type\t\t\t: ", acc_type[i])
                                print("\t\t\t\t\t\tExpiry Date\t\t\t: ", exp_date[i])
                                print()

                        print("\n\n\t\t\t\t\t\tDo you want to delete this account? (0 - No , 1 - Yes)")
                        ans = input("\t\t\t\t\t\tAnswer: ")

                        while ans != "0" and ans != "1":
                            print("\t\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                            ans = input("\t\t\t\t\t\tAnswer: ")

                        if ans=="1":
                            with open("accountlist.txt","w+") as account_list:
                                account_list.seek(0)
                                account_list.truncate()
                                acc_num.pop(int(ac_num)-1)
                                acc_ID.pop(int(ac_num)-1)
                                acc_name.pop(int(ac_num)-1)
                                acc_type.pop(int(ac_num)-1)
                                exp_date.pop(int(ac_num)-1)
                                acc_borrow.pop(int(ac_num)-1)
                                for i in range(len(acc_num)):
                                    account_list.write("%d|%s|%s|%s|%s|%s\n"%(int(i)+1,acc_ID[i],acc_name[i],acc_type[i],exp_date[i],acc_borrow[i]))
                            account_list.close()
                        
                            print("\n")
                            for x in range(0, 3):
                                sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                                time.sleep(0.5)
                                sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                                time.sleep(0.3)

                            print("\n\t\t\t\t\t\tCompleted! The account is successfully deleted.")
                            print("\n\t\t\t\t\t\tDo you want to delete another account? (0 - No , 1 - Yes)")
                            ans = input("\t\t\t\t\t\tAnswer: ")

                            while ans != "0" and ans != "1":
                                print("\t\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                                ans = input("\t\t\t\t\t\tAnswer: ")

                            if ans != "1":
                                repeat_accountlist=True
                                break

# Book Management--------------------------------------------------------------------------------------------------------------------------------------------
def BookManagement():
    repeat_bkmgt=True
    while repeat_bkmgt == True:
        os.system("cls")
        print("\u001b[33m\n\n\t\t\t\t\t\t\t\t1. Add Book\n\t\t\t\t\t\t\t\t2. Delete Book") # Display book management menu
        print("\n\n") # \u001b[33m is to set console text colour to yellow
        option=input(("\t\t\t\t\t\tOption[1-2](Press '0' to return to menu or exit program): "))
        while option < "0" or option > "2" or len(option) > 1:
            print("\t\t\t\t\t\tInvalid input!!")
            print("\t\t\t\t\t\tPlease enter valid option from '1' to '2'.")
            option = input("\t\t\t\t\t\tOption[1-2]:")
        if option =="0":
            repeat_bkmgt=False
        else:
            OpenFile()
            if option=="1": # Add book
                while True:
                    os.system("cls")
                    print("\t\t\t\t\t\t\t\tAdd Book")
                    bk_title=input("\n\n\t\t\t\t\t\t\tBook Title: ")
                    while bk_title.isnumeric():
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tBook Title should only contain alphabets.")
                        bk_title=input("\t\t\t\t\t\t\tBook Title: ")

                    bk_author=input("\t\t\t\t\t\t\tBook Auhtor: ")
                    while bk_author.isnumeric():
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tBook Author should only contain alphabets.")
                        bk_author=input("\t\t\t\t\t\t\tBook Auhtor: ")
                    
                    bk_barcode=input("\t\t\t\t\t\t\tBarcode: ")
                    while len(bk_barcode)!=10 or bk_barcode[0]!='U' and bk_barcode[0]!='u':
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tBarcode should only contain 9 digits with first letter of 'U'.")
                        bk_barcode=input("\t\t\t\t\t\t\tBarcode: ")
                    
                    bk_callnum=input("\t\t\t\t\t\t\tCall Number: ")
                    
                    bk_isbnnum=input("\t\t\t\t\t\t\tISBN Number: ")
                    while bk_isbnnum.isnumeric()==False or len(bk_isbnnum)!=13:
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tISBN Number should only contain 13 digits.")
                        bk_isbnnum=input("\t\t\t\t\t\t\tISBN Number: ")

                    bk_avail=input("\t\t\t\t\t\t\tNumber of Book Available: ")
                    while bk_avail.isnumeric()==False:
                        print("\t\t\t\t\t\t\tInvalid input!!")
                        print("\t\t\t\t\t\t\tNumber of Book Available should only contain digits.")
                        bk_avail=input("\t\t\t\t\t\t\tNumber of book available: ")

                    for x in range(0, 3):
                        sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                        time.sleep(0.5)
                        sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                        time.sleep(0.3)

                    with open("booklist.txt","a+") as book_list:
                        book_num.append(str(int(book_num[-1])+1))
                        book_list.write("%s|%s|%s|%s|%s|%s|%s\n"%(book_num[-1],bk_barcode.capitalize(),bk_callnum,bk_isbnnum,bk_title,bk_author,bk_avail))
                    book_list.close()

                    print("\n\t\t\t\t\t\t\tCompleted! The book is successfully added.")
                    print("\n\t\t\t\t\t\t\tDo you want to add another book? (0 - No , 1 - Yes)")
                    ans = input("\t\t\t\t\t\t\tAnswer: ")

                    while ans != "0" and ans != "1":
                        print("\t\t\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                        ans = input("\t\t\t\t\t\t\tAnswer: ")

                    if ans != "1":
                        break

            elif option=="2": # Delete book
                while True:
                    os.system("cls")
                    print("\t\t\t\t\t\t\t\tDelete Book")
                    print("\n\n")
                    print("No.\t  Barcode\t     Call no.\t\t   ISBN no.\t\t\t\tBook Title\t\t\t\t     Book Availability")
                    print("-"*150)
                    longest_title = max(len(x) for x in book_title)
                    for x in range(len(book_num)):
                        if len(book_title[x])<longest_title:
                            book_title[x]=book_title[x]+" "*(longest_title-len(book_title[x]))
                        print(book_num[x], "\t", book_barcode[x], "\t", book_callnum[x], "\t",
                              book_isbnnum[x], "\t", book_title[x], "\t\t", book_availability[x])
                    print()
                    print("-"*150)
                    print()
                    print("\t\t\t\t\tTo delete the book,please enter the No.")
                    bk_num = input("\t\t\t\t\tNo.(0 - Back): ")

                    while bk_num not in book_num and bk_num != "0":
                        print("\t\t\t\t\tThe number is invalid, no account is found with the number. Please try again. ")
                        bk_num = input("\t\t\t\t\tNo.(0 - Back): ")
                    
                    if bk_num=="0":
                        repeat_bkmgt = True
                        break
                    else:
                        repeat_bkmgt = False
                        for i in range(len(book_num)):
                            if bk_num == book_num[i]:
                                print("\n\n\t\t\t\t\tInformation of Book Selected\n") # Display information of book
                                print("\t\t\t\t\tBook Title\t\t\t\t\t: ", book_title[i])
                                print("\t\t\t\t\tBook Author\t\t\t\t\t: ", book_author[i])
                                print("\t\t\t\t\tBarcode\t\t\t\t\t\t: ", book_barcode[i])
                                print("\t\t\t\t\tCall Number\t\t\t\t\t: ", book_callnum[i])
                                print("\t\t\t\t\tISBN Number\t\t\t\t\t: ", book_isbnnum[i])
                                print("\t\t\t\t\tNumber of book(s) available to be borrowed\t: ", book_availability[i])
                                print()

                        print("\n\n\t\t\t\t\tDo you want to delete this book? (0 - No , 1 - Yes)")
                        ans = input("\t\t\t\t\tAnswer: ")

                        while ans != "0" and ans != "1":
                            print("\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                            ans = input("\t\t\t\t\tAnswer: ")

                        if ans=="1":
                            with open("booklist.txt","w+") as book_list:
                                book_list.seek(0)
                                book_list.truncate()
                                book_num.pop(int(bk_num)-1)
                                book_barcode.pop(int(bk_num)-1)
                                book_callnum.pop(int(bk_num)-1)
                                book_isbnnum.pop(int(bk_num)-1)
                                book_title.pop(int(bk_num)-1)
                                book_author.pop(int(bk_num)-1)
                                book_availability.pop(int(bk_num)-1)
                                for i in range(len(book_num)):
                                    book_list.write("%d|%s|%s|%s|%s|%s|%s\n"%(int(i)+1,book_barcode[i],book_callnum[i],book_isbnnum[i],book_title[i],book_author[i],book_availability[i]))
                            book_list.close()
                        
                            print("\n")
                            for x in range(0, 3):
                                sys.stdout.write("\r\t\t\t\t\t\t\t\tProcessing...")
                                time.sleep(0.5)
                                sys.stdout.write("\r\t\t\t\t\t\t\t\t             ")
                                time.sleep(0.3)

                            print("\n\t\t\t\t\tCompleted! The book is successfully deleted.")
                            print("\n\t\t\t\t\tDo you want to delete another book? (0 - No , 1 - Yes)")
                            ans = input("\t\t\t\t\tAnswer: ")

                            while ans != "0" and ans != "1":
                                print("\t\t\t\t\tInvalid Input. There is only 2 options, '0' for No or '1' for Yes.")
                                ans = input("\t\t\t\t\tAnswer: ")

                            if ans != "1":
                                repeat_bkmgt=True
                                break

# Record-----------------------------------------------------------------------------------------------------------------------------------------------------
def Record():
    repeat_record=True
    while repeat_record==True:
        os.system("cls")
        print("\u001b[34m\n\n\t\t\t\t\t\t\t\t1. Check Out's Record\n\t\t\t\t\t\t\t\t2. Check In's Record") # Display record menu
        print("\n\n") # \u001b[34m is to set console text colour to blue
        option=input(("\t\t\t\t\t\tOption[1-2](Press '0' to return to menu or exit program): "))
        while option < "0" or option > "2" or len(option) > 1:
            print("\t\t\t\t\t\tInvalid input!!")
            print("\t\t\t\t\t\tPlease enter valid option from '1' to '2'.")
            option = input("\t\t\t\t\t\tOption[1-2]:")
        if option =="0":
            repeat_record=False
        else:
            if option =="1": # Check out's record
                while True:
                    os.system("cls")
                    print("\t\t\t\t\t\t\t\tCheck Out's Record")
                    print("\t\tNo.\t   ID\t\t  Barcode\t Start Date\t  End Date")
                    print("-"*150)
                    for x in range(len(chkout_num)):
                        print("\t\t",chkout_num[x],"\t", chkout_ID[x], "\t", chkout_barcode[x], "\t", chkout_strt[x],"\t",chkout_end[x])
                    print("-"*150)
                    print("\n\t\t\t\t\tTo view the details of the record, please enter the No.")
                    num_out = input("\t\t\t\t\tNo.(Press '0' if don't want to proceed): ")

                    while num_out != "0" and num_out not in acc_num:
                        print("\t\t\t\t\tThe number is invalid, no record is found with the number. Please try again. ")
                        num_out = input("\t\t\t\t\tNo.(Press '0' if don't want to proceed: ")

                    if num_out != "0":
                        for i in range(len(chkout_num)):
                            if num_out == chkout_num[i]:
                                print("\n\n\t\t\t\t\tInformation of Record Selected\n") # Display information of record
                                print("\t\t\t\t\tAccount ID\t\t\t: ", chkout_ID[i])
                                print("\t\t\t\t\tName\t\t\t\t: ", acc_name[acc_ID.index(chkout_ID[i])])
                                print("\t\t\t\t\tBook Title\t\t\t: ", book_title[book_barcode.index(chkout_barcode[i])])
                                print("\t\t\t\t\tBook Author\t\t\t: ",book_author[book_barcode.index(chkout_barcode[i])])
                                print("\t\t\t\t\tBarcode\t\t\t\t: ", chkout_barcode[i])
                                print("\t\t\t\t\tCall Number\t\t\t: ",book_callnum[book_barcode.index(chkout_barcode[i])])
                                print("\t\t\t\t\tISBN Number\t\t\t: ",book_isbnnum[book_barcode.index(chkout_barcode[i])])
                                print("\t\t\t\t\tStart Date of CheckOut\t\t: ",chkout_strt[i])
                                print("\t\t\t\t\tEnd Date of CheckOut\t\t: ",chkout_end[i])
                                print()
                                os.system("pause")
                    else:
                        break
            else: # Chcek in's record
                while True:
                    os.system("cls")
                    print("\t\t\t\t\t\t\t\tCheck In's Record")
                    print("\t\tNo.\t   ID\t\t  Barcode\t Return Date")
                    print("-"*150)
                    for x in range(len(chkin_num)):
                        print("\t\t",chkin_num[x],"\t", chkin_ID[x], "\t", chkin_barcode[x], "\t", chkin_return[x])
                    print("-"*150)
                    print("\n\t\t\t\t\tTo view the details of the record, please enter the No.")
                    num_in = input("\t\t\t\t\tNo.(Press '0' if don't want to proceed): ")

                    while num_in != "0" and num_in not in acc_num:
                        print("\t\t\t\t\tThe number is invalid, no record is found with the number. Please try again. ")
                        num_in = input("\t\t\t\t\tNo.(Press '0' if don't want to proceed: ")

                    if num_in != "0":
                        for i in range(len(chkin_num)):
                            if num_in == chkin_num[i]:
                                print("\n\n\t\t\t\t\tInformation of Record Selected\n") # Display information of record
                                print("\t\t\t\t\tAccount ID\t\t\t: ", chkin_ID[i])
                                print("\t\t\t\t\tName\t\t\t\t: ", acc_name[acc_ID.index(chkin_ID[i])])
                                print("\t\t\t\t\tBook Title\t\t\t: ", book_title[book_barcode.index(chkin_barcode[i])])
                                print("\t\t\t\t\tBook Author\t\t\t: ",book_author[book_barcode.index(chkin_barcode[i])])
                                print("\t\t\t\t\tBarcode\t\t\t\t: ", chkin_barcode[i])
                                print("\t\t\t\t\tCall Number\t\t\t: ",book_callnum[book_barcode.index(chkin_barcode[i])])
                                print("\t\t\t\t\tISBN Number\t\t\t: ",book_isbnnum[book_barcode.index(chkin_barcode[i])])
                                print("\t\t\t\t\tReturn Date of Book\t\t: ",chkin_return[i])
                                print()
                                os.system("pause")
                    else:
                        break

# Return to main menu and Exit-------------------------------------------------------------------------------------------------------------------------------
def ReturnExit():
    print("\n\n")
    print("\t\t\t\t\t\t\t\u001b[0mOption:<1>Return to main menu    <2>Exit") # \u001b[0m is to set console text colour back to white
    choice = input("\t\t\t\t\t\t\tSelect your choice:")
    while choice < "1" or choice > "2":
        print("\t\t\t\t\t\t\t\u001b[0mInvalid input!!") # \u001b[0m is to set console text colour back to white
        print("\t\t\t\t\t\t\tPlease enter valid option from '1' to '2'.")
        choice = input("\t\t\t\t\t\t\tSelect your choice:")

    if choice == "1": # Return to main menu
        return True
    else: # Exit
        os.system("cls")
        print("\n\n\n\n\n\n\n\n")
        for x in range(0,3):
            sys.stdout.write("\r\t\t\t\t\t\t\tExiting the program......")
            time.sleep(0.6)
            sys.stdout.write("\r\t\t\t\t\t\t\t                         ")
            time.sleep(0.4)
        input("\n\t\t\t\t\t\t\t\tThank You!")
        return False

# Main function----------------------------------------------------------------------------------------------------------------------------------------------
Security()
repeat = True
while repeat == True:
    MainMenu()
    OpenFile()
    option = input("\t\t\t\t\t\t\t\u001b[0mOption[1-9]:")
    while option < "1" or option > "9" or len(option) > 1:
        print("\t\t\t\t\t\t\tInvalid input!!")
        print("\t\t\t\t\t\t\tPlease enter valid option from '1' to '9'.")
        option = input("\t\t\t\t\t\t\tOption[1-9]:")

    if option != "9":
        if option == "1":
            BookList()
            repeat = ReturnExit()

        elif option == "2":
            SearchBook()
            repeat= ReturnExit()

        elif option == "3":
            CheckOut()
            repeat = ReturnExit()

        elif option == "4":
            CheckIn()
            repeat = ReturnExit()

        elif option == "5":
            AccountList()
            repeat = ReturnExit()

        elif option == "6":
            BookManagement()
            repeat = ReturnExit()

        elif option =="7":
            Record()
            repeat = ReturnExit()
            
        else:
            os.system("cls")
            print("\n\n\n\n\n\n\n\n")
            for x in range(0,3):
                sys.stdout.write("\u001b[31m\r\t\t\t\t\t\t\t\tWhile In Progress......") # \u001b[31m is to set console text colour to red
                time.sleep(0.6)
                sys.stdout.write("\r\t\t\t\t\t\t\t\t                       ")
                time.sleep(0.4)

    else:
        os.system("cls")
        print("\n\n\n\n\n\n\n\n")
        for x in range(0,3):
            sys.stdout.write("\r\t\t\t\t\t\t\tExiting the program......")
            time.sleep(0.6)
            sys.stdout.write("\r\t\t\t\t\t\t\t                         ")
            time.sleep(0.4)
        input("\n\t\t\t\t\t\t\t\tThank You!") # Press any key to exit the programme
        repeat = False
