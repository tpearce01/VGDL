## REINA ROUTE ##
# SCENE 1
label re_scene1:
    #Week 2
    scene bg meeting_1 with fade
    "Pitches"
    "It’s another crowded meeting. Today, we’ll hear about the different projects and choose a team."
    mc "(I told myself I would work as an artist, but what team should I join?)"
    show gd calm with dissolve
    gd "...And so, without further ado, here are this quarter’s pitches!"
    hide gd calm with dissolve
    "Each project lead takes to the stage, sharing their game ideas."
    mc "(That blue-haired girl from the other day, she was pretty cute.)"
    "Platformer, infinite runner, dating sim, none of them really appeal to me."
    mc "(Maybe I’ll get on a team with her.)"
    "Then I see some familiar faces take the stage."
    show md calm at left with dissolve
    show md calm:
        linear 0.5 xalign 0.2
    show re calm at right with dissolve
    show re calm:
        linear 0.5 xalign 0.8
    md "This quarter, me and Reina are leading a product-oriented game."
    md "We’re looking for experienced members only."
    md "This project is going to need some programmers who know their stuff."
    "Melody nudges Reina gently"
    re "Ah! We’re looking for artists as well."
    "Her voice is quiet, but just audible in the lecture hall."
    mc "(A team with Reina looking for artists? I think I found my project.)"
    return
# END SCENE 1    

# SCENE 2
label re_scene2:
    scene bg meeting_2 with fade
    "After the Meeting"
    show md calm with dissolve
    md "So you’re really interested in our game, huh?"
    mc "Yeah, it sounded really neat. I’d love to be part of the team."
    md "I dunno man, how good are you?"
    mc "(Gulp)"
    mc "I’m pretty good."
    # To be continued...
    return
# END SCENE 2

# SCENE 3
#First choice: Week 3
label re_scene3:
    menu reina_option_1:
        "What should I do?"
        
        "Ask to talk to Reina":
             #[Option 1- Ask to talk to Reina]
             #Location?
             scene bg meeting_2 with fade
             show re calm with dissolve
             mc "(This is my only chance...! I’ve got to do it!)"
             mc "Excuse me, Reina?"
             re "Hmm?"
             mc "Well, I was just wondering, would you happen to be free right now?"
             "She tilted her head to the side in confusion."
             re "I am, yes... Why?"
             mc "Weeellll you see, I’m kiinda bored, and could use someone to talk to."
             mc "You think you can grace me with your presence for just a bit?"
             #show re confused with dissolve ?
             "Reina looked taken aback, and shifted her eyes away from me."
             re "U-Umm... I’m sorry, but, I’m not really all that good company..."
             re "But, uh, you can talk to anyone else here?"
             mc "Hmmm... I could, sure. But I only want to talk to you."
             #show re blush with dissolve ?
             "At that, she visibly blushed."
             re "Me? B-But--"
             mc "Hey, don’t be shy~ Sit with me, I promise you won’t regret it!"
             re "...."
             mc "Pleeeaaaase..?"
             re " ... Nnn..."
             "After a moment of further hesitation, Reina eventually gave in and sat down across from me. I couldn’t help but grin."
             mc "Alright, sweet!"
             re "...."
             mc "So, tell me about yourself."
             re "...."
             mc "...."
             mc "Umm... Reina..?"
             re "... Listen, I..."
             re "I’m really... not one for conversations. I’m sorry..."
             "She looked down, biting her lip in apparent disappointment."
             mc "Hmmm..."
             mc "Well, that’s fine then."
             re "... huh?"
             mc "We don’t have to talk to learn more about each other, you know. In fact, think it’s funner this way!"
             show re calm with dissolve
             re "Funner...?"
             mc "Yea! Here, to heck with this talking thing. Why don’t we play a game?"
             re "A game? You have one with you?"
             mc "Anything’s accessible with internet connection!"
             "I whipped out my phone and threw a wink her way."
             #show re happy with dissolve ?
             re " Pff... hehe, I guess you’re right."
             mc "(Dear lord. A giggle that cute should be illegal--)"
             mc "O-Of course I am!"
             mc "Anyway, ever heard of a game called \"Gad Mab?\"" 
             show re calm with dissolve
             "She shook her head."
             mc "It’s a game where you say a set of words out loud, and the other person has to uncover the hidden words within it."
             mc "For example, the phrase \"Ail Huck Each Arm\" has the hidden words \"A lucky charm\" in it. Get it?"
             re "Oh! I hear it!"
             re "Okay, this sounds fun. Let’s play."
             mc "Alright, here’s your first phrase..."
             "I scrolled through a list of Gab Mab phrases on my phone and selected one I found funny."
             mc "Pooh Teal Is Shush"            
             re "Pooh teal is shush...."
             re "... Umm..."
             re "Is it... ‘Putty... lease.. us...?"
             mc "Snrk.."
             re "What?"
             mc "That makes no sense, Reina."
             re "I-It does to! What is it then?"
             "I cleared my throat and leaned forward, looking her dead in the eye."
             mc "..."
             mc "Bootylicious." #omg kiara you're so lame
             #show re happy with dissolve
             re "Pfff-"
             re "Hahaha! And you said my phrase made no sense!"
             mc "Hey, this makes waaaaay more sense than \"putty lease us!\""
             "She laughed, and the day went on like that, with us chuckling over a silly kid’s game."
             "In the end, she left with a grin on her face."
             "I wished to myself that I could keep making her smile like that."
     
     #[Option 2- Work on drawing] 
        "Work on drawing":
             md "What, you staying here, [mcname]?"
             mc "Me? Oh, uh.. yea."
             mc "Just got some work to finish up before the end of the day. Nothing major."
             md "Woa, responsible. I like it."
             md "Keep those work ethics up for our project and I just might start respecting you!"
             mc "Haha, sounds like a plan!"
             "They team filed out, and I was left alone."
             "I whipped out my brand new tablet, and started testing out an art program I downloaded the other day."
             mc "(It may not be much, but... Anything is better than nothing.)"
     
     
     
     #Second choice: Week 4
    menu reina_option_2:
        "What should I do?"
     #[Option 1- Ask Reina out for lunch]
        "Ask Reina out for lunch":
            "Placeholder"
     
     #[Option 2- Work on drawing]
        "Work on drawing":
            "Placeholder"
     
     
     
     #Third choice: Week 5
    menu reina_option_3:
        "What should I do?"
     #[Option 1- Ask to hang out with Reina]
        "Ask to hang out with Reina":
            "Placeholder"
     
     #[Option 2- Work on drawing]
        "Work on drawing":
            "Placeholder"
     
     
     
     #Final choice: Week 6
    menu reina_option_4:
        "What should I do?"
     #[Option 1- Invite Reina over to your room]
        "Invite Reina over to my room":
            "Placeholder"
     
     #[Option 2- Work on drawing]
        "Work on drawing":
            "Placeholder"
     
     
     
     #[[GOOD ENDING]]
label re_good_ending:
    scene bg startbucks with fade
    "I'm midway into week six, and three weeks into Melody's game project."
    "I've spent as much time as I could practicing art and animating, but there's only so much I can get done in this much time."
    mc "(This... was definitely a mistake.)"
    "I was inside the coffee shop in the Student Center working on character designing."
    "My hand started to cramp up, so I took a short break from tablet work."
    "Now, I was reading through a tutorial on animating. The process wasn't all too complicated, but I definitely don't have the skill to make it as fluid as I'd like."
    "I leaned back closed my eyes, rubbing my temples."
    mc "(No point in complaining now, though. I've just got to tough it out, and contribute however I can.)"
    "After a moment, I let out a sigh and opened my eyes."
    show re calm with dissolve
    re "..."
    mc "(?!)"
    mc "R-Reina?!"
    "I bolted upright."
    re "[mcname]. Um... Can I sit next to you?"
    mc "Huh..? Sit next to me?"
    mc "Um, sure. Go right on ahead."
     
     
     #[[BAD ENDING]]
label re_bad_ending:
    