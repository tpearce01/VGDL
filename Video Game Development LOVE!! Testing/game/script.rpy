# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define kt = Character("Karen Tendo")
define mc = Character("[mcname]")

define you_are_weeb_trash = True

# The game starts here. 
    
label start:
    stop music fadeout 1.0
    python:
        renpy.music.set_volume(0.25, 0, channel="music")
    queue music "test-music-a.ogg" loop
    #python:
    #    renpy.music.set_volume(0.25, 0, channel="music")
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

    menu weeb_trash:
        "Am I weeb trash?"
        
        "Thank you for noticing":
            "You truly are weeb trash."
            
        "No, I'm not!" if you_are_weeb_trash:
            $ you_are_weeb_trash = False
            "Yes, you are."
            jump weeb_trash
            
        "Yes, I am" if not you_are_weeb_trash:
            "You truly are weeb trash."

    hide karen tendo test 
    with dissolve
    with Pause(1)
    show anim
    with Pause(3)

    call end_scene

    # This ends the game.

    return
    
label end_scene:
    scene black
    show end_text:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    stop music fadeout 1.0
    with Pause(1)
    return
    
init:
    define anim_speed = .08
    
    image end_text = Text("{size=90}The End\n{size=40}Thanks for playing!", text_align=0.5)
    image anim = Animation("1.png", anim_speed, "2.png", anim_speed, "3.png", anim_speed, "4.png", anim_speed, "5.png", anim_speed, "6.png", anim_speed, "7.png", anim_speed, "8.png", anim_speed)