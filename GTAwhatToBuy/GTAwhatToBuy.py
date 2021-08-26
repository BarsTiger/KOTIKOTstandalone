import json, os, shutil, subprocess, sys
try:
    import curses
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'windows-curses'])
    import curses
import sys

os.system("title " + "GTA BuyBase")

logo = [
            "|---------------------------------------------------------------------|",
            "|               KOTIKOT, script by BarsTiger                          |",
            "|                                                                     |",
            "|                                                                     |",
            "|   _____ _______         ____                ____                    |",
            "|  / ____|__   __|/\     |  _ \              |  _ \                   |",
            "| | |  __   | |  /  \    | |_) |_   _ _   _  | |_) | __ _ ___  ___    |",
            "| | | |_ |  | | / /\ \   |  _ <| | | | | | | |  _ < / _` / __|/ _ \   |",
            "| | |__| |  | |/ ____ \  | |_) | |_| | |_| | | |_) | (_| \__ \  __/   |",
            "|  \_____|  |_/_/    \_\ |____/ \__,_|\__, | |____/ \__,_|___/\___|   |",
            "|                                      __/ |                          |",
            "|                                     |___/                           |",
            "|---------------------------------------------------------------------|"
        ]

def glstdscr(stdscr):
    return stdscr

globalstdscr = curses.wrapper(glstdscr)

def print_center(stdscr=globalstdscr, text=""):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    x = w//2 - len(text)//2
    y = h//2
    stdscr.addstr(y, x, text)
    stdscr.refresh()

def printlogo():
    print("\n" * ((os.get_terminal_size().lines // 2 - (len(logo) // 2)) + 1))
    for line in logo:
        print(" " * ((os.get_terminal_size().columns//2 - (len(line)//2)) - 1) + line)
    print("\n" * ((os.get_terminal_size().lines // 2 - (len(logo) // 2)) - 1))
    input()
    cls()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def softcls():
    print("\n" * (os.get_terminal_size().lines * 2))

def print_menu(stdscr, selected_row_idx, menu):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()

doing = 0
menulist = {"main": ['Data output', 'Database loading and options', 'Add new item', 'Owning options', 'Exit'],
            "output": ['Print all database', 'Print all items', 'Print all items by type', 'Print all items by shop', 'Print all items by price below this', 'Back'],
            "baseoptions": ['Create backup of opened database', 'Open another database', 'Create new database', 'Validate database', 'Back'],
            "ownoptions": ['Edit own or not', 'Show only owned', 'Show only unowned', 'Show all', 'Back'],
            "exit": ["Exit", "Back"]}

def exitmenu(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row, menulist["exit"])

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menulist["exit"])-1:
            current_row += 1

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                exit()
            if current_row == 1:
                mainmenu(stdscr)
                break

        print_menu(stdscr, current_row, menulist["exit"])

def mainmenu(stdscr):
    global doing
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row, menulist["main"])

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_UP and current_row == 0:
            current_row = len(menulist["main"])-1
        elif key == curses.KEY_DOWN and current_row < len(menulist["main"])-1:
            current_row += 1
        elif key == curses.KEY_DOWN and current_row == len(menulist["main"]) - 1:
            current_row = 0

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == 0:
                outputmenu(stdscr)
                break

            if current_row == 1:
                baseoptionsmenu(stdscr)
                break

            if menulist["main"][current_row] == "Add new item":
                doing = menulist["main"][current_row]
                break

            if current_row == 3:
                ownmenu(stdscr)
                break

            if current_row == len(menulist["main"])-1:
                exitmenu(stdscr)
                break

        print_menu(stdscr, current_row, menulist["main"])

def outputmenu(stdscr):
    global doing
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row, menulist["output"])

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_UP and current_row == 0:
            current_row = len(menulist["output"])-1
        elif key == curses.KEY_DOWN and current_row < len(menulist["output"])-1:
            current_row += 1
        elif key == curses.KEY_DOWN and current_row == len(menulist["output"]) - 1:
            current_row = 0

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(menulist["output"])-1:
                mainmenu(stdscr)
                break
            else:
                doing = menulist["output"][current_row]
                break

        elif key == curses.KEY_BACKSPACE or str(key) in ['KEY_BACKSPACE', '8', '127']:
            mainmenu(stdscr)
            break

        print_menu(stdscr, current_row, menulist["output"])

def baseoptionsmenu(stdscr):
    global doing
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row, menulist["baseoptions"])

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_UP and current_row == 0:
            current_row = len(menulist["baseoptions"])-1
        elif key == curses.KEY_DOWN and current_row < len(menulist["baseoptions"])-1:
            current_row += 1
        elif key == curses.KEY_DOWN and current_row == len(menulist["baseoptions"]) - 1:
            current_row = 0

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(menulist["baseoptions"])-1:
                mainmenu(stdscr)
                break
            else:
                doing = menulist["baseoptions"][current_row]
                break

        elif key == curses.KEY_BACKSPACE or str(key) in ['KEY_BACKSPACE', '8', '127']:
            mainmenu(stdscr)
            break

        print_menu(stdscr, current_row, menulist["baseoptions"])

def ownmenu(stdscr):
    global doing
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    print_menu(stdscr, current_row, menulist["ownoptions"])

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_UP and current_row == 0:
            current_row = len(menulist["ownoptions"])-1
        elif key == curses.KEY_DOWN and current_row < len(menulist["ownoptions"])-1:
            current_row += 1
        elif key == curses.KEY_DOWN and current_row == len(menulist["ownoptions"]) - 1:
            current_row = 0

        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row == len(menulist["ownoptions"])-1:
                mainmenu(stdscr)
                break
            else:
                doing = menulist["ownoptions"][current_row]
                break

        elif key == curses.KEY_BACKSPACE or str(key) in ['KEY_BACKSPACE', '8', '127']:
            mainmenu(stdscr)
            break

        print_menu(stdscr, current_row, menulist["ownoptions"])

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
    if show == "All":
        for key in keys:
            print(key + ":  " + dictionary[key][0] + "   " + dictionary[key][1] + "   " + "{:,}".format(dictionary[key][2]))
            print()
    elif show == "Owned":
        for key in keys:
            if dictionary[key][3] == True:
                print(key + ":  " + dictionary[key][0] + "   " + dictionary[key][1] + "   " + "{:,}".format(dictionary[key][2]))
                print()
    elif show == "Unowned":
        for key in keys:
            if dictionary[key][3] == False:
                print(key + ":  " + dictionary[key][0] + "   " + dictionary[key][1] + "   " + "{:,}".format(
                    dictionary[key][2]))
                print()

def checkbelow(belowthis, dictionary):
    yesbelow = {}
    for key in list(dictionary):
        if dictionary[key] <= int(belowthis):
            yesbelow[key] = dictionary[key]
    return yesbelow

basename = 'default.database'
backname = str(os.path.splitext(basename)[0]) + ".databack"
show = "All"

if not os.path.isfile(basename):
    basewrite = open(basename, 'w+')
    empty = {}
    json.dump(empty, basewrite, indent=3)
    basewrite.close()

baseread = open(basename)
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

def openbase():
    global baseread, database, buyitems, typesofitems, shops, bytype, byshop, byprice, backname
    if not os.path.isfile(basename):
        basewrite = open(basename, 'w+')
        empty = {}
        json.dump(empty, basewrite, indent=3)
        basewrite.close()

    baseread = open(basename)
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
    backname = str(os.path.splitext(basename)[0]) + ".databack"

printlogo()

while True:
    curses.wrapper(mainmenu)

    if doing == menulist["output"][0]:
        print("Name:  Type   Shop   Price")
        print()
        printbase(database)
        print()
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["output"][1]:
        if show == "All":
            for item in buyitems:
                print(item)
        elif show == "Owned":
            for item in buyitems:
                if database[item][3] == True:
                    print(item)
        elif show == "Unowned":
            for item in buyitems:
                if database[item][3] == False:
                    print(item)
        print()
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["output"][2]:
        print("Types to search in database: ")
        for item in typesofitems:
            print(item)
        print()
        if show == "All":
            for item in getkeys(input("For which type I should check: "), bytype):
                print(item)
        elif show == "Owned":
            for item in getkeys(input("For which type I should check: "), bytype):
                if database[item][3] == True:
                    print(item)
        elif show == "Unowned":
            for item in getkeys(input("For which type I should check: "), bytype):
                if database[item][3] == False:
                    print(item)

        print()
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["output"][3]:
        print("Types to search in database: ")
        for item in shops:
            print(item)
        print()
        if show == "All":
            for item in getkeys(input("For which type I should check: "), byshop):
                print(item)
        elif show == "Owned":
            for item in getkeys(input("For which type I should check: "), byshop):
                if database[item][3] == True:
                    print(item)
        elif show == "Unowned":
            for item in getkeys(input("For which type I should check: "), byshop):
                if database[item][3] == False:
                    print(item)
        print()
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["output"][4]:
        belowthisprice = checkbelow(input("I will check for items below this price: "), byprice)
        if show == "All":
            for item in list(belowthisprice):
                print(item + ": " + "{:,}".format(belowthisprice[item]))
        elif show == "Owned":
            for item in list(belowthisprice):
                if database[item][3] == True:
                    print(item + ": " + "{:,}".format(belowthisprice[item]))
        elif show == "Unowned":
            for item in list(belowthisprice):
                if database[item][3] == False:
                    print(item + ": " + "{:,}".format(belowthisprice[item]))
        print()
        input("To go back to menu press Enter...")
        softcls()

    elif doing == "Add new item":
        print()
        print("Adding new item")
        specif = []
        nameofnewitem = input("Type here name of new item: ")
        specif.append(input("Type here type of item: "))
        specif.append(input("Type here shop, where item can be bought: "))
        specif.append(int(input("Type here price of item (without spaces or comas): ")))
        isowneditem = bool(input("Do you own this item? (1 - Yes, 0 - No): ") == "1")
        specif.append(isowneditem)
        database[nameofnewitem] = specif
        basewrite = open(basename, 'w+')
        json.dump(database, basewrite, indent=3, ensure_ascii=False)
        basewrite.close()
        softcls()

    elif doing == menulist["baseoptions"][0]:
        print()
        shutil.copy(basename, backname)
        if os.path.isfile(backname):
            print("Backup successful")
        print()
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["baseoptions"][1]:
        alldatabases = []
        for file in os.listdir(os.getcwd()):
            if '.database' in file:
                alldatabases.append(os.path.splitext(file)[0])
        print("Which database would you like to open?")
        for base in alldatabases:
            print(base)
        basename = input("Type here: ") + ".database"
        openbase()
        print("Other DB opened")
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["baseoptions"][2]:
        print("Creating new DB. Choose name for it")
        basename = input("Type here: ") + ".database"
        openbase()
        print("New DB created")
        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["baseoptions"][3]:
        print("Checking file valid")
        try:
            openbase()
            print("File is valid")
        except:
            print("File is !INvalid!")
            print("Try to check file by yourself or create new DB")

        print()
        print("Checking if all owning options are valid")

        for item in buyitems:
            try:
                if database[item][3] == True:
                    pass
                elif database[item][3] == False:
                    pass
                else:
                    database[item][3] = False
            except:
                databasethisitem = database[item]
                databasethisitem.append(False)
                database[item] = databasethisitem

        basewrite = open(basename, 'w+')
        json.dump(database, basewrite, indent=3, ensure_ascii=False)
        basewrite.close()

        print("Owning options were checked and validated if needed")

        input("To go back to menu press Enter...")
        softcls()

    elif doing == menulist["ownoptions"][0]:
        print("Select type of editor")
        typeofedit = input("1 - Edit all items\n2 - Edit one at a time\nType here: ")
        if typeofedit == "2":
            print()
            print("Which item you would like to change?")
            whattodonow = input("1 - Print all items\n2 - Search item\nType here: ")
            if whattodonow == "1":
                for item in buyitems:
                    print(item)
                print()
            elif whattodonow == "2":
                whichtocontain = input("Start typing name here: ")
                containthis = []
                for item in buyitems:
                    if whichtocontain.lower() in item.lower():
                        containthis.append(item)
                for item in containthis:
                    print(item)
            itemtoedit = input("Type here name of item: ")
            print(itemtoedit + " is now " + str(database[itemtoedit][3]))
            isowneditem = bool(input("Do you own this item? (1 - Yes, 0 - No): ") == "1")
            database[itemtoedit][3] = isowneditem

            basewrite = open(basename, 'w+')
            json.dump(database, basewrite, indent=3, ensure_ascii=False)
            basewrite.close()

        elif typeofedit == "1":
            ownbasename = str(os.path.splitext(basename)[0]) + ".ownbase"
            print("Will be created file named " + ownbasename)
            owningtempbase = {}
            for item in buyitems:
                owningtempbase[item] = database[item][3]

            with open(ownbasename, 'w+') as ownwrite:
                json.dump(owningtempbase, ownwrite, indent=3, ensure_ascii=False)

            print()
            print("File is created. Open it with any text editor (notepad will be opened automatically on Windows)")
            print("If you own item, type true near its name. If not - false")
            print("It shold be like this: ")
            print('"Avenger": true,')
            print("After each line shold be a ','")
            print()
            if sys.platform == "win32":
                input("After you press Enter, notepad app will be opened")
                command = 'cmd /c "notepad.exe {}"'.format(ownbasename)
                os.system(command)

            print()

            input("When you are ready, press Enter")
            input("Press Enter to load data from ownbase file")

            with open(ownbasename) as ownread:
                owningtempbase = json.load(ownread)

            for item in buyitems:
                database[item][3] = owningtempbase[item]

            basewrite = open(basename, 'w+')
            json.dump(database, basewrite, indent=3, ensure_ascii=False)
            basewrite.close()

            os.remove(ownbasename)

            print("All data from ownbase file moved to database file")
            print("Ownbase file deleted")
            print()
            input("To go back to menu press Enter...")
            softcls()

    elif doing == menulist["ownoptions"][1]:
        show = "Owned"
    elif doing == menulist["ownoptions"][2]:
        show = "Unowned"
    elif doing == menulist["ownoptions"][3]:
        show = "All"
