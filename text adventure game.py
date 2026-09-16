"""
Chapter 3 Mini-Project: Text Adventure Game
Topic: Conditionals (if / elif / else)

A multi-path decision game where choices lead to winning
or secret endings.
"""

print("=== THE MYSTERIOUS FOREST ===")
print("You wake up in a dark forest with two paths ahead.\n")

path = input("Do you go LEFT or RIGHT? ").strip().lower()

if path == "left":
    print("\nYou find a quiet river with a small boat tied to a tree.")
    boat = input("Do you TAKE the boat or WALK along the river? ").strip().lower()

    if boat == "take":
        print("\nThe boat drifts you safely downstream to a sunny village.")
        print("🏆 YOU WIN! You've reached safety.")
    elif boat == "walk":
        print("\nYou walk for hours and stumble into a hidden cave behind a waterfall.")
        print("✨ SECRET ENDING: You discover a chest of ancient treasure!")
    else:
        print("\nConfused, you wander in circles until nightfall.")
        print("💀 GAME OVER: The forest claims another lost soul.")

elif path == "right":
    print("\nYou come across an old wooden cabin with smoke rising from it.")
    cabin = input("Do you KNOCK on the door or SNEAK around back? ").strip().lower()

    if cabin == "knock":
        print("\nA friendly hermit answers and gives you a map out of the forest.")
        print("🏆 YOU WIN! You find your way home safely.")
    elif cabin == "sneak":
        print("\nYou peek through a window and see a wizard casting spells.")
        secret_word = input("He notices you! Quick, shout a magic word: ").strip().lower()

        if secret_word == "abracadabra":
            print("\nThe wizard laughs and teleports you home as a reward.")
            print("✨ SECRET ENDING: You befriend a wizard!")
        else:
            print("\nThe wizard turns you into a frog. Ribbit.")
            print("💀 GAME OVER: You're now an amphibian.")
    else:
        print("\nYou hesitate too long and a bear wanders over.")
        print("💀 GAME OVER: The bear was not friendly.")

else:
    print("\nYou freeze, unable to decide, as darkness falls around you.")
    print("💀 GAME OVER: Indecision is dangerous in the forest.")

print("\nThanks for playing!")

