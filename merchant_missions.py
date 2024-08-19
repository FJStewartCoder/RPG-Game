from dialogue import dialogue
import random as r
import witch_games as w

# if you gain more than a certain amoint of damage or health, you cant play any missions


def swordsmith(player):
    reward_multiplier = 1

    dialogue("You walk to the Swordsmith's hut.")
    dialogue('\nWhen he sees you coming, he begins grunting at you.')
    dialogue('\nYou ask "Do you have a quest, for me?"')

    if player.damage >= 12:
        dialogue('He says "YOU TOO POWERFUL!" Then, he shuts you out.')
        return

    enemy_type = r.choice(['z', 'w'])
    enemy_amount = r.randint(1, 15)
    enemy_code = enemy_type + str(enemy_amount)

    if enemy_type == 'z':
        enemy_name = 'zombie'
    else:
        enemy_name = 'wild boar'
        reward_multiplier = 2

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


def armourer(player):
    # similar quest to mission 5
    # there will be 5 merchants that all sell 2 items. this is constant.
    # However, the merchant will want 3 different random items each time.
    # based on how many yoh return you get better reward
    pass


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


def witch_1(player, bonus_type):
    # go in to the witch's house
    # she has a magic locked container
    # can't be opened with magic
    # it has a riddle on it
    # random riddle from a selection
    # if you get it wrong you leave
    pass


def witch_2(player, bonus_type):
    # you walk towards the hills
    # you've never seen them before
    # you reach an infested village
    # defeat all the enemies
    # if you fail to defeat them you run back
    # otherwise you raid the village
    # you can raid one of three houses
    # the reward in each is randomised
    pass


def witch_3(player, bonus_type):
    dialogue('Well, I do have some games for you. To prove your worth, we will begin with a best of 5 game of the classic...')
    dialogue('Rock, Paper, Scissors... Good luck!')
    if w.rock_paper_scissors(5, 'Witch'):
        dialogue('Well done... Well done... You played well.')
        dialogue('Now that you have proven you are good enough, I have another game for you.')
    else:
        dialogue('Hahahahahaha. You lose, So, you must leave. Goodbye Adventurer!')
        return

    dialogue('The next game, although simple, is entirely luck based. You will have 2 dice and you will roll them.')
    dialogue('I, also, have 2 dice and will roll them. Whoever has the highest roll wins the round.')
    dialogue('This game will be best of 5. Good luck!')

    if w.dice_game(5, 'Witch'):
        pass

    # If you win dice game you recieve a reward from the spinning wheel. Random number between 1, 2.
    # else, you spin the de-buff wheel and recieve a debuff between 0.5 - 1
    pass


def witch(player):
    # gives options 3 options for percentage buffs - damage, health, both
    # then you will recieve one of three predetermined but randomised wuests
    dialogue("You walk to the Witch's hut.")
    dialogue('She teleports infront of you, causing you to jump. You say to her "You really have to stop doing that. It is scaring off the neighbours."')
    dialogue('She asks "What do you want anyway? A quest?"')
    dialogue('Yes... how did you know?')

    bonus_type = ''

    if player.max_health >= 75 and player.damage >= 20:
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

    dialogue('Will you accept my offer, Adventurer?', 0)

    while True:
        choice: str = input('>>> ').lower()
        match choice:
            case 'yes':
                dialogue('Great! Let us begin.')
                break
            case 'no':
                dialogue('Unfortunate. Goodbye Adventurer.')
                return
            case _:
                print('Try again!')
                continue

    quest_number = r.randint(1, 3)
    eval(f'witch_{quest_number}(player, bonus_type)')
