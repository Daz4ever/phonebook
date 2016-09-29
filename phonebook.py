import pickle
from os.path import exists

if exists('phonebook.pickle'):
    phonebook_file = open('phonebook.pickle', 'r')
    phonebook_dict = pickle.load(phonebook_file)
    phonebook_file.close()
else:
    phonebook = {}

def lookup1():
    name = (raw_input("Name: ")).upper()
    number = phonebook.get(name, 'not found')
    print number


def set2():
    name = (raw_input("Name? ")).upper()
    number = raw_input("Number? ")
    phonebook[name] = number
    print "%s's number is %s" % (name, number)

def delete3():
    name = (raw_input("Entry to delete? (give name) ")).upper()
    if name in phonebook:
        del phonebook[name]
        print "%s deleted!" % name
    else:
        print "%s is not in phone book" % name

def listall4():
    print phonebook.items()


active_phonebook = True

while active_phonebook:

    print "1\. Look up an extry"
    print "2\. Set an entry"
    print "3\. Delete an entry"
    print "4\. List all entries"
    print "5\. Save Entries"
    print "6\. Quit"


    choice = raw_input("What do you want to do (1-6)? ")

    print choice

    if choice == "1":
        lookup1()
    elif choice == "2":
        set2()
    elif choice == "3":
        delete3()
    elif choice == "4":
        listall4()
    elif choice == "5":
        phonebook_file = open('phonebook.pickle', 'w')
        pickle.dump(phonebook, phonebook_file)
        phonebook_file.close()
    elif choice == "6":
        print "Bye!"
        active_phonebook = False
    else:
        print "Invalid choice"
