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
                dialogue('Laketree Village:')
                dialogue('\nLaketree Village is situated in the centre of everything nearby. The Abandoned Village is on the hill next to the village; the Forest surrounds the village and the Castle is situated in down the gravel path that connects to the village.')
                dialogue('Laketree Village was built by The Founders. Comprised of THE ALMIGHTY, the Guardian and the Witch, the village was built by them hundreds of years ago.')
                dialogue('The village is said to provide anyone with infinite life but this may be a way of hiding the real way The Founders have lived so long.')
                dialogue('\nThe village was constructed from a magic brick that is unidentifiable for most but The Founders. This means that the houses look new forever.')
                dialogue('Curiously, there is a shrine in the centre of the village that appears to be wearing slowly. This may be the source of the magic.\n')
                continue
            case 'The Forest':
                dialogue('Forest:')
                dialogue('\nThe Forest has concerned many people, for many years. The Forest has been growing very rapidly since the first tree was planted.')
                dialogue('This has sparked many theories as to why it does this. The conclusion that most people arrived at was that the forest was drawing magic and energy from the ground to fuel the village.')
                dialogue('However, this means that zombies and wild boars are created from summoning stones.')
                dialogue('This may have been originally used to create power for THE ALMIGHTY but this may have corrupted his thoughts.')
                dialogue('Predictions say that the trees may draw more power than is avalible within the next 5 years causing the entire forest to go up in flames.\n')
                continue
            case 'The Castle':
                dialogue('Castle:')
                dialogue('\nThe Castle used to be a ruined monument that could have revealed the past of the land.')
                dialogue("Once The Founders arrived, they restored ther castle using the village's magic. Since they restored it, they destroyed all evidence of the past.")
                dialogue("So, we don't know the history of the castle and it simply sits they as THE ALMIGHTY's den.")
                dialogue("Currently, the castle is occupied by THE ALMIGHTY and also holds THE ALMIGHTY's prisoners.")
                dialogue('It is very dangerous to go down to the Castle but it holds lots of treasure and valuable people.\n')
                continue
            case 'Abandoned Village':
                # the original village.
                dialogue('Abandoned Village:')
                dialogue('\nThe Abandoned Village was once the home of adventurers. However, it got left behind in hope of a new place to settle.')
                dialogue('It is currently occupied by many zombies. The village used to have hundreds of markets and huts but these were all destroyed.')
                dialogue('The history of the village is mostly hidden by The Founders in a hidden chamber somewhere. The horrid history of the village is best not known.\n')
                continue
            case 'Return':
                return
            case _:
                print('Try again.')
                continue


def people():
    choices = ['The Guardian', 'Swordsmith', 'Armourer', 'Witch', 'Metalworker', 'Woodworker', 'Chemist', 'Villager', 'Return']

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
            case 'The Guardian':
                dialogue('The Guardian:')
                dialogue('\nThe Guardian is one of the 3 founders of Laketree Village. Known for his incredible magic skills and intelligence, he was the protector of the founders.')
                dialogue('Along with the Witch and THE ALMIGHTY, he built the foundations of the new village for newcomers to survive in.')
                dialogue('However, when THE ALMIGHTY turned on them he was the only alive founder. He thought...')
                dialogue('The Guardian can be found only in the village. Due to the imminent threat from THE ALMIGHTY, he keeps his distance.\n')
                continue
            case 'Swordsmith':
                dialogue('Swordsmith:')
                dialogue("\nThe Swordsmith is an unusual character. Although he doesn't speak much he knows a lot more than most.")
                dialogue('He is the trusted sword maker in the village and he keeps the wild boars out of the other villagers way.')
                dialogue('He is often found in the forest and at his hut making swords and hammers. His boar that he keeps around is not very friendly. So, make sure you do not get on his bad side.\n')
                continue
            case 'Armourer':
                dialogue('Armourer:')
                dialogue('\nThe newcomer of the bunch is the Armourer. His incredible talent to create beautiful patterns in his armour is apreciated by the other villagers.')
                dialogue('He was once hired by THE ALMIGHTY, until he escaped his cage one day. He now provides villagers with shields, in case of an attack.')
                dialogue('He is definitely not known for his spelling, however. The sign on his hut reads "WElLcOm too Mee Hut! ArM oRuH."')
                dialogue('He can be found walking through the forest at times but this leaves him vulnerable to being robbed. This happens often... too often.\n')
                continue
            case 'Witch':
                dialogue('Witch:')
                dialogue('\nThe Witch is one of the 3 founder of Laketree Village. She was the only female survivor from the old village.')
                dialogue('Within the village, she was responsible for constructing everything with the power of magic. However, when THE ALMIGHTY got jealous of her ability he captured her.')
                dialogue('For years she was suspected to be in the castle but it was never truly known.')
                dialogue('She is often found hiding in her hut, conjuring magic and creating puzzles and games.\n')
                continue
            case 'Metalworker':
                dialogue('Metalworker:')
                dialogue('\nThe Metalworker is like the Swordsmith of the new generation. He mines his own metals and ores and completes the entire process from scratch.')
                dialogue('His item are very expensive but well crafted. They are the best in all of the land. However, he is a simple and lazy person.')
                dialogue('So, you can often find him sleeping at his hut. He is willing to bargain when half asleep. So, for the best deals wake him up first.\n')
                continue
            case 'Woodworker':
                dialogue('Woodworker/Bushcraft Warrior:')
                dialogue('\nWhether he is or is not actually a woodworker, we do not know. However, he is an incredible pickpocket and robber.')
                dialogue('We know that he goes by the name "The Bushcraft Warrior" at night. He roams the forest looking for victims. In the day, he attempts to rob houses. Especially the armourer.')
                dialogue('We do not know where he often is. If we did, we would stop getting robbed.\n  ')
                continue
            case 'Chemist':
                dialogue('Chemist:')
                dialogue('\nThe Chemist is the younger, alchemist brother of the Witch. He is known for his tricks.')
                dialogue('The Chemist has talent similar to the Witch but he uses it to trick villagers instead.')
                dialogue('The Chemist was the first child born and raised in the new village.')
                dialogue('The Chemist can be found at his house, brewing potions in his garden.\n')
                continue
            case 'Villager':
                dialogue('Villager:')
                dialogue("\nThis villager is lacking intelligence. So, he keeps drinking the Chemist's potions")
                dialogue('We do no know much about the Villager because he always is cursed by something. Currently, he is only able to speak backwards. Previously, he has been turned into a frog; was only able to walk on his hands; thought he was a dog and he became French.')
                dialogue('He is often found at his house, shouting for help.\n')
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

    choices = ['Places', 'People', 'Enemies', 'Return']

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
            case 'People':
                people()
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
