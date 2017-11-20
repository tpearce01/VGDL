## END SCENE ##
## Display The End and credits ##
label end_scene:
    scene black
    show end_text:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide end_text 
    with dissolve
    with Pause(1)
    show credits_formatted at Move((0.5,4.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    stop music fadeout 1.0
    with Pause(1)
    return
## END END SCENE ##

image end_text = Text("{size=90}The End\n{size=40}Thanks for playing!", text_align=0.5)
image credits_formatted = Text(credits, text_align=0.5)

init:
    define credits_speed = 15
    python:
        credits = "{size=80}Credits\n\n"
        credits_data = ('Art (Part Time)', 'Alonso'), ('Art', 'Carolee'), ('Art', 'Ha'), ('Art', 'Kierstin'), ('Art (Part Time)', 'Mark'), ('Audio', 'Derek'), ('Programming', 'Em'), ('Programming', 'Tyler'), ('Writing', 'Adrian'), ('Writing', 'Edric'), ('Writing', 'Phuoc'), ('Special Thanks', 'Naz - Officer Buddy'), ('Special Thanks', 'VGDC - For making this possible')
        c_temp = ''
        for c in credits_data:
            if not c_temp==c[0]:
                credits += "\n{size=40}" + c[0] + "\n"
            credits += "{size=60}" + c[1] + "\n"
            c_temp = c[0]
            