# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define kt = Character("Karen Tendo")
define mc = Character("[mcname]")
define gd = Character("George Dan")

define you_are_weeb_trash = True

## START ##
# The game starts here. 
label start:
    
    # jump george_dan_intro
    jump george_dan_route1scene1
    

    # call end_scene

    # This ends the game.

    return
## END START ##
    
init:
    define anim_speed = .08
    image anim = Animation("1.png", anim_speed, "2.png", anim_speed, "3.png", anim_speed, "4.png", anim_speed, "5.png", anim_speed, "6.png", anim_speed, "7.png", anim_speed, "8.png", anim_speed)
    image sparkle_anim = Animation("sparkle1.gif", anim_speed, "sparkle2.gif", anim_speed, "sparkle3.gif", anim_speed, "sparkle4.gif", anim_speed)