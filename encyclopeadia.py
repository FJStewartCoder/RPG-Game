from dialogue import dialogue


def places():
    choices = ['Laketree Village', 'The Forest', 'The Castle', 'Abandoned Village', 'Return']

    while True:
        for option_num, option in enumerate(choices):
            print(f'{option_num + 1} - {option}')
        dialogue('\nWhat would you like information on?', 0)

        try:
            choice = int(input('>>> '))
            if choice > len(choices) or choice <= 0:
                print('Try again.')
                continue
        except ValueError:
            print('Try again!')
            continue

        match choices[choice - 1]:
            case 'Laketree Village':
                print('LTree Vlg')
                continue
            case 'The Forest':
                print('Frst')
                continue
            case 'The Castle':
                print('Cstl')
                continue
            case 'Abandoned Village':
                print('Abndnd Vlg')
                continue
            case 'Return':
                return
            case _:
                print('Try again.')
                continue


def merchants():
    choices = ['Swordsmith', 'Armourer', 'Witch', 'Metalworker', 'Woodworker', 'Chemist', 'Villager', 'Return']

    while True:
        for option_num, option in enumerate(choices):
            print(f'{option_num + 1} - {option}')
        dialogue('\nWhat would you like information on?', 0)

        try:
            choice = int(input('>>> '))
            if choice > len(choices) or choice <= 0:
                print('Try again.')
                continue
        except ValueError:
            print('Try again!')
            continue

        match choices[choice - 1]:
            case 'Swordsmith':
                print('Swrdsmth')
                continue
            case 'Armourer':
                print('Armr')
                continue
            case 'Witch':
                print('Wtch')
                continue
            case 'Metalworker':
                print('Mtlwrkr')
                continue
            case 'Woodworker':
                print('Wdwrkr')
                continue
            case 'Chemist':
                print('Chmst')
                continue
            case 'Villager':
                print('Vlgr')
                continue
            case 'Return':
                return
            case _:
                print('Try again.')
                continue


def enemies():
    choices = ['Zombie Child', 'Zombie', 'Guard', 'Wild Boar', 'Boar Merchant', 'Bushcraft Warrior', 'MEGA GUARD', 'THE ALMIGHTY', 'Return']

    while True:
        for option_num, option in enumerate(choices):
            print(f'{option_num + 1} - {option}')
        dialogue('\nWhat would you like information on?', 0)

        try:
            choice = int(input('>>> '))
            if choice > len(choices) or choice <= 0:
                print('Try again.')
                continue
        except ValueError:
            print('Try again!')
            continue

        match choices[choice - 1]:
            case 'Zombie Child':
                dialogue('Zombie Child: 10 Health Points, 2 Damage.')
                dialogue('\nThe zombie child is a simple creature. All it knows is fighting. This has been learned from their parents - the zombie.')
                dialogue('They enjoy wandering around, mindlessly and they are mostly found in the forest.\n')
                continue
            case 'Zombie':
                dialogue('Zombie: 15 Health Points, 3 Damage.')
                dialogue('\nWe are unaware of where the zombies originally came from. It is suspected that they came from the Abandoned Village and THE ALMIGHTY brought them to the forests.')
                dialogue('The zombies are simple in nature but some of the older zombies appear to have more intelligence. Seemly, they are devolving with time.')
                dialogue('The zombies enjoy wandering in the forest and this is where they are most commonly found.\n')
                continue
            case 'Guard':
                dialogue('Guard: 35 Health Points, 5 Damage.')
                dialogue('\nThese are the unspoken warriors of the world. These once were villagers of the town. Since THE ALMIGHTY destroyed the Abandoned Village, the villagers were put under a spell and converted to Guards.')
                dialogue('Every guard is different in nature but they are unable to perform any tasks without instructions from THE ALMIGHTY.')
                dialogue('The Guard is found most often in the forest and by the castle.\n')
                continue
            case 'Wild Boar':
                dialogue('Wild Boar: 50 Health Points, 10 Damage.')
                dialogue('\nThese creature have roamed the forest since before the villagers.')
                dialogue('All that we know about the boars is that they appear from a stone in the forest. Called the summoning stone, they are teleported to the stone from an unknown location.')
                dialogue("Unusually, they are attracted to the Swordsmith's hut. They can be mostly found in the forest and around the castle.\n")
                continue
            case 'Boar Merchant':
                dialogue('Boar Merchant aka. Swordsmith: 150 Health Points, 20 Damage.')
                dialogue('\nInformation on the Boar Merchant/Swordsmith can be found in the Swordsmith section of the Merchants menu.\n')
                continue
            case 'Bushcraft Warrior':
                dialogue('Bushcraft Warrior aka. Woodworker: 200 Health Points, 10 Damage.')
                dialogue("\nThis is the Woodworker's night time identity. He dresses in entirely camoflage to hide from his unsuspecting victims.")
                dialogue('On several occasions he has been able to rob people but he tried too hard on his camoflage and he has very little damage because of it.')
                dialogue('He can be found in the forest if you take the wrong path.\n')
                continue
            case 'MEGA GUARD':
                dialogue('MEGA GUARD: 300 Health Points, 20 Damage.')
                dialogue('\nSince the MEGA GUARD is seen so rarely, not much information is known about it.')
                dialogue('All that is known about it is that it only shows itself in situations of maximum threat.')
                dialogue('It has only ever been seen at the castle.\n')
                continue
            case 'THE ALMIGHTY':
                dialogue('THE ALMIGHTY: 3500 Health Points, 125 Damage.')
                dialogue('\nTHE ALMIGHTY was like you once, an innocent adventurer. However, he got power hungry and gained too much. With as much power as he had, he became corrupt and began to take over.')
                dialogue('It is said that he came from the Abandoned Village but when he tried to gain more power he ruined the village and his size grew huge.')
                dialogue('A legend, written in stone in the forest, says that whoever defeats him will gain his power. What truly happens though is unknown.')
                dialogue('He can be found anywhere and everywhere due to his god-like abilities.\n')
                continue
            case 'Return':
                return
            case _:
                print('Try again.')
                continue


def encyclopeadia():
    dialogue('\nWelcome to the encyclopeadia of this game.')

    choices = ['Places', 'Merchants', 'Enemies', 'Return']

    while True:
        for option_num, option in enumerate(choices):
            print(f'{option_num + 1} - {option}')
        dialogue('\nWhat would you like information on?', 0)

        try:
            choice = int(input('>>> '))
            if choice > len(choices) or choice <= 0:
                print('Try again.')
                continue
        except ValueError:
            print('Try again!')
            continue

        match choices[choice - 1]:
            case 'Places':
                places()
                continue
            case 'Merchants':
                merchants()
                continue
            case 'Enemies':
                enemies()
                continue
            case 'Return':
                break
            case _:
                print('Try again.')
                continue


if __name__ == '__main__':
    encyclopeadia()