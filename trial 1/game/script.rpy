# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character('me', color="#E6E6FA")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    "We the People"
    "The Soliloquy"

    label choices:
        "Everyday I wake up to a gray world or red thick air. My head is filled with these questions..."
    menu:
        "to be?":
            $ answer = True

        "or not to be?":
            $ answer = True
    menu:
         "who to know?":
             $ answer = True

         "To Know who?":
             $ answer = True
    menu:
        "Why, you ask?":
            $ answer = True

        "Just ask, why not?":
            $ answer = True
    menu:
        "Who to say?":
            $ answer = True

        "Or perhaps, say to who?":
            $ answer = True
    menu:
        "Can I?":
            $ answer = True

        "Can you?":
            $ answer = True
    menu:
        "How could I?":
            $ answer = True

        "How I could?":
            $ answer = True
    menu:
        "Why do you bother?":
            $ answer = True

        "Why bother you?":
            $ answer = True
    menu:
        "Mind you?":
            $ answer = True

        "Do you mind?":
            $ answer = True
    menu:
        "Love is blind":
            $ answer = True

        "Blinding love":
            $ answer = True
    menu:
        "Who could blame me?":
            $ answer = True

        "Who could I blame?":
            $ answer = True
    menu:
        "I must argue":
            $ answer = True

        "Must I argue?":
            $ answer = True
    menu:
        "To love":
            $ answer = True

        "To be love":
            $ answer = True

        "Or none":
            $ answer = True
    menu:
        "There's no hope":
            $ answer = True

        "Is there?":
            $ answer = True
    "I turn my head to look out the window, I see it is a nice day today."
    "I take a deep breath and think to myself"
    "If winter comes, can spring be far behind"



    return
