    
## GEORGE DAN ROUTE ##
## PLACEHOLDER TEXT FOR NOW, GETTING AN IEDEA FOR FLOW AND THE EXPRESSIONS/BACKGROUNDS WE NEED ##

# INTRO SCENE
label gd_intro:
    scene bg park_2
    ""
    scene bg park_2 with hpunch
    "The main character(player) bumps into a mysterious person and the player drops her stuff."
    show gd calm
    gd "He then calmly looks at the player and gives the player a small, but charming smile and then proceeds to pick up the player&#x27;s stuff. Seeing a book that he likes, the mysterious person then tells the player that she has really good taste for books."
    # show gd smile
    # gd "-He then smiles and exits. "
    hide gd smile with dissolve
    "Wondering who the guy was, the player thought that he is very cute."
    # show ren greeting
    "A person approaches the player and this person is her closest friend from highschool who is 1 year above the player."
    # show ren calm
    "Ren and the player talks for a bit and then Ren asks the player if they are going to join any clubs."
    "Ren then forces the player to join VDGC with her because they both love videogames. Ren tells the player that the meeting is tonight."
    # show ren farewell
    "Player and Ren then part ways."
    # hide ren farewell with dissolve
    return
#END INTRO SCENE

# FIRST MEETING SCENE
label gd_route1_scene1:
    #**Setting: Lecture hall/meeting hall**
    #**Club introduction **
    #The board introduces the members
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
    "So he was the one that I bumped into earlier..George dan.. What a cute name. "
    "Why can't I stop looking at him. My heart feels heavy, my hands are starting to sweat, what is this excitement? "
    "Is it because of him? I don't even know him, he is just a guy that I randomly bumped into earlier!"
    "But when he bumped into me .. when he briefly told me those words.. and when I see him now, it's like..."
    hide sparkle_anim
    hide gd calm
    with dissolve
    with Pause(0.25)
    #show ren smile
    ren "Hey, I didn't expect to see you here nerd!"
    "Oh it's Ren, I haven't seen her in a long time. I miss the good old times we spent together back in highschool. "
    "She's like a big sister to me. Always taking care of me and watching over me."
    mc "Ren! It's been awhile!"
    ren "Are you planning to join VGDC? You're so busy now so seeing you here is so unexpected!"
    "This feeling is false. I don't have time for something this irrelevant. I need to focus, work hard, and succeed."
    mc "Are you going to pitch a game idea for the next meeting? I think you should, since you do have experience in creating videogames!"
    ren "Yeah, I'm considering doing it, but will I have enough time or the ability to run a whole team? My computer science classes are already killing me."
    mc "I believe you can do it. And don't worry, if anything, your personal artist will be here to help you out."
    ren "Thanks! But I really think you should also pitch a game yourself. You're very capable 'protagonist'!"
    mc "Yeah I'll consider it, but no promises."
    "At that moment I saw him coming up towards us. The nervous feeling started to come back. Why is he coming here? Why is he walking towards me?! But then.."
    show gd calm at right
    with dissolve
    gd "Hey Ren, long time no see. I need to ask you something, can you come with me?"
    ren "Heya Prez, what's up with the outfit? You know this was only a VGDC meeting, not some meet and greet with celebrities... Who are you trying to impress anyway?"
    gd "I'm trying to impress the beautiful Ren of course."
    # show ren blush
    ren "Shut up. I'm not going to fall for your flattery."
    gd "Hahaha, I was only joking, anyway, come with me for a sec."
    hide ren 
    with dissolve
    with Pause(0.25)
    "I didn't know Ren knew him...They get along pretty well. I should just leave now...I don't want to make everything awkward."
    "He then turned to me, gave me a the same charming smile from before and then asks..."
    gd "Hi, Have we met before?"
    menu:
        "What should I say?"
        "Yes":
            call gd_route1_scene1_yes
        "No":
            call gd_route1_scene1_no
        "Ignore and walk away":
            call gd_route1_scene1_ignore
    return
# END FIRST MEETING SCENE

# YES
label gd_route1_scene1_yes:
    mc "Yeah, we saw each other earlier today."
    gd "Oh yes, I remember now. My apologies for knocking down your stuff."
    #show ren 
    #at left 
    #with dissolve
    ren "Let's go Prez, I don't have all day what do you need me for?"
    #hide ren 
    #with dissolve
    #with Pause(0.25)
    hide gd 
    with dissolve
    with Pause(0.25)
    "...Ren and the President walked away. "
    "He looks cuter than before... NO NO NO!"
    return
# END YES

# NO 
label gd_route1_scene1_no:
    "I looked at him in the eyes and said.."
    mc "No, I don't think we've really met."
    gd "I like your glasses. You have good taste."
    "Those words. That smile. That timeless smile..."
    $ gd_affection += 1;
    return
# END NO

# IGNORE
label gd_route1_scene1_ignore:
    "You quickly walk away."
    gd "Hey wait.."
    #show ren 
    #at left
    #with dissolve
    gd "Did I say something wrong Ren?"
    ren "You're a heartbreaker..."
    $ gd_affection -= 1
    return
# END IGNORE

# ROUTE1 SCENE2
label gd_route1_scene2:
    #bg apartment
    mc "Who did that guy think he was?! Asking me if we've met before?! I BET HE REMEMBERED AND HE WAS JUST PLAYING WITH ME! UGHH!"
    mc "That was so embarrassing. Everything felt so embarrasing!!"
    mc "Ren and him looked so happy when they talked... are they each other's lover?!?"
    "Whatever. Just ignore it.. Just ignore it.. Just ignore him..."
    "Why am I'm thinking about him again?!!! Ughhh GET OUT OF MY HEAD!!!"
    "Okay. Okay... Focus... I need to prepare for my speech. And I also need to prepare a videogame project and pitch."
    "*phone rings*"
    mc "Hello Father?... Yes father. I know father. Don't worry father I know better."
    "sigh.. he still treats me like a kid."
    return                                                            
# END ROUTE1 SCENE1

# ROUTE1 SCENE3
label gd_route1_scene3:
    scene bg meeting_1
    "*next day in the lecture hall*"
    #show prof 
    #with dissolve
    prof "Hello everyone, thank you for attending this special research lecture."
    prof "Our special guest for today is a young prodigy, the child of the Chancellor of UCI himself, [mcname]!"
    crowd "Wow no way! That's the Chancellor's child?!?"
    crowd "So young and already giving lectures?! Amazing."
    crowd "I knew that the Chancellor is an extremely well known and accomplished researcher, but his child too?? I guess it runs in the family"
    mc "Hi everyone, thank you for having me today."
    mc "I'm extremely pleased to present my research that I've been working on..."
    #hide prof
    #with dissolve
    "*after lecture*"
    mc "That concludes my lecture. Does anyone have any questions?"
    mc "Yes, over ther..."
    show gd calm
    "Why is he here?!? Was he here listening to my presentation the whole time?!"
    gd "That was an amazing presentation, and your research is amazing. Will you have after hours to talk and discuss about your research more?"
    "Say no [mcname]!! Why are you so nervous now [mcname]?! Just answer his question and leave!"
    menu:
        "What should I say?"
        "Answer him":
            call gd_route1_scene3_answer
        "Leave":
            call gd_route1_scene3_leave
    return
# ROUTE1 SCENE3 ANSWER
label gd_route1_scene3_answer:
    mc "Umm I.. I.. am busy. So I am not able to. Sorry. But I will definitely be happy to talk to you about it if you find me around..."
    mc "Sorry everyone that will be all for now. Thank you everyone for coming..."
    "*quickly exits*"
    crowd "Wait you only answered 1 question"
    crowd "Wait I have a question..!"
    crowd "Me too..."
    crowd "Looks like she's gone after only answering 1 question.. I wonder what happened to her..."
    return
# END ROUTE1 SCENE3 ANSWER
# ROUTE1 SCENE3 LEAVE
label gd_route1_scene3_leave:
    "*quickly exits*"
    crowd "Wait you didn't answer any questions..."
    crowd "Wait I have a question..!"
    crowd "Me too..."
    return
# END ROUTE1 SCENE3 LEAVE
# ROUTE1 SCENE3 END
label gd_route1_scene3_end:
    scene bg park_2
    mc "My hands are shaking..."
    "That was so embarrassing... I was able to confidently give a lecture but once *he* asked me a question I started to breakdown..."
    mc "THAT GUY IS SO ANNOYING!!!!"
    show gd #smile 
    with dissolve
    gd "I bet he is annoying."
    "WHAT?! WHERE DID HE COME FROM. OH NO HE PROBABLY HEARD ME. WHAT DO I SAY."
    mc "AHAHAHA"
    mc "Yeah my father is always so strict and overprotective! Such an annoying guy..AHAHA"
    "*I fake a smile and pretend that my phone is ringing*"
    mc "Oh look he's calling me right now! I gotta go ~!"
    gd "Hahah, alright, see you later."
    mc "Good save [mcname]!!"
    mc "Phewww... I seriously need to stop talking out loud to myself.."
    "Just ignore it.. just ignore it.. time to go home."
    return
# END ROUTE1 SCENE3 END
# END ROUTE1 SCENE3

# ROUTE1 SCENE4
label gd_route1_scene4:
    scene bg meeting_1
    "*the next VGDC meeting, aka pitch day*"
    show gd calm with dissolve
    gd "Alright everyone, today is the big day. Let's hear those pitches."
    "*crowd claps*"
    "*a few pitches later*"
    "It's almost my turn...why am I nervous?! I can give a lecture to full hall of professionals for hours,"
    "but I'm nervous about this small presentation..."
    gd "Up next we have a game called Faker by 'protagonist'"
    hide gd with dissolve
    "*crowd claps*"
    mc "Hi everyone. My gum... I mean AH I mean game is called Faker..."
    show gd with dissolve
    "*I turn my head slightly and see George Dan*"
    "UGHHH WHY IS HE LOOKING AT ME. THIS GUY IS IRRATING ME. Focus... Focus... I can do this."
    hide gd with dissolve
    mc "So my game is a text based game with animation where the player plays as the chracters and choose their fate."
    mc "There will be an abnormal villain/kidnapper that can morph himself into anyone."
    mc "His goal of this game is for the player to find the kidnapper as soon as possible..."
    "*continues for another 2 minutes of torture*"
    mc "That's the gist of it, Thank you for listening."
    "*crowd claps*"
    "THAT WAS THE WORST PRESENTATION THAT I'VE DONE. THAT GUY IS REALLY PISSING ME OFF!!"
    #show ren
    ren "Hey [mcname] you did great. I expected nothing less from my little girl."
    mc "Thanks Ren, but I choked pretty hard up there..."
    mc "Jeez I never get nervous."
    ren "You did amazing, don't worry too much. Maybe it's because you present to so many people that presenting to a smaller group makes you nervous Hahaha."
    #hide ren
    show gd calm
    with dissolve
    "*I look to George Dan"
    "Or maybe I'm nervous because this idiot's face distracts me so much it irritates me."
    hide gd
    with dissolve
    #show ren with dissolve
    ren "Anyway, we'll find out who will be in our group in the next meeting. I have to head out now, but I'll catch you later"
    mc "By Ren, thanks for the talk."
    ren "No problem, anytime."
    #hide ren
    show gd with dissolve
    ren "You did a nice job up there."
    gd "Though you still never told me your name...are you going to run away this time before telling me?"
    "*protagonist gets angry*"
    mc "Well don't you already know my name since you went to both my lecture and pitch."
    gd "Sorry Hahahaha! You're right. But, we've never formally met. So may I ask for your name?"
    show gd #smile
    "That dumb smile of his. I hate it...but it brings a gentle warmth that one can't resist but to blush."
    menu:
        "What should I say"
        "Tell him my name":
            call d_route1_scene4_tellname
        "Ignore him and leave":
            call gd_route1_scene4_ignore
        "Tell him that you'll never tell him your name.":
            call gd_route1_scene4_nevetell
    hide gd calm
    return
# ROUTE1 SCENE4 TELL NAME
label gd_route1_scene4_tellname:
    mc "Fine if you want my name that badly. My name is [mcname]."
    gd "Hi [mcname] it's a pleasure to meet you."
    "*George Dan puts his hands out and smiles*"
    "This guy..."
    return
# END ROUTE1 SCENE4 TELL NAME
# ROUTE1 SCENE4 IGNORE
label gd_route1_scene4_ignore:
    mc "No. I will not give you my name!"
    gd "You are one interesting girl."
    show gd #smile
    gd "My name is George Dan, nice to meet you!"
    "who is...this guy."
    $ gd_affection += 1
    return
# END ROUTE1 SCENE4 IGNORE
# ROUTE1 SCENE4 NEVER TELL
label gd_route1_scene4_nevetell:
    mc "*With attitude* \"I'll never tell you my name even if you ask for it a million times.\""
    gd "Haha fair enough. My name is George Dan, it's a honor to meet you [mcname]"
    "*We look at each other in the eyes as George Dan puts his hands out and smiles*"
    "This guy... never stops to make my heart jump."
    $ gd_affection += 2
    return
# END ROUTE1 SCENE4 NEVER TELL
# END ROUTE1 SCENE4

# ROUTE1 SCENE5
label gd_route1_scene5:
    scene bg classroom
    "*a few days later*"
    #show ren with dissolve
    ren "Hey [mcname]."
    mc "Oh, Hi Ren!"
    ren "Are you excited? We find out our team members today."
    "Hopefully I don't get *him* on my team."
    ren "Hopefully the prez will be on my team!"
    ren "He's such a good writer and a good leader."
    mc "yuck. He irritates me.."
    ren "Wait what did you say? Sorry! I didn't hear you."
    mc "Oh nothing! Ha ha ha."
    #show ren smile
    ren "Okay, let's go to the meeting!"
    #hide ren with dissolve
    scene bg meeting_2
    "*later*"
    "WHAT?! HES ON MY TEAM AS THE GROUP SUPERVISOR?! "
    "I bet he purposely put himself on my group..."
    "That nervous feeling is coming back...my hands are starting to sweat again... THIS GUY IS IRRITATING ME."
    show gd calm with dissolve
    gd "Hey everyone. It's an honor to be working with you guys and supervising the team."
    gd "Everyone please introduce yourself. I have another group to meet up with, please write your info down on the paper."
    mc "*with sarcasm* \"Okay Gore, oops! George! It was nice meeting you, okay bye!\""
    hide gd calm with dissolve
    "Thank goodness he's gone. He's heading over to Ren's group..."
    mc "What a great supervisor. He ditches us to wonder off and never come back. Whatever. We won't need him."
    team "Eh hahaha."
    "*after meeting the members*"
    "Hmmm it's getting late, I should head back soon, I don't want to make the old man angry if he finds out im out this late."
    mc "Okay guys, let's call it a day and head home."
    show gd calm
    gd "Oh yeah, I'll message you later to get the information that I missed."
    mc "*sarcastically* \"But of course my amazing supervisor!\""
    gd "Hahaha, be safe when you go home."
    hide gd calm with dissolve
    mc "Laters."
    return
# END ROUTE1 SCENE5

# ROUTE 1 SCENE 6
label gd_route1_scene6:
    #scene apartment
    "*later that night*"
    #show phone
    "*text from phone*"
    "It's 12 a.m... why is someone texting me this late"
    #show phone georgedan
    "WHAT DOES HE WANT ITS 12AM. Why am I so awake now..."
    gd "Hey, this is me Jeorge, sorry for messaging you this late, but I was wondering when you wanted to meet up to discuss about the game?"
    "HMMM should I wait till the morning and answer or should I answer it now..." 
    "WHAT. WHY DOES THAT MATTER. I'll just answer it now."
    mc "Uhh yeah I can meet up whenever after 6p.m tomorrow."
    gd "Okay, where do you want to meet up?"
    mc "Wherever is fine."
    gd "My apartment?"
    "WAIT WHAT. WHAT DID HE SAY."
    mc "your apartment?"
    gd "Yeah, I'll give you a ride there."
    "My hands are starting to sweat like crazy... WHAT DO I SAY. HIS APARTMENT?!"
    mc "Yeah sure if you want"
    "WHY DID I SAY YES. WHY DID I SAY THAT."
    gd "Let's meet up at the library when you're done?"    
    mc "Yeah"
    "HOW DID THIS HAPPEN."    
    #hide phone with dissolve
    "*3 hours later*"
    "It's 3 a.m... I'm going to be so tired tomorrow but I can't sleep. ALL BECAUSE OF HIM AGAIN."
    return
# END ROUTE 1 SCENE 6

# ROUTE 1 SCENE 7
label gd_route1_scene7:
    #scene gd_apartment_outside
    "So this is where the president lives huh?"
    show gd calm
    gd "Yeah, it's pretty empty inside"
    #scene gd_apartment_inside
    "It's so clean... His apartment is extremely clean!!"
    mc "Your apartment is so clean!!! How is this possible? You're... you're a guy. Guys are messy."
    mc "It's so sad when a guy's apartment is cleaner than yours..."
    gd "Hahaha, I just like to keep things clean I guess."
    gd "Would you like anything to drink or eat?"
    mc "Yeah, what do you have?! I haven't eaten anything today."    
    gd "Well the fri... I guess you found the fridge."
    mc "Wow... you have so much fresh foods and ingredients stocked in here!"
    gd "Feel free to cook yourself anything."
    mc "I.. I can't cook. I don't know how. Or well I never learned how to... I never got the chance to try."
    gd "Ah I see. As the daughter of the prestige Chancellor, you're always too busy with research to cook food for yourself."
    gd "That's fine, I'll cook you dinner."
    gd "In the mean time can you give layout your project and give me a rundown of what you plan on doing for the next week."
    mc "wait... can I..?"
    gd "You want to help me cook is what you were going to ask?"
    "WAIT WHAT.HOW DID HE KNOW. WHY DID I SAY THAT. NOT KNOWNIG HOW TO COOK IS ALREADY EMBARRASSING."
    gd "No."
    #*protagonist gives a scare/frozen expression*
    gd "Hahaha, I'm just kidding. Yeah, I'll teach you how to cook."
    mc "You could've frozen African with those words..."
    mc "What are we cooking?!"
    gd "Steak and veggies"
    mc "REALY STEAK?!" 
    "The only beef I had since arriving here was chinese beef from fast food..."
    gd "You probably only had fast food since you arrived here am I wrong?"
    "Either this guy is some kind of mind reader or he's from the future. He can read me like a book."
    "*awkwardly laughs*"
    mc "AHAHAHAHA...."
    gd "Okay, can you clean the veggies?"
    hide gd calm with dissolve
    "*an hour later*"
    show gd calm with dissolve
    gd "And we're done!"
    mc "Wow!!! That smell is so amazing!!!!!!! I can already taste the richness of the meat through my nose"
    #show gd smile
    gd "You made it. You did a great job."
    #*protagonist extremely happy and starts to devour the beef*
    show gd calm
    gd "Alright, so what's the plan for next week? When do you plan to have the meetings and what are the deadlines?"
    mc "I... Oooooooo is that your halloween costume?! Waah it's so nice!"
    mc "This is one good detective costume! Where did you get it?!"
    gd "Oh, I made it."
    mc "What?! You did all that by yourself?! Wow..."
    mc "You're not just a useless supervisor after all"
    gd "Huh?"
    #*protagonist stands up*
    "*I stand up*"
    mc "Oh shoot, my shirt caught the table and it ripped... and today was going so well too..."
    gd "Here, take off your shirt"
    mc "WHAT?! HUH?! YOU PERVERT."
    #*J.D smiles and chuckles*
    #show gd smile
    gd "Here take this shirt, put it on, and give me the one that ripped, I'll won't look."
    mc "This guy.. what is he up to."
    mc "Here."
    "*George Dan pulls out his sewing kit*"
    "Wow... he's going to sew it back for me.."
    "*George Dan hands back the shirt*"
    gd "Here ya go, sorry I wasn't able to do a better job."
    mc "You sure know how to do everything huh... You're like a mom..."
    gd "It's called being a responsible adult." 
    mc "So you're saying I'm not an adult?!"
    mc "That's insulting..."
    gd "Hahaha, there are many different kinds of adults... The ones that can cook and sew."
    gd "The ones that take care of their children...And the ones that work hard endlessly throughout the day and night."
    #*J.D pokes protagonist in the nose*
    "*George Dan pokes me in the nose*"
    gd "Well it's late, we weren't able to discuss much, but we can talk about the game another day."
    gd "Let's go, I'll drive you home."
    #*J.D puts on his coat and the protagonist looks*
    "He's so mature... and those eyes... that expression... He's been through a lot."
    hide gd with dissolve
    return
# END ROUTE1 SCENE7

# ROUTE1 SCENE8
# DIALOGUE NOT YET IMPLEMENTED
# END ROUTE1 SCENE8
## END GEORGE DAN ROUTE ##