
import random


def play():
    templates = ["1", "2", "3"]
    valid_choices = ["1", "2", "3", "4"]

    print("Welcome to the Mad Libs Story Game!")
    print("Choose a template:")
    print("1 - Hospital")
    print("2 - Camping")
    print("3 - Enchanted Castle")
    print("4 - Random template")

    choice = input("Enter 1, 2, 3, or 4: ")

    while choice not in valid_choices:
        print("Invalid choice. Please try again.")
        choice = input("Enter 1, 2, 3, or 4: ")

    if choice == "4":
        choice = random.choice(templates)
        print(f"Randomly selected template: {choice}")

    if choice == "1":
        print("\nLet's create your hospital story!")

        number = input("Type a number: ")
        time = input("Type a measure of time: ")
        transportation = input("Type a mode of transportation: ")
        adjective = input("Type an adjective: ")
        adjective2 = input("Type another adjective: ")
        noun = input("Type a noun: ")
        color = input("Type a color: ")
        body = input("Type a part of the body: ")
        verb = input("Type a verb: ")
        number2 = input("Type another number: ")
        noun2 = input("Type another noun: ")
        noun3 = input("Type another noun: ")
        body2 = input("Type another part of the body: ")
        verb2 = input("Type another verb: ")
        noun4 = input("Type another noun: ")
        adjective3 = input("Type another adjective: ")
        silly = input("Type a silly word: ")

        story = (
            f"It was about {number} {time} ago when I arrived at "
            f"the hospital in a {transportation}. "
            f"The hospital is a/an {adjective} place, there are "
            f"a lot of {adjective2} {noun} here. "
            f"There are nurses here who have {color} {body}. "
            f"If someone wants to come into my room, I told them "
            f"that they have to {verb} first. "
            f"I've decorated my room with {number2} {noun2}. "
            f"Today I talked to a doctor and they were wearing a "
            f"{noun3} on their {body2}. "
            f"I heard that all doctors {verb2} {noun4} every day "
            f"for breakfast. The most {adjective3} thing about "
            f"being in the hospital is the {silly} {noun}!"
        )

        print("\nYour Story:")
        print(story)

    elif choice == "2":
        print("\nLet's create your camping story!")

        name = input("Type a person's name: ")
        noun = input("Type a noun: ")
        feeling = input("Type a feeling adjective: ")
        verb = input("Type a verb: ")
        feeling2 = input("Type another feeling adjective: ")
        animal = input("Type an animal: ")
        verb2 = input("Type another verb: ")
        color = input("Type a color: ")
        ing_verb = input("Type a verb ending in -ing: ")
        adverb = input("Type an adverb ending in -ly: ")
        number = input("Type a number: ")
        time = input("Type a measure of time: ")
        color2 = input("Type another color: ")
        silly = input("Type a silly word: ")
        noun2 = input("Type another noun: ")

        story = (
            f"This weekend I am going camping with {name}. "
            f"I packed my lantern, sleeping bag, and {noun}. "
            f"I am so {feeling} to {verb} in a tent. "
            f"I am {feeling2} we might see a(n) {animal}; "
            f"I hear they're kind of dangerous. "
            f"While we're camping, we are going to hike, fish, "
            f"and {verb2}. I have heard that the {color} lake "
            f"is great for {ing_verb}. "
            f"Then we will {adverb} hike through the forest for "
            f"{number} {time}. If I see a {color2} {animal} while "
            f"hiking, I am going to bring it home as a pet! "
            f"At night we will tell {number} {silly} stories "
            f"and roast {noun2} around the campfire!"
        )

        print("\nYour Story:")
        print(story)

    elif choice == "3":
        print("\nLet's create your enchanted castle story!")

        name = input("Type a person's name: ")
        adjective = input("Type an adjective: ")
        color = input("Type a color: ")
        animal = input("Type an animal: ")
        place = input("Type a place: ")
        adjective2 = input("Type another adjective: ")
        creature = input("Type a magical creature (plural): ")
        adjective3 = input("Type another adjective: ")
        creature2 = input("Type another magical creature (plural): ")
        room = input("Type a room in a house: ")
        noun = input("Type a noun: ")
        noun2 = input("Type another noun: ")
        noun3 = input("Type a plural noun: ")
        adjective4 = input("Type another adjective: ")
        noun4 = input("Type another plural noun: ")
        number = input("Type a number: ")
        time = input("Type a measure of time: ")
        verb = input("Type a verb ending in -ing: ")
        adjective5 = input("Type another adjective: ")
        noun5 = input("Type another noun: ")

        story = (
            f"Dear {name}, I am writing to you from a {adjective} "
            f"castle in an enchanted forest. I found myself here "
            f"one day after going for a ride on a {color} {animal} "
            f"in {place}. There are {adjective2} {creature} and "
            f"{adjective3} {creature2} here! "
            f"In the {room}, there is a pool full of {noun}. "
            f"I fall asleep each night on a {noun2} of {noun3} "
            f"and dream of {adjective4} {noun4}. "
            f"It feels as though I have lived here for {number} "
            f"{time}. I hope one day you can visit, although the "
            f"only way to get here now is {verb} on a "
            f"{adjective5} {noun5}!"
        )

        print("\nYour Story:")
        print(story)


play()
