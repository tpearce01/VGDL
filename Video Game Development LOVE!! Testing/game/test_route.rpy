## TEST ROUTE ##
## This route is for testing only ##

# TEST EFFECTS
label test_effects:
    scene bg park_1
    show yu calm
    with Pause(1)
    scene bg park_2 with irisin
    return
# END TEST EFFECTS

label test_moon:
    python:
        string_data = "Not a full moon"
        get_time()
        is_fullmoon = moon_phase(month, day, year)
        if is_fullmoon:
            string_data = "Full moon"
    "[string_data]"

label test_time:
    $ get_time()
    "[day], [month], [year]"
    return

label test_monologue:
    scene bg black
    "Inner monologue text"
    "(Inner monologue text"
    mc "(Inner monologue text)"
    return

label test_route:
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
    
label test_image_effects:
    scene bg black with fade
    # Invert
    image yu_calm = im.MatrixColor("yu calm.png", im.matrix.invert())
    show yu_calm
    "Inverted"
    hide yu_calm
    image yu_calm1 = im.MatrixColor("yu calm.png", im.matrix.brightness(0.5))
    show yu_calm1
    "Brightness 0.5"
    hide yu_calm1
    image yu_calm2 = im.MatrixColor("yu calm.png", im.matrix.brightness(-0.5))
    show yu_calm2
    "Brightness -0.5"
    hide yu_calm2
    image yu_calm3 = im.MatrixColor("yu calm.png", im.matrix.colorize("#f00", "#00f"))
    show yu_calm3
    "Swap red and blue"
    hide yu_calm3
    image yu_calm4 = im.MatrixColor("yu calm.png", im.matrix.contrast(1))
    show yu_calm4
    "Contrast 1"
    hide yu_calm4
    image yu_calm5 = im.MatrixColor("yu calm.png", im.matrix.contrast(0.5))
    show yu_calm5
    "Contrast 0.5"
    hide yu_calm5
    image yu_calm6 = im.MatrixColor("yu calm.png", im.matrix.desaturate())
    show yu_calm6
    "Desaturate"
    return
    
label test_transitions:
    scene bg park_2
    image gd_calm = im.MatrixColor("gd calm.png", im.matrix.invert())
    show gd_calm
    "fade"
    scene bg park_1 with fade
    "dissove"
    scene bg park_2 with dissolve
    "pixellate"
    scene bg park_1 with pixellate
    "move"
    scene bg park_2 with move
    "moveinright"
    scene bg park_1 with moveinright
    "moveinleft"
    scene bg park_2 with moveinleft
    "ease"
    scene bg park_1 with ease
    show gd calm with ease
    "zoomin"
    scene bg park_2 with zoomin
    show gd calm with zoomin
    "zoomout"
    scene bg park_1 with zoomout
    show gd calm with zoomout
    "zoominout"
    scene bg park_2 with zoominout
    show gd calm with zoominout
    "vpunch"
    scene bg park_1 with vpunch
    "hpunch"
    scene bg park_2 with hpunch
    "blinds"
    scene bg park_1 with blinds
    "squares"
    scene bg park_2 with squares
    "wipeleft"
    scene bg park_1 with wipeleft
    "slideleft"
    scene bg park_2 with slideleft
    "slideawayleft"
    scene bg park_1 with slideawayleft
    "pushright"
    scene bg park_2 with pushright
    "irisin"
    scene bg park_1 with irisin
    
## END TEST ROUTE ## 
