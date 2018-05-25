#License GNU-GPL v 3.0
#Battle Ship v 1.0 last updated 5/24/18
#One player game of battleship. Player is facing the random computer generator
#Needs a New_Game file to work
#Keenan Hui



import os
import time
import random



Player_board = []
Opp_board = []
Attack_board = []



Ship = 1
length = 0



Oppcarrier = []
Oppbattle = []
Oppcruiser = []
Oppsub = []
Oppdestroyer = []



Pcarrier = []
Pbattle = []
Pcruiser = []
Psub = []
Pdestroyer = []



class Add_New_Ship:
    def __init__(self, place, ship, up, left, right):
        self.place = place
        self.ship = ship
        self.x = int(place[0]) + 1  #I did plus one to the values, because scince I am using matrixes, the inputed value would not be at the correct spot
        self.y = int(place[2]) + 1
        if up == 'y':  #Checks if the ship is up, left, or right. I did not add down because I thought that one could survive without it
            self.front = int(self.y) - int(self.ship)
            self.direction = 'u'
        elif left == 'y':
            self.front = int(self.x) - int(self.ship)
            self.direction = 'l'
        elif right == 'y':
            self.front = int(self.x) + int(self.ship)
            self.direction = 'r'



    def Place(self):  #Place the player ship
        global Pcarrier
        global Pbattle
        global Pcruiser
        global Psub
        global Pdestroyer

        global Ship
        
        if self.front < 0:  #Checks if the ship will go out of bound from the board
            print('\nYou can not place your ship there')
            time.sleep(1.5)
            PlacePlayerShip()
            
        elif self.front > 10:
            print('\nYou can not place your ship there')
            time.sleep(1.5)
            PlacePlayerShip()

        elif self.front < 1:
            print('\nYou can not place your ship there')
            time.sleep(1.5)
            PlacePlayerShip()
            
        else:
            if self.direction == 'u':
                m = self.front
                while self.y >= m:  #The first loop is to check if there is a ship in the path of the ship you are placing, if there is, it will warn you.
                    if Player_board[m][self.x] == 'S':
                        print('\nYou can not place your ship there')
                        time.sleep(1.5)
                        if Ship == 1:
                            Pcarrier = []
                        elif Ship == 2:
                            Pbattle = []
                        elif Ship == 3:
                            Pcruiser = []
                        elif Ship == 4:
                            Psub = []
                        elif Ship == 5:
                            Pdestroyer = []
                        PlacePlayerShip()
                    
                    m += 1
                m = self.front
            
                while self.y >= m:  #If the first loop does not find any ship sections, it will change the possitions into an S
                    xy = self.x - 1,m - 1
                    a = str(xy).replace(' ','').replace('(','').replace(')','')
                
                    Player_board[m][self.x] = 'S'
                    if Ship == 1:  #Adds the coordinates of the ships to a list, so the game could get rid of the ships
                        Pcarrier.append(a)
                    elif Ship == 2:
                        Pbattle.append(a)
                    elif Ship == 3:
                        Pcruiser.append(a)
                    elif Ship == 4:
                        Psub.append(a)
                    elif Ship == 5:
                        Pdestroyer.append(a)
                    m += 1
                Ship += 1

            elif self.direction == 'l':
                m = self.front
                while self.x >= m:
                    if Player_board[self.y][m] == 'S':
                        print('\nYou can not place your ship there')
                        if Ship == 1:
                            Pcarrier = []
                        elif Ship == 2:
                            Pbattle = []
                        elif Ship == 3:
                            Pcruiser = []
                        elif Ship == 4:
                            Psub = []
                        elif Ship == 5:
                            Pdestroyer = []
                        time.sleep(1.5)
                        PlacePlayerShip()
                    m += 1
                m = self.front

                while self.x >= m:
                    xy = m - 1,self.y - 1
                    a = str(xy).replace(' ','').replace('(','').replace(')','')
                    Player_board[self.y][m] = 'S'
                    if Ship == 1:
                        Pcarrier.append(a)
                    elif Ship == 2:
                        Pbattle.append(a)
                    elif Ship == 3:
                        Pcruiser.append(a)
                    elif Ship == 4:
                        Psub.append(a)
                    elif Ship == 5:
                        Pdestroyer.append(a)
                    m += 1
                Ship += 1

            elif self.direction == 'r':
                m = self.front
                while self.x <= m:
                    if Player_board[self.y][m] == 'S':
                        print('\nYou can not place your ship there')
                        if Ship == 1:
                            Pcarrier = []
                        elif Ship == 2:
                            Pbattle = []
                        elif Ship == 3:
                            Pcruiser = []
                        elif Ship == 4:
                            Psub = []
                        elif Ship == 5:
                            Pdestroyer = []
                        time.sleep(1.5)
                        PlacePlayerShip()
                    m -= 1
                m = self.front

                while self.x <= m:
                    xy = m - 1,self.y - 1
                    a = str(xy).replace(' ','').replace('(','').replace(')','')
                    Player_board[self.y][m] = 'S'
                    if Ship == 1:
                        Pcarrier.append(a)
                    elif Ship == 2:
                        Pbattle.append(a)
                    elif Ship == 3:
                        Pcruiser.append(a)
                    elif Ship == 4:
                        Psub.append(a)
                    elif Ship == 5:
                        Pdestroyer.append(a)
                    m -= 1
                Ship += 1



    def PlaceOpp(self):  #Works the same way as placing the player, bot it does not need to warn the player of the computers fault
        global Oppcarrier
        global Oppbattle
        global Oppcruiser
        global Oppsub
        global Oppdestroyer

        global Ship
        
        if self.front < 0:
            PlaceOppShip()
        
        elif self.front > 10:
            PlaceOppShip()

        elif self.front < 1:
            PlaceOppShip()
        
        else:
            if self.direction == 'u':
                m = self.front
                while self.y >= m:
                    if Opp_board[m][self.x] == 'S':
                        if Ship == 1:
                            Oppcarrier = []
                        elif Ship == 2:
                            Oppbattle = []
                        elif Ship == 3:
                            Oppcruiser = []
                        elif Ship == 4:
                            Oppsub = []
                        elif Ship == 5:
                            Oppdestroyer = []
                        PlaceOppShip()
                    m += 1
                m = self.front
                
                while self.y >= m:
                    xy = self.x - 1,m - 1
                    a = str(xy).replace(' ','').replace('(','').replace(')','')
                    Opp_board[m][self.x] = 'S'
                    if Ship == 1:
                        Oppcarrier.append(a)
                    elif Ship == 2:
                        Oppbattle.append(a)
                    elif Ship == 3:
                        Oppcruiser.append(a)
                    elif Ship == 4:
                        Oppsub.append(a)
                    elif Ship == 5:
                        Oppdestroyer.append(a)
                    m += 1
                Ship += 1

            elif self.direction == 'l':
                m = self.front
                while self.x >= m:
                    if Opp_board[self.y][m] == 'S':
                        if Ship == 1:
                            Oppcarrier = []
                        elif Ship == 2:
                            Oppbattle = []
                        elif Ship == 3:
                            Oppcruiser = []
                        elif Ship == 4:
                            Oppsub = []
                        elif Ship == 5:
                            Oppdestroyer = []
                        PlaceOppShip()
                    m += 1
                m = self.front
                
                while self.x >= m:
                    xy = m - 1,self.y - 1
                    a = str(xy).replace(' ','').replace('(','').replace(')','')
                    Opp_board[self.y][m] = 'S'
                    if Ship == 1:
                        Oppcarrier.append(a)
                    elif Ship == 2:
                        Oppbattle.append(a)
                    elif Ship == 3:
                        Oppcruiser.append(a)
                    elif Ship == 4:
                        Oppsub.append(a)
                    elif Ship == 5:
                        Oppdestroyer.append(a)
                    m += 1
                Ship += 1

            elif self.direction == 'r':
                m = self.front
                while self.x <= m:
                    if Opp_board[self.y][m] == 'S':
                        if Ship == 1:
                            Oppcarrier = []
                        elif Ship == 2:
                            Oppbattle = []
                        elif Ship == 3:
                            Oppcruiser = []
                        elif Ship == 4:
                            Oppsub = []
                        elif Ship == 5:
                            Oppdestroyer = []
                        PlaceOppShip()
                    m -= 1
                m = self.front
                
                while self.x <= m:
                    xy = m - 1,self.y - 1
                    a = str(xy).replace(' ','').replace('(','').replace(')','')
                    Opp_board[self.y][m] = 'S'
                    if Ship == 1:
                        Oppcarrier.append(a)
                    elif Ship == 2:
                        Oppbattle.append(a)
                    elif Ship == 3:
                        Oppcruiser.append(a)
                    elif Ship == 4:
                        Oppsub.append(a)
                    elif Ship == 5:
                        Oppdestroyer.append(a)
                    m -= 1
                Ship += 1


def makePboard():  #Makes the board of the player
    N_Game = open('New_Game.txt', 'r')
    matrixline = []
    for line in N_Game:
        nsline = line.replace(' ','').replace('\n','')
        for i in nsline:
            matrixline.append(i)
        Player_board.append(matrixline)
        matrixline = []
    N_Game.close()



def makeOboard():  #Makes the opponent board, though it will be a blank board, just like the player and attack one. I did this because I was planning to do a save game, but I did not have enough time to do that
    N_Game = open('New_Game.txt', 'r')
    matrixline = []
    for line in N_Game:
        nsline = line.replace(' ','').replace('\n','')
        for i in nsline:
            matrixline.append(i)
        Opp_board.append(matrixline)
        matrixline = []
    N_Game.close()



def makeAboard():
    N_Game = open('New_Game.txt', 'r')
    matrixline = []
    for line in N_Game:
        nsline = line.replace(' ','').replace('\n','')
        for i in nsline:
            matrixline.append(i)
        Attack_board.append(matrixline)
        matrixline = []
    N_Game.close()



def StartScreen():  #Start screen
    print('''



__________         __    __   __             _________ __     __        
\______   \_____ _/  |__/  |_|  |   ____    /   _____/|  |__ |__|_____  
 |    |  _/\__  \\\   __\   __\  | _/ __ \   \_____  \ |  |  \\|  | ___ \\
 |    |   \ / __ \|  |  |  | |  |_\  ___/   /        \|   |  \\  | |_|  |
 |______  /(____  |__|  |__| |____/\___ \\  /_______  /|___|  /__|   __/ 
        \/      \/                     \/          \/      \/   |__|


        
''')
    en = input('Press enter to start: ')
    if en == '':
        menu()
    menu()



def menu():
    os.system('cls')
    global Oppcarrier  #All the globals is so when you start a new game, it would get rid of everything
    global Oppbattle
    global Oppcruiser
    global Oppsub
    global Oppdestroyer

    global Pcarrier
    global Pbattle
    global Pcruiser
    global Psub
    global Pdestroyer
    
    global Player_board
    global Opp_board
    global Attack_board

    global Ship

    Oppcarrier = []
    Oppbatle = []
    Oppcarrier = []
    Oppsub = []
    Oppdestroyer = []

    Pcarrier = []
    Pbattle = []
    Pcruiser = []
    Psub = []
    Pdestroyer = []

    Player_board = []
    Opp_board = []
    Attack_board = []

    Ship = 1
    
    inp = input('''1 - New Game
2 - Quit
: ''')
    if inp == '1':
        os.system('cls')
        makePboard()
        makeOboard()
        makeAboard()
        PlaceOppShip()
    elif inp == '3':
        quit()
    else:
        print('\nYou did not chose one of the options\n')
        menu()



def NewGame():  #Directions
    
    print('''How To Play -

1 - The Ships:
    There are 5 different types of ships -
        a - The Carrier(5)
        b - The Battleship(4)
        c - The Cruiser(3)
        d - The submarine(3)
        e - The Destroyer(2)
        
2 - How to place the ship:
    To place the ships, type in the cordinates of the end of your ship (x,y) and either up, left, or right
    Example:
        Where do you want the end of the ship to be: 9,4
        What direction do you want thte ship to face: u

3 - How to attack:
    To attack, input the spot you want to attack
    Example:
        Where do you want to attack: 4,5''')

    start = input("\nPress enter to start the game ").lower()
    
    if start == '':
        PlacePlayerShip()
        
    PlacePlayerShip()



def PlacePlayerShip():  #Player places the ship
    global length
    os.system('cls')
    if Ship == 1:
        ShipName = 'CARRIER'
        length = 4
    elif Ship == 2:
        ShipName = 'BATTLE SHIP'
        length = 3
    elif Ship == 3:
        ShipName = 'CRUISER'
        length = 2
    elif Ship == 4:
        ShipName = 'SEBMARINE'
        length = 2
    elif Ship == 5:
        ShipName = 'DESTROYER'
        length = 1
    else:
        Attack()

    print('This is your board\n')
    for i in Player_board:
        a = str(i).replace("'",'').replace(',','').replace('[','').replace(']','')
        print(a)

    EndOfShip = input('\nWhere do you want the end of your %s to be(EX: 9,2): ' %(ShipName))

    if len(EndOfShip) != 3:  #All of the if, elif, and try except is to check the input of the player
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        PlacePlayerShip()

    elif EndOfShip[1] != ',':
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        PlacePlayerShip()

    elif EndOfShip == '' or EndOfShip == ' ':
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        PlacePlayerShip()

    try:
        b = EndOfShip.replace(EndOfShip[1],'')
        c = int(b)
    except ValueError:
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        PlacePlayerShip()
    
    direction = input('''u = Up
l = Left
r = Right
What direction do you want the %s to be: ''' %(ShipName))
    if direction == 'u':  #Tells the class what direction the ship is supposed to go
        up = 'y'
        left = 'n'
        right = 'n'
    elif direction == 'r':
        up = 'n'
        left = 'n'
        right = 'y'
    elif direction == 'l':
        up = 'n'
        left = 'y'
        right = 'n'
    else:
        print('\nYou did not input a valid input')
        time.sleep(1.5)
        PlacePlayerShip()
    
    Fship = Add_New_Ship(EndOfShip, length, up, left, right)
    Add_New_Ship.Place(Fship)
    PlacePlayerShip()



def PlaceOppShip():  #Opponent places ship, same as player but the places are random
    global Ship
    global length
    
    if Ship == 1:      #This is all to get rid of extra Place_(whatever ship) that was here before
        length = 4  #The length is how many to subtract so that the ships length is 5 and not 6
    elif Ship == 2:
        length = 3
    elif Ship == 3:
        length = 2
    elif Ship == 4:
        length = 2
    elif Ship == 5:
        length = 1
    else:
        Ship = 1
        NewGame()

    rnumberx = random.randrange(0,10)
    rnumbery = random.randrange(0,10)

    xy = rnumberx,rnumbery
    EndOfShip = str(xy).replace(' ','').replace('(','').replace(')','')
    
    rnumberd = random.randrange(1,4)
    
    if rnumberd == 1:
        up = 'y'
        left = 'n'
        right = 'n'
    elif rnumberd == 2:
        up = 'n'
        left = 'y'
        right = 'n'
    elif rnumberd == 3:
        up = 'n'
        left = 'n'
        right = 'y'

    Fship = Add_New_Ship(EndOfShip, length, up, left, right)
    Add_New_Ship.PlaceOpp(Fship)
    PlaceOppShip()



def Attack():  #Player attacks
    global Opp_board
    global Attack_board
    
    global Oppcarrier
    global Oppbattle
    global Oppcruiser
    global Oppsub
    global Oppdestroyer
    
    os.system('cls')
    print('This is your board\n')
    for i in Player_board:
        a = str(i).replace("'",'').replace(',','').replace('[','').replace(']','')
        print(a)
    print('\n\nThis is your opponents board\n')
    for i in Attack_board:
        a = str(i).replace("'",'').replace(',','').replace('[','').replace(']','')
        print(a)

    attack = input('Where do you want to attack(EX: 4,5): ')
    numb = attack.replace(',','')

    if len(numb) != 2 or len(attack) != 3:  #All of this also checks if the value inputed is correct
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        Attack()

    elif numb == '' or numb == ' ':
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        Attack()

    elif attack[1] != ',':
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        Attack()

    try:
        c = int(numb)
    except ValueError:
        print('\nYou did not input a correct value')
        time.sleep(1.5)
        Attack()

    x = attack[0]
    y = attack[2]

    if Attack_board[int(y)+1][int(x)+1] == 'O' or Attack_board[int(y)+1][int(x)+1] == 'X':
        print('\nYou can not attack there')
        time.sleep(1.5)
        Attack()

    elif Opp_board[int(y)+1][int(x)+1] == 'S':
        Opp_board[int(y)+1][int(x)+1] = 'X'
        Attack_board[int(y)+1][int(x)+1] = 'X'
        print('\nYou hit a ship')
        time.sleep(1.5)
        
    elif Opp_board[int(y)+1][int(x)+1] == '-':
        Opp_board[int(y)+1][int(x)+1] = 'O'
        Attack_board[int(y)+1][int(x)+1] = 'O'
        print('\nYou missed')
        time.sleep(1.5)
        
    

    NOppship = []
    if str(attack) in Oppcarrier:  #Gets rid of the coordinates from the list
        for i in Oppcarrier:
            if i != str(attack):
                NOppship.append(i)
        Oppcarrier = NOppship
    
    elif str(attack) in Oppbattle:
        for i in Oppbattle:
            if i != str(attack):
                NOppship.append(i)
        Oppbattle = NOppship
        
    elif str(attack) in Oppcruiser:
        for i in Oppcruiser:
            if i != str(attack):
                NOppship.append(i)
        Oppcruiser = NOppship
        
    elif str(attack) in Oppsub:
        for i in Oppsub:
            if i != str(attack):
                NOppship.append(i)
        Oppsub = NOppship
        
    elif str(attack) in Oppdestroyer:
        for i in Oppdestroyer:
            if i != str(attack):
                NOppship.append(i)
        Oppdestroyer = NOppship

    checkSunkShip()



def OppAttack():  #Opponent attack, the same as the player one, but it is random
    global Pcarrier
    global Pbattle
    global Pcruiser
    global Psub
    global Pdestroyer

    x = random.randrange(0,10)
    y = random.randrange(0,10)
    xy = x,y
    attack = str(xy).replace(' ','').replace('(','').replace(')','')

    if Player_board[int(y)+1][int(x)+1] == 'O' or Player_board[int(y)+1][int(x)+1] == 'X':
        OppAttack()

    elif Player_board[int(y)+1][int(x)+1] == 'S':
        Player_board[int(y)+1][int(x)+1] = 'X'
        print('\nYour opponent hit one of your ships')
        time.sleep(1.5)
        
    elif Player_board[int(y)+1][int(x)+1] == '-':
        Player_board[int(y)+1][int(x)+1] = 'O'
        print('\nYour opponent missed')
        time.sleep(1.5)


    NPship = []
    if str(attack) in Pcarrier:
        for i in Pcarrier:
            if i != str(attack):
                NPship.append(i)
        Pcarrier = NPship
    
    elif str(attack) in Pbattle:
        for i in Pbattle:
            if i != str(attack):
                NPship.append(i)
        Pbattle = NPship
        
    elif str(attack) in Pcruiser:
        for i in Pcruiser:
            if i != str(attack):
                NPship.append(i)
        Pcruiser = NPship
        
    elif str(attack) in Psub:
        for i in Psub:
            if i != str(attack):
                NPship.append(i)
        Psub = NPship
        
    elif str(attack) in Pdestroyer:
        for i in Pdestroyer:
            if i != str(attack):
                NPship.append(i)
        Pdestroyer = NPship

    checkOppSunkShip()



def checkSunkShip():  #Checks if the list of the ship is empty, if it is, it will tell you
    global Oppcarrier
    global Oppbattle
    global Oppcruiser
    global Oppsub
    global Oppdestroyer


    if Oppcarrier == []:
        print('\nYou have sunk the opponents CARRIER')
        time.sleep(1.5)
        Oppcarrier.append('a')  #If it does not do this, then it will keep telling the palyer that they have sunk the ship
    elif Oppbattle == []:
        print('\nYou have sunk the opponents BATTLE SHIP')
        time.sleep(1.5)
        Oppbattle.append('a')
    elif Oppcruiser == []:
        print('\nYou have sunk the opponents CRUISER')
        time.sleep(1.5)
        Oppcruiser.append('a')
    elif Oppsub == []:
        print('\nYou have sunk the opponents SUBMARINE')
        time.sleep(1.5)
        Oppsub.append('a')
    elif Oppdestroyer == []:
        print('\nYou have sunk the opponents DESTROYER')
        time.sleep(1.5)
        Oppdestroyer.append('a')

    if Oppcarrier == ['a'] and Oppbattle == ['a'] and Oppcruiser == ['a'] and Oppsub == ['a'] and Oppdestroyer == ['a']:
        os.system('cls')
        print('''
_____ ___                __      __ __
\__  |   | ____  __ __  /  \    /  \__| ____
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \\
 \____   (  <_> )  |  /  \        /|  |   |  \\
 / ______|\____/|____/    \__/\  / |__|___|  /
 \/                            \/          \/''')
        time.sleep(1.5)
        Again()
            

    OppAttack()



def checkOppSunkShip():  #Same as the player one
    global Pcarrier
    global Pbattle
    global Pcruiser
    global Psub
    global Pdestroyer

    
    if Pcarrier == []:
        print('\nYour opponent has sunk the your CARRIER')
        time.sleep(1.5)
        Pcarrier.append('a')
    elif Pbattle == []:
        print('\nYour opponent has sunk the your BATTLE SHIP')
        time.sleep(1.5)
        Pbattle.append('a')
    elif Pcruiser == []:
        print('\nYour opponent has sunk the your CRUISER')
        time.sleep(1.5)
        Pcruiser.append('a')
    elif Psub == []:
        print('\nYour opponent has sunk the your SUBMARINE')
        time.sleep(1.5)
        Psub.append('a')
    elif Pdestroyer == []:
        print('\nYour opponent has sunk the your DESTROYER')
        time.sleep(1.5)
        Pdestroyer.append('a')
        
    if Pcarrier == ['a'] and Pbattle == ['a'] and Pcruiser == ['a'] and Psub == ['a'] and Pdestroyer == ['a']:
        os.system('cls')
        print('''
_____ ___                ____                        
\__  |   | ____  __ __  |    |    ____  ______ ____  
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \\
 \____   (  <_> )  |  / |    |__(  <_> )___ \\\  ___/ 
 / ______|\____/|____/  |_______ \____/____  /\___ \\
 \/                             \/         \/     \/''')
        time.sleep(1.5)
        Again()
        
    Attack()


def Again():
    again = input('\nDo you want to play again(y,n): ').lower()
    if again == 'y':
        menu()
    elif again == 'n':
        quit()
    else:
        print('You did not chose one of the potions')
        time.sleep(1.5)
        Again()

    
StartScreen()
