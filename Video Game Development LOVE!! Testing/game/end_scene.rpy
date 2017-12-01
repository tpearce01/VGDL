## END SCENE ##
## Display The End and credits ##
label end_scene:
    scene black
    $ renpy.music.set_volume(0.25, 0, channel="music")
    queue music "test-music-a.ogg" loop
    show end_text:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide end_text 
    with dissolve
    show credits_formatted at Move((0.5,4.3), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    stop music fadeout 1.0
    with Pause(1)
    return
## END END SCENE ##

image end_text = Text("{size=90}The End\n{size=40}Thanks for playing!", text_align=0.5)
image credits_title = Text("{size=60}Credits", text_align=0.5)
image credits_formatted = Text(credits, text_align=0.5)

init:
    define credits_speed = 35   # Number of seconds it takes to scroll through the credits - Higher value results in slower scroll
    python:
        credits = "{size=80}Credits\n"
        credits_data = ('Art', 'Carolee Nguyen'), ('Art', 'Ha Hoang'), ('Art', 'Kierstin Roque'), ('Art', 'Mark Pareja'), ('Audio', 'Derek Giap'), ('Programming', 'Emily Chan'), ('Programming', 'Tyler Pearce'), ('Writing', 'Adrian '), ('Writing', 'Alonso Rojas'), ('Writing', 'Edric Truong'), ('Writing', 'Fishies'), ('Writing', 'Lexi Olah'), ('Writing', 'Phuoc Trinh'), ('Writing', 'Riley'), ('Special Thanks', 'Naz Hartoonian- Officer Buddy'), ('Special Thanks', 'VGDC - For making this possible')
        c_temp = ''
        for c in credits_data:
            if not c_temp==c[0]:
                credits += "\n\n{size=40}" + c[0] + "\n"  # Header, Font Size = 40
            credits += "{size=60}" + c[1] + "\n"        # Content, Font Size = 60
            c_temp = c[0]
            