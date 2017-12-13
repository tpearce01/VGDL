## MELODY ##

# MELODY SCENE 1
label melody_scene1:
    #SSLH - After Initial Meeting
    scene bg sslh with dissolve
    mc "(I can't believe I left my phone in the lecture hall...)"
    mc "(Crap, crap, crap...)"
    mc "(Please let it still be there...)"
    "When I entered the lecture hall, I saw a girl drawing on the far wall."
    show md calm with dissolve
    "It kind of looked like the Audio Officer from the VGDC meeting."
    mc "\"Excuse me?\""
    md "What do you want?"
    mc "\"Just wondering if you’ve seen a phone around here.\""
    md "Not really."
    hide md calm with dissolve
    "As Melody was leaving, Alex made his way inside."
    show ax calm with dissolve
    ax "Hey, what’s taking you so long? You ?"
    mc "\"Yeah… I just got caught up with talking to Melody.\""
    ax "The Audio Officer Melody?"
    mc "\"The one and only!\""
    ax "So which one of you did the lovely art on the wall?"
    mc "\"That? Oh! Uh, not me!\""
    ax "I can believe that. You aren’t exactly known for your artistic talent."
    mc "\"Hey!\""
    ax "Relax! I’m joking!"
    return
# END MELODY SCENE 1 

# MELODY SCENE 2
label melody_scene2:
    #LANGSON LIBRARY - Forming Pitch
    scene bg library_1 with dissolve
    show md calm with dissolve
    md "Hey, bromiga."
    mc "\"Bromiga?\""
    md "It's a combination of 'bro' and 'amiga'. Hence, 'bromiga'."
    mc "\"Oh, well, hey back, bromiga!\""
    md "No... no, it doesn't sound right coming from you."
    mc "\"Um... okay. Did you need something?\""
    md "Just thought I'd come by to see what you're up to."
    mc "\"I'm working on my pitch.\""
    md "So you're gonna pitch a game next week?"
    mc "\"Yeah. I'm just not sure what kind I'm going to do.\""
    md "Alex isn't going to be part of your team, is he? I've heard he's like, your best friend or something."
    mc "\"I'm not sure yet.\""
    md "I'll join your team if you can promise me that he won't join it."
    mc "\"Uh... do you mind me asking why I couldn't have both of you guys?\""
    md "We don't work well together."
    mc "(I felt bad about ditching Alex, but at the same time, to have someone as talented as Melody...)"
    mc "\"Okay, it's a deal.\""
    md "You're not gonna regret this, [mcname]. Here's my number."
    ax "Hey! What's up?"
    mc "\"Nothin' much.\""
    ax "So, you ready to think of a pitch?"
    mc "\"Um, the thing is... I'm gonna pitch with Melody.\""
    ax "Oh. I see. Is that why she was here?"
    mc "\"Yeah. What happened between you two?\""
    ax "Why don't you ask her yourself?"
    mc "(Alex left without saying another word.)"
    return
# END MELODY SCENE2
    
# MELODY SCENE 3
label melody_scene3:
    #SSLH - Pitching Game
    scene bg black with dissolve
    #???? - Video Game Related
    "Melody sent me a text a few minutes later."
    mc "(We should get together to talk about the game.)"
    mc "(Meet me at the Student Center Starbucks tonight.)"
    return
# END MELODY SCENE3

# MELODY SCENE 4
label melody_scene4:
    #STUDENT CENTER - Path Divergence
    scene bg studentcenter with dissolve
    show md calm with dissolve
    md "Oh, [mcname], you're finally here!"
    mc "\"Hey. What's up?\""
    md "I need you to help me with something."
    mc "\"I'll do what I can!\""
    md "That's hella sweet. So, Alex has been trying to get me kicked out of the club forever now."
    md "I need your help in pranking him. To teach him a lesson. What do you say, bromiga?"
    mc "\"I don't know. Why is he trying to get you kicked out?\""
    show md upset with dissolve
    md "He thinks I'm a \"no-good degenerate\", that I'm bad for the club's image."
    mc "\"He's my friend though...\""
    show md calm with dissolve
    md "That's exactly why I need you to help me out. You can help me get to him."
    menu help_him_out:
        "That's exactly why I need you to help me out. You can help me get to him."
        #CHOICE A - 
        "Okay, I'll help you.":
            mc "\"You're right. Let's teach him a lesson!\""
            md "I knew you were gonna come through for me!"
            mc "\"Hey, we're a team now!\""
            mc "(And I'd do anything for someone so cute...)"
            md "I gotta say... I really wasn't expecting you to say yes."
            mc "\"He's kind of been a jerk lately.\""
            call melody_scene4a_1
        #CHOICE B - 
        "No, I don't think so...":
            mc "\"I can't do that. Not to my best friend.\""
            md "That's weak, bromiga."
            mc "\"It's not that I don't want to help you. I just don't want to do something nasty to my best friend.\""
            md "Oh, no, I get it."
            mc "\"We're still cool with the game thing?\""
            md "I guess so. There's nothing I can say to make you change your mind?"
            mc "\"Not really.\""
            md "Fine. I'll text you tomorrow."
            call melody_scene4b_1
    return
    
#CHOICE A SCENE 1
label melody_scene4a_1:
    scene bg black with dissolve
    "I almost texted Alex to let him know the situation."
    "But all his secrets, his attitude... I didn't like it."
    "Maybe he deserved this."
    show md calm with dissolve
    md "So, I've finally got the details planned out."
    mc "\"I'm ready for anything.\""

# CHOICE A SCENE 2


# CHOICE A SCENE 3


# CHOICE A SCENE END
label melody_scene4a_end:
    scene bg black with dissolve
    show md calm with dissolve
    md "Look, I'm... I didn't mean to destroy your friendship with Alex."
    mc "\"I don't think what you did was right. But what he did was even worse.\""
    md "So, forgive me?"
    mc "\"I can't stay mad at someone so beautiful.\""
    md "Shut up. You're gonna make me blush. I can't be seen blushing."
    return

# CHOICE B SCENE 1
label melody_scene4b_1:
    #[scene 1]
    scene bg black with dissolve
    "The first thing I did was text Alex."
    mc "(We need to talk. Pronto.)"
    ax "(I'm busy tonight. First thing tomorrow morning?)"
    mc "(Yeah, fine. First thing at the Starbucks.)"
    mc "\"Oh geez... I got a text from Melody.\""
    ax "What'd she say?"
    mc "("

# CHOICE B SCENE 2
label melody_scene4b_2:
    #[scene 2]
    scene bg black with dissolve
    "Melody was waiting for me when I got out of class."
    show md calm with dissolve
    md "Fancy seeing you here."
    mc "\"You're not still mad, are you?\""
    md "Me? Nah. We're still a part of team, remember? Still gotta finish that."
    mc "\"O-of course!\""

# CHOICE B SCENE 3
label melody_scene4b_3:
    #[scene 3]
    scene bg black with dissolve
    "I thought that a fight was going to break out between the two."

# CHOICE B SCENE END
label melody_scene4b_end:
    #[end]
    scene bg black with dissolve
    md "I really wish that things had turned out different between us."
    mc "\"I kind of did too. You're talented, and smart...\""
    md "Loyalty is everything. And you did nothing to help me."
    return