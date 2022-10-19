import json, os, datetime

maxlen = 51
# save.json location
savedfile = './saved/save.json'

'''
checks if there is a save.json and it contains [] or not, and if not then
the programs will create save.json and write [] in save.json
'''
try:
    with open(savedfile, 'r') as data:
        read_data = data.read()
        if '[' not in read_data or ']' not in read_data:
                with open(savedfile, 'w') as data:
                    data.write('[]')
except:
    with open(savedfile, 'w') as data:
        data.write('[]')

def showFile(title):
    with open(savedfile, 'r') as data:
            info = json.load(data)
            # Make the display look better
            length = maxlen - len(title)
            length = length // 2
            print(f'{"-"*length}{title}{"-"*length}')
            # If there is no data in save.json
            if len(info) == 0:
                print('No files found')
                os.system('pause')
                return
            # If there is data in save.json
            else:
                i = 1
                for slot in info:
                    for name in slot[0]:
                        savename = name
                    # Make the display look better
                    length = maxlen - len(f'[{i}] {savename}{slot[1]["time"]}')
                    print(f'[{i}] {savename}{" "*length}{slot[1]["time"]}')
                    i += 1
                print('\n[0] Back')

def newFile():
    os.system('cls')
    players = input('Players (separate with comma (,)):\n').split(',')

    # Insert players into playersdict with each key with a value of 0
    playersdict = dict()
    for player in players:
        playersdict[player] = 0

    global saveslot, load
    saveslot = -1
    load = playersdict
    playFile()

def saveFile(x):
    # If previously just created a file, the program will go to this if
    if x == -1:
        savename = input('Save name:\n')
        svfile = []
        progress = dict()
        time = dict()

        now = datetime.datetime.today()
        progress[savename] = load
        time['time'] = f'{now.strftime("%x")}, {now.strftime("%X")}'
        svfile.extend([progress, time])

        # Read save.json and append the data
        with open(savedfile, 'r') as data:
            info = json.load(data)
            info.append(svfile)
            json_object = json.dumps(info, indent=4)
            global saveslot
            saveslot = len(info)-1

        # Write changes into save.json
        with open(savedfile, 'w') as data:
            data.write(json_object)

    # If previously loaded the file, the program will go to this else
    else:
        # Read save.json and changes the data from index
        with open(savedfile, 'r') as data:
            now = datetime.datetime.today()
            info = json.load(data)
            for savename in info[x][0]:
                info[x][0][savename] = load
            for time in info[x][1]:
                info[x][1][time] = f'{now.strftime("%x")}, {now.strftime("%X")}'
            json_object = json.dumps(info, indent=4)

        # Write changes into save.json
        with open(savedfile, 'w') as data:
            data.write(json_object)

def loadFile():
    while True:
        os.system('cls')
        # Show files to user
        showFile('Load File')
        with open(savedfile, 'r') as data:
            info = json.load(data)
            # If there is no data in save.json
            if len(info) == 0:
                return
            # If there is data in save.json
            else:
                try:
                    global saveslot, load
                    saveslot = int(input('Load> '))-1
                except:
                    continue
                # Back
                if saveslot == -1:
                    return
                # Load file
                elif saveslot in range(len(info)):
                    for savename in info[saveslot][0]:
                        load = info[saveslot][0][savename]
                # Index out of range
                else:
                    print('file not found')
                    os.system('pause')
                    return
                break
    playFile()

def deleteFile():
    while True:
        os.system('cls')
        # Show files to user
        showFile('Delete File')
        with open(savedfile, 'r') as data:
            info = json.load(data)
            # If there is no data in save.json
            if len(info) == 0:
                return
            # If there is data in save.json
            else:
                try:
                    answer = int(input('Delete> '))-1
                except:
                    continue
                # Back
                if answer == -1:
                    return
                # Delete file
                elif answer in range(len(info)):
                    while True:
                        confirmation = input('Are you sure?[y/n]: ')
                        if confirmation == 'y':
                            info.pop(answer)
                            json_object = json.dumps(info, indent=4)
                            with open(savedfile, 'w') as data:
                                data.write(json_object)
                            break
                        elif confirmation == 'n':
                            return
                        else:
                            continue
                    break
                # Index out of range
                else:
                    print('file not found')
                    os.system('pause')
                    return

def playFile():
    while True:
        os.system('cls')
        print('-------ScoreBoard-------')
        for player in load:
            print(f'{player}: {load[player]}')
        print('------------------------')
        for player in load:
            score = input(f'{player} = ')
            try:
                score = int(score)
            except:
                # Commands
                if score == '/exit':
                    exit()
                elif score == '/save':
                    saveFile(saveslot)
                    break
                elif score == '/menu':
                    return
                else:
                    break
            load[player] += score
        continue

while True:
    os.system('cls')
    print('-----------MENU-----------')
    print('[1] New File')
    print('[2] Load File')
    print('[3] Delete File\n')
    print('[0] Exit')

    try:
        answer = int(input('> '))
    except:
        continue
    if answer == 1:
        newFile()
    elif answer == 2:
        loadFile()
    elif answer == 3:
        deleteFile()
    elif answer == 0:
        exit()