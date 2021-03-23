# welcome back to another episode of I make bad comments, wahoo have fun in this mess of a program

import random
import time

deck = []
symbols = ["N", "&", "#", "?", "8", "~", "{", "\\", "L", ">", "+", "=", "!"] # pool of pickable symbols, switched out randomly for each round

basedeck = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] # the alphabet??!?!!!!? what??!!!??!?!?!??
facedeck = [] # the deck shown to the player and to the AI

safedeck = [] # the set of matched cards for the ai to use   (like how i rhymed the names? the side of me which likes the sound does but the side of me which has to remember the difference doesn't)

game = True

decksize = ''

observed = []

mode = ''



def DeckSetup(deck, symbols): # sets up deck before game
    global decksize
    global safedeck
    global observed
    global facedeck
    decksize = ''
    
    
    while type(decksize) != int or decksize == 2 or decksize % 2 != 0: # gets the decksize assigned, and checks that it's an even number between 2 and 26
        decksize = ''
        try:
            decksize = int(input("Input size of deck. Make sure it's an even number, is less than or equal to 26, and is greater than 2. "))
            assert decksize % 2 == 0
            assert decksize != 2
            
        except:
            print("Invalid input.")
        print("")


    locsymbols = []
    ran = 'null'

    for n in range(int(decksize/2)): # creates local list of symbols for the flipped deck to be made from. this allows the size of the deck to be variable whilst there is always
        ran = random.choice(symbols) # a full deck of matching symbols
        
        while ran in locsymbols:
            ran = random.choice(symbols)
        
        locsymbols.append(ran)


    for n in range(decksize): # sets up the facedeck (the one with the letters) by filling it with a number of letters equal to the decksize
        facedeck.append(basedeck[n])
    safedeck = facedeck.copy()
    observed = facedeck.copy()
        
    
    for n in range(decksize): # randomizes the deck and i have absolutely no idea how it works
        sym = locsymbols[random.randint(0, len(locsymbols)-1)]

        if deck.count(sym) == 1:
            deck.append(sym)
        else:
            sym = locsymbols[random.randint(0, len(locsymbols)-1)]

            while deck.count(sym) == 2:
                sym = locsymbols[random.randint(0, len(locsymbols)-1)]

            deck.append(sym)



def DisplayDeck(deck):
    global decksize
    
    print("""
--- --- --- ---
|{0}| |{1}| |{2}| |{3}|
--- --- --- ---""".format(deck[0], deck[1], deck[2], deck[3])) # yeah this is completely disgusting and i hate how it looks so what


    for n in range(decksize-4): # prints out the deck
        if (n+1) % 4 != 0 and n != decksize-5: # the parameters for a set of lines are: if the true card index is divisible by four make a new line, if it's the last card make a new line
            print("|{0}| ".format(deck[n+4]), end='')
            
        else:
            print("|{0}| ".format(deck[n+4]), end='')
            
            if n == decksize-5:
                if decksize % 4 == 2: # checks how many lines should be made based off of the decksize
                    print("\n--- ---")
                else:
                    print("\n--- --- --- ---")
            else:
                print("\n--- --- --- ---")



def GameLoop(deck, basedeck, facedeck):
    global observed
    game = True
    
    while game:
        DisplayDeck(facedeck) # first flip
        selection = 0

        time.sleep(0.5)
        
        while not (selection in basedeck and selection in facedeck): # this loop takes input from user
            selection = input("Enter the letter of the card you would like to flip. ")
            try:
                assert selection in basedeck and selection in facedeck
            except AssertionError:
                print("Invalid input.")
            else:
                break

        facedeck[basedeck.index(selection)] = deck[basedeck.index(selection)]


        DisplayDeck(facedeck) # second flip
        selection2 = 0

        time.sleep(1)
        
        while not (selection2 in basedeck and selection2 in facedeck): # this loop takes input from user
            selection2 = input("Enter the letter of the card you would like to flip. ")
            try:
                assert selection2 in basedeck and selection2 in facedeck
            except AssertionError:
                print("Invalid input.")
            else:
                break

        facedeck[basedeck.index(selection2)] = deck[basedeck.index(selection2)]


        DisplayDeck(facedeck)

        time.sleep(1)

        if facedeck[basedeck.index(selection)] == facedeck[basedeck.index(selection2)]: # evaluates match
            print("Match!")
        else:
            print("No match!")
            facedeck[basedeck.index(selection)] = selection
            facedeck[basedeck.index(selection2)] = selection2

        time.sleep(1)

        
        if facedeck == deck: # evaluates win
            print("You won!")
            time.sleep(3)
            game = False
            


def AILoop(deck, basedeck, facedeck): # oh boy here we go       (future me: the oh boy was necessary this was hard)
    prevselection = 0
    game = True
    
    while game:
        spot = False
        earlyspot = False
        
        selection = prevselection # so that it will always get an initial selection
        
        DisplayDeck(facedeck)

        for n in range(len(observed)):
            for i in range(len(observed)):
                if observed[i] == observed[n] and i != n and observed[i] not in facedeck: # if the ai finds that two cards have been revealed which match, it will override the rest and match them
                    earlyspot = True
                    
                    print("The AI has found a match!")
                    time.sleep(1)
                    
                    print("The AI chose {0}.".format(facedeck[n]))
                    
                    facedeck[n] = deck[n]
                    observed[n] = deck[n]
                    
                    time.sleep(1.5)
                    DisplayDeck(facedeck)

                    time.sleep(1)
                    
                    print("The AI chose {0}.".format(facedeck[i]))

                    facedeck[i] = deck[i]
                    observed[i] = deck[i]
                    
                    time.sleep(1.5)
                    DisplayDeck(facedeck)

                    print("Match!")
                    safedeck.remove(basedeck[n])
                    safedeck.remove(basedeck[i]) # this whole section above is a dumbed down version of the entire below program, have fun making sense of any of it, future me


        if not earlyspot:
            
            safeselection = random.randint(0, len(safedeck)-1)
            while safeselection == prevselection: # first flip
                safeselection = random.randint(0, len(safedeck)-1)
            
            time.sleep(1)
            print("The AI chose {0}.".format(safedeck[safeselection]))

            selection = facedeck.index(safedeck[safeselection]) # the original selection number is chosen from safedeck, meaning it isn't accurate to the actual deck. this changes that

            facedeck[selection] = deck[selection] # 'flips' the card
            selection2 = selection # primes the while loop coming up
            prevselection = selection # stops the ai from choosing this same thing next time round
            observed[selection] = deck[selection] # updates observed cards
            
            time.sleep(1.5)
            DisplayDeck(facedeck)

            
            for n in range(len(observed)):
                if observed[n] == facedeck[selection] and n != selection: # checks through the observed list to see if there are any available matches, overrides below if so
                    print("The AI found a match!")
                    spot = True
                    selection2 = n
                    safeselection2 = safedeck.index(facedeck[selection2])
                    break


            if spot == False:
                safeselection2 = random.randint(0, len(safedeck)-1)
            while safeselection2 == safeselection and spot == False: # second flip
                safeselection2 = random.randint(0, len(safedeck)-1)

            time.sleep(1)
            print("The AI chose {0}.".format(safedeck[safeselection2]))

            if spot == False:
                selection2 = facedeck.index(safedeck[safeselection2])

            facedeck[selection2] = deck[selection2]
            observed[selection2] = deck[selection2]
            
            time.sleep(1.5)
            DisplayDeck(facedeck)

    
            if facedeck[selection] == facedeck[selection2]: # evaluates match
                print("Match!")
                safedeck.remove(basedeck[selection]) # updates safedeck so the ai doesn't pick any matched cards
                safedeck.remove(basedeck[selection2])
                
            else:
                print("No match!")
                facedeck[selection] = basedeck[selection] # resets facedeck
                facedeck[selection2] = basedeck[selection2]

        time.sleep(2)


        if facedeck == deck: # evaluates win
            print("The AI won!")
            time.sleep(3)
            game = False


def ModeSelect():
    global deck
    global symbols
    global basedeck
    global facedeck
    global mode
    
    mode = input("""Which mode would you like to run?
    1 - Singleplayer
    2 - watch an AI be better at match than you little baby man ha ha baby haha baby man
     > """)

    while mode not in ("1", "2"):
        mode = input("Invalid input. Make sure you enter something from the list. ") # that's not a list, it's a tuple!!!!! lol!!!!!

    facedeck = []
    safedeck = []
    observed = []
    deck = []
    
    DeckSetup(deck, symbols)


    if mode == "1": # all that monstrous code initialised in four lines       hmm really lends to the amount of time i spent on this mess
        GameLoop(deck, basedeck, facedeck)
    else:
        AILoop(deck, basedeck, facedeck)



ModeSelect()


while True: # controls the starting and stopping of the game and gamemodes
    retry = input("""\nWould you like to play again?
y - play again
n - quit
g - pick gamemode
 > """)
    
    print("")
    if retry == 'y':
        if mode == "1":
            print("Restarting Singleplayer")
            time.sleep(2)
            
            facedeck = []
            safedeck = []
            observed = []
            deck = []
            DeckSetup(deck, symbols)
            
            GameLoop(deck, basedeck, facedeck)

        else:
            print("Restarting AI")
            time.sleep(2)
            
            facedeck = []
            safedeck = []
            observed = []
            deck = []
            DeckSetup(deck, symbols)

            AILoop(deck, basedeck, facedeck)

    elif retry == 'n':
        print("Thanks for playing")
        time.sleep(2)
        quit()

    elif retry == 'g':
        ModeSelect()


# hope you had fun reading this creature
