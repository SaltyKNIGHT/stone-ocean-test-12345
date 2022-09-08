# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define hero = Character("[player_name]")
define girl = Character("Girl")

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

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    $ player_name = "Protagonist"

    hero "..."

    hero "Unemployed..."

    hero "Nothing to do..."

    hero "What should I do!"

    hero "Damn it!"

    hero "I guess I will search the web for a while, maybe I can find a job on the web."

    "Surfing the web for quite some time, 
    however the protagonist get distracted from
    his original goal and browse for a new games instead.
    "
    
    hero "Huh... What is this... A game with a lot of boobs."

    "And so the protagonist is being controlled by his lust to download the game."

    hero "I hope there is no virus."

    "When the download is complete,"

    "The protagonist opens the game."

    "'Enter your name', says the game on the screen."

    "The protagonist inputs the name."

    "When the protagonist clicks the enter button, his laptop goes blue screen"

    hero "I knew it! Damn it! I hope it does not break anything important,
    God knows I can't even pay for food right now."

    "As the laptop reboots itself, a single message appears."

    "Welcome to Alda"

    "The protagonist proceeds to click OK."

    "He feels like his body is being pulled into the screen."

    "Everything is black around him."

    "Then, the protagonist opens his eyes,
    as he arrives in a world different from his own world."

    girl "What are you doing sitting on the floor like that?"

    hero "Am I dead?"

    girl "Well, you will be, if you keep laying on the floor like that."

    girl "Come on, everyone is watching."

    "The protogonist looks at everyone that is passing by looking at him."

    # $ player_name = renpy.input("My name is", "", length=20,)
    
    # hero "test"
    

    # This ends the game.

    return
