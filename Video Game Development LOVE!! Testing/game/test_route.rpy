## TEST ROUTE ##
## This route is for testing only ##
label test_route:
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
    
    return
    
label test_route_func:
    "Route: [route]"
    "Value: [max_affection]"
    python:
        gd_affection = 69
        set_route()
    "Route: [route]"
    "Value: [max_affection]"
    return
    
## END TEST ROUTE ## 

init:
    define mcname = ""