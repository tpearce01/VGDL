## ALEX ##

# ALEX SCENE 1
label alex_scene1:
    #***ADD IN TEXT W/ GIRL AND DENIM JACKET***
    #Food Court - After Initial Meeting
    scene bg foodcourt
    "I hadn’t talked to Alex since finding out that he was a design officer in the VGDC."
    "I had so many questions."
    "I managed to meet up with him in the food court the next day."
    show ax smile with dissolve
    ax "Bonjour, [mcname]!"
    mc "\"Since when did you speak French?\""
    ax "Since finding out it’s the language of love, and that chicks really dig bilingual guys."
    mc "(We were just friends, but it always hurt to hear him talk about other girls.)"
    mc "\"Um, okay. So, why didn’t you tell me that you were in the VGDC?\""
    show ax calm with dissolve
    ax "I dunno. I wanted it to be a surprise."
    mc "\"It was a crappy surprise.\""
    ax "Sorry I made you feel that way, [mcname]."
    mc "\"I just feel like there’s a lot of things I don’t know about you anymore.\""
    ax "I think I can help with that, if you help me with something."
    mc "\"What are you talking about?\""
    ax "So, I went out with the girl last night that I met at the Involvement Fair." 
    mc "\"What's her name?\""
    ax "Naomi. Anyways, it uh, went south pretty quickly."
    mc "\"How’d you manage to screw it up so fast?\""
    ax "I guess I have a ‘reputation’ for being a womanizer. And Naomi called me out on it."
    mc "\"Dude… that sucks.\""
    ax "Tell me about it. Anyways, this is where you come in."
    mc "\"What are you gonna make me do?\""
    ax "I’ll need you to pretend to be in a fake relationship with me."
    mc "\"Um…\""
    ax "Please say you'll help me, [mcname]."
    #Diverges into 2 options:
    menu help_alex:
        "Please say you'll help me, [mcname]."
        "Yes":
            #[Pos. Option] "Yes"
            mc "\"Okay, but how does it benefit me?\""
            ax "You'll get the satisfaction of helping your best friend in his time of need."
            mc "\"That's it?\""
            ax "I'll also help you with a pitch for the meeting next week."
            mc "(I did want to pitch something next week...)"
            mc "(And if I had the help of one of the official officers, I was sure to get accepted.)"
            mc "\"All right. As long as your plan doesn't involve anything super awful.\""
            ax "Nah! I’ll text you later about it."
        "No":
            #[Neg. Option] "No"
            mc "\"I'm not comfortable with doing soemthing like that.\""
            show ax frown with dissolve
            ax "So you're gonna abandon your friend in his time of need?"
            mc "\"I'm not 'abandoning' you...\""
            ax "Look, help me with this, and I'll help you with your pitch for next week."
            mc "\"How'd you know that I wanted to pitch...?\""
            ax "Just a good guess."
            mc "(I did want to pitch something next week...)"
            mc "(And if I had the help of one of the official officers, I was sure to get accepted.)"
            mc "\"Fine. I'll help, but I'm still not comfortable with all of this.\""
            ax "It won't be for very long, I promise. I'll text you later about it."
    hide ax with dissolve
    "Although I thought that his revenge plan was an awful idea, I missed doing stuff with Alex."
    "He had changed. Whether or not for the better, I hadn’t decided yet."
    "But it didn’t really matter. He was my friend, and we were doing stuff together again, like old times."
    return
# END ALEX SCENE 1

# ALEX SCENE 2
label alex_scene2:
    #Scene 2 - Starbucks Student Center
    scene bg starbucks with dissolve
    show ax calm with dissolve
    ax "Okay, so we have to have some sort of a plan for the pitch."
    mc "I was thinking of a dating sim, but with cats."
    ax "So kind of like Hatoful Boyfriend?"
    mc "Yeah! But with cats."
    ax "Okay, okay..."
    "Before Alex could continue, a girl in a demin jacket walked up to our table."
    show ax calm:
        linear 0.5 xalign 1.0
    with Pause(0.5)
    show nm calm with dissolve
    nm "Alex."
    ax "Naomi."
    nm "Hi, I don't believe I know you."
    mc "My name is [mcname]."
    nm "So, how do you two know each other?"
    mc "We've known each other forever. We went to different high schools, but we were able to reconnect when I came here."
    nm "Heh. I assume he's told you about me, then?"
    ax "Actually... I haven't told [mcname] anything about you."
    nm "What a surprise. Look, [mcname], the guy you knew back when you were kids... that guy isn't around anymore."
    ax "How would you know?"
    nm "I just don't want you to hurt [mcname]'s feelings."
    ax "Can you please leave, Naomi?"
    nm "I know you two are the new \"it\" couple. Everyone's been talking about it. [mcname], get out while you can."
    hide nm with dissolve
    show ax calm:
        linear 0.5 xalign 0.5
    with Pause(0.5)
    "Naomi left, and I sat there baffled."
    mc "Everyone's talking about it?"
    ax "Don't worry. She's just trying to psyche you out."
    mc "If you say so."
    return
# END ALEX SCENE 2

# ALEX SCENE 3
label alex_scene3:
    #Scene 3 - Food Court
    scene bg foodcourt with dissolve
    mc "I had no idea you were into the whole design thing."
    ax "Sure am! It's really pretty cool."
    return
# END ALEX SCENE 3

# ALEX SCENE 4
label alex_scene4:
    #SSLH - Pitching Game
    scene bg meeting with fade
    "A week passed, and the most important club meeting of the quarter was near - the Pitch Meeting."
    "We had finally decided on a theme for the game - the old west."
    "I’ve never been a huge fan of speaking in front of huge crowds."
    "But with Alex at my side, we could conquer anything."
    show ax calm with dissolve
    ax "Hello everyone! My name is Alex, and this is my friend, [mcname]."
    mc "\"Hi! Uh... so the basic gist of our game is that it's a dating simulator about cats.\""
    ax "Think \'Hatoful Boyfriend\'."
    return
# END ALEX SCENE 4

# ALEX SCENE 5
label alex_scene5:
    #ALDRICH PARK - Scouting for Scenes
    scene bg park_1 with fade
    show ax calm with dissolve
    ax "What do you think of the campus so far? It's not quite UCLA, but..."
    mc "\"Well, I think it's really, really green.\""
    ax "Is... is that good?"
    mc "\"Nature is good. And I like how like, you can get most places by going in a circle.\""
    ax "Oh, Ring Road?"
    mc "\"Yeah! Ring Road is super convenient.\""
    ax "Speaking of circles... it's funny."
    mc "\"What is?\""
    ax "You remember how we 'went out' in Junior High for a week?"
    mc "\"Oh yeah! That was crazy. Why did we break up again?\""
    ax "Because I wasn't Legolas."
    mc "\"Right. Uh, why is that funny?\""
    return
# END ALEX SCENE 5

# ALEX SCENE 6
label alex_scene6:
    #FOOD COURT - Path Divergence
    show bg foodcourt
    show ax calm with dissolve
    ax "Thanks for meeting me here."
    mc "\"Of course. What do you need?\""
    ax "I've got a confession to make."
    show ax serious with dissolve
    "Alex had become uncharacteristically quiet."
    mc "\"What happened? Are you not the president of Hot Wheels like you've claimed to be in the past?\""
    ax "No. No, that's not it."
    mc "\"Whatever it is, it's not going to change our relationship.\""
    ax "I wouldn't be so sure about that."
    mc "\"Well, are you going to tell me? Or keep stringing me along?\""
    ax "I'm sorry. I'm sorry."
    ax "..."
    ax "I don't want to pretend anymore."
    mc "\"Pretend what?\""
    ax "This. Us. You and me. [mcname], I've liked you for so long. Since we were kids."
    mc "\"I... don't know what to say...\""
    ax "Say that we can stop pretending. Say that you feel the same way about me. I love you, [mcname]."
    menu pretend:
        "Say that we can stop pretending. Say that you feel the same way about me. I love you, [mcname]."
        "\"I love you!\"":          # CHOICE A
            mc "\"I love you too, Alex. Let's... let's stop pretending.\""
            show ax happy with dissolve
            ax "Phew... that was hard..."
            mc "\"But what about Naomi?\""
            jump alex_scene6a_1

        "\"Wait a second...\"":     # CHOICE B
            mc "\"I'm still not completely convinced, Alex.\""
            show ax frown with dissolve
            ax "Y-yeah... sure. Y'know, I was just kidding."
            mc "\"It didn't look like it.\""
            ax "Nah. You and me, officially a couple? If we were going to do that, we would have done it forever ago."
            mc "\"Yeah, I guess.\""
            jump alex_scene6b_1

# CHOICE A SCENE 1
label alex_scene6a_1:
    scene bg black     # PLACEHOLDER
    ax "Wow, you and me, together. This feels... good."

# CHOICE A SCENE 2
label alex_scene6a_2:
    #[scene 2]
    scene bg black with fade
    "Weeks passed, and we were so happy."
    "We did everything together. Just like old time."
    "The only difference was that we were past the friend stage. We were in love."

# CHOICE A SCENE 3
label alex_scene6a_3:
    #[scene 3]
    scene bg black     # PLACEHOLDER
    "Our game was set to be completed in the following week."
    "Alex had stopped returning my texts. He didn't want to meet up for lunch..."
    "Things had gone south very fast."

# CHOICE A SCENE END
label alex_scene6a_end:
    #[end]
    scene bg black     # PLACEHOLDER
    mc "\"You're really going to pin all of this on me?\""
    ax "We didn't finish the game because of YOU."
    mc "\"How is it my fault!?\""
    ax "Your constant nagging, dragging me to places instead of to the meetings so we could finish things."
    mc "\"That's what couples do!\""
    ax "If you love someone, then you're not going to keep them from doing what they want to do."
    mc "\"Alex! Don't leave. I love you!\""
    ax "Yeah, and I thought I loved you too."
    return

# CHOICE B SCENE 1
label alex_scene6b_1:
    #CHOICE B
    scene bg black3     # PLACEHOLDER
    ax "Look, about the other day..."
    mc "\"Forget about it. Let's just work on our game, okay?\""

# CHOICE B SCENE 2
label alex_scene6b_2:
    scene bg black with fade
    "Our game was set to be completed in the following week."
    "One of the writers in our group had flaked out early on."
    "We were scrambling to get everything done on time."

# CHOICE B SCENE 3
label alex_scene6b_3:
    scene bg black     # PLACEHOLDER
    ax "Wow, our game turned out great!"

# CHOICE B SCENE END
label alex_scene6b_end:
    scene bg black     # PLACEHOLDER
    ax "Thanks for everything, [mcname]."
    mc "\"It's what friends do!\""
    ax "Then I'm super lucky to have a friend like you."
    return
# END ALEX SCENE 6