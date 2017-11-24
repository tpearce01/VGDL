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
define dad = Character("Dad")           # MC's Dad
define nm = Character("Naomi")          # Alex's Friend

# Main Character 
define mc = Character("[mcname]")       # Main Character / Protagonist

# TEST VARS
define you_are_weeb_trash = True
define kt = Character("Karen Tendo")


## START ##
# MAIN GAME LOOP
label start:
    stop music fadeout 1.0      # Stop music from menu in case it has not been stopped
    #queue music "insert_song_name.ogg" loop    # Template for queueing music
    scene bg black              # Default to black scene in case of missing background
    
    # TESTING
    call test_moon
    #call test_time
    #call test_monologue
    #call test_effects
    #call test_transitions
    #call test_image_effects
    # END TESTING
    
    # INTRODUCTION / PRE-PROLOGUE
    call get_name               # Get main character name
    call get_gender             # Get main character gender
    
    # PROLOGUE
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
   
    # GEORGE DAN
    #call gd_scene1              # GEORGE DAN SCENE 1
    #call gd_scene2              # GEORGE DAN SCENE 2
    
    # ALEX
    #call alex_scene1            # ALEX SCENE 1
    #call alex_scene2            # ALEX SCENE 2
    #call alex_scene3            # ALEX SCENE 3
    #call alex_scene4            # ALEX SCENE 4
    
    # MELODY
    #call melody_scene1          # MELODY SCENE 1
    #call melody_scene2          # MELODY SCENE 2
    #call melody_scene3          # MELODY SCENE 3
    #call melody_scene4          # MELODY SCENE 4
    
    # Credits
    call end_scene              # Credits Scene

    # This ends the game.
    return
## END START ##
    
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
                they = "her"
                they_c = "Her"
                their = "hers"
                their_c = "Hers"
    return
# END GET GENDER
## END NON ROUTE SCENES ##
    
init:
    # CHARACTER ATTRIBUTES
    define mcname = "Tyler"     # Default main character name
    define gender = "m"         # Default character gender
    
    # DIALOGUE VARIABLES
    define they = "he"          # UNUSED - Variable for setting gender he/she
    define they_c = "He"        # He/She Capital version
    define their = "his"        # UNUSED - Variable for setting gender his/hers
    define their_c = "His"        # His/Hers Capital version
    
    # SYSTEM TIME / WERECAT VARIABLES
    define year = 0
    define month = 0
    define day = 0
    define is_werecat = false
    
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
    
    # ANIMATIONS
    define anim_speed = .08
    image anim = Animation("1.png", anim_speed, "2.png", anim_speed, "3.png", anim_speed, "4.png", anim_speed, "5.png", anim_speed, "6.png", anim_speed, "7.png", anim_speed, "8.png", anim_speed)
    image sparkle_anim = Animation("sparkle1.gif", anim_speed, "sparkle2.gif", anim_speed, "sparkle3.gif", anim_speed, "sparkle4.gif", anim_speed)
    
init python:
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
        ## NOTES ON WERECAT GEORGE DAN ##
        # TO DO:
        #       > Add werecat art
        #       > Find + Replace all "show gd calm" --> 
        #           if is_werecat:
        #               show gd werecat calm
        #           else:
        #               show gd calm
        #       > Repeat for all emotions
    
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
    
        
        