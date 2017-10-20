# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define kt = Character("Karen Tendo")
define mc = Character("[mcname]")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg test with Dissolve(1)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show karen tendo test

    # These display lines of dialogue.

    "Welcome to Video Game Development LOVE!!"
    
    python:
        mcname = renpy.input("What is your name?")
        mcname = mcname.strip();
        if not mcname:
            mcname = "Default_Name"
    
    show karen tendo test with Fade(0.1, 0.0, 0.5, color="#fff")
    
    kt "Nice to meet you, [mcname]!" 

    kt "You're weaboo trash."

    kt "That is all!"

    call end_scene

    # This ends the game.

    return
    
label end_scene:
    scene black
    show end_text:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    return
    
init:
    image end_text = Text("{size=90}The End\n{size=40}Thanks for playing!", text_align=0.5)
