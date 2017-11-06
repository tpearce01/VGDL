# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gd = Character("George Dan")     # Writer
define yu = Character("Yukiko")         # Programmer
define re = Character("Reina")          # Artist
define kd = Character("Kendrick")       # Production
define md = Character("Melody")         # Audio
define ax = Character("Alexander")      # Design

# Minor Characters
define ren = Character ("Ren")          # Childhood friend
define prof = Character("Professor")    # Teacher
define crowd = Character("Crowd")       # Crowd of people
define team = Character("Team")         # Projet team

# Main Character 
define mc = Character("[mcname]")       # Main Character / Protagonist

# TEST VARS
define you_are_weeb_trash = True
define kt = Character("Karen Tendo")


## START ##
# The game starts here. 
label start:
    call get_name
    call gd_intro
    call gd_route1_scene1
    call gd_route1_scene2
    call gd_route1_scene3
    call gd_route1_scene4
    call gd_route1_scene5
    call gd_route1_scene6
    call gd_route1_scene7
    
    # Credits
    call end_scene

    # This ends the game.
    return
## END START ##
    
init:
    # CHARACTER NAME
    define mcname = ""
    define they = "he"
    define their = "his"
    
    # CURRENT ROUTE
    define route = "common"
    
    # AFFECTION
    define max_affection = 0
    define gd_affection = 0
    define yu_affection = 0
    define re_affection = 0
    define kd_affection = 0
    define md_affection = 0
    define ax_affection = 0
    
    # ANIMATIONS
    define anim_speed = .08
    image anim = Animation("1.png", anim_speed, "2.png", anim_speed, "3.png", anim_speed, "4.png", anim_speed, "5.png", anim_speed, "6.png", anim_speed, "7.png", anim_speed, "8.png", anim_speed)
    image sparkle_anim = Animation("sparkle1.gif", anim_speed, "sparkle2.gif", anim_speed, "sparkle3.gif", anim_speed, "sparkle4.gif", anim_speed)
    
init python:
    # SET ROUTE STRING BASED ON AFFECTION
    def set_route():
        global max_affection
        global route
        if gd_affection > max_affection:
            route = "georgedan"
            max_affection = gd_affection
        if yu_affection > max_affection:
            route = "yukiko"
            max_affection = yu_affection
        if re_affection > max_affection:
            route = "reina"
            max_affection = re_affection
        if kd_affection > max_affection:
            route = "kendrick"
            max_affection = kd_affection
        if md_affection > max_affection:
            route = "melody"
            max_affection = md_affection
        if ax_affection > max_affection:
            route = "alexander"
            max_affection = ax_affection
    
        
        