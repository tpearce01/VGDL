## END SCENE ##
## Display The End and credits ##
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
## END END SCENE ##