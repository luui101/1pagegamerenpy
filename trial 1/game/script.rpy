# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character('me', color="#E6E6FA")
image image_1= "bg_skye.jpg"
define me = Character('me')
# The game starts here.

label start:

     "It's the morning, again."

     scene image_1

     "Everyday, I wake up to a gray world of red thick air."

     show fullbody_eyeclose_mouthclose

     "With pain and sorrow."
     "I'm not sure if I can keep going."

     hide fullbody_eyeclose_mouthclose

     "As always,"
     "my head is filled with these questions..."

     show halfbody_eyeclose_mouthclose

     menu:
        "To be?":
            $ answer = True

        "Or not to be?":
            $ answer = True

     menu:
         "Who am I?":
             $ answer = True

         "Who am I NOT?":
             $ answer = True

     hide halfbody_eyeclose_mouthclose

     show halfbody_eyeclose_mouthsmile

     "(chuckle)"

     hide halfbody_eyeclose_mouthsmile

     show halfbody_eyeclose_mouthopen

     menu:
         "Who knows?":
             $ answer = True

         "Knowing who?":
             $ answer = True

     hide halfbody_eyeclose_mouthopen

     show halfbody_eyeclose_mouthclose

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

        "How could you?":
            $ answer = True

     hide halfbody_eyeclose_mouthclose

     show halfbody_eyeclose_mouthopen

     menu:
        "Why do you bother?":
            $ answer = True

        "Why bother you?":
            $ answer = True
     menu:
        "Mind you.":
            $ answer = True

        "But, do you mind?":
            $ answer = True

     hide halfbody_eyeclose_mouthopen

     show halfbody_eyeclose_mouthclose

     menu:
        "That Love is blind.":
            $ answer = True

        "And I blindly love.":
            $ answer = True
     menu:
        "Who could blame me?":
            $ answer = True

        "Who could I blame?":
            $ answer = True

     "But myself..."

     hide halfbody_eyeclose_mouthclose

     show halfbody_eyeclose_mouthopen

     menu:
        "I must argue!":
            $ answer = True

        "Must I argue?":
            $ answer = True

     hide halfbody_eyeclose_mouthclose

     show halfbody_eyeclose_mouthopen

     menu:
        "To love.":
            $ answer = True

        "To be loved":
            $ answer = True

        "Or none.":
            $ answer = True
     menu:
        "There's no hope!":
            $ answer = True

        "Is there?":
            $ answer = True

     hide halfbody_eyeclose_mouthclose
     show halfbody_eyeopen_mouthclose

     "I turn my head to look out the window, I see it is a nice day today."

     hide halfbody_eyeopen_mouthclose
     show halfbody_eyeopen_mouthopen

     "I take a deep breath and think to myself"

     hide halfbody_eyeclose_mouthopen
     show halfbody_eyeopen_mouthsmile


     "If winter comes, can spring be far behind?"

     hide halfbody_eyeclose_mouthopen
     show halfbody_eyeopen_mouthsmile

     "I'm okay."


     return
