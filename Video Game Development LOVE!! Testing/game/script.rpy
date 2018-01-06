# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gd = Character("Jeorge Dan")     # Writer
define yu = Character("Yukiko")         # Programmer
define re = Character("Reina")          # Artist
define kd = Character("Kendrick")       # Production
define md = Character("Melody")         # Audio
define ax = Character("Alexander")      # Design

# Minor Characters
define unknown = Character("???")       # Unknown Character
define ren = Character ("Ren")          # Childhood friend
define prof = Character("Professor")    # Teacher
define crowd = Character("Crowd")       # Crowd of people
define team = Character("Team")         # Projet team
define dad = Character("Dad")           # MC's Dad
define nm = Character("Naomi")          # Alex's Friend
define su = Character("Supervisor")

# Main Character
define mc = Character("[mcname]")       # Main Character / Protagonist

# TEST VARS
define you_are_weeb_trash = True
define kt = Character("Karen Tendo")

# CHARACTER ATTRIBUTES
define mcname = "Tyler"     # Default main character name
define gender = "m"         # Default character gender

# DIALOGUE VARIABLES
define gender_d = "male"
define they = "he"          # UNUSED - Variable for setting gender he/she
define they_c = "He"        # He/She Capital version
define their = "his"        # UNUSED - Variable for setting gender his/hers
define their_c = "His"        # His/Hers Capital version
define them = "him"

# CURRENT ROUTE
define route = "common"     # UNUSED - Define current route title

# AFFECTION - UNUSED
define max_affection = 0    # Highest current affection, used for affection function
define gd_affection = 0     # George Dan affection
define yu_affection = 0     # Yukiko affection
define re_affection = 0     # Reina affection
define kd_affection = 0     # Kendrick affection
define md_affection = 0     # Melody affection
define ax_affection = 0     # Alexander affection

## START ##
# MAIN GAME LOOP
label start:
    stop music fadeout 1.0      # Stop music from menu in case it has not been stopped
    #queue music "insert_song_name.ogg" loop    # Template for queueing music
    scene bg black              # Default to black scene in case of missing background

    # TESTING
    #call test_md_2
    #call test_werecat
    #call kd_route
    #call end_scene
    #call test_moon
    #call test_time
    #call test_monologue
    #call test_effects
    #call test_transitions
    #call test_image_effects
    # END TESTING

    # INTRODUCTION / PRE-PROLOGUE
    call get_name               # Get main character name
    call get_gender             # Get main character gender

    # CORE ROUTE
    call prologue

    # Credits
    call end_scene              # Credits Scene

    # This ends the game.
    return
## END START ##

## ROUTE CONTROL ##
# PROLOGUE
label prologue:
    call prologue_scene1        # PROLOGUE SCENE 1
    call prologue_scene2        # PROLOGUE SCENE 2
    call prologue_scene3        # PROLOGUE SCENE 3
    call prologue_scene4        # PROLOGUE SCENE 4
    call prologue_scene5        # PROLOGUE SCENE 5
    call prologue_scene6        # PROLOGUE SCENE 6
    call prologue_scene7        # PROLOGUE SCENE 7
    call prologue_scene8        # PROLOGUE SCENE 8
    call prologue_scene9        # PROLOGUE SCENE 9
    call prologue_scene10       # PROLOGUE SCENE 10
    return
# END PROLOGUE

# GEORGE DAN
label gd_route:
    call gd_scene1              # GEORGE DAN SCENE 1
    call gd_scene2              # GEORGE DAN SCENE 2
    call gd_scene3
    call gd_scene4
    call gd_scene5
    call gd_scene6
    return
# END GEORGE DAN

# ALEX
label alex_route:
    call alex_scene1            # ALEX SCENE 1
    return
# END ALEX

# MELODY
label melody_route:
    call melody_scene1          # MELODY SCENE 1
    return
#END MELODY

# YUKIKO
label yu_route:
    call yu_scene1
    return
# END YUKIKO

# REINA
label re_route:
    #"Placeholder Reina Route"
    call re_scene1
    call re_scene2
    return
# END REINA

# KENDRICK
label kd_route:
    #"Placeholder Kendrick route"
    call kd_scene1
    call kd_scene2
    return
# END KENDRIK
## END ROUTE CONTROL ##

## NON-ROUTE SCENES ##

# GET MCNAME
label get_name:
    scene bg black
    python:
        mcname = renpy.input("What is your name?")
        mcname = mcname.strip();
        if not mcname:
            mcname = "Default_Name"
    return
# END GET MCNAME

# GET GENDER
label get_gender:
    menu gender:
        "What is your gender?"

        "Male":
            # Gender defaults to male - no change needed. Adding statement to satisfy renpy menu syntax
            $ gender = "m"
        "Female":
            python:
                gender = "f"
                gender_d = "female"
                they = "her"
                they_c = "Her"
                their = "hers"
                their_c = "Hers"
                them = "her"
        "Other":
            python:
                gender = "?"
                gender_d = "person"
                they = "they"
                they_c = "They"
                their = "their"
                their_c = "Their"
                them = "them"

    return
# END GET GENDER
## END NON ROUTE SCENES ##


## INIT ##
# VARIABLES DEFINED HERE WILL NOT BE SAVED BETWEEN RUNTIME
init:
    # SYSTEM TIME / WERECAT VARIABLES
    define year = 0
    define month = 0
    define day = 0
    define is_werecat = False
    image gd calm = "gd calm.png"

    # ANIMATIONS
    define anim_speed = .08
    image anim = Animation("1.png", anim_speed, "2.png", anim_speed, "3.png", anim_speed, "4.png", anim_speed, "5.png", anim_speed, "6.png", anim_speed, "7.png", anim_speed, "8.png", anim_speed)
    image sparkle_anim = Animation("sparkle1.gif", anim_speed, "sparkle2.gif", anim_speed, "sparkle3.gif", anim_speed, "sparkle4.gif", anim_speed)

init python:
    config.font_replacement_map["DejaVuSans.ttf", False, True] = ("Comfortaa-Regular.ttf", False, False)
    # MODULE IMPORTS
    import time

    # FUNCTION get_time - GET CURRENT SYSTEM TIME
    def get_time():
        global year
        global month
        global day
        year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

    # FUNCTION is_fullmoon - DETERMINE IF GEORGE DAN IS A CAT
    # Original code by bumsfield (https://www.daniweb.com/programming/software-development/code/216727/moon-phase-calculator#post968407)
    # Modified by Tyler Pearce
    def moon_phase(month, day, year):
        global is_werecat
        ages = [18, 0, 11, 22, 3, 14, 25, 6, 17, 28, 9, 20, 1, 12, 23, 4, 15, 26, 7]
        offsets = [-1, 1, 0, 1, 2, 3, 4, 5, 7, 7, 9, 9]

        if day == 31:
            day = 1
        days_into_phase = ((ages[(year + 1) % 19] + ((day + offsets[month-1]) % 30) + (year < 1900)) % 30)
        index = int((days_into_phase + 2) * 16/59.0)

        if index == 4:
            is_werecat = True
            return True
        is_werecat = False
        return False


    # FUNCTION set_route - SET ROUTE STRING BASED ON AFFECTION
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

    # AUDIO
    renpy.music.set_volume(0.25, 0, channel="music")

    # EFFECTS
    flash = Fade(0.25, 0, 0.75, color="#fff")

    # INIT - SETTING VARIABLES EVERY TIME THE GAME IS RUN
    #image gd calm = ("gd calm.png")
    #get_time()
    #moon_phase(month, day, year)
    #if is_werecat:
    #    image gd_calm = ("werecat.png")
init:
    $ get_time()
    $ moon_phase(month, day, year)
    if is_werecat:
        image gd calm = "werecat.png"
        image gd flustered = "gd flustered_ears.png"
        image gd sad = "gd sad_ears.png"
        image gd serious = "gd serious_ears.png"
        image gd smile = "gd smile_ears.png"
