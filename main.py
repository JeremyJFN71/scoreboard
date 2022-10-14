import json, os

svdfile = './saved/save.json'

def newFile():
    os.system('cls')
    players = input('Players (separate with comma (,)):\n').split(',')

    playersdict = dict()
    for player in players:
        playersdict[player] = 0
    global load, saveslot
    saveslot = -1
    load = playersdict
    playFile()

def saveFile(x):
    if x == -1:
        with open(svdfile, 'r') as data:
            info = json.load(data)
            info.append(load)
            json_object = json.dumps(info, indent=4)
            global saveslot
            saveslot = len(info)-1

        with open(svdfile, 'w') as data:
            data.write(json_object)
    else:
        with open(svdfile, 'r') as data:
            info = json.load(data)
            info[saveslot] = load
            json_object = json.dumps(info, indent=4)

        with open(svdfile, 'w') as data:
            data.write(json_object)

def loadFile():
    os.system('cls')
    with open(svdfile, 'r') as data:
        info = json.load(data)
        print('-------Saved Files-------')
        if len(info) == 0:
            print('No files found')
            os.system('pause')
            return
        else:
            for i in range(1, len(info)+1):
                print(f'[{i}] Save{i}')

            global load, saveslot
            saveslot = int(input('Load> '))-1
            load = info[saveslot]
            playFile()

def deleteFile():
    while True:
        os.system('cls')
        with open(svdfile, 'r') as data:
            info = json.load(data)
            print('-------Delete File-------')
            if len(info) == 0:
                print('No files found')
                os.system('pause')
                return
            else:
                for i in range(1, len(info)+1):
                    print(f'[{i}] Save{i}')
                print('[0] Back')
                try:
                    answer = int(input('Delete> '))-1
                except:
                    continue

                if answer == -1:
                    return
                elif answer == range(len(info)):
                    while True:
                        surely = input('Are you sure?[y/n]: ')
                        if surely == 'y':
                            info.pop(answer)
                            json_object = json.dumps(info, indent=4)
                            with open(svdfile, 'w') as data:
                                data.write(json_object)
                            break
                        elif surely == 'n':
                            return
                        else:
                            continue
                    break
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
    print('-------MENU--------')
    print('[1] New File')
    print('[2] Load File')
    print('[3] Delete File')
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