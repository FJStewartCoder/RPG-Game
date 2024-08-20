from random import randint
from dialogue import dialogue

# change code A once missions are checked
# test stats


def die():
    dialogue('\nUnfortunately, this is the end of the road for you...')
    quit()


def mission_1(player):
    dialogue(
        'Now that you are familiar with Laketree Village, we must venture back into the forest.')
    dialogue('Should we go left or right?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                direction = 'left'
                break
            case 'right':
                direction = 'right'
                break
            case _:
                print('Try again!')
                continue

    if direction == 'right':
        dialogue(
            'This way is notoriously difficult to navigate and you may meet some WILD BOARS on the way.')

        if player.fight(True, 'w10'):
            dialogue(
                'WOW! No one has ever survived that. I wonder what is down here...')
            dialogue('There is a path here. We should follow it...')
            dialogue(
                '\nYou find some armour and weapons and you are teleported back to the village. You gain 10dmg and 50hp.')
            dialogue('\nYou remember nothing...', bonus_sleep_time=1)

            player.damage += 10
            player.max_health += 50
            player.health = player.max_health
        else:
            dialogue(
                '\nI forgot to mention that no one has ever survived that. I am glad you are alive.')
            dialogue(
                '\nI will heal you this once but in future I will not be here to help.')
            dialogue('\nWe should return to the village...', bonus_sleep_time=1)

            player.health = player.max_health
    else:
        dialogue('Whew! I thought you would pick the right. No one has ever survived that way. Thank you for taking the safe way.')
        dialogue(
            '\nYou walk for many miles into the forest and you find nothing. Until you reach a large ravine.')
        dialogue('Strung high on a tree, a sign reads "x 4 $$$$$".')
        dialogue('What will you do... jump or leave?', 0)

        while True:
            choice: str = input('>>> ').lower()
            match choice:
                case 'jump':
                    pass
                case 'leave':
                    dialogue('\nDisappointing journey... We will leave.')
                    break
                case _:
                    print('Try again!')
                    continue

            dialogue('It is a noble choice to jump. We must do it.')
            dialogue(
                'You make the jump and explore the area. You find some treasure...')
            dialogue(
                'You find a shiny sword and wooden shield. You gain 1dmg and 5hp. Then you head back to the village.')

            player.damage += 1
            player.max_health += 5
            player.health = player.max_health

            break

        dialogue('\nYou are now back at the village.')


def mission_2(player):
    dialogue("Today, you will be meeting one of the shopkeepers here. Be warned he doesn't like to speak.", bonus_sleep_time=1)
    dialogue('You will be alone from now on. Good luck!')
    dialogue(
        '\nSlowly, you walk towards the man. Tall and stern, he stands towering over you.')
    dialogue('Suddenly, he says *GRUNT*')
    dialogue('What do you say back... grunt or greeting?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'grunt':
                dialogue('He says back *GRRRRRUNNTT*')
                dialogue('\nSuddenly, you see his Wild Boar coming to attack you.')

                if player.fight(True, 'w1'):
                    dialogue(
                        'You anger the merchant. He is coming to attack you.')

                    if player.fight(False, 'm1'):
                        dialogue(
                            'You proved yourself to the merchant. He provides you with a Legendary Sword. You gain 5dmg.')

                        player.damage += 5
                        break
                    else:
                        dialogue('You WERE warned...', bonus_sleep_time=1)
                        break
                else:
                    dialogue('Well that IS a bad start...', bonus_sleep_time=1)
                    break

            case 'greeting':
                dialogue(
                    '\nYou attempt to engage in conversation with the merchant but he, simply, grunts back.')
                dialogue(
                    '\nHe hands you a new sword concept, he had come up with. He grunts to approve you taking it.')
                dialogue(
                    'You inspect the sword. Attached, there is a small shield and a well crafted leather grip.')
                dialogue(
                    '\nYou thank him and leave, swiftly. You gain 1dmg and 5hp.')

                player.damage += 1
                player.max_health += 5
                player.health += 5

                break
            case _:
                print('Try again!')
                continue

    dialogue('\n*Swordsmith Unlocked*')


def mission_3(player):
    dialogue('I see you met the Swordsmith. How was he, anyways?')
    dialogue('Before we continue this adventure I think you should upgrade your equipment. I will provide you with 2 options. Mighty ARMOUR or The Brave SWORD. Which will you take?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'sword':
                dialogue(
                    '\nBrilliant choice, Adventurer. This sword has been mine, since I was a small child. Wield it well and keep it safe for me.')
                dialogue('\nYou take the sword, carefully. You gain 3dmg.')

                player.damage += 3
                break
            case 'armour':
                dialogue("\nThe scared man's choice. Well, don't fear. This armour will provide you with incredible protection. Made from the strongest titanium, you'll be almost invincible with this.")
                dialogue('\nYou put on the armour. You gain 15hp.')

                player.max_health += 15
                player.health += 15
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nNow, we can continue the adventure. Towards the castle we go.')
    dialogue(
        'After a short walk, down the gravel path, you encounter several paths in the road.')
    dialogue('\nThere is rock, between the four paths, that reads "FOUR numbers form the sequence. ONE leads to the treasure. THREE leads to your demise and TWO contain monsters you would not want to fight."')
    dialogue(
        'So, which path will you take? Path ONE, path TWO, path THREE or path FOUR.', 0)
    find_treasure = False

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'one':
                find_treasure = True
                dialogue(
                    "\nYou walk down the path, completely safe, but don't get greedy...", bonus_sleep_time=1)
                break
            case 'two':
                dialogue("\nThe fighter's choice... Let the fight begin.")
                dialogue(
                    '\nYOU WILL FACE 3 WAVES OF MONSTERS. WORST OF LUCK TO YOU.')
                dialogue('\nWAVE 1 COMMENCING...')

                if player.fight(True, 'z5', 'g3', 'w1'):
                    dialogue('WAVE 2 COMMENCING...')
                else:
                    dialogue(
                        'Running causes the mob to get angry. They capture and kill you.')
                    die()

                if player.fight(True, 'g5', 'w3'):
                    dialogue('WAVE 3 COMMENCING...')

                else:
                    dialogue(
                        'Running causes the mob to get angry. They capture and kill you.')
                    die()

                if player.fight(True, 'w5'):
                    dialogue('URRGGHHHH...', 1)
                    dialogue('GO THROUGH...', 1)
                    break
                else:
                    dialogue(
                        'Running causes the mob to get angry. They capture and kill you.')

                    die()
            case 'three':
                dialogue(
                    'You wander down the path. You turn around... and see... THE FOG.', bonus_sleep_time=2)
                dialogue('You are engulfed by the fog and die...')

                die()
            case 'four':
                dialogue(
                    'You walk down the path but you see some enemies... and you are trapped.', bonus_sleep_time=1)

                if player.fight('z5', 'w5'):
                    dialogue(
                        'Whew! I thought we were going to die. We should run.')
                else:
                    dialogue(
                        '\nWe should return to the village. This is too dangerous.')
                    return
                break
            case _:
                print('Try again!')
                continue

    if find_treasure:
        dialogue(
            'Hey, look! There is some treasure there. Will you pick it up... yes or no?', 0)
        while True:
            choice: str = input('>>> ').lower()
            match choice:
                case 'yes':
                    dialogue('\nI SAID DO NOT BE GREEDY...',
                             bonus_sleep_time=1)
                    dialogue(
                        'Suddenly, you are dropped into a pit of guards. You are killed.')

                    die()
                case 'no':
                    dialogue(
                        'Well done! You passed the greed test. As a reward, take a 5hp bonus.')

                    player.max_health += 5
                    player.health += 5
                    break
                case _:
                    print('Try again!')
                    continue

    dialogue('\nHere is the castle...', bonus_sleep_time=0.5)
    dialogue('\nThe castle is surrounded by guards and boars. You will have to fight them, before we continue. Good luck!')

    if player.fight(True, 'g5', 'w3'):
        dialogue(
            'You walk, carefully, through the castle. Pictures flood the walls of captured warriors...')
        dialogue('You hear a whoosh...', 1)
        dialogue('You turn...', 1)
        dialogue('You are alone.', 1)
        dialogue('You run back to the village, with no guardian to see.')

    else:
        dialogue(
            'As you run, you realise you are alone. Your guardian is gone...', bonus_sleep_time=1)

    dialogue('\n*GUARDIAN has been captured*')


def mission_4_alt1(player):
    # Forest way
    dialogue('You choose to wander into the forest.\n')
    dialogue('Immediately, you are faced with a fork in the road.')
    dialogue('Will you take the LEFT or RIGHT path?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                dialogue(
                    'Since last time, a bridge over the ravine has been constructed.')

                dialogue('You walk across the bridge...')
                break

            case 'right':
                dialogue(
                    'The boars remembered since last time. They have increased their numbers.')

                if player.fight(True, 'w25'):
                    dialogue('"Whew!" you think. You run along.')
                else:
                    dialogue(
                        'When you run, you drop your weapon. However, you have survived. You lose 2dmg.')

                    player.damage -= 2
                break
            case _:
                print('Try again!')
                continue

    dialogue(
        '\nYou arrive at some enemies. Some boars and guards stand infront of you.')

    if not player.fight(True, 'w3', 'g5'):
        dialogue(
            'When you run, you trip. The guards pick you up and throw you into the ravine. You die from the fall.')
        die()

    dialogue(
        'You survive the ambush. Ahead of you is a straight path to the merchant. You follow it.')
    dialogue(
        '\nYou see something sparking out of the ground. Do you pick it up... yes or no?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'yes':
                dialogue('Upon touching the treasure, you are cursed.')
                dialogue(
                    'The curse causes you to lose half of your maximum health and damage.')

                if player.damage > 1:
                    player.damage //= 2
                if player.max_health > 1:
                    player.max_health //= 2
                if player.health > player.max_health:
                    player.health = player.max_health
                dialogue('Cursed, you walk down the path.\n')
                break
            case 'no':
                dialogue('You walk, shortly, down the path...')
                break
            case _:
                print('Try again!')
                continue


def mission_4_alt2(player):
    # New tunnel
    dialogue('You choose to follow the tunnel.\n')
    dialogue('You approach with caution but soon realise it is safe.')
    dialogue('\nYou think "This must be what the riddle meant...". Feeling confident, you travel down the long, round tunnel.')
    dialogue('\nAt the end, you see two, identical paths. However, one has some wandering boars. The other has a man at the end.')
    dialogue('Will you take the path with the BOARS or the path with the MAN?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'boars':
                dialogue(
                    'What did you think would happen? You died... I do not know what to tell you.')
                die()
            case 'man':
                dialogue(
                    'You follow the path. The man greets you. He says "Hello. I am nice man."')
                break
            case _:
                print('Try again!')
                continue

    dialogue(
        'He points to the left and says "That way!" You thank him and continue on.')
    dialogue('\nYou follow the path for many miles. It feels never ending. However, you continue over the hills. Finally, you end up in the forest with a straight path to the merchant.')
    dialogue('\nThen, after a short walk down the path...')


def mission_4_ending(player):
    dialogue('You make it to the merchant. Five guards surround him.')
    dialogue('\nThe merchant shouts to you "Defeat the guards and I will be freed."')

    if player.fight(True, 'g5'):
        dialogue(
            'Well done, Adventurer. Thank you for saving me. Take this armour as a reward. You gain 5hp.')

        player.max_health += 5
        player.health += 5

        dialogue('We should run back to the village. Tommorow, meet me for a quest.')
        dialogue('\nYou return to the village.\n')
        dialogue('*Armourer Unlocked*')
    else:
        dialogue(
            'You try to run but you get captured. Waiting years, you die of old age.')
        die()


def mission_4(player):
    dialogue('Now that you are alone, you must select your own paths and adventures.')
    dialogue('\nYou find some directions, although cryptic, it reads...')
    dialogue('"Plees HElp. I um thuh merCHunT. I hoeP yoo finD thus MeSSij. I huV been taykun by thuH moNsturrrS. Too FiND mee tayk thuh Paff in thuH darrrrk. ThUh loong Rownd. No by thuh PiGGees. There nice Man too Hulp. Then Mee is thurrr. Gud Look!!"\n')
    dialogue('You see a tunnel, which you have never explored. Also, you remember the gravel path and the way through the forest.')
    dialogue('Which path with you take? Tunnel, gravel or forest?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'gravel':
                break
            case 'forest':
                mission_4_alt1(player)
                mission_4_ending(player)
                return
            case 'tunnel':
                mission_4_alt2(player)
                mission_4_ending(player)
                return
            case _:
                print('Try again!')
                continue

    # gravel path way (Castle)
    dialogue('You choose to walk via the castle.\n')
    dialogue('As you walk down the path, you hear screams from the castle. You think "I did not hear those screams the first time."')
    dialogue('\nYou begin to regret this choice but you continue anyway. You see some boars. They are chasing you...', bonus_sleep_time=1)
    if player.fight(True, 'w10'):
        dialogue('The boars drop some treasure. You investigate...',
                 bonus_sleep_time=1)

        bonus = randint(1, 3)
        if bonus == 1:
            dialogue('You find a damaged helmet. You gain 5hp.')
            player.health += 5
            player.max_health += 5
        elif bonus == 2:
            dialogue('You find a blunt mace. You gain 1dmg.')
            player.damage += 1
        else:
            dialogue(
                'You find a damaged helmet and a blunt mace. You gain 5hp and 1dmg.')
            player.health += 5
            player.max_health += 5
            player.damage += 1

    else:
        dialogue(
            'You sprint past the boars. Exhausted, you are glad to have survived.')

    dialogue('\nPassed the boars now, you make it to a hilly stone path. You continue on...', bonus_sleep_time=1)
    dialogue('As you walk along, you trip down a hill.')
    dialogue(
        '\nYou drop your weapons and damage them. You are injured and lose some health.')

    if player.health <= 15:
        dialogue(
            '\nDue to your previous injuries, the fall causes you to bleed to death.')
        die()
    else:
        weapon_damage = player.damage // 2
        dialogue(f'\nYou permenantly lose 15hp and {weapon_damage}dmg.')

        player.health -= 15
        player.max_health -= 15
        player.damage -= weapon_damage

    dialogue('\nNow, you can see the merchant through the trees. However, you are faced with multiple paths...', bonus_sleep_time=1)
    dialogue('You see a left path that leads through some brambles, a path in the middle that leads straight to the merchant and a path to the right. You can see nothing on the right path.')
    dialogue('Which path will you take... left, middle or right?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                dialogue(
                    'A camoflaged man appears from the bushes... The Bushcraft Warrior')

                if player.fight(False, 'b1'):
                    dialogue('You make it past the dead warrior...\n')
                    break
                else:
                    dialogue(
                        'Shaken, you run and trip into some brambles. You die from the poison.')
                    die()

            case 'middle':
                dialogue('You think you are safe...', bonus_sleep_time=2)
                dialogue(
                    'Suddenly, you are shot by several arrow traps. You die from your injuries.')
                die()
            case 'right':
                dialogue(
                    'Although dark, you feel your way through. You leave the darkness, completely safe...', bonus_sleep_time=2)
                break
            case _:
                print('Try again!')
                continue

    mission_4_ending(player)


def mission_5_swordsmith(money, inventory):
    dialogue("You walk to the Swordsmith's\n")

    if money >= 100:
        dialogue(
            'When you arrive, the Swordsmith grunts at you and presents you a small hammer and a large hammer...')
        dialogue('Which hammer will you take... large or small?', 0)

        while True:
            choice: str = input('>>> ').lower()
            match choice:
                case 'large':
                    dialogue('You take a large hammer.')

                    inventory.append('LH')
                    break
                case 'small':
                    dialogue('You take a small hammer.')

                    inventory.append('SH')
                    break
                case _:
                    print('Try again!')
                    continue

        dialogue('\nYou assume the hammer is free...')
        dialogue('Until the Swordsmith tackles you and takes 100 of your gold coins.')
        money -= 100

    else:
        dialogue('When you arrive, the Swordsmith pick you up and throws you away.')
        dialogue('He can smell that you do not have enough gold coins.')

    return money


def mission_5_woodworker(money, inventory):
    dialogue("You walk to the Woodworker's\n")
    dialogue('You see that he does not have many items to offer.')

    if money != 0:
        dialogue(
            'When you arrive, he shoves some sandpaper into your hands and takes all the gold you have.')

        money = 0
        inventory += ['SP']

        dialogue(
            'Despite being angry, you leave swiftly to ensure you are safe from the Woodworker.')
    else:
        dialogue('When you arrive, no one is there. So, you leave.')

    return money


def mission_5_metalwork(money, inventory):
    dialogue("You walk to the Metalworker's\n")
    dialogue('When you arrive, the Metalworker asks to see how much gold you have.')
    dialogue(f'\nYou present him with {money} gold coins.\n')

    if money >= 75:
        dialogue('He says "I have a steel rod or steel sheet that I can offer you."')
        dialogue('Then, he says "Which will you take... the ROD or SHEET?"', 0)
        while True:
            choice: str = input('>>> ').lower()
            match choice:
                case 'rod':
                    dialogue('You take a steel rod.')

                    inventory.append('SR')
                    break
                case 'sheet':
                    dialogue('You take a steel sheet.')

                    inventory.append('SS')
                    break
                case _:
                    print('Try again!')
                    continue

        dialogue(
            '\nHe tells you "That is 75 gold coins." Then, you give him the gold coins.')

        money -= 75

        dialogue('\nHe thanks you for the trade and you leave, swiftly.')
    else:
        dialogue(
            'He tells you "You do not have enough money, so you will have to leave."')

    return money


def mission_5(player):
    dialogue("You remember what the merchant said. You walk through the village in search of his hut. Although it isn't immediately obvious to you which hut is his, once you see his sign, you know the small, brown hut is where he resides.")
    dialogue('\nYou walk over to his hut...')
    dialogue('\nHe says, in a slow, wise voice, "I have been robbed, while in the forest. I will provide you with 200 gold coins and you will need to buy me some items. I need a steel sheet, a small hammer and some sandpaper. If you are left with any spare money, do what you want with it. However, it will disappear once you leave."', bonus_sleep_time=2)
    dialogue('\nYou leave, to begin shopping.')

    inventory = []
    money = 200

    while True:
        print(f'\nGold Coins: {money}\n')

        choices = ['Swordsmith', 'Woodworker', 'Metalworker',
                   'Return to Armourer', 'Abandon Mission']

        for option_num, option in enumerate(choices):
            print(f'{option_num + 1} - {option}')

        while True:
            try:
                choice = int(input('>>> '))
                if choice > len(choices) or choice <= 0:
                    print('Try again.')
                    continue
                break
            except ValueError:
                print('Try again!')
                continue

        match choices[choice - 1]:
            case 'Swordsmith':
                money = mission_5_swordsmith(money, inventory)
            case 'Woodworker':
                money = mission_5_woodworker(money, inventory)
            case 'Metalworker':
                money = mission_5_metalwork(money, inventory)
            case 'Return to Armourer':
                dialogue('Returning to Armourer...\n')
                break
            case 'Abandon Mission':
                dialogue('Ending Mission...')
                return
            case _:
                print('Try again!')

    dialogue('Thank you Adventurer for returning to me, hopefully, with some items.\n')

    reward = 0

    if 'SP' in inventory:
        reward += 1
    if 'SS' in inventory:
        reward += 1
    if 'SH' in inventory:
        reward += 1

    if reward == 0:
        dialogue(
            'Unfortunately, you brought be back no items that I needed. Very disappointing.')
        dialogue('\nYou leave...', 1)
        return
    elif reward == 1:
        dialogue(
            'Thank you for bringing back one item I need. You could have brought back more...', bonus_sleep_time=1)

    elif reward == 2:
        dialogue('Two items is very good. Thank you for these. However, we must wonder what could have happened if you had brought all of the items back...', bonus_sleep_time=1)
    else:
        dialogue('Incredible job, Adventurer. I knew that I could count on you to bring me back all of the items. I wish you the best of luck in the rest of your adventures.')

    armour_reward = reward * 5

    dialogue(
        f'\nAnyways, here is a reward based on the items you brought back for me. You get a {armour_reward}hp bonus.')

    player.max_health += armour_reward
    player.health += armour_reward

    dialogue('\nThank you again, Adventurer.')
    dialogue('\nYou leave...', 1)


def mission_6(player):
    dialogue('You wake up, in a cold sweat, at midnight. You are having visions of your guardian trapped in the castle. You see this as a sign to try investigate his location.')
    dialogue('As you leave, you hear whispers saying "Good luck..."',
             bonus_sleep_time=1)
    dialogue('You descend the gravel path, towards the castle. Running swiftly, you know you must get to the castle as soon as possible.')
    dialogue('However, you know that you are in for some trouble when you see some guards chasing you down.')

    if player.fight(True, 'g5'):
        dialogue('After you defeat the guards, you interogate one of them.')
        dialogue('The guard says "As I ran from the back of the castle... I took the path on the left... that one has guards. I urge you to take the other path. The code to the gate was on a rock..." Then, the guard drops dead.', bonus_sleep_time=2)
    else:
        dialogue(
            'You run through the guards. They lose sight of you, in the dark. You are injured but safe.')

    dialogue('\nThe castle is now infront of you, surrounded by a lava moat. Stones collapse from the towers and walls as you are stood there.')
    dialogue('\nOut of nowhere, two paths appear. One that leads to the left of the castle and another that leads around the right of the castle.')
    dialogue('Which path will you take... left or right?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                direction = 'left'
                break
            case 'right':
                direction = 'right'
                break
            case _:
                print('Try again!')
                continue

    if direction == 'left':
        if player.max_health <= 10:
            dialogue(
                'Due to the heat of the lava and your lack of armour, the heat melts you. You die.')
            die()
        else:
            dialogue(
                'You walk a short way down the path. As you walk, your armour melts off due to the heat of the lava. You lose 10hp.')

            player.max_health -= 10
            if player.health > player.max_health:
                player.health = player.max_health

    else:
        dialogue(
            'Once you see guards running at you, you realise he meant his left. The guards trample you and you die.')
        die()

    dialogue('You arrive at a gate. You see it has a lock on it. There is a 4 digit code that must be entered on the lock...')
    dialogue('What do you do... LEAVE or enter a CODE?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'leave':
                dialogue('Unsure of the code, you leave defeated.')
                return
            case 'code':
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nYou choose to enter a code.\n')

    code = input('CODE: ').strip()
    if code != '4132':
        dialogue(
            'Unfortunately, this code is incorrect. You are dropped into the pit of lava. You die.')
        die()

    dialogue('The code is correct. The gate opens.')
    dialogue('\nOnce you enter the castle, it is pitch black. Nothing. You begin getting cold and scared. Alone.', bonus_sleep_time=1)
    dialogue('\nWhen you think all hope is lost... you see a light. A woman in a cage, with a long purple robe and crooked, pointy hat. A witch.')
    dialogue(
        '\nWith hope that she has some information, you attempt to break her out.')
    dialogue('\nShe whispers to you "Go. I will try to weaken the cage, while you sleep. Come back and free me, later. To be prepared, do you want a DAMAGE buff or HEALTH buff?"', 1)

    while True:
        choice: str = input('>>> ').lower()

        dialogue('The witch waves her wand...', 1)

        match choice:
            case 'damage':
                dialogue('You gain 10dmg.')

                player.damage += 10
                return
            case 'health':
                dialogue('You gain 50hp.')

                player.health += 50
                player.max_health += 50
                break
            case _:
                print('Try again!')
                continue

    dialogue('Swiftly, you thank her. Then, you run back to the village...')


def mission_7_riddle_left():
    dialogue('You choose to take the left path...\n')
    dialogue('As you walk across the sticks and stones, you slip and trip several times. These treacherous conditions catch you out. Then, you arrive at a giant rock in the middle of the path.\n')
    dialogue('There is a riddle, encraved in the rock. It reads:\n')
    dialogue('It is like me but from the sea. Put me on your food and it will be tasty. I dissolve in water, like sugar but if you eat too much it is unhealthy. What am I?', 0)

    answers = {'salt', 'salts', 'sea salt'}
    answer = input('>>> ').lower()

    dialogue(f'You encrave the answer, {answer}, into the rock...')
    dialogue('The rock rolls...', 2)

    if answer in answers:
        dialogue('...to the side and lets you pass. You continue down the path.')
    else:
        dialogue('...on top of you, crushing you. You die.')
        die()


def mission_7_riddle_right():
    dialogue('You choose to take the right path...\n')
    dialogue('You stumble over the fallen logs. You accumulate some scratches to your gear as you go. You get to some trees that you have to duck under and you hit your head a couple of times.')
    dialogue('Then, you reach a wall of trees. Pinned on, there is a piece of paper with a riddle on it. It reads:\n')
    dialogue('Brown and brittle, a child of mine. They cover me, like spines. The other path is covered with these. You could use me as a sword. What am I?', 0)

    answers = {'stick', 'sticks', 'branch', 'branches'}
    answer = input('>>> ').lower()

    dialogue(f'You write the answer, {answer}, onto the paper...')
    dialogue('The trees fall...', 2)

    if answer in answers:
        dialogue('...forwards, forming a bridge. You continue over the bridge.')
    else:
        dialogue('...towards you, crushing you. You die.')
        die()


def mission_7_gravel(player):
    dialogue('He tells you should take the gravel path.')
    dialogue('You continue via the gravel path...')
    dialogue('\nImmediately, you are swarmed by enemies...')
    if player.fight(True, 'z10', 'g10', 'w10'):
        dialogue('You are happy that the enemies are out of the way. You continue.')
    else:
        dialogue(
            'You run passed the swarm. They lose sight of you because of their numbers.')

    dialogue(
        '\nYou climb over some collapsed trees, before you reach a fork in the road.')
    dialogue('\nHaving never seen this before, you take caution in your observations. You see, on the left path, many rocks and sticks that lay around. This appears to be a hazard. On the right path, there are some fallen trees that sit in the middle of the path.')
    dialogue('Which path will you take... left or right?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                mission_7_riddle_left()
                break
            case 'right':
                mission_7_riddle_right()
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nExhausted from thinking, you walk and see that the paths rejoin. You have to jump over some fences and dodge some traps but you are now able to see the castle.')
    dialogue(
        '\nJust when you thought this journey was over, some guards spring out at you.')

    if player.fight(True, 'g15'):
        dialogue(
            'Quickly, you steal their armour and swords before running. You gain 20hp and 4dmg.')

        player.health += 20
        player.max_health += 20
        player.damage += 4
    else:
        dialogue('Upon running you drop some gear. You lose 1dmg and 5hp')

        player.damage -= 1
        player.max_health -= 5
        if player.health > player.max_health:
            player.health = player.max_health

    dialogue('You have to jump over another fence but...')


def mission_7_tunnel(player):
    dialogue('He tells you should take the tunnel.')
    dialogue('You continue via the tunnel...')
    dialogue('\nWith a long walk down the tunnel ahead, you wonder what could have been. If you never started this adventure. If you had never taken a certain path. If you had made a certain choice. If you had never let your guardian get captured...')
    dialogue('\nHowever, you are interupted by a swarm of enemies.')

    if not player.fight(True, 'w10', 'g20'):
        dialogue('Upon running you drop some gear. You lose 1dmg and 5hp.')

        player.damage -= 1
        player.max_health -= 5
        if player.health > player.max_health:
            player.health = player.max_health

    dialogue('\nYou see more enemies coming... You run.', bonus_sleep_time=1)
    dialogue('\nYou do not walk far, before a shadow descends upon you.')
    dialogue('You see a towering, armoured guard before you. You must fight it.')

    if player.fight(False, 'M1'):
        dialogue('After defeating the mega guard, you pick up some of the gear it had. You gain 20hp from the carbon-plated armour and 4dmg from the lava sword.')
        dialogue('\nYou see that there is a short walk left to go.')

        player.health += 20
        player.max_health += 20
        player.damage += 4
    else:
        dialogue(
            "Due to it's slow speed, you are able to run passed it. You see only a short way left to go.")

    dialogue('\nYou make the short way down the path, before...')


def mission_7(player):
    dialogue('You are woken, by banging around the village. You look out of your window and see thousands of guards and boars surrounding the village.')
    dialogue('\nYou wonder whether entering the castle caused an attack on the village. All you know is that you must get to the castle.')
    dialogue(
        'The armourer rushes through the door. The shouts, in a panic, "THE CASTLE! THE CASTLE!"')
    dialogue('\nYou decide that you should pick a way to make it to the castle. You decide to ask the merchant which path to take... the gravel or tunnel?')
    dialogue('\nHe thinks...', 3)

    if randint(1, 2) == 1:
        mission_7_gravel(player)
    else:
        mission_7_tunnel(player)

    dialogue('You make it to the front of the castle, once again.')
    dialogue('\nYou run around the side and to the back by the gate. The large metal gate stands infront of you.')
    dialogue('\nYou realise there is only one way through... smash through the door.')
    dialogue("You punch the door and it explodes off of its hinges.")
    dialogue('\nThe shaken witch is sitting in the middle of the cage room. She tells you that when she broke out of the cage, it set off the security and the guards came to attack the village.')
    dialogue(
        '\nShe thanks you for coming back for her and she teleports you back to the village...')


def mission_8(player):
    dialogue('You are visited by the witch.')
    dialogue('\nShe says "I know where he is. The guardian. He was wheeled in, in a cage. They took him and dropped him through a hole in the floor. I have seen people go in there before. The basement is down there."')
    dialogue('She waits, before saying "We should collect some gear and upgrade it together. Then, we can all fight together to get the guardian back."')
    dialogue('Then, she says "I can give you a small buff. So which do you want... DAMAGE buff, HEALTH buff or buff BOTH."', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'damage':
                dialogue('She says "I will give you a 20% damage boost."')

                player.damage *= 1.2
                player.damage = round(player.damage)
            case 'health':
                dialogue('She says "I will give you a 20% health boost."')

                player.max_health *= 1.2
                player.max_health = round(player.max_health)
                player.health = player.max_health
            case 'both':
                dialogue(
                    'She says "I will give you a 10% damage boost and 10% health boost."')

                player.damage *= 1.1
                player.damage = round(player.damage)

                player.max_health *= 1.1
                player.max_health = round(player.max_health)
                player.health = player.max_health
            case _:
                print('Try again!')
                continue
        break

    dialogue('"Good choice." she says.')
    dialogue("\nYou leave and begin walking to the swordsmith. You walk through the scared villagers, before arriving at the swordsmith's shop.")
    dialogue(
        '\nBefore you get to speak to him, he shows you two hammers and shouts "HAMMER!"')
    dialogue('\nOne hammer is made from carbon steel and engraved with a picture of a boar. The other is made from sharp obsidian and is covered with spikes.')
    dialogue(
        'Which hammer will you pick... the CARBON hammer or the OBSIDIAN hammer?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'carbon':
                dialogue('You choose the carbon steel hammer. You gain 4dmg.')

                player.damage += 4
                break
            case 'obsidian':
                dialogue('You choose the obsidian hammer. You gain 5dmg.')

                player.damage += 5
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nBefore you leave, the swordsmith grunts at you. You leave swiftly.')
    dialogue('\nYou only need one more piece of gear, before you return. Some armour. So, you begin your walk over to the armourer.')
    dialogue('He is already standing outside. He is expecting you. He tells you "The witch told me to prepare you two armour options. So, which do you want?"')
    dialogue('\nOne of the pieces is a pair of fireproof boots made from the strongest, boar leather. The other is a titanium helmet, designed to look like a dragon.')
    dialogue(
        'He says "Which piece would you like... the fireproof BOOTS or the dragon HELMET?"', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'boots':
                dialogue('You choose the fireproof boots. You gain 30hp.')

                player.health += 30
                player.max_health += 30
                break
            case 'helmet':
                dialogue('You choose the dragon helmet. You gain 15hp and 3dmg.')

                player.health += 15
                player.max_health += 15
                player.damage += 3
                break
            case _:
                print('Try again!')
                continue

    dialogue(
        '\nGreat choice Adventurer. You better run along now. Go save our guardian!')
    dialogue('\nYou leave...')


def mission_9_tunnel(player):
    dialogue('You begin digging a hole.')
    dialogue('\nYou find that digging a hole will take a while. So, the witch provides you with a magical drill.')
    dialogue(
        '\nThis proves highly effective and allows you to dig most of the way under the castle.')
    dialogue('\nAfter you have been digging for 15 minutes, you think about giving up. However, your tunnel is stormed guards. You must fight.')

    if not player.fight(True, 'g20'):
        dialogue(
            'You try to run but you have no where to go. The guards capture you.')
        die()

    dialogue('You are glad that you defeated the guards. You continue digging out the tunnel until you reach the wall.')
    dialogue('Now at the wall, there is only one way through. Dig out the wall.')
    dialogue('Once you begin digging, the walls above you collapse. Trapped, you die from being crushed.')
    die()


def mission_9_maze():
    dialogue('Which way will you go... left or right?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                return 'left'
            case 'right':
                return 'right'
            case _:
                print('Try again!')
                continue


def mission_9_front(player):
    dialogue('You choose the front door.')
    dialogue(
        '\nBefore you even get to the door, guards attack you. The castle is well guarded.')

    if not player.fight(True, 'g15', 'w5'):
        dialogue('You were unable to defeat the guards. They capture you.')
        die()

    dialogue('You slam the door, to prevent any more guards coming in. Pictures fall off the wall. Only ONE is LEFT. Suddenly, the lights turn on and you are faced with two paths.')
    dialogue('\nYou are unable to see anything down the paths. You must guess.',
             bonus_sleep_time=1)

    if mission_9_maze() != 'left':
        dialogue(
            '\nYou take the right path. It is trapped. A boulder falls from the ceiling. You are crushed.')
        die()

    dialogue('\nYou take the left path. You wonder if you have gone the RIGHT way. Your question is answered when you reach another fork.')
    dialogue('\nFOUR roof tiles falls behind you. You must make a choice, quickly.')

    if mission_9_maze() != 'right':
        dialogue('\nYou take the left path. The roof collapses on you. The injuries you sustain leaves you immobile. Guards capture you.')
        die()

    dialogue('\nYou take the right path and you end up in a room with many statues. On your left are SIX guards. On your RIGHT there are three boars.')
    dialogue('\nContinuing reveals another two paths to take but...')

    if mission_9_maze() != 'right':
        dialogue('\nYou take the left path and you step on a pressure plate. This animates the statues and they capture you immediately.')
        die()

    dialogue('\nYou take the right path. You get to rest now, as there is a long path ahead of you. You think "I have already taken THREE paths. How many are LEFT."')
    dialogue('\nThen, you reach another fork. There is nothing, anywhere.')

    if mission_9_maze() != 'left':
        dialogue(
            '\nYou take the right path. You walk for miles and miles. You get nowhere. You are trapped.')
        die()

    dialogue('\nYou take the left path. You are immediately greeted with a sign, that reads "Only TWO paths remaining."')
    dialogue('\nAs you walk to the next fork, you wonder if it is RIGHT.')

    if mission_9_maze() != 'right':
        dialogue(
            '\nYou take the left path. A large sign swings from the ceiling, hitting you. You die, immediately.')
        die()

    dialogue('\nYou take the right path. You know, LEFT, there is only ONE more path.')
    dialogue('\nAfter a short walk, you make it.')

    if mission_9_maze() != 'left':
        dialogue(
            '\nYou take the right path. On the final hurdle, you stumble. So close to the guards, they capture you.')
        die()

    dialogue('\nYou take the left path. You are greeted with a door. It has a six digit pin but no hints.')
    dialogue('\nAfter some careful thinking, you realise that there have been clues along the way. The six statues, the one painting, the four tiles.')
    dialogue('What is the code?')

    intended_answer = '146321'
    answer = input('CODE: ').strip()

    if answer == intended_answer:
        dialogue('\nThe door opens. You walk through and down the stairs.')
    else:
        dialogue('\nA hole in the floor opens. You fall into a pit of lava. You got the code wrong and the consequence is death.')
        die()


def mission_9_back(player):
    dialogue('You take the path around the back.')
    dialogue('\nThe path is engulfed by guards, running towards the village. You are fearful of what will happen to the village.')
    dialogue('\nYou are arrive at the blown off door, it is guarded strongly. The guards immediately try to attack you.')

    if not player.fight(True, 'g25'):
        dialogue('The guards swarm you. Unfortunately, they capture you.')
        die()

    dialogue('After passing the guards, you walk down a long corridor. The walls still flooded with pictures of captured warriors. However, there is a new one. It is of the guardian.')
    dialogue('\nYou do not walk long before you are met with a locked door. It has a six digit code on it. Next to the door, there is a puzzle that reads:\n')

    intended_answer = '698512'

    dialogue('There are three pairs of consecutive digits. None of the digits are the same. The sum of the six digits is 31. The sum of the smallest and largest digit is ten. If you rotate, 180 degrees, the first digit, the first two digits would be the same. The first two digits are in ascending order. Digits in position two and three are a consecutive pair, in reverse order. The smallest digit is in the fifth position. The sum of digits in the fourth and fifth positions is six.')

    answer = input('CODE: ').strip()

    if answer == intended_answer:
        dialogue('\nThe gate opens. You walk through and down the stairs.')
    else:
        dialogue('\nA hole in the floor opens. You fall into a pit of lava. You got the code wrong and the consequence is death.')
        die()


def mission_9(player):
    dialogue('The witch says "Nice haul of gear that you have got there. Now, we must infiltrate the castle. I will teleport us outside but then you will be alone from there."')
    dialogue('\nTeleporting...', 2)
    dialogue('You appear outside of the castle.')
    dialogue('\nYou must now decide your method of infiltration. Will enter through the FRONT, around the BACK or TUNNEL underground to get to the basement?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'front':
                mission_9_front(player)
                break
            case 'back':
                mission_9_back(player)
                break
            case 'tunnel':
                mission_9_tunnel(player)
            case _:
                print('Try again!')
                continue

    dialogue(
        'When you arrive at the guardian, several swarms of guards prepare to attack you.')

    dialogue('\nWAVE 1 COMMENCING...')
    if player.fight(True, 'z25', 'g15', 'w10'):
        dialogue('WAVE 2 COMMENCING...')
    else:
        dialogue('Running causes the boars trample you. You die from your injuries.')
        die()

    if player.fight(True, 'g20', 'w15'):
        dialogue('WAVE 3 COMMENCING...')
    else:
        dialogue('Running causes the mob to get angry. They capture and kill you.')
        die()

    if not player.fight(True, 'w25'):
        dialogue(
            'Running causes the boars to see you as lunch. They eat you alive and you die.')
        die()

    dialogue('All of the guards are defeated.')
    dialogue("\nYou run over to the guardian's cage. Before anymore guards arrived, you attempt to smash open the door. You, desperately, hit the bars with your hammer. Although damaged, the cage was not open.")
    dialogue('\nYour banging causes THE ALMIGHTY to wake up. You realise he is the person behind these capturings. However, you do not have enough time to process this before you are attacked.')

    player.fight(False, 'a1')

    dialogue('You realise that it is impossible. You NEED more power. The witch sees you struggling and teleports you back to the village.')
    dialogue('\nYou feel defeated... the guardian was still trapped.',
             bonus_sleep_time=1)
    dialogue('\nYou hear a voice shout "What do you look so disappointed about?"',
             bonus_sleep_time=1)
    dialogue('You turn around...', 2)
    dialogue('It is the guardian...', 2)


def mission_10_guardian_sacrifice():
    dialogue('You choose to sacrifice the guardian...\n')
    dialogue('With this power, your team will be able to defeat THE ALMIGHTY. First, you must all gather around me. Once I begin this procedure, you must hold on tightly. You will be granted my power, upon reaching THE ALMIGHTY and you will have to work together to defeat him. Good luck!')
    dialogue('\nIt will be sad to see y...')
    dialogue(
        '\nHe ascends and begins glowing. You grab on. He begins to spin and his heat rises.')
    dialogue(
        '\nBANG! He explodes, in a ball of light and you are thrown across the village.')
    dialogue('\nSuddenly, THE ALMIGHTY arrives.')
    dialogue(
        'Once he arrives, everyone gains a golden aura around them. Together, you feel powerful.')
    dialogue('\nEveryone begins swinging their weapons at him but nothing happens. The power seems disappointing. You hear a voice. "TOGETHER." You relay the message.')
    dialogue('\nYou come together and are able to create a golden, plasma laser. Together you use it to defeat THE ALMIGHTY.')
    dialogue('As he is taken down, the castle collapses, the guards fall dead and the forest is cleared of its fog. YOU SAVED THE WORLD!')
    dialogue('Despite feelings of elation, you are missing a piece. Your guardian...',
             bonus_sleep_time=2)
    dialogue('\nWELL DONE ADVENTURER! You beat the game. If you would like to play again to try other paths, please restart. You may find that there are other endings.')
    quit()


def mission_10_sacrifice_everyone(player):
    dialogue('You choose to sacrifice everyone...\n')
    dialogue('You apologise to everyone. It must be done, to gain enough power.')
    dialogue(
        '\nThe guardian says "I will do this quickly, so you do not have to suffer."')
    dialogue('He snaps his fingers and everyone but him disappears. He begins glowing. Before he sacrifices himself, he says "Save the world, for us."')
    dialogue('He says "Goodbye, Adventurer." Then, he disappears. You feel powerful.')

    player.max_health = 500
    player.damage = 200
    player.health = player.max_health

    dialogue('\nThen, THE ALMIGHTY arrives screaming. He sends out some minions...')

    if not player.fight(True, 'g50', 'w100'):
        dialogue('Unfortunately, you are overwhelmed by minions.')
        dialogue('THE ALMIGHTY takes over your village and grows in power. Eventually, he gains enough power to take over the rest of the world.\n')
        dialogue('Your adventure has come to an end and the game is over. Unfortunately, you lose. If you would like to play again to try other paths, please restart. You may find that there are other endings.')
        quit()

    dialogue(
        'HOW DARE YOU DEFEAT MY MINIONS! TAKE ME ON, IF YOU THINK YOU ARE SO POWERFUL!')

    if not player.fight(False, 'a1'):
        dialogue('HAHAHA. WEAKLING. I KNEW YOU WERE AS WEAK AS YOU LOOK.')
        dialogue('THE ALMIGHTY, with a new found rage, kills everyone. I mean EVERYONE. The world is now covered with boars, guards and fire.\n')
        dialogue('Your adventure has come to an end and the game is over. Unfortunately, you lose. If you would like to play again to try other paths, please restart. You may find that there are other endings.')
        quit()

    dialogue('THE ALMIGHTY HAS FALLEN! You feel incredible. The all powerful.')
    dialogue('\nHowever, no one is left to celebrate. You sacrificed all of them. Then, you realise...', bonus_sleep_time=2)
    dialogue('YOU WERE THE ALMIGHTY, ALL ALONG. YOU KILLED EVERYONE FOR POWER...',
             bonus_sleep_time=2)
    dialogue('\nAlthough you completed the objective and won, is this really the reality you wanted? If you would like to play again to try other paths, please restart. You may find that there are other endings.')
    quit()


def mission_10_team_effort():
    dialogue('You choose the team effort...\n')
    dialogue('If we plan, it will never work out. Just attack him with whatever you have got and with the power of teamwork, we will take him down.')
    dialogue('Everyone agrees. They decide to shout "WE ARE READY FOR YOU, ALMIGHTY!" The swordsmith just grunts.')
    dialogue(
        '\nSuddenly, THE ALMIGHTY rises from the ground shouting "ARE YOU CHALLENGING ME?"')
    dialogue('\nYES. YES WE ARE. Everyone charges.')
    dialogue('\nYou slash him with your sword; the guardian uses a powerful laser beam; the swordsmith bites his leg; the armourer shields the team and the witch casts curses. Your efforts fail.')
    dialogue('\nYOU THOUGHT THAT WOULD WORK?')
    dialogue('\nYou have one last idea... with an almighty power you never had before. You hold your breath... and sacrifice yourself.', bonus_sleep_time=2)
    dialogue('\nYou remember nothing. You live on as a ghost. The battle is over. The world is returned to normal.')
    dialogue('In the middle of the village, there is monument of you, erected in your memory. On the plaque, it reads "THE BRAVE ADVENTURER!"')
    dialogue('\nWELL DONE ADVENTURER! You saved the world. Although dead, you live on in the memory of everyone. You win. If you would like to play again to try other paths, please restart. You may find that there are other endings.')
    quit()


def mission_10(player):
    dialogue('You ask "How did you get out? It is a miracle."\n')
    dialogue('He says "There is no time to explain. We MUST come up with a plan to defeat THE ALMIGHTY."')
    dialogue('We could make a sacrifice. If I sacrifice myself, you will all reach maximum power. Together, you will be able to defeat him.\n')
    dialogue('You do not think this is enough power. You suggest sacrificing everyone and you will save the world. Alone.\n')
    dialogue('"We could all just fight. Everyone. Together." says the witch.\n')
    dialogue('You are now left with options. Which will you take... sacrifice GUARDIAN, SACRIFICE everyone or EVERYONE goes to fight?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'guardian':
                mission_10_guardian_sacrifice()
            case 'sacrifice':
                mission_10_sacrifice_everyone(player)
            case 'everyone':
                mission_10_team_effort()
            case _:
                print('Try again!')
                continue


if __name__ == '__main__':
    print('Wrong file')
