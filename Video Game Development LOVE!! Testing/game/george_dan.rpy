    
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
    show production with dissolve
    "production"
    hide production with dissolve
    show artist with dissolve
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
    show sparkle_anim:
        xalign 0.5 yalign 0.6
    "-The player then recognizes the president as the person she bumped into earlier. 
    -Realizing that Jeorge Dan was that person, for some odd reason the player could not keep her eyes off of him.
    -The player starts to talk about how she is getting nervous, sweaty hands, and excitement but the player is in denial and denies that the president is the reason for it."
    hide sparkle_anim with dissolve
    "Towards the end of the meeting, the player tells Ren that she wants to try and pitch an idea (the player hopes that by pitching an idea, Jeorge will notice her, she also hopes that deep down Jeorge will choose to be the group leader of her group.)"
    hide gd calm with dissolve
    #show ren with dissolve
    "Ren is also pitching and she wishes the player good luck."
    #hide ren with dissolve
    show gd calm with dissolve
    "After the meeting, the president then headed towards the player. The player started to nervously wonder why the president was heading towards her. She couldn&#x27;t believe it, she assumed that president remembered her from this morning and that he was going to introduce himself to her personally."
    #show ren:
    show artist:
        xalign -0.5 yalign 1.0
        linear 0.5 xalign 0.0 yalign 1.0
    "-Before she said anything, the president and Ren greeted each other. (they know each other). He then asks Ren to come with him as he needed to talk to her.
    -Not only did the player feel embarrassed, she goes into denial and tries to reject her interest in Jeorge, but deep down she felt very sad."

    return
## END GEORGE DAN ROUTE ##