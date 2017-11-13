## ALEX ##
label alex_scene1:
    #***ADD IN TEXT W/ GIRL AND DENIM JACKET***
    #Food Court - After Initial Meeting
    scene bg foodcourt
    "I hadn’t talked to Alex since finding out that he was a design officer in the VGDC."
    "I had so many questions."
    "I managed to meet up with him in the food court the next day."
    show ax calm with dissolve
    ax "Bonjour, [mcname]!"
    mc "\"Since when did you speak French?\""
    ax "Since finding out it’s the language of love, and that chicks really dig bilingual guys."
    mc "(We were just friends, but it always hurt to hear him talk about other girls.)"
    mc "\"Yeah, cool. So, um, why didn’t you tell me that you were in the VGDC?\""
    ax "You never asked. You’re not mad, are you?"
    mc "\"No, I’m not mad. I just feel like there’s a lot of things I don’t know about you anymore.\""
    ax "I think I can help with that, if you help me with something."
    mc "\"What are you talking about?\""
    ax "So, I went out with the girl last night that I met at the Involvement Fair. It uh, went south pretty quickly."
    mc "\"How’d you manage to screw it up so fast?\""
    ax "I guess I have a ‘reputation’ for being a womanizer. And the girl called me out on it."
    mc "\"Dude… that’s intense.\""
    ax "Tell me about it. Anyways, we set up a dare."
    mc "\"What kind of a dare?\""
    ax "This is actually where you come in. I’ll need you to pretend to be in a fake relationship with me."
    mc "\"Um…\""
    ax "And then we’ll break up when she says, \"I was wrong about you.\" I’ll get my $20, and hopefully the lady."
    mc "\"That sounds complicated and unnecessary...\""
    ax "Please, [mcname]... I really like this girl. I gotta clear my name. You’re my best friend, right?"
    mc "(I was, at one time...)"
    mc "\"Yeah, that’s right.\""
    ax "So, can you please help me?"
    mc "\"...Okay.\""
    ax "Since we’re gonna be together a lot more now anyways, why don’t you help me with my pitch for next week, too?"
    mc "\"For the club? You’re gonna pitch a game?\""
    ax "Yeah! The gameplay is gonna be like, old school Final Fantasy."
    mc "\"What else?\""
    ax "Well, that’s all I have so far. Maybe you could help me brainstorm a little more?"
    mc "\"Okay. After class?\""
    ax "Totally. I’ll text you."
    "Although I thought that his revenge plan was an awful idea, I missed doing stuff with Alex."
    "He had changed. Whether or not for the better, I hadn’t decided yet."
    "But it didn’t really matter. He was my friend, and we were doing stuff together again, like old times."
    return

label alex_scene2:
    #SSLH - Pitching Game
    scene bg meeting with fade
    "A week passed, and the most important club meeting of the quarter was near - the Pitch Meeting."
    "We had finally decided on a theme for the game - the old west."
    "I’ve never been a huge fan of speaking in front of huge crowds."
    "But with Alex at my side, we could conquer anything."
    show ax calm with dissolve
    ax "Hello everyone! My name is Alex, and this is my friend, [mcname]."
    mc "\"Hi! Uh... so the basic gist of our game is a 2D, turn-based fighting system set in the old west.\""
    return

    #ALDRICH PARK - Scouting for Scenes
label alex_scene3:
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

label alex_scene4:
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
        ""
        "\"I love you!\"":          # CHOICE A
            mc "\"I love you too, Alex. Let's... let's stop pretending.\""
            show ax happy with dissolve
            ax "Phew... that was hard..."
            #augment relationship vars
            jump alex_scene4_a1

        "\"Wait a second...\"":     # CHOICE B
            mc "\"You're asking a lot from me, Alex. I... I'll need some time to think about it.\""
            show ax frown with dissolve
            ax "Y-yeah... sure. Y'know, I was just kidding."
            mc "\"It didn't look like it.\""
            ax "Nah. You and me, officially a couple? If we were going to do that, we would have done it forever ago."
            mc "\"Yeah, I guess.\""
            #augment relationship vars
            jump alex_scene4_b1

# CHOICE A
label alex_scene4_a1:
    #[scene 1]
    ax "Wow, you and me, together. This feels... good."

label alex_scene4_a2:
    #[scene 2]
    scene bg black with fade
    "Weeks passed, and we were so happy."
    "We did everything together. Just like old time."
    "The only difference was that we were past the friend stage. We were in love."

label alex_scene4_a3:
    #[scene 3]
    "Our game was set to be completed in the following week."
    "Alex had stopped returning my texts. He didn't want to meet up for lunch..."
    "Things had gone south very fast."

label alex_scene4_aend:
    #[end]
    #scene bg ??
    mc "\"You're really going to pin all of this on me?\""
    ax "We didn't finish the game because of YOU."
    mc "\"How is it my fault!?\""
    ax "Your constant nagging, dragging me to places instead of to the meetings so we could finish things."
    mc "\"That's what couples do!\""
    ax "If you love someone, then you're not going to keep them from doing what they want to do."
    mc "\"Alex! Don't leave. I love you!\""
    ax "Yeah, and I thought I loved you too."
    return

# CHOICE B
label alex_scene4_b1:
    #CHOICE B
    #[scene 1]
    #scene bg ??
    ax "Look, about the other day..."
    mc "\"Forget about it. Let's just work on our game, okay?\""

label alex_scene4_b2:
    #[scene 2]
    scene bg black with fade
    "Our game was set to be completed in the following week."
    "One of the writers in our group had flaked out early on."
    "We were scrambling to get everything done on time."

label alex_scene4_b3:
    #[scene 3]
    #scene bg ??
    ax "Wow, our game turned out great!"

label alex_scene4_bend:
    #[end]
    ax "Thanks for everything, [mcname]."
    mc "\"It's what friends do!\""
    ax "Then I'm super lucky to have a friend like you."
    return