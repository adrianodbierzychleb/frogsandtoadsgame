test = ['Toad','Toad','Toad','Empty Space','Frog','Frog','Frog']
restart = ['Toad','Toad','Toad','Empty Space','Frog','Frog','Frog']
win = ['Frog','Frog','Frog','Empty Space','Toad','Toad','Toad']
def main():
    print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
    menu = int(input('Please select an option from the menu'))
    f = 0
    while menu != 5:
        if menu == 1:
            global test
            global restart
            test = ['Toad','Toad','Toad','Empty Space','Frog','Frog','Frog']
            print('Press 1 to start a new game\nPress 2 to restart your game\nPress 3 to go back to the menu')
            reset = int(input('Please select an option'))
            while reset != 3:
                if reset == 1 or reset == 2:
                    print(test)
                    while test != win and reset != 3:
                        f = int(input('where from?'))
                        f2 = f-1
                        t = int(input('where to?' ))
                        t2 = t-1
                        if test[f2] == 'Toad':
                            if (f2-t2==-1 or f2-t2==-2) and test[t2] == 'Empty Space':
                                test[t2] = test[f2]
                                test[f2] = 'Empty Space'
                            else:
                                print('move unavilable')
                            print(test)
                        if test[f2] == 'Frog':
                            if (f2-t2==1 or f2-t2==2) and test[t2] == 'Empty Space':
                                test[t2] = test[f2]
                                test[f2] = 'Empty Space'
                            else:
                                print('move unavilable')
                            print(test)
                        print('Press 1 to continue\nPress 2 to restart your game\nPress 3 to go back to the menu')
                        reset = int(input('Please select an option'))
                        if reset == 2:
                            test = restart
                            print(test)
                    if test == win:
                        print(win)
                        test = ['Toad','Toad','Toad','Empty Space','Frog','Frog','Frog']
                        print("Well done, you have won the game, by making the frogs and toads swap places")
                        won = input("Do you wish to go back to the menu?(yes/no)")
                        if won == 'yes':
                            print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
                            menu = int(input('Please select an option from the menu'))
                        else:
                            print('Thank you for playing, see you soon')
            test = restart
            print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
            menu = int(input('Please select an option from the menu'))
        elif menu == 2:
            print("There are two ways to solve the game, version 1 starting from left hand side,\nand version 2 starting from right hand side")
            select = int(input('Which method do you wish to see, version 1 or version 2?'))
            if select == 1:
                print(test)
                print('Step 1: Move the toad from position 3 to position 4')
                print("['Toad', 'Toad', 'Empty Space', 'Toad', 'Frog', 'Frog', 'Frog']")
                print("Step 2: Move the frog from position 5 to position 3\n['Toad', 'Toad', 'Frog', 'Toad', 'Empty Space', 'Frog', 'Frog']")
                print("Step 3: Move the frog from position 6 to position 5\n['Toad', 'Toad', 'Frog', 'Toad', 'Frog', 'Empty Space', 'Frog']")
                print("Step 4: Move the toad from position 4 to position 6\n['Toad', 'Toad', 'Frog', 'Empty Space', 'Frog', 'Toad', 'Frog']")
                print("Step 5: Move the toad from position 2 to position 4\n['Toad', 'Empty Space', 'Frog', 'Toad', 'Frog', 'Toad', 'Frog']")
                print("Step 6: Move the toad from position 1 to position 2\n['Empty Space', 'Toad', 'Frog', 'Toad', 'Frog', 'Toad', 'Frog']")
                print("Step 7: Move the frog from position 3 to position 1\n['Frog', 'Toad', 'Empty Space', 'Toad', 'Frog', 'Toad', 'Frog']")
                print("Step 8: Move the frog from position 5 to position 3\n['Frog', 'Toad', 'Frog', 'Toad', 'Empty Space', 'Toad', 'Frog']")
                print("Step 9: Move the frog from position 7 to position 5\n['Frog', 'Toad', 'Frog', 'Toad', 'Frog', 'Toad', 'Empty Space']")
                print("Step 10: Move the toad from position 6 to position 7\n['Frog', 'Toad', 'Frog', 'Toad', 'Frog', 'Empty Space', 'Toad']")
                print("Step 11: Move the toad from position 4 to position 6\n['Frog', 'Toad', 'Frog', 'Empty Space', 'Frog', 'Toad', 'Toad']")
                print("Step 12: Move the toad from position 2 to position 4\n['Frog', 'Empty Space', 'Frog', 'Toad', 'Frog', 'Toad', 'Toad']")
                print("Step 13: Move the frog from position 3 to position 2\n['Frog', 'Frog', 'Empty Space', 'Toad', 'Frog', 'Toad', 'Toad']")
                print("Step 14: Move the frog from position 5 to position 3\n['Frog', 'Frog', 'Frog', 'Toad', 'Empty Space', 'Toad', 'Toad']")
                print("Step 15: Move the toad from position 4 to position 5\n['Frog', 'Frog', 'Frog', 'Empty Space', 'Toad', 'Toad', 'Toad']")
                print("The demonstration is complete, you will now be returned to the menu")
                print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
                menu = int(input('Please select an option from the menu'))
            else:
                print(test)
                print("Step 1: Move the frog from position 5 to position 4\n['Toad', 'Toad', 'Toad', 'Frog', 'Empty Space', 'Frog', 'Frog']")
                print("Step 2: Move the toad from position 3 to position 5\n['Toad', 'Toad', 'Empty Space', 'Frog', 'Toad', 'Frog', 'Frog']")
                print("Step 3: Move the toad from position 2 to position 3\n['Toad', 'Empty Space', 'Toad', 'Frog', 'Toad', 'Frog', 'Frog']")
                print("Step 4: Move the frog from position 4 to position 2\n['Toad', 'Frog', 'Toad', 'Empty Space', 'Toad', 'Frog', 'Frog']")
                print("Step 5: Move the frog from position 6 to position 4\n['Toad', 'Frog', 'Toad', 'Frog', 'Toad', 'Empty Space', 'Frog']")
                print("Step 6: Move the frog from position 7 to position 6\n['Toad', 'Frog', 'Toad', 'Frog', 'Toad', 'Frog', 'Empty Space']")
                print("Step 7: Move the toad from position 5 to position 7\n['Toad', 'Frog', 'Toad', 'Frog', 'Empty Space', 'Frog', 'Toad']")
                print("Step 8: Move the toad from position 3 to position 5\n['Toad', 'Frog', 'Empty Space', 'Frog', 'Toad', 'Frog', 'Toad']")
                print("Step 9: Move the toad from position 1 to position 3\n['Empty Space', 'Frog', 'Toad', 'Frog', 'Toad', 'Frog', 'Toad']")
                print("Step 10: Move the frog from position 2 to position 1\n['Frog', 'Empty Space', 'Toad', 'Frog', 'Toad', 'Frog', 'Toad']")
                print("Step 11: Move the frog from position 4 to position 2\n['Frog', 'Frog', 'Toad', 'Empty Space', 'Toad', 'Frog', 'Toad']")
                print("Step 12: Move the frog from position 6 to position 4\n['Frog', 'Frog', 'Toad', 'Frog', 'Toad', 'Empty Space', 'Toad']")
                print("Step 13: Move the Toad from position 5 to position 6\n['Frog', 'Frog', 'Toad', 'Frog', 'Empty Space', 'Toad', 'Toad']")
                print("Step 14: Move the Toad from position 3 to position 5\n['Frog', 'Frog', 'Empty Space', 'Frog', 'Toad', 'Toad', 'Toad']")
                print("Step 15: Move the Frog from position 4 to position 3\n['Frog', 'Frog', 'Frog', 'Empty Space', 'Toad', 'Toad', 'Toad']")
                print("The demonstration is complete, you will now be returned to the menu")
                print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
                menu = int(input('Please select an option from the menu'))
        elif menu == 3:
            print('The rules of the game are the following:')
            print('1. The frog or toad can only move in one direction,\nif they start on the left, they can only move right,\nand if they start on the right, they can only move left.')
            print('2. The frog or toad can only move either one place to an empty space,\nor jump over another frog or toad in to an empty space.\n3. They can not jump over two or more forgs\nor move in to a space already occupied by a frog or toad.')
            print('4. The wining condition is to have the frogs and toads swap places.')
            print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
            menu = int(input('Please select an option from the menu'))
        else:
            print("Menu\nPress 1 to start a game\nPress 2 to watch a demonstration game\nPress 3 to read the rules of the game\nPress 4 to desplay the menu\nPress 5 to exit")
            menu = int(input('Please select an option from the menu'))
            
    print('Thank you for playing the game, hope to see you soon.')
main()
