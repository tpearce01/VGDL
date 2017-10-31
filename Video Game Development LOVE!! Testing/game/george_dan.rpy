    
## GEORGE DAN ROUTE ##
## PLACEHOLDER TEXT FOR NOW, GETTING AN IEDEA FOR FLOW AND THE EXPRESSIONS/BACKGROUNDS WE NEED ##

# INTRO SCENE
label gd_intro:
    scene bg ring_road
    with Pause(1)
    scene bg ring_road with hpunch
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
    "\"Ren! It's been awhile!\""
    ren "Are you planning to join VGDC? You're so busy now so seeing you here is so unexpected!"
    "This feeling is false. I don't have time for something this irrelevant. I need to focus, work hard, and succeed."
    "\"Are you going to pitch a game idea for the next meeting? I think you should, since you do have experience in creating videogames!\""
    ren "Yeah, I'm considering doing it, but will I have enough time or the ability to run a whole team? My computer science classes are already killing me."
    "\"I believe you can do it. And don't worry, if anything, your personal artist will be here to help you out.\""
    ren "Thanks! But I really think you should also pitch a game yourself. You're very capable 'protagonist'!"
    "\"Yeah I'll consider it, but no promises.\""
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
    "\"Yeah, we saw each other earlier today.\""
    gd "Oh yes, I remember now. My apologies for knocking down your stuff."
    #show ren 
    #at left 
    #with dissolve
    ren "\"Let's go Prez, I don't have all day what do you need me for?\""
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
    "\"No, I don't think we've really met.\""
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
    "\"Who did that guy think he was?! Asking me if we've met before?! I BET HE REMEMBERED AND HE WAS JUST PLAYING WITH ME! UGHH!\""
    "\"That was so embarrassing. Everything felt so embarrasing!!\""
    "\"Ren and him looked so happy when they talked... are they each other's lover?!?\""
    "Whatever. Just ignore it.. Just ignore it.. Just ignore him..."
    "Why am I'm thinking about him again?!!! Ughhh GET OUT OF MY HEAD!!!"
    "Okay. Okay... Focus... I need to prepare for my speech. And I also need to prepare a videogame project and pitch."
    "*phone rings*"
    "\"Hello Father?... Yes father. I know father. Don't worry father I know better.\""
    "sigh.. he still treats me like a kid."
    return                                                            
# END ROUTE1 SCENE1

# ROUTE1 SCENE3
label gd_route1_scene3:
    #bg lecture_hall
    "*next day in the lecture hall*"
    #show prof 
    #with dissolve
    prof "Hello everyone, thank you for attending this special research lecture."
    prof "Our special guest for today is a young prodigy, the child of the Chancellor of UCI himself, [mcname]!"
    crowd "Wow no way! That's the Chancellor's child?!?"
    crowd "So young and already giving lectures?! Amazing."
    crowd "I knew that the Chancellor is an extremely well known and accomplished researcher, but his child too?? I guess it runs in the family"
    "\"Hi everyone, thank you for having me today.\""
    "\"I'm extremely pleased to present my research that I've been working on...\""
    #hide prof
    #with dissolve
    "*after lecture*"
    "\"That concludes my lecture. Does anyone have any questions?\""
    "\"Yes, over ther...\""
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
    "\"Umm I.. I.. am busy. So I am not able to. Sorry. But I will definitely be happy to talk to you about it if you find me around...\""
    "\"Sorry everyone that will be all for now. Thank you everyone for coming...\""
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
    #bg outside
    "\"My hands are shaking...\""
    "That was so embarrassing... I was able to confidently give a lecture but once *he* asked me a question I started to breakdown..."
    "\"THAT GUY IS SO ANNOYING!!!!\""
    show gd #smile 
    with dissolve
    gd "I bet he is annoying."
    "WHAT?! WHERE DID HE COME FROM. OH NO HE PROBABLY HEARD ME. WHAT DO I SAY."
    "\"AHAHAHA\""
    "\"Yeah my father is always so strict and overprotective! Such an annoying guy..AHAHA\""
    "*I fake a smile and pretend that my phone is ringing*"
    "Oh look he's calling me right now! I gotta go ~!"
    gd "Hahah, alright, see you later."
    "Good save [mcname]!!"
    "Phewww... I seriously need to stop talking out loud to myself.."
    "Just ignore it.. just ignore it.. time to go home."
    return
# END ROUTE1 SCENE3 END
# END ROUTE1 SCENE3

# ROUTE1 SCENE4
label gd_route1_scene4:
    #bg lecture_hall
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
    "Hi everyone. My gum... I mean AH I mean game is called Faker..."
    show gd with dissolve
    "*I turn my head slightly and see George Dan*"
    "UGHHH WHY IS HE LOOKING AT ME. THIS GUY IS IRRATING ME. Focus... Focus... I can do this."
    hide gd with dissolve
    "\"So my game is a text based game with animation where the player plays as the chracters and choose their fate.\""
    "\"There will be an abnormal villain/kidnapper that can morph himself into anyone.\""
    "\"His goal of this game is for the player to find the kidnapper as soon as possible...\""
    "*continues for another 2 minutes of torture*"
    "\"That's the gist of it, Thank you for listening.\""
    "*crowd claps*"
    "THAT WAS THE WORST PRESENTATION THAT I'VE DONE. THAT GUY IS REALLY PISSING ME OFF!!"
    #show ren
    ren "Hey 'protagonist' you did great. I expected nothing less from my little girl."
    "\"Thanks Ren, but I choked pretty hard up there...\""
    "\"Jeez I never get nervous.\""
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
    "\"By Ren, thanks for the talk.\""
    ren "No problem, anytime."
    #hide ren
    show gd with dissolve
    ren "You did a nice job up there."
    gd "Though you still never told me your name...are you going to run away this time before telling me?"
    "*protagonist gets angry*"
    "\"Well don't you already know my name since you went to both my lecture and pitch.\""
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
    return
# ROUTE1 SCENE4 TELL NAME
label gd_route1_scene4_tellname:
    "\"Fine if you want my name that badly. My name is [mcname].\""
    gd "Hi [mcname] it's a pleasure to meet you."
    "*J.D puts his hands out and smiles*"
    "protagonist This guy..."
    return
# END ROUTE1 SCENE4 TELL NAME
# ROUTE1 SCENE4 IGNORE
label gd_route1_scene4_ignore:
    "\"No. I will not give you my name!\""
    gd "You are one interesting girl."
    show gd #smile
    gd "My name is George Dan, nice to meet you!"
    "who is...this guy."
    $ gd_affection += 1
    return
# END ROUTE1 SCENE4 IGNORE
# ROUTE1 SCENE4 NEVER TELL
label gd_route1_scene4_nevetell:
    "*With attitude* \"I'll never tell you my name even if you ask for it a million times.\""
    gd "Haha fair enough. My name is George Dan, it's a honor to meet you [mcname]"
    "*they both look at each other in the eyes as J.D puts his hands out and smiles*"
    "This guy... never stops to make my heart jump."
    $ gd_affection += 2
    return
# END ROUTE1 SCENE4 NEVER TELL
# END ROUTE1 SCENE4

# ROUTE1 SCENE5
    #bg lecture_hall
    "*a few days later*"
    #show ren with dissolve
    ren "Hey [mcname]."
    "\"Oh, Hi Ren!\""
    ren "Are you excited? We find out our team members today."
    "Hopefully I don't get *him* on my team."
    ren "\"Hopefully the prez will be on my team!\""
    ren "\"He's such a good writer and a good leader.\""
    "yuck. He irritates me.."
    ren "Wait what did you say? Sorry! I didn't hear you."
    "\"Oh nothing! Ha ha ha.\""
    #show ren smile
    ren "Okay, let's go to the meeting!"
    #hide ren with dissolve
    "*later*"
    "WHAT?! HES ON MY TEAM AS THE GROUP SUPERVISOR?! "
    "I bet he purposely put himself on my group..."
    "That nervous feeling is coming back...my hands are starting to sweat again... THIS GUY IS IRRITATING ME."
    gd "Hey everyone. It's an honor to be working with you guys and supervising the team."
    gd "Everyone please introduce yourself. I have another group to meet up with, please write your info down on the paper."
    "*with sarcasm* \"Okay Gore, oops! George! It was nice meeting you, okay bye!\""
    "Thank goodness he's gone. He's heading over to Ren's group..."
    "\"What a great supervisor. He ditches us to wonder off and never come back. Whatever. We won't need him.\""
    team "Eh hahaha."
    "*after meeting the members*"
    "Hmmm it's getting late, I should head back soon, I don't want to make the old man angry if he finds out im out this late."
    "\"Okay guys, let's call it a day and head home.\""
    show gd calm
    gd "Oh yeah, I'll message you later to get the information that I missed."
    "*sarcastically* \"But of course my amazing supervisor!\""
    gd "Hahaha, be safe when you go home."
    "\"Laters.\""
# END ROUTE1 SCENE5
## END GEORGE DAN ROUTE ##