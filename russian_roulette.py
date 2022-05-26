def russisch_roulette():

    # RUSSISCH ROULETTE

    #####   SECTION B   #####
    def _start_roulette(select, user_status):
        
        totalprize = int(12_000_000 / select)
        print('You can choose between a (G)loc 19 with 15 rounds \nor a (C)olt 45 with 6 rounds:')
        pick = ''
        
        # Plausibilitätskontrolle für Gun-Auswahl
        while pick != 'G' and pick != 'C':
            print('Pick a gun!: G/C')
            pick = input()
        
        gun = {'G' : 15, 'C' : 6}
        mag = [0]

        # Array auf Basis der Magazingräße der Gun bauen (lange Version zum Üben)
        for bullets in mag:
            if max(mag) < gun[pick]-1:
                mag.append(max(mag)+1)
        
        # Array für Spieleranzahl bauen (kurze Version)
        players = list(range(select-1))
                    
        import random
        
        # Dem User eine zufällige Nummer für seine Züge zuweien
        # Damit es Zufall ist ob er oder ein "Computer" anfängt
        user = random.choice(players)
        
        # Der Patrone einen zufälligen Platz im Magazin zuweisen
        bullet = random.choice(mag)

        turn = 0
        player = 0
        for turn in mag:
            # Prüfung ob der User jetzt dran ist
            if player == user:
                msg = 'Your turn! Good Luck Buddy! ... press Enter'
            else:
                if turn == 0:
                    if select == 2:
                        msg = 'Your opponent is is pointing the gun to his temple and preparing to pull the trigger  ... press Enter.'
                    else:
                        msg = 'The first dude pointing the gun to his temple and preparing to pull the trigger  ... press Enter.'
                else:
                    if select == 2:
                        msg = 'Your opponent is pointing the gun to his temple and preparing to pull the trigger  ... press Enter.'
                    else:
                        msg = 'He is pointing the gun to his temple and preparing to pull the trigger  ... press Enter.'
            print(msg)
            input()
            # Prüfung ob in diesem Zug einer stirbt
            if turn == bullet:
                # Prüfung ob der User in diesem Zug stirbt
                if player == user:
                    select -= 1
                    print('You are dead!')
                    user_status = 'dead'
                    print('Press enter ...')
                    input()
                    return select, user_status
                    break
                else:
                    select -= 1
                    prize = int(totalprize/(select))
                    user_status = 'alive'
                    if select == 1:
                        print('He just shot himself in the head!')
                        print(f'Your face is full of his blood and brain.')
                    else:
                        print('That dude just shot himself in the head!')
                        if player -1 == user:
                            print(f'Your face is full of his blood and brain.')
                        else:
                            print(f'The dude next to him is full of his blood and brain.')
                    print(f'But you\'ve just won {prize} Bucks! \nYou Lucky Idiot xD')
                    print('Press enter to take the money and leave the table...')
                    input()
                    return select, user_status
                    break
            else:
                # Prüfung ob jeder Spieler schonmal dran war
                if player < select-1:     
                    player += 1
                    turn +=1
                    # Prüfung der User als nächstes dran ist
                    if player-1 == user:
                        if select == 2:
                            print('You survived! You pass the gun to your opponent!')
                        else:
                            print('You survived! You pass the gun to the next dude!')
                    else:
                        if player == user:
                            print('He survives and passes the gun to you!')
                        else:
                            print('He survives and passes the gun to the next dude.')                 
                else:
                    player = 0
                    turn +=1
                    # Prüfung der User als nächstes dran ist
                    if player-1 == user:
                        print('You survived! Pass the gun to the next dude!')
                    else:
                        if (player) == user:
                            print('He survives and passes the gun to you!')
                        else:
                            print('He survives and passes the gun to the next dude.')                 
              
              
    #####   SECTION A   #####

    print('You got into a bar in a questionable district.')
    print('And you are sitting on a round table with some shady dudes.')
    print('Now they force you to play russian roulette with them.')
    print('At least they leave you the chance to choose between 3 and 8 players.')
    print('But the less players you choose the more money you can win.')

    # Plausibilitätskontrolle für Spieleranzahl
    while True:
        try:
            print('Type an amount of players between 3 and 8:')
            select = int(input())
            while select < 3 or select > 8:
                select = int(input())
        except ValueError:

            continue
        break

    #select = input()
    select = int(select)
    totalprize = 0


    user_status = 'alive'

    while user_status == 'alive' and select > 1:
        select, user_status = _start_roulette(select, user_status)


    #####   SECTION C   #####
        # Überprüfen ob richtige Werte aus Funktion übergeben wurden
        # print(user_status)
        # print(select)

        # Prüfen ob User gestorben ist
        if user_status == 'dead':
            print('\nFortunately you\'ve got numerous lives.')
            print('But if you wanna move forward on your journey, focus and don\'t drink too much!')
            print('It can put you in serious trouble!')
            print('Anyway, you have to start your journey from the very beginning!')
            break
        else:   
            if select > 1:
                totalprize = int(12_000_000 / select)
                prize = int(totalprize / (select-1))
                print('\nYou are offered to play another round with one player less')
                print(f'There are {select} players left, including you.')
                print(f'This time you can win {prize} Bucks.')
                next = ''
                # Plausibilitätskontrolle für ja / nein antwort
                while next != 'y' and next != 'n':
                    print('You wanna go for it? (y/n)')
                    next = input()
                
                # Wenn User nicht gestorben ist, Wiederholung mit Restspeilern anbieten
                if next == 'y':
                    print('No Risk no fun. But you\'re a f!#king maniac pal!')
                    user_status = 'alive'
                    #_start_roulette(select, user_status)
                elif next == 'n':
                    print('Wise decision! Focus and keep yourself off of any trouble in future!')
                    # go to game start
                    print('')
                    break

            
        
russisch_roulette()