import json, os

def getkey(value, dictionary):
    for key, val in dictionary.items():
         if value == val:
             return key

def getkeys(value, dictionary):
    listofkeys = []
    for key, val in dictionary.items():
         if value == val:
             listofkeys.append(key)
    return listofkeys

def dictsortedkey(dictionary):
    sorteddict = {}
    for key in sorted(dictionary.keys()):
        sorteddict[key] = dictionary[key]
    return sorteddict

def printbase(dictionary):
    keys = list(dictionary)
    for key in keys:
        print(key + ":  " + dictionary[key][0] + "   " + dictionary[key][1] + "   " + "{:,}".format(dictionary[key][2]))

def checkbelow(belowthis, dictionary):
    yesbelow = {}
    for key in list(dictionary):
        if dictionary[key] <= int(belowthis):
            yesbelow[key] = dictionary[key]
    return yesbelow


if not os.path.isfile('whattobuy.database'):
    basewrite = open('whattobuy.database', 'w+')
    empty = {}
    json.dump(empty, basewrite, indent=3)
    basewrite.close()

baseread = open('whattobuy.database')
database = json.load(baseread)
baseread.close()

database = dictsortedkey(database)

buyitems = list(database)
typesofitems = []
shops = []
bytype = {}
byshop = {}
byprice = {}

for item in buyitems:
    bytype[item] = database[item][0]

for item in buyitems:
    byshop[item] = database[item][1]

for item in buyitems:
    byprice[item] = database[item][2]

for key in buyitems:
    typesofitems.append(bytype[key])
typesofitems = set(typesofitems)
typesofitems = list(typesofitems)
typesofitems = sorted(typesofitems)

for key in buyitems:
    shops.append(byshop[key])
shops = set(shops)
shops = list(shops)
shops = sorted(shops)

# print(buyitems)
# print(bytype)
# print(byshop)
# print(byprice)

print(r'''KOTIKOT, script by BarsTiger                                         |
                                                                     |
   _____ _______         ____                ____                    |
  / ____|__   __|/\     |  _ \              |  _ \                   |
 | |  __   | |  /  \    | |_) |_   _ _   _  | |_) | __ _ ___  ___    |
 | | |_ |  | | / /\ \   |  _ <| | | | | | | |  _ < / _` / __|/ _ \   |
 | |__| |  | |/ ____ \  | |_) | |_| | |_| | | |_) | (_| \__ \  __/   |
  \_____|  |_/_/    \_\ |____/ \__,_|\__, | |____/ \__,_|___/\___|   |
                                      __/ |                          |
                                     |___/                           |
---------------------------------------------------------------------|
''')

while True:
    print("What you want to do?")
    print("1 - Print all database")
    print("2 - Print all items")
    print("3 - Print all items by type")
    print("4 - Print all items by shop")
    print("5 - Print all items by price below this")
    print("6 - Add new item to database")
    print("7 - Exit")
    doing = input("Type here: ")
    print()

    if doing == "1":
        print("Name:  Type   Shop   Price")
        printbase(database)
        print()
        input("To go back to menu press Enter...")

    elif doing == "2":
        for item in buyitems:
            print(item)
        print()
        input("To go back to menu press Enter...")

    elif doing == "3":
        print("Types to search in database: ")
        for item in typesofitems:
            print(item)
        print()
        for item in getkeys(input("For which type I should check: "), bytype):
            print(item)
        print()
        input("To go back to menu press Enter...")

    elif doing == "4":
        print("Types to search in database: ")
        for item in shops:
            print(item)
        print()
        for item in getkeys(input("For which shop I should check: "), byshop):
            print(item)
        print()
        input("To go back to menu press Enter...")

    elif doing == "5":
        belowthisprice = checkbelow(input("I will check for items below this price: "), byprice)
        for item in list(belowthisprice):
            print(item + ": " + "{:,}".format(belowthisprice[item]))
        print()
        input("To go back to menu press Enter...")

    elif doing == "6":
        print()
        print("Adding new item")
        specif = []
        nameofnewitem = input("Type here name of new item: ")
        specif.append(input("Type here type of item: "))
        specif.append(input("Type here shop, where item can be bought: "))
        specif.append(int(input("Type here price of item (without spaces or comas): ")))
        database[nameofnewitem] = specif
        basewrite = open('whattobuy.database', 'w+')
        json.dump(database, basewrite, indent=3)
        basewrite.close()

    elif doing == "7":
        print("---------------------------------------------------------------------")
        input("To exit press Enter...")
        exit()


