# Stick and Move
# Text-Based Boxing Game

print("================================")
print("         STICK AND MOVE")
print("================================")
print("Welcome to Stick and Move!")
print("Train your boxer and prepare to fight Drago!")
print()

def game():


    health = 50
    power = 10
    skill = 10
    endurance = 0
    drago_health = 100

    inventory = []

    current_room = "The Locker Room"

    print("Current Room:", current_room)
    print("Health:", health)
    print("Power:", power)
    print("Skill:", skill)
    print("Endurance:", endurance)
    print("Inventory:", inventory)

    #Game Map
    game_map = {
        "The Locker Room": {
            "South": "Boxing Gym"
        },

        "Boxing Gym": {
            "North": "The Locker Room",
            "East": "The Equipment Store",
            "South": "Creed's Gym"
        },

        "The Equipment Store": {
            "West": "Boxing Gym",
            "East": "The Local Ring",
            "South": "Weigh Station"
        },

        "The Local Ring": {
            "West": "The Equipment Store",
            "South": "Massage Parlor"
        },

        "Creed's Gym": {
            "North": "Boxing Gym",
            "East": "Weigh Station"
        },

        "Weigh Station": {
            "North": "The Equipment Store",
            "West": "Creed's Gym",
            "East": "Massage Parlor",
            "South": "Championship Arena"
        },

        "Massage Parlor": {
            "North": "The Local Ring",
            "West": "Weigh Station"
        },

        "Championship Arena": {
            "North": "Weigh Station"
        }
    }

    #Moving around the Map
    while True:
        print()
        print("You are currently in:", current_room)

        direction = input("Enter a direction (North, South, East, West), Stats or Exit: ")
        direction = direction.title()

        if direction == "Exit":
            print("Thanks for playing Stick and Move!")
            break
    #Stats Command
        elif direction == "Stats":
            print()
            print("----- FIGHTER STATS -----")
            print("Health:", health)
            print("Power:", power)
            print("Skill:", skill)
            print("Endurance:", endurance)
            print("Inventory:", inventory)

    #Movement
        elif direction in game_map[current_room]:

            next_room = game_map[current_room][direction]
            if next_room == "Championship Arena":
                if health >= 120 and power >= 50 and skill >= 50 and endurance >= 30:
                    current_room = next_room
                    print("You entered the Championship Arena!")
                    print("Drago IS WAITING FOR YOU!")
                    print()
                    print("================================")
                    print("        CHAMPIONSHIP FIGHT")
                    print("================================")
                    print("Drago: I MUST BREAK YOU!")
                    print()

                    while drago_health > 0 and health > 0:

                        print("Your Health:", health)
                        print("Drago's Health:", drago_health)
                        print()

                        attack = input("Choose your attack (Jab, Hook, Uppercut): ")
                        attack = attack.title()

                        if attack == "Jab":
                            damage = 10 + (skill // 10)
                            drago_health -= damage
                            print("You hit Drago with a Jab!", damage, "damage!")

                        elif attack == "Hook":
                            damage = 15 + (power // 10)
                            drago_health -= damage
                            print("You landed a Hook!", damage, "damage!")

                        elif attack == "Uppercut":
                            damage = 20 + (endurance // 10)
                            drago_health -= damage
                            print("BOOM! Uppercut!")

                        else:
                            print("You missed your chance to attack!")

                        if drago_health > 0:
                            health -= 20
                            print("Drago hits you! -20 HP")
                        if health > 0:
                            print()
                            print("DRAGO IS DOWN!")
                            print("YOU ARE THE CHAMPION!")

                            inventory.append("CHAMPIONSHIP BELT")

                            print("You received the CHAMPIONSHIP BELT!")
                            print("Inventory:", inventory)
                            break

                        else:
                            print()
                            print("Drago knocked you out!")
                            print("GAME OVER!")
                            break
                else:
                    print("You're not ready to fight Drago!")
                    print("You need:")
                    print("200 Health")
                    print("50 Power")
                    print("50 Skill")
                    print("30 Endurance")
            else:
                current_room = next_room
                print("You moved to:", current_room)



    #Items and Stats Boosts

            if current_room == "The Locker Room" and "Boxing Gloves" not in inventory:
                print("You found a pair of Boxing Gloves!")
                inventory.append("Boxing Gloves")
                power += 10
                skill += 10

                print("Power increased by 10!")
                print("Skill increased by 10!")
    #Boxing Gym and Heavy Bag
            elif current_room == "Boxing Gym" and "Heavy Bag" not in inventory:
                print("You trained at the Boxing Gym!")
                print("You found the Heavy Bag!")

                inventory.append("Heavy Bag")

                health += 5
                power += 5
                skill += 5
                endurance += 5

                power += 20

                print("All stats increased by 5!")
                print("The Heavy Bag increased your Power by 20!")
        #The equipment store
            elif current_room == "The Equipment Store" and "Boxing Shorts" not in inventory:
                print("You entered The Equipment Store!")
                print("You got a pair of Boxing Shorts!")

                inventory.append("Boxing Shorts")

                skill += 10
                endurance += 10

                print("Skill increased by 10!")
                print("Endurance increased by 10!")
        #The Local Ring sparring increases stats but lowers Health by 10!
            elif current_room == "The Local Ring":
                print("You entered The Local Ring!")
                print("Time to spar!")

                health -= 10
                power += 10
                skill += 10
                endurance += 10

                print("Power increased by 10!")
                print("Skill increased by 10!")
                print("Endurance increased by 10!")
                print("Sparring cost you 10 Health!")
        #Creeds Gym gives 20 to all stats only once.
            elif current_room == "Creed's Gym" and "Creed Training" not in inventory:
                print("You entered Creed's Gym!")
                print("Time for some serious training!")

                inventory.append("Creed Training")

                health += 20
                power += 20
                skill += 20
                endurance += 20

                print("Creed Training increased all your stats by 20!")
    # The Weigh Station Gives you the Energy Bar and 50 Hp
            elif current_room == "Weigh Station" and "Energy Bar" not in inventory:
                print("You entered the Weigh Station!")
                print("You found an Energy Bar!")

                inventory.append("Energy Bar")

                health += 50

                print("The Energy Bar increased your Health by 50!")
    #The massage parlor gives 50 hp!
            elif current_room == "Massage Parlor" and "Massage" not in inventory:
                print("You entered the Massage Parlor!")
                print("Time to recover!")


                health += 50
                endurance += 10


                print("The Massage restored 50 Health!")
                print("Massage increased endurance by 10!")

                if "Massage" not in inventory:
                    inventory.append("Massage")


    # Python Checks for Minimum required stats



        else:
            print("Hard headed huh? TRY A DIFFERENT DIRECTION!!!")
play_again = "Yes"

while play_again == "Yes":
    game()

    print()
    play_again = input("Would you like to play again? (Yes/No): ")
    play_again = play_again.title()

print()
print("Thanks for playing STICK AND MOVE!")