    
## GEORGE DAN ROUTE ##
## PLACEHOLDER TEXT FOR NOW, GETTING AN IEDEA FOR FLOW AND THE EXPRESSIONS/BACKGROUNDS WE NEED ##

# INTRO SCENE
label george_dan_intro:
    scene bg ring_road
    "The main character(player) bumps into a mysterious person and the player drops her stuff."
    show gd calm
    gd "He then calmly looks at the player and gives the player a small, but charming smile and then proceeds to pick up the player&#x27;s stuff. Seeing a book that he likes, the mysterious person then tells the player that she has really good taste for books."
    # show gd smile
    # gd "-He then smiles and exits. "
    hide gd smile with dissolve
    "Wondering who the guy was, the player thought that he is very cute."

    # show ren greeting
    # "A person approaches the player and this person is her closest friend from highschool who is 1 year above the player."
    # hide ren greeting
    # show ren calm
    # "Ren and the player talks for a bit and then Ren asks the player if they are going to join any clubs."
    # "Ren then forces the player to join VDGC with her because they both love videogames. Ren tells the player that the meeting is tonight."
    # show ren farewell
    # "Player and Ren then part ways."
    # hide ren farewell with dissolve
    return
#END INTRO SCENE
label george_dan_route1scene1:
    scene bg classroom
    show gd calm
    gd "The board introduces the members"
    show gd:
        linear 0.5 xalign 1.0
    with Pause(1)
    show production at truecenter with dissolve
    "production"
    hide production with dissolve
    show artist at truecenter with dissolve
    "artist"
    hide artist with dissolve
    show programmer with dissolve
    "programmer"
    hide programmer with dissolve
    show audio with dissolve
    "audio"
    hide audio with dissolve
    show gd calm:
        linear 0.5 xalign 0.5
    gd "introduces himself"

    return
## END GEORGE DAN ROUTE ##