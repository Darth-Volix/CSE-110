'''
Weeks 5 & 6 Assignment: Text-based Adventure Game
Nicholas Wilkins 
10/21/2023
'''
import time 

# Program begins, welcoming the user to the game
print()
print('Welcome to "Forest of Terror!", the text-based Adventure Game from VOLIX Studios!')
print('In this game you will be presented a story with options to choose from at various points. When typing in your choice, be sure to watch your\nspelling lest things take a horrific turn! If they do, the game is over and you do not see the end of the story!')
print()

# Program asks the user if they would like to to begin the game
game_start = input('Would you like to begin? (type YES or NO): ')
if game_start.lower() == 'yes':
    # The story starts because the player has conviction
    print()
    choice1 = input('You wake up in a forest at midnight, the fog is thick and the moon is full. You have no idea how you got here.\nYou have no food, weapons, water, or a phone. With any luck, someone is nearby or there is a town not too far away if you follow the northern star.\nDo you call out for help or try and follow the northern star? (type CALL OUT or FOLLOW STAR): ')
    if choice1.lower() == 'call out':
        # Player chose to call out, the story branches based on that choice 
        print()
        print('You call out for help but are only met with silence. Suddenly, an unearthly moaning echoes through the woods, sending shivers down your spine.')
        choice2A = input('Do you investigate the sound? (type YES or NO): ')
        if choice2A.lower() == 'yes':
            # Player chose to investigate the noise
            print()
            print('You cautiously wander towards the source of the noise, thinking another person may be lost out in the woods with you, hurt or confused.\nSuddenly, Shia LaBeouf sprints out of the woods wielding an ax. There is death in his eyes! You realize he must have captured you,\nleft you out here in the woods, and is now hunting you for sport.')
            choice3A = input('Do you fight Shia or try to reason with him? (type FIGHT or REASON): ')
            if choice3A.lower() == 'fight':
                # Player chose to fight Shia, triggering an ending
                print()
                print('You sprint at Shia and slam into him at full speed, sending you both to the ground. You start hand to hand grappling with him. Unfortunately,\nyou have no knowledge of jujitsu and are quickly subdued by Shia, who sends you to eternal sleep with one swift stroke.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            elif choice3A.lower() == 'reason':
                # Player chose to reason with Shia, unlocking a secret ending involving a 4th choice for the player
                print()
                print('With Shia closing in, you quickly point out to him that killing you is meaningless because we are all gonna die someday.\nSomehow, this works and Shia drops his axe in shame. He apologizes and offers to get you out and buy you a burger.')
                choice4A = input('Do you accept his generous offer? (type YES or NO): ')
                if choice4A.lower() == 'yes':
                    # Player chose to get a burger with Shia
                    print()
                    print('You and Shia walk out of the woods together, get in his car, and have a hearty meal of burgers and fries at IN-N-OUT Burger.\nYou stay in touch and eventually become best friends, producing several movies together. You retire rich and famous!')
                    print()
                    time.sleep(2)
                    print('THE END')
                    print()
                elif choice4A.lower() == 'no':
                    # Player chose to not go with Shia
                    print()
                    print('Scared of Shia, you decline and tell him you will find your own way out. Long story short, you never do and end up living with a pack of wolves\nYou die from rabies 5 years later.')
                    print()
                    time.sleep(2)
                    print('THE END')
                    print()
                else:
                    # Player typed something that is not a choice
                    print()
                    print('Oh no! A chicken-duck-woman-thing jumps out from the bushes and pecks you and Shia to death!')
                    print()
                    time.sleep(2)
                    print('THE END')
                    print()
            else:
                # Player typed something that is not a choice
                print()
                print('Oh no! A Starfield Terrormorph appears from the darkness and mauls you and Shia to death!')
                print()
                time.sleep(2)
                print('GAME OVER')
                print()
        elif choice2A.lower() == 'no':
            # Player did not investigate the noise
            print() 
            print('Deciding to not be that dumb person in a horror movie, you quickly and silently wander the other direction. You stumble around in the dark until\nyou come across some railroad tracks snaking their way through the woods.')
            choice3B = input('Do you follow the railroad tracks or wait to see if a train will come? (type FOLLOW TRACKS or WAIT): ')
            if choice3B.lower() == 'follow tracks':
               # Player chose to follow the railroad tracks
               print()
               print('You follow the railroad tracks for miles, eventually finding a railway station. The ticket agent quickly helps you call a cab home\nand before you know it, you are home safe and sound.') 
               print()
               time.sleep(2)
               print('The END')
               print()
            elif choice3B.lower() == 'wait':
                # Player chose to wait at the railroad tracks
                print()
                print('You wait by the tracks for hours and eventually fall asleep. You suddenly awaken in your own bed and realize that the entire ordeal\nwas just a dream, nothing more. You chuckle to yourself, eat a bowl of Cheerios, and head to work.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            else:
                # Player typed something that is not a choice
                print()
                print('Oh no! The spider Sheelob from Lord of The Rings appears and webs you up for dinner!')
                print()
                time.sleep(2)
                print('GAME OVER')
                print()
        else:
            # Player typed something that is not a choice
            print()
            print("Oh no! A pack of wizard toads appears and Avada Kedavra's you into oblivion!")
            print()
            time.sleep(2)
            print('GAME OVER')
            print()
    elif choice1.lower() == 'follow star':
        # Player chose to follow star, the story branches based on that choice
        print()
        print('You follow the northern star in the hopes that it will lead you to civilization or a road. Ahead in the darkness, you see a cabin with a light glowing in the window.\nAs you approach the window, you notice the cabin appears empty but has a landline. You try the door, but its locked.')
        choice2B = input('Do you kick down the door or try the window? (type KICK DOOR or TRY WINDOW): ')
        if choice2B.lower() == 'kick door':
            # Player choose to kick the door down
            print()
            print('You kick the door down and walk into the cabin. It looks like somone was here recently and may return soon. There is food, a landline phone, and a gun.')
            choice3C = input('Do you go for the food, phone, or gun? (type FOOD, PHONE, or GUN): ')
            if choice3C.lower() == 'food':
                # Player chose the food
                print()
                print('You sit down to eat some of the food you found just as the three bears come tromping in. You stare at them, they stare at you.\nThe last thing you hear before everything goes black is growling.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            elif choice3C.lower() == 'phone':
                # Player chose the phone 
                print()
                print('You pick up the phone and call your best friend for help. Turns out you had been on a camping trip with some friends, slept walked, woken up\nin the woods, and then come across the local Forest Service cabin. Your friends quickly locate you and take you back to camp.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            elif choice3C.lower() == 'gun':
                # Player chose the gun
                print()
                print('You pick up the gun just as you hear a creak behind you. Frightened, you spin around, bring the gun up and fire. To your horror, you realize\nthat you have just killed a Forest Service Ranger. His partner walks in behind him and quickly arrests you for murder. You spend the\nrest of your life in prison.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            else:
                # Player typed something that is not a choice
                print()
                print('Oh no! A murderuous chicken comes out of the back of the cabin and pecks you to death!')
                print()
                time.sleep(2)
                print('GAME OVER')
                print()
        elif choice2B.lower() == 'try window':
            # Player chose to try the window
            print()
            print('You try punching the glass to break through the window, but unfortunately the glass is hardened and bulletproof, so you break your hand and scream in pain.\nYou quickly discover that the cabin actually has an occupant when the owner stomps out of a bedroom, angrily opens the door, and asks what you want.')
            choice3D = input('Do you tell him that you are lost and show him your broken hand, or do you run away in fright? (type TALK or RUN): ')
            if choice3D.lower() == 'talk':
                # Player chose to talk to the home owner
                print()
                print('The cabin owner quickly apologizes for his angry response. He brings you inside, provides you with a warm meal, and calls for medical help.\nThe paramedics arrive before too long and take you to the hospital to care for your hand before getting you a cab home. You stay in touch with the cabin owner,\nwho becomes a good friend that you have over for Thanksgiving every year.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            elif choice3D.lower() == 'run':
                # Player chose to run away from the home owner
                print()
                print('You run away from the cabin owner in fright, ending up even more lost than before. Unfortunately, you have wandered close a cliff.\nThe last thing you experience before the world goes black is the horrifying sensation of stepping out into air and nothingness in a deadly fall.')
                print()
                time.sleep(2)
                print('THE END')
                print()
            else:
                # Player typed something that was not a choice
                print()
                print('Oh no! A murderous chimpmunk jumps out of a tree and slays you and the cabin owner!')
                print()
                time.sleep(2)
                print('GAME OVER')
                print()
        else:
            # Player typed something that was not a choice
            print()
            print('Oh no! A furious land shark appears out of the darkness and devours you!')
            print()
            time.sleep(2)
            print('GAME OVER')
            print()
    else:
        # Player typed something that is not a choice
        print()
        print('Oh no! A cocaine-bear appears and mauls you visciously. The horror!')
        print()
        time.sleep(2)
        print('GAME OVER')
        print()
else:
    # Obviously, the player lacks conviction because they dont want to play
    time.sleep(0.5)
    print()
    print('Oh no! A ninja suddenly appears and cuts you in half because you lack conviction. Have a nice day!')
    print()