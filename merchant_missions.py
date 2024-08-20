from dialogue import dialogue
import random as r
import witch_games as w

# if you gain more than a certain amoint of damage or health, you cant play any missions
# spacing on witch mission 3


def swordsmith(player):
    reward_multiplier = 1

    dialogue("You walk to the Swordsmith's hut.")
    dialogue('\nWhen he sees you coming, he begins grunting at you.')
    dialogue('\nYou ask "Do you have a quest, for me?"')

    if player.damage >= 20:
        dialogue('He says "YOU TOO POWERFUL!" Then, he shuts you out.')
        return

    enemy_type = r.choice(['z', 'w'])

    if enemy_type == 'z':
        enemy_name = 'zombie'
        enemy_amount = enemy_amount = r.randint(1, 15)
    else:
        enemy_name = 'wild boar'
        enemy_amount = enemy_amount = r.randint(1, 5)
        reward_multiplier = 2
    
    enemy_code = enemy_type + str(enemy_amount)

    reward_multiplier += enemy_amount // 5

    dialogue(f'YOU GET SWORD. KILL {enemy_name.upper()}. {enemy_amount}.', 5)
    dialogue('\nYou begin walking, into the forest. The Swordsmith guides you.')
    dialogue('\nSome trees stand in your way...')
    dialogue('What will you do... MOVE or JUMP over the trees?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'move':
                dialogue('You ask "Can you move th..."')
                dialogue('He already moved them.')
                dialogue('You thank him and continue on.')
                break
            case 'jump':
                dialogue('You tell him "We have to jump over the logs."')
                dialogue('\nBefore you know it, you are dangling in the air.')
                dialogue(
                    'Then, the Swordsmith puts you down and he jumps over the logs.')
                dialogue(
                    'Not what you meant but it worked. You thank the Swordsmith and continue on.')
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nAfter a long, winding walk through the forest, you eventually reach a shrine like area. A summoning rock.')
    dialogue('The Swordsmith bangs on the rock. The enemies appear.')

    if player.fight(True, enemy_code):
        reward = 1 * reward_multiplier

        dialogue(
            f'The Swordsmith picks up a {enemy_name} on his back. You walk back to his hut.')
        dialogue(
            f'\nWhen you arrive back, the Swordsmith presents you with a sword. You gain {reward} damage.')

        player.damage += reward
    else:
        dialogue(f'The Swordsmith sees you struggling. So he performs a secret whistle that stops the {enemy_name}s from attacking you.')
        dialogue('\nHe picks you up by your feet and drags you back to his hut.')
        dialogue('He says "YOU FAIL!"')


def shop_swordsmith(money, inventory):
    dialogue("You walk to the Swordsmith's\n")
    dialogue('Before you arrive at his hut, he stands outside. He is shouting "HAMMER!"')
    if money == 0:
        dialogue('He immediately charges at you and throws you away. He could smell that you did not have enough gold.')
        return money
    dialogue('\nOnce you arrive, he presents you with two hammers. A small hammer and a large hammer.')
    dialogue('Which hammer will you take... large or small?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'large':
                dialogue('You take a large hammer.')
                inventory.append('Large Hammer')
                break
            case 'small':
                dialogue('You take a small hammer.')
                inventory.append('Small Hammer')
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nThe Swordsmith grunts. Then, he shouts "MONEY!"')
    dialogue('How much money will you give him?')

    while True:
        try:
            cost = int(input('>>> '))
            if cost <= 0 or cost > money:
                print('Try again.')
                continue
            break
        except ValueError:
            print('Try again.')
            continue

    if cost < 50:
        money_stolen = r.randint(cost, money)
        dialogue('\nYOU DID NOT GIVE HIM ENOUGH MONEY. HE IS ANGRY!')
        dialogue(f'\nHe tackles you and steals {money_stolen - cost} of your money. Then, he throws you out.')
        money -= money_stolen
    else:
        money -= cost
        dialogue('\nHe grunts at you. You leave, quickly.')

    return money


def shop_woodworker(money, inventory):
    dialogue("You walk to the Woodworker's\n")
    if money == 0:
        dialogue('No one is to be seen. You leave.')
        return money

    dialogue('He moves around, swiftly. He runs up to you and asks "You need stuff? I have wood or sandpaper. Watcha want?"')
    dialogue('Will you take the WOOD or the SANDPAPER?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'wood':
                dialogue('You take the plank of wood.')
                inventory.append('Plank of Wood')
                break
            case 'sandpaper':
                dialogue('You take the sandpaper.')
                inventory.append('Sandpaper')
                break
            case _:
                print('Try again!')
                continue

    dialogue('\nYou can have it free. I have enough.')
    dialogue('\nYou thank him. However, your pockets feel very light. Your money has been stolen. You turn around. No one.')

    if r.random() >= 0.5:
        inventory = []
    money = 0

    dialogue('You leave, swiftly.')

    return money


def shop_metalworker(money, inventory):
    dialogue("You walk to the Metalworker's\n")
    dialogue('When you arrive and knock on his door, he is woken from his slumber.')
    dialogue('\nI have just woken up. What do you want? I only have an axe or pickaxe, on hand.')
    dialogue('\nHow much money do you have?')
    dialogue(f'You present him {money} gold coins.')
    if money < 50:
        dialogue('Unfortunately, I can not offer you one.')
        return money
    
    cost = 50
    final_offer = False

    dialogue(f'\nSince, I have just woken. I will offer you one for {cost} gold coins.')

    while True:
        dialogue('Will you accept... Yes or no?', 0)
        choice: str = input('>>> ').lower()
        match choice:
            case 'yes':
                break
            case 'no':
                if final_offer:
                    dialogue('Unfortunately, I can not offer you this item. You leave.')
                    return money
                else:
                    if r.randint(1, 3) == 1 and cost > 40:
                        cost -= r.randint(1, cost - 40)

                        messages = [f'How about {cost}?', f'Maybe, I can do {cost}', f'I could go to {cost}.', f'Will you take one for {cost}?']
                        message = r.choice(messages)
                        
                        dialogue(f'\n{message}')
                    else:
                        dialogue('\nUnfortunately, I can not go any lower.')
                        final_offer = True
                    continue
            case _:
                print('Try again!')
                continue
    
    dialogue('\nI like your offer. However, which item would you like?')
    dialogue('Would you like the PICKAXE or the AXE?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'pickaxe':
                dialogue('You take the pickaxe.')
                inventory.append('Pickaxe')
                break
            case 'axe':
                dialogue('You take the axe.')
                inventory.append('Axe')
                break
            case _:
                print('Try again!')
                continue
    
    dialogue('\nIt was good doing business, with you. Goodbye, Adventurer.')
    money -= cost

    return money


def shop_chemist(money, inventory):
    dialogue("You walk to the Chemist's\n")
    dialogue('When you arrive, he is brewing a potion in the garden outside his hut.')
    dialogue('\nWelcome! I am guessing you come for some items. Well, I have only two items. A glass bottle and this potion.')
    dialogue('Surely, you need one of them. First, how much money do you have? It costs 10 gold for one.')
    dialogue(f'\nYou present him with {money} gold coins.')

    if money < 10:
        dialogue('\nUnfortunately, you do not have enough money for my items.')
        dialogue('You leave.')
        return money
    
    dialogue('\nSo, which item do you want... the glass BOTTLE or the POTION?', 0)
    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'potion':
                dialogue('You take the potion.')
                inventory.append('Potion')
                break
            case 'bottle':
                dialogue('You take the glass bottle.')
                inventory.append('Glass Bottle')
                break
            case _:
                print('Try again!')
                continue
    
    money -= 10

    dialogue('\nHEHEHEHEHEHE. Thank you, Adventurer, for you purchase.')
    dialogue('Worried, you leave.')

    return money


def shop_villager(money, inventory):
    dialogue("You walk to the Villager's\n")
    dialogue("He comes out screaming 'HUUUAAAHHHHHH sdrawkcab kaeps ylno nac I dna noitop s'tsimehC eht knurd I !esaelp ,em pleH'", bonus_sleep_time=4)

    if 'Potion' in inventory:
        dialogue('?on ro seY .tceffe siht esrever dluohs tI ?noitop eht ekat I fi ,dnim uoy oD', bonus_sleep_time=4)
        while True:
            choice: str = input('>>> ').lower()
            match choice:
                case 'no':
                    dialogue('You give him the potion')
                    inventory.remove('Potion')
                    in_reverse = False
                    break
                case 'yes':
                    dialogue('Sorry. I am just looking for some items.')
                    in_reverse = True
                    break
                case _:
                    print('Try again!')
                    continue
    else:
        dialogue('.tceffe siht xif lliw ti ,noitop a em teg nac uoy fI', bonus_sleep_time=4)
        in_reverse = True
    
    if in_reverse:
        dialogue('\nThe villager runs off screaming "HHHUUUUUAAAAAHHHHHHHHH!"')
    else:
        dialogue('\nI can not thank you enough, Adventurer.')
        dialogue('Take this bucket and shovel, for free.')
        dialogue('\nYou leave, equipped with a bucket and shovel.')
        
        inventory.append('Bucket')
        inventory.append('Shovel')

    return money


def armourer(player):
    dialogue("You walk to the Armourer's hut.\n")
    if player.health >= 100:
        dialogue('You have just caught me, as I leave to go shopping. I will catch up with you later.')
        return
    
    items_needed = r.choices(['Small Hammer', 'Large Hammer', 'Plank of Wood', 'Sandpaper', 'Pickaxe', 'Axe', 'Glass Bottle', 'Potion', 'Bucket', 'Shovel'], k=3)

    dialogue('I am so glad to see you Adventurer. I have been robbed. Again. That Woodworker is a menace. He keeps robbing me of my things.')
    dialogue('So, I need you to get me some items and I will reward with some armour.')
    dialogue('\nThe items that I need are:', 0)
    for item in items_needed:
        dialogue(f'-{item}', 1)

    inventory = []
    money = 200

    while True:
        print(f'\nGold Coins: {money}\n')

        choices = ['Swordsmith', 'Woodworker', 'Metalworker', 'Chemist', 'Villager', 'Return to Armourer', 'Abandon Mission']

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
                money = shop_swordsmith(money, inventory)
            case 'Woodworker':
                money = shop_woodworker(money, inventory)
            case 'Metalworker':
                money = shop_metalworker(money, inventory)
            case 'Chemist':
                money = shop_chemist(money, inventory)
            case 'Villager':
                money = shop_villager(money, inventory)
            case 'Return to Armourer':
                dialogue('Returning to Armourer...\n')
                break
            case 'Abandon Mission':
                dialogue('Ending Mission...')
                return
            case _:
                print('Try again!')
    
    items_collected = 0
    for item in items_needed:
        if item in inventory:
            items_collected += 1

    dialogue('Thank you, Adventurer, for returning. It is good to see you. I hope you have brought me back some items.')
    dialogue("Let's see what you got...\n")

    if items_collected == 0:
        dialogue('I know that you could have done better than that. No items. Disappointing.')
        dialogue('Unfortunately, you get no reward for that.')
        dialogue('\nYou leave.')
        return
    elif items_collected == 1:
        dialogue('One item. I would have liked more but it is better than nothing.')
        dialogue('For your effort, I will award you a shield. A 5hp bonus.')
    elif items_collected == 2:
        dialogue('Two items. One away from a full house. I appreciate your efforts.')
        dialogue('As you collected two items, I will award you a helmet. A 10hp bonus.')
    else:
        dialogue('A full house. Very well done, Adventurer. Now, I will be able to go on with everything I want to.')
        dialogue('For your incredible effort, I will award you a chestplate. A 15hp bonus.')
    
    player.max_health += items_collected * 5
    player.health += items_collected * 5

    dialogue('\nThank you again, Adventurer. Goodbye!')


def give_reward(player, bonus_type, reward_amount):
    if bonus_type == 'health':
        player.max_health *= reward_amount
        player.max_health = round(player.max_health)
        player.health = player.max_health

    elif bonus_type == 'damage':
        player.damage *= reward_amount
        player.damage = round(player.damage)

    else:
        reward_amount = (reward_amount + 1)/2

        player.damage *= reward_amount
        player.damage = round(player.damage)

        player.max_health *= reward_amount
        player.max_health = round(player.max_health)
        player.health = player.max_health


def witch_riddle_1():
    intended_answers = ['mouse', 'mice', 'mouses', 'rat', 'rats']
    dialogue('Small and furry, I run around. Maybe, in your house. I scurry around and you try to catch me but I am in your walls. I like cheese. So, you set out a trap. I am Jerry, to Tom. What am I?')
    answer = input('>>> ').lower()

    dialogue(f'On the box, you write the answer {answer}.')

    if answer in intended_answers:
        return True
    else:
        return False


def witch_1(player, bonus_type):
    dialogue('Well, I do have a riddle that you could try.')
    dialogue('I have this box and in order to open it, you must answer the riddle. However, I have never been able to solve it. Maybe, you could give it a go.')
    dialogue("\nYou walk inside of the Witch's hut.")
    dialogue('She presents you a box, with a riddle on top. The riddle reads...\n')

    riddles = [witch_riddle_1()]
    riddle_number = r.randint(1, len(riddles))

    if riddles[riddle_number - 1]:
        dialogue('\nThe box opens.')
        dialogue('Thank you. For your efforts, I will reward you greatly.')
        give_reward(player, bonus_type, 1.3)
    else:
        dialogue('\nThe box remains closed.')
        dialogue('Unfortunate. I thought you would be able to open it.')

    dialogue('\nYou leave.')


def witch_2(player, bonus_type):
    dialogue('Well, there is a village that I needed raiding.')
    dialogue('However, it is infested with zombies.')
    dialogue('\nLet me show you...')
    dialogue('She teleports you both outside of the village. There is a large hill, that stands infront of you, that you will have to climb.')
    dialogue('\nYou ask "Can you not teleport us up to the village"?')
    dialogue('No. There is too many zombies to fight.')
    dialogue('\nOnce you get to the top of the hill, zombies immediately attack you.')

    if player.fight(True, 'z250'):
        dialogue('I did not expect there to be that many zombies. I am glad we defeated them.')
    else:
        dialogue('We should go back to the village. There is only more from here.')
        return
    
    dialogue('\nThere are three houses that you could raid. If you help me, I will give the same amount of buff that is in the house.')
    dialogue('\nSuddenly, more zombies appear.')

    if player.fight(True, 'z100'):
        dialogue('Whew! Another lot defeated.')
    else:
        dialogue('We should go back to the village. You never know when more will appear.')
        return

    dialogue('\nFinally, you reach the three huts. Which one will you raid... the LEFT hut, the MIDDLE hut or the RIGHT hut.', 0)
    
    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'left':
                dialogue('The left hut. An interesting choice.')
                break
            case 'middle':
                dialogue('The middle hut. The perfect middle ground.')
                break
            case 'right':
                dialogue("The right hut. Did you pick this because you think that it is the 'right' option?")
                break
            case _:
                print('Try again!')
                continue
    
    reward = round(r.random() + 1, 2)
    dialogue(f'\nOnce you finish raiding the hut, the Witch says "Nice job! I can reward you, with a {round(100 * (reward - 1))}% boost."')
    dialogue('\nWe will now return to the village, victorious.')
    give_reward(player, bonus_type, reward)


def witch_3(player, bonus_type):
    dialogue('Well, I do have some games for you. To prove your worth, we will begin with a best of 5 game of the classic...')
    dialogue('Rock, Paper, Scissors... Good luck!\n')

    if w.rock_paper_scissors(5, 'Witch'):
        dialogue('\nWell done... Well done... You played well.')
        dialogue('Now that you have proven you are good enough, I have another game for you.')
    else:
        dialogue('\nHahahahahaha. You lose, So, you must leave. Goodbye Adventurer!')
        return

    dialogue('\nThe next game, although simple, is entirely luck based. You will have 2 dice and you will roll them.')
    dialogue('I, also, have 2 dice and will roll them. Whoever has the highest roll wins the round.')
    dialogue('This game will be best of 5. Good luck!\n')

    if w.dice_game(5, 'Witch'):
        dialogue('\nWell... I did not expect that.')
        dialogue('Well done! I will let you go.')
        dialogue('\nBefore you go, I will spin this wheel of fortune. This will determine the reward that you will recieve.')
        reward = round(r.random() + 1, 2)
    else:
        dialogue('\nI knew that I would beat you, at that one.')
        dialogue('\nBefore you leave, I will spin this wheel of unfortune. This will determine the curse you will recieve.')
        dialogue('BECAUSE YOU LOSE!')
        reward = round((r.random() + 1)/2, 2)

    give_reward(player, bonus_type, reward)

    dialogue(f'\nThe witch waves her wand and you recieve a {round(100 * (reward - 1))}% {bonus_type} bonus.')
    dialogue('\nThen, you leave.')


def witch(player):
    dialogue("You walk to the Witch's hut.")
    dialogue('\nShe teleports infront of you, causing you to jump. You say to her "You really have to stop doing that. It is scaring off the neighbours."')
    dialogue('\nShe asks "What do you want anyway? A quest?"')
    dialogue('Yes... how did you know?\n')

    bonus_type = ''

    if player.max_health >= 150 and player.damage >= 30:
        # not eligable for any reward.
        dialogue('Unfortunately, my spells are not strong enough to provide you any buffs. You must leave.')
        return
    elif player.damage >= 20:
        dialogue('You are, already, very strong. I can offer you a health boost.')
        bonus_type = 'health'
    elif player.max_health >= 75:
        dialogue('You, already, have a lot of armour. So, I can offer you a damage boost.')
        bonus_type = 'damage'
    else:
        dialogue('I see that your armour is weak, as well as you. I can offer to buff both your health and damage.')
        bonus_type = 'both'

    dialogue('\nWill you accept my offer, Adventurer?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'yes':
                dialogue('Great! Let us begin.')
                break
            case 'no':
                dialogue('Unfortunate. Goodbye, Adventurer.')
                return
            case _:
                print('Try again!')
                continue

    quest_number = r.randint(1, 3)
    eval(f'witch_{quest_number}(player, bonus_type)')
