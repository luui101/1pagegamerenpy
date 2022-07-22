# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character('me', color="#E6E6FA")
image image_1= "bg_skye.jpg"
define me = Character('me')
# The game starts here.

label start:
      "me""We the People"
      "me""The Soliloquy"
label backgound:
     scene image_1

     show fullbody_eyeclose_mouthclose


     "me""Everyday I wake up to a gray world or red thick air. My head is filled with these questions..."
     show halfbody_eyeclose_mouthclose

     menu:
        "to be?":
            $ answer = True

        "or not to be?":
            $ answer = True
     show halfbody_eyeclose_mouthsmile

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
     show halfbody_eyeopen_mouthclose

     "me""I turn my head to look out the window, I see it is a nice day today."
     "me""I take a deep breath and think to myself"
     "me""If winter comes, can spring be far behind"
     show halfbody_eyeopen_mouthsmile
     


     return
