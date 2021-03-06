define re_affection = 0
#define max_affection = 4

## REINA ROUTE ##
# SCENE 1
label re_scene1:
    #Week 2
    scene bg meeting_1 with fade
    play music "/Audio Dumpster/Waiting Music.mp3" fadeout 1.0 fadein 1.0 loop
    "Pitches"
    "It’s another crowded meeting. Today, we’ll hear about the different projects and choose a team."
    mc "(I told myself I would work as an artist, but what team should I join?)"
    show gd calm with dissolve
    gd "...And so, without further ado, here are this quarter’s pitches!"
    hide gd calm with dissolve
    "Each project lead takes to the stage, sharing their game ideas."
    mc "(That blue-haired girl, she was pretty cute. Reina was it?)"
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
    show re surprised with dissolve
    re "Ah! We’re looking for artists as well."
    show re calm with dissolve
    "Her voice is quiet, but just audible in the lecture hall."
    mc "(Reina’s team looking for an artist? I think I found my project.)"
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
    md "Can I see what you got man?"
    mc "Huh?"
    md "Your work, you got a portfolio or something I can see?"
    mc "(Ah crap.)"
    mc "Sorry, I left my laptop at home."
    md "No worries man, show me next time."
    md "I’ll let Reina know we found an artist. It was [mcname], right?"
    mc "Yeah."
    show md happy with dissolve
    md "Sweet. I’ll see what I can do about getting you on the team."
    show md calm with dissolve
    md "You should get in touch with Reina, you’ll be working together a lot on this project."
    mc "(I hope so. I really want to get a chance to talk to her more.)"

    #--black screen--
    scene bg black with fade
    play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
    "The Game Lab, Later that Week"
    scene bg gameroom with dissolve
    "A few club members are scattered around the room, chatting and working on their devices. Thankfully, Alex is nowhere to be found."
    "I recognize Yukiko helping someone out. She sends a smile my way. Reina is in the corner again, drawing."
    mc "(Alright, I’ll give her fair warning this time.)"
    "I clear my throat as I get closer."
    mc "Ahem. Reina?"
    "No response."
    mc "Reina?"
    "I lightly tap her on the shoulder."
    show re surprised with hpunch
    re "Ah?!"
    "She jolts back, but I catch the chair before it falls."
    re "You?"
    mc "I want to say that one was your fault."
    re "No way! Stop sneaking up on me!"
    show re blush with dissolve
    re "But thanks for catching me...again."
    "She’s blushing a bit again."
    mc "Anyway, I spoke to Melody and I’ll be working with you guys this quarter."
    mc "So I’ve got your back, literally."
    show re calm with dissolve
    "She chuckles, but stops herself."
    mc "My name’s [mcname] by the way, didn’t get a chance to introduce myself the last time I caught you."
    "She lets a few more giggles escape."
    re "It’s not like I would keep falling if you weren’t so quiet."
    "I hold my hand out to shake. Her grip is gentle and she quickly looks away."
    re "Reina, sorry for being so jumpy…"
    re "Oh right...um…"
    re "Melody asked me to take a look at your past work. Do you have your laptop on you?"
    mc "Right, here we go."
    "I bring up some art I found online the other night. It’s not mine, but I could probably pull off something like it if I tried."
    re "These are pretty good. I mean…it’s not like I haven’t seen better, but this isn’t bad."
    re "How long have you been drawing?"
    mc "I drew a lot throughout high school, practiced whenever I could."
    "It’s not entirely a lie...I doodled quite a bit in math."
    re "Mm, it’s incredible what practice can do."
    "She seems legitimately impressed with ‘my’ work. I just wish what I was showing her was as real."
    show re happy with dissolve
    re "Yeah, this will do fine. I’m looking forward to working with you [mcname]."
    "She smiles, brushing her hair to the side. Slight dimples form at her cheeks."
    mc "(Cute…)"
    show re calm with dissolve
    re "But make sure you carry your weight this quarter."
    mc "Right."
    "I pack up my computer and start heading home. Reina returns to her work. I catch her glancing back at me once or twice."
    hide re calm with dissolve
    mc "(Oh man. How am I going to keep this up?)"
    "I want to get to know Reina better, but I can’t keep lying to her about the art."
    "This can only get worse over time. Maybe I can…? I don’t know…"
    mc "(What was it she said?)"
    "...it’s incredible what practice can do."
    mc "(If I put my mind to it, maybe I can do the work and come clean.)"
    scene bg black with fade
    "Maybe."
    
    #-------------------------------------------

    #First choice: Week 3

    #--black--
    stop music fadeout 1.0
    with Pause(0.5)
    "And thus started my first quarter in VGDC."
    "As expected, the team I'm part of is filled with skilled members."
    mc "(Well, excluding myself of course. But no one needs no know that."
    mc "(... At least, not yet.)" 

    #--Game Room--
    scene bg gameroom with dissolve
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "A week had passed" 
    "Today marks our first ever team meeting, and it went by without a hitch."
    "I bought a drawing tablet beforehand and practiced enough to at least look like I know what I'm doing."
    "Nothing too impressive, just working on minor assets."
    "After what felt like forever, the meeting finally ended, and the group shuffled to get their things together."
    mc "(Reina's getting ready too...)"
    mc "(What do I do?)"

# SCENE 3
#First choice: Week 3
label re_scene3:
    menu reina_option_1:
        "(What do I do?)"
        
        "Ask to talk to Reina":
             #[Option 1- Ask to talk to Reina]
             mc "(This is my only chance...! I’ve got to do it!)"
             mc "Excuse me, Reina?"
             show re calm with dissolve
             re "Hmm?"
             mc "Well, I was just wondering, would you happen to be free right now?"
             "She tilted her head to the side in confusion."
             re "I am, yes... Why?"
             mc "Weeellll you see, I’m kiinda bored, and could use someone to talk to."
             mc "You think you can grace me with your presence for just a bit?"
             show re surprised with dissolve 
             "Reina looked taken aback, and shifted her eyes away from me."
             re "U-Umm... I’m sorry, but, I’m not really all that good company..."
             re "But, uh, you can talk to anyone else here?"
             mc "Hmmm... I could, sure. But I only want to talk to you."
             show re blush with dissolve
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
             show re happy with dissolve 
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
             re "Is it... ‘Putty... lease.. us...?'"
             mc "Snrk.."
             re "What?"
             mc "That makes no sense, Reina."
             re "I-It does to! What is it then?"
             "I cleared my throat and leaned forward, looking her dead in the eye."
             mc "..."
             mc "Bootylicious." #omg kiara you're so lame
             show re happy with dissolve
             re "Pfff-"
             re "Hahaha! And you said my phrase made no sense!"
             mc "Hey, this makes waaaaay more sense than \"putty lease us!\""
             hide re happy with dissolve
             "She laughed, and the day went on like that, with us chuckling over a silly kid’s game."
             "In the end, she left with a grin on her face."
             "I wished to myself that I could keep making her smile like that."
     
     #[Option 2- Work on drawing] 
        "Work on drawing":
            $ re_affection = re_affection + 1
            show md calm with dissolve
            md "What, you staying here, [mcname]?"
            mc "Me? Oh, uh.. yea."
            mc "Just got some work to finish up before the end of the day. Nothing major."
            show md happy with dissolve
            md "Woa, responsible. I like it."
            md "Keep those work ethics up for our project and I just might start respecting you!"
            mc "Haha, sounds like a plan!"
            hide md happy with dissolve
            "They team filed out, and I was left alone."
            "I whipped out my brand new tablet, and started testing out an art program I downloaded the other day."
            mc "(It may not be much, but... Anything is better than nothing.)"
     
     #---------------------------------------------------------------------------------------
    scene bg gameroom with fade
     #Second choice: Week 4
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "It’s another day in the game lab, everyone doing their own thing. George Dan is in the front, leading a workshop on writing dialogue."
    "It sounds somewhat interesting. I listen in while browsing the internet. I’m starving."
    "I see Reina in the corner, it looks like she’s finishing up some work. Maybe she’s got some free time?"
    menu reina_option_2:
        "What should I do today?"
     #[Option 1- Ask Reina out for lunch]
        "Ask Reina out for lunch":
            show re calm with dissolve
            mc "Hey Reina, would you like to go and get some lunch with me?"
            re "Oh, um…I’m not really hungry right now."
            mc "C’mon, my treat. We’ve been working hard, I think it’s a good time for a break."
            "Reina glances back to her work, she’s just finished a character. Suddenly, her stomach grumbles quietly."
            show re surprised with dissolve
            re "Eep! Er, maybe a break would be good, if you’re paying."
            "Before I can make a joke about it, my stomach growls even louder."
            mc "Haha, it seems we’re in agreement here. Let’s go."
            
            scene bg black with fade
            play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
            "We decide to go to one of the food courts on campus."
            scene bg foodcourt_1 with dissolve
            show re calm with dissolve
            mc "So what do you think you’re going to get? I’m gonna get the spicy Italian, got it once and I was hooked."
            re "Oh, actually I was going to get that too. It’s one of my favorites…"
            mc "No way! What a coincidence."
            "She’s looking away, brushing her hair behind her ear. As I glance at her, my thoughts slip from my mouth."
            mc "God, you are so cute."
            show re blush with dissolve
            "Reina blushes a bright red. If she wasn’t looking directly at me before, she was directly avoiding eye contact now."
            mc "(Oh God I said that?)"
            re "You don’t actually mean it."
            mc "No, I do! I wouldn’t lie to you."
            mc "(Er…)"
            mc "...Not about that."
            show re calm with dissolve
            "We get our orders and sit down at a table near a window. It’s a nice day outside."
            mc "So, how long have you been drawing, Reina?"
            re "Hm? Well, I’ve always enjoyed drawing since I was little. I started taking it more seriously towards the end of middle school though."
            mc "Yeah it shows, your work is really good Reina."
            re "It’s not that amazing. But thanks I guess."
            mc "So your middle school and high school, they must have had pretty good art programs, huh?"
            re "Actually I was homeschooled, so yes and no."
            re "We didn’t spend a lot of time on art in class, but in my downtime I drew a lot."
            mc "Huh."
            mc "(I don’t want to stereotype, but maybe that’s why she’s less comfortable talking around people.)"
            "We eat for a while. Reina glances outside, watching some people pass by."
            re "I know it’s a little unrealistic, but I’d like to one day write a webcomic or something."
            mc "That’s awesome! You could totally do that."
            re "Thanks, but it’s a lot of work, and I have a long ways to go till I’m good enough for something like that."
            mc "Well when it happens, let me know how it goes. I’ll be one of the first readers."
            "That gets a small, but warm smile from my lunchtime companion."
            mc "Something I was wondering about, if you don’t mind my asking..."
            re "What is it?"
            mc "How long does it take to dye your hair like that?"
            re "...What do you mean?"
            mc "Your hair, it’s uh… nevermind. It looks really good on you."
            scene bg black with fade
            "We finish up and head back to the game lab."
            scene bg foodcourt_1 with dissolve
            show re blush with dissolve
            mc "Aah, that was a good meal. Was even better because I got to be there with you."
            re "Oh, um, yeah. It was nice."
            re "Maybe, um, we could do it again sometime [mcname]..."
            mc "I’d like that."
            "Reina glances at her phone and notices the time."
            show re surprised with dissolve
            re "Oh no, I’m going to be late to class! I have to run now, bye!"
            re "I had a good time [mcname], make sure you don’t slack off though.."
            mc "Bye Reina, have a good one."
     
     #[Option 2- Work on drawing]
        "Work on drawing":
            $ re_affection = re_affection + 1
            "I shook my head."
            mc "(No, no distractions. I've got to get to work!)"
            "I mentally pump myself up before opening up my drawing software and pulling out my tablet."
            "After a bit of warming up, I get right to it."
            mc "(Straight line. Straight line. Straight line.)"
            "Sketch, undo, sketch undo."
            mc "(How do people do this right?)"
            show re calm with dissolve
            re "[mcname] I think you’re gonna break your Z key."
            mc "Wha?!"
            "I quickly open a new canvas, nearly falling out of my chair in the process."
            show re happy with dissolve
            re "Pffft. Now we’re almost even."
            "She stifles a laugh."
            show re calm with dissolve
            re "I’m sorry."
            mc "Nah, it’s fine. I’m just… uh… warming up a bit before I get to my work on the project. I can’t seem to get my lineart right."
            re "It’s good to see you hard at work. May I see your settings?"
            mc "Uh, sure."
            "She leans up close. I can feel her gentle presence beside me."
            re "If you’re having trouble, maybe you should adjust the stabilizer to help keep your lines straight. Of course, you could just keep at it until you get a steady hand, too.."
            mc "Right. Maybe after warming up some more they’ll be back to normal."
            "Lying again."
            re "Here, try now."
            "Reina takes a step back, and I try drawing a line on the clean slate."
            "Even when my hand gets unsteady, the line comes out a little cleaner."
            mc "Hey, that makes a big difference, thanks."
            show re happy with dissolve
            re "I’m happy to help."
            "She smiles for a moment, then looks away."
            show re calm with dissolve
            re "It’s part of my job after all."
            re "I have to go to class. Keep up the good work [mcname]."
            mc "Will do Reina, see you later."
            mc "(Straight line, straight line, straight line…)"
            "It was really nice of her to help me out there. I hope she isn’t catching on though."

            #---------------------------------------------------------------------------------------
     
     
     #--Aldrich Park--
    scene bg park_1 with fade
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Hahhh..."
    "I set my sketchbook down on the grass and stretched my arms."
    mc "(Geez... How long have I been sitting out on the grass?)"
    "The rest of my classes for the day had been cancelled, so I decided to practice some landscape drawing in Aldrich Park."
    "I'd lost track of time since I got here. The sun's much lower."
    mc "(Ugh... perspective is harder than I thought. Especially when there's a bunch of hills.)"
    "It's a quarter past three, so there aren't many students walking through the park. They're either in a classroom or at home."
    "After scanning the area, I could only see one person within the vicinity."
    mc "(A girl? Oh, now here's a cutie...)"
    mc "(... Hmm? Oh, wait-)"
    mc "(Is that Reina?)"
    
     #Third choice: Week 5
    menu reina_option_3:
        "What should I do?"
     #[Option 1- Ask to hang out with Reina]
        "Call out to her.":
            #[Option 1- Call out to her]
            mc "(I've practiced enough, right? I think I've earned a little break...)"
            "As soon as she came within earshot, I called out to her."
            mc "Heyy! Reina!"
            show re surprised with dissolve
            re "Huh?"
            "Surprised, she faltered a bit before locking eyes with me. I couldn't help but grin."
            re "[mcname]? What are you doing here?"
            mc "Oh, nothing much. Just got a little burst of inspiration after looking at the park and decided to doodle for a bit."
            show re calm with dissolve
            re "Doodle?"
            "Her eyes fell to my sketchbook, closed on the grass right next to me."
            re "That sounds really nice, actually. Do you think I can take a peek?"
            mc "Huh? Oh, um, actually..."
            "I turned to open my bad and put away the sketchbook as passively as possible."
            mc "I'd love to show you, really, but... it turned out waaaay worse than I'd like to admit, haha..."
            re "...? But-"
            "I clapped my hands together and cut Reina off."
            mc "Oh, enough of that! What brings YOU here, hmm?"
            re "Me? Um, well... I was just passing by to get to my dorm."
            mc "Your dorm, huh... Does that mean you're done with classes for the day?"
            re "Umm, yes..."
            mc "That's great news! Now you can chill here with me!"
            show re blush with dissolve
            re "Wait.. what?!"
            mc "Now now, don't be shy. There's plenty of room, come on!"
            "I patted to the spot to my left and smiled at her blushing face."
            "She glanced around her surroundings before hesitantly approaching her spot."
            re "I... guess I could..."
            show re calm with dissolve
            "I cheered as she took a seat."
            "She responded with exasperation, but it was obvious from her features that she was enjoying herself."
            "We talked from there, a bit about video games, and a bit about our own peronal lives."
            "Being there together just conversing felt unbelieveably pleasant. It was as though time eluded us."
            "Maybe it was the warmth of the sun, or maybe being around Reina made me feel that comfortable, but I couldn't help but feel drowsy all of a sudden."
            "I tried to cover up a yawn, but Reina noticed."
            re "You tired?"
            mc "Mmm.. Not at all."
            re "Hehe. Well, just know you can rest, if you'd like."
            mc "Nahh, I'd much rather spend my time with you."
            show re blush with dissolve
            re "O-Oh..."
            "She coughed awkwardly and looked away, red tinting her cheeks."
            re "Umm... Well, I could stay here, if you'd like."
            mc "... Really?"
            "She nodded. I pursed my lips in thought."
            mc "... In that case, hope you don't mind if I just--"
            "I scooted forward a bit before laying down on my side."
            mc "Ahh... That's better..."
            "I took a deep breath and allowed my eyelids to fall close."
            mc "God... The grass is soft, and the sun is warm. I'm just about ready to pass out."
            re "Are you that tired?"
            mc "..."
            re "....? [mcname]?"
            mc "... Hey, Reina?"
            re "Hmm?"
            mc "Wanna take a nap with me?"
            show re surprised with dissolve
            "I peeked up at her in time to see her expression burst in surprise."
            re "!! A... n-nap?!"
            mc "Yea. C'mon, why not, right?"
            re "W-Well, there are lots of things wrong with it!"
            mc "Like what?"
            show re blush with dissolve
            re "...."
            mc "Do you hate me or something?"
            re "...."
            mc "Oh... So you do..."
            re "!! N-No, I don't!"
            mc "Hehe... Glad you were so against the thought, there."
            re "Ngh... I-It's not like I like you or anything, though..."
            mc "Mhmm. I'll take your word for it, Reina."
            re "Humph."
            mc "... But that means, there's nothing wrong with it then, right?"
            re "... What do you mean?"
            mc "Taking a nap with me. You don't hate me, and you don't like me. So there's nothing weird about it, right?"
            re "..."
            mc "C'mon~ Just for a bit!"
            re "Nnn..."
            "After a long moment of hesitation, Reina finally took a deep breath and laid down next to me."
            "She was facing my direction, but her eyes refused to meet my own."
            mc "(She's blushing really hard... How cute.)"
            re "J-Just for a minute, alright?"
            mc "Mhmm. Just a minute."
            "I scooted a little closer toward her. She didn't even flinch."
            "Filled with an inexplicable amount of happiness, I couldn't hold back the smile that pulled at my lips as drowsiness pulled on my eyelids."
            "I wasn't able to catch Reina looking back at me in adoration before closing her own eyes."
            #--black--
            scene bg black with fade
            "Needless to say, we ended up staying like that for much longer than a minute."
     
     #[Option 2- Work on drawing]
        "Stay focused.":
            #play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
            #Option 2- Stay focused]
            $ re_affection = re_affection + 1
            mc "(Ngh... As much as I want to...)"
            "I sighed and turned my back to the pathway so I faced away from her."
            mc "(I'm getting better, little by little. I can't stop now.)"
            "After pumping myself up a bit, I picked up the skecthbook at my side."
            "The sun supplied light, the park provided inspiration, and the guilt at the pit of my stomach dispensed endless encouragement."
            "So I kept at it, completely oblivious to the attention I was getting."

            #------------------------------------------------------------------------------------------
     
     
    scene bg black with fade
     #Final choice: Week 6
    menu reina_option_4:
        "What should I do today?"
     #[Option 1- Invite Reina over to your room]
        "Invite Reina over to my apartment.":
            #Final choice: Week 6
            #[Option 1 - Invite Reina to the Apartment]
            scene bg gameroom with dissolve
            play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
            "It’s a little later in the evening in the game lab. A small group of officers have left to get some dinner."
            "It seems like one of them didn’t go along."
            show re calm with dissolve
            mc "Hey Reina, why didn’t you go along with the other officers?"
            re "Oh, I wasn’t hungry. Besides, I prefer to be by myself."
            "She glances away."
            show re blush with dissolve
            re "And maybe with…"
            "I couldn’t quite hear the last part."
            mc "Hm?"
            show re calm with dissolve
            re "Oh, nothing."
            mc "Alright, well I’m going to head home for the day."
            re "..."
            mc "Hey...Reina?"
            re "Yes?"
            mc "This is going to sound kind of dumb,  but do you want to come along? Just hang out at my apartment for a while? It might be nice to unwind a bit, you’ve been working all day."
            show re blush with dissolve
            "She seems a little flustered at the question, but I can hear a quiet response."
            re "I’d like that."
            #The two go to the apartment.
            scene bg mc_apartment_inside with dissolve
            show re calm with dissolve
            play music "/Audio Dumpster/Piano Solo 1.mp3" fadeout 1.0 fadein 1.0 loop
            mc "So, here’s my apartment, the grand loft."
            "I cleaned up earlier, so the place wasn’t too messy. My roommates had left some dishes in the sink though."
            "A few desks line the walls of a medium-sized living room. It’s not the most organized, but it’s a welcoming place."
            "Reina sits on the couch. She seems out of place there, a beautiful person in a quaint apartment."
            mc "Want anything to drink?"
            re "No thanks."
            "She hesitates for a moment."
            re "Your apartment is pretty nice."
            mc "Yeah, it does what it should as your standard school housing."
            "I left some music playing on my computer. It’s quiet, basically just some background noise."
            "I sit down next to her, not too close though."
            mc "I’ll be completely honest, I didn’t plan this far. What do you want to do?"
            re "Um, I’m not sure. We could just...talk like this. This is nice."
            mc "I didn’t expect you of all people would want to talk."
            show re blush with dissolve
            re "No, but I… I don’t know."
            re "I feel like when I’m around you…"
            re "Like, when I’m with Melody, it’s hard to find the words. She’s always so loud and forward."
            re "But with you, I feel like I can talk, and no matter what I say, you’d listen."
            re "Um, yeah."
            mc "I’m glad you feel that way, Reina."
            show re calm with dissolve
            play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
            "One of my favorite songs starts playing and I get an idea."
            mc "Oh, this song is great. Come on, let’s dance!"
            "I turn up the volume, then gently grasp Reina’s hands and pull her to her feet."
            show re happy with dissolve
            re "Pfft, I don’t know how to dance [mcname]!"
            mc "You think that I do? Relax, just move with the music."
            re "You idiot! You better not step on my feet [mcname]!"
            "We step and sway as the song continues. Neither of us really know what we’re doing."
            "Reina and I laugh as we swing along."
            "Our dancing is an odd mix of imitating the movies and bobbing around."
            "And just like that, with her hand in mine, Reina spins and lands right in my arms."
            "Her deep green eyes gaze into mine. Her thin smile with dimples on the sides softens a little."
            show re calm with dissolve
            re "I uh…"
            mc "Heh, you must really like me or something. Coming to my apartment, agreeing to dance."
            show re blush with dissolve
            re "I-I-I do not! I just needed to take a break."
            "I lean in a little closer."
            mc "Are you sure? You don’t sound all that convinced."
            "Just then the music ends and the player turns on a loud advertisement."
            show re surprised with dissolve
            re "Ah!"
            "In her surprise, Reina manages to trip on my foot. Thankfully, I catch her before she falls."
            mc "Looks like I’ve got your back, again."
            re "Oh wipe that dumb grin off your face."
            show re blush with dissolve
            re "I-I might like you...a bit."
            "We embrace, her hands gently alight on my back as the ad plays on. I could hold this moment forever."
            "I only realized later that when I had turned up the volume on my computer, a certain piece of my ‘original’ work showed up on my screen for just long enough."

     
     #[Option 2- Work on drawing]
        "Practice drawing.":
            #[Option 2 - Practice Drawing]
            $ re_affection = re_affection + 1
            scene bg gameroom with dissolve
            "It’s a little later in the evening in the game lab. A small group of officers have left to get some dinner."
            "Unfortunately, one of them didn’t go along."
            show ax calm with dissolve
            play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
            ax "Wow [mcname], I never took you for the artistic type."
            "I’m trying to finish some backgrounds for the project. It’s been getting easier, when Alex isn’t around."
            mc "I doodled in high school."
            ax "Yeah, but that doesn’t get you into a product based project in your first year as an artist."
            mc "A lot can happen in four years."
            mc "(Dude, just leave me alone… I know I’m not doing the best, but I’m trying.)"
            ax "True, true. Your backgrounds are looking pretty good, not going to lie."
            mc "(Really?)"
            mc "Oh, thanks."
            mc "(Backgrounds are one thing, but I still need to work on the art and animations for a few npc’s. That’s going to be rough.)"
            ax "Anyway, I never thought you’d join Melody’s team of all people."
            mc "What do you mean?"
            ax "Ah, well, she’s… she’s quite something."
            ax "She’s pretty cute, no? I keep trying to chat with her, but she won’t give me the time of day."
            ax "Of course, she’s not the only cute girl on the team, huh? Reina’s pretty nice, too."
            mc "Yeah…"
            show ax happy with dissolve
            "Alex smirks."
            show ax calm with dissolve
            ax "She’s a bit quiet though."
            mc "She is, but when she smiles, man."
            ax "Must take someone pretty special to get her to open up, huh?"
            mc "I don’t know, but… wait a minute, why am I even talking to you about this?"
            ax "Haha, face it friend, you’ve got a crush on her."
            mc "Shut up, don’t you dare talk to anyone about this."
            ax "Wait wait, how bad is it? You ask her out yet?"
            mc "Leave me alone Alex, I have work to do."
            ax "Oh, it’s bad alright. You like her."
            ax "Wait, don’t tell me. You joined the team just to get close to her. I’m right aren’t I?"
            mc "(Just going to keep working on this background, maybe he’ll leave.)"
            ax "Oh you hopeless romantic. And you thought I was bad? You’re a natural Romeo, a Cyrano, a lover just looking for the right time and place."
            mc "Alex, unless you want to be the next Tybalt, I would let me work if I were you.."
            "Respectfully ignoring my words, Alex proceeds to playfully bob my chair back and forth."
            ax "You like her, you do. You really really like her!"
            "At that moment, the lab door opens and one blue-haired art officer walks in on the two of us."
            show ax calm:
                linear 0.5 xalign 0.2
            show re calm with dissolve
            show re calm:
                linear 0.5 xalign 0.8
            mc "Reina! Hi."
            show re blush with dissolve
            re "..."
            "Lightly blushing, she leaves as suddenly as she came in."
            hide re blush with dissolve
            show ax calm:
                linear 0.5 xalign 0.5
            ax "Don’t worry, your secret is safe with me [mcname]."
            hide ax calm with dissolve
            "With a wink, he leaves, heading out the door."
            mc "(I sure hope he doesn’t say anything.)"
            "Unfortunately, there’s still a lot to be done for the project."
            mc "(Ugh, what a mess I’ve gotten myself into.)"
     
    if re_affection >= 3:
        jump re_good_ending
    else:
        jump re_bad_ending
     
     #[[GOOD ENDING]]
label re_good_ending:
    scene bg sturbacks with fade
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "I'm midway into week six, and three weeks into Melody's game project."
    "I've spent as much time as I could practicing art and animating, but there's only so much I can get done in this much time."
    mc "(This... was definitely a mistake.)"
    "I was inside the coffee shop in the Student Center working on character design."
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
    re "[mcname]. Um… Can I sit next to you?"
    mc "Huh..? Sit next to me?"
    mc "Um, sure. Go right on ahead."
    "Reina pulled back the chair to my side and took a seat." 
    re "So, what have you been doing up until now?"
    mc "Hmm? I’ve just been browsing around, I guess. Nothing too productive."
    re "Browsing…"
    "She then peered into my laptop screen."
    re " ...‘An Introduction to Animation’...?"
    "(Oh crud, I forgot to close out my art tabs--)"
    mc "Uh, yea. I’ve been… browsing for a good article to reference this one high schooler to!"
    re "..."
    mc "Apparently they saw my work and got super inspired. Wanted to create something of their own. But, I’m not much of a teacher myself, so I’ve been looking for a good tutorial to send to them."
    stop music fadeout 1.0
    re "For the past 4 hours…?"
    mc "..."
    mc "... huh..?"
    "Reina stared straight at me, her emerald eyes boring into my own."
    mc "Wait, Reina, how long have you-?"
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    re "Long enough to know that you’re lying to me."
    mc "?!"
    re "But, the real questions is: are you just lying to me, here and now?" 
    re "Or... have you been lying to the whole team, for the past 3 weeks?"
    mc "..."
    "She’s caught on."
    "I gripped the base of my chair firmly, and faced her gaze head on."
    mc "(...Dang. What the heck do I do?)"
    "We’d been staring at each other for what felt like an eternity, but those eyes never wavered. Not once."
    mc "... Heh"
    re "..."
    "I leaned back on my chair and let out a dry chuckle, breaking eye contact."
    mc "Looks like I’ve been caught, huh…"
    re "..."
    "I could see Reina stiffen just a little, but overall, she seemed largely unfazed."
    mc "Alright, the jig is up. I never was an art prodigy, not that it was any surprise to you apparently."
    re "...Yea."
    mc "Heh..."
    mc "You're pretty amazing, you know. How were you able to figure it out? I thought I did a pretty good job faking it."
    re "Good job..? No, not at all."
    mc "Oh?"
    re "..."
    "Her eyebrows scrunched up, and she finally broke eye contact with me."
    "Curious, I turned in my chair to face her and leaned in ever so slightly."
    "After a few seconds, she took a deep breath and faced me."
    re "Whenever we have our team meetings, you'd always stay much later than the rest of us and just draw."
    re "Not only that, but I'd see you around here a lot with your tablet, too."
    re "At first, I didn't think much of it. \"He's just working on homework or his projects,\" I'd think."
    re "But as I kept looking at you throughout the week, you always looked so serious and... frustrated."
    re "I couldn't help but think something was off when a 'prodigy' worked so hard for so long, and never even once seemed happy."
    mc "Hmmm... so that gave it away, huh?"
    mc "Heh... guess I should've looked around more."
    "I sat there, a wry smile on my face, just looking up at the ceiling."
    mc "(Right now, Reina is confronting me.)"
    mc "(Reina, the girl that could barely speak to anyone without crumbling down into a blushing, stuttering mess, is confronting the truth.)"
    mc "(All I've been doing these past three weeks is run away from it...)"
    re "..."
    re "[mcname], please. Be honest with me."
    mc "..."
    mc "I'm... sorry."
    "I took a deep breath and bowed my head at her, putting as much sincerity in my words and actions as I could."
    mc "You're right. I'm no artist, much less a prodigy of any sort."
    mc "I lied so I could get placed in the same team as you." 
    mc "I didn't think much of it when I did it, but as time went on, this awful feeling started building up in my gut."
    mc "I thought I'd be fine if I could learn how to draw and pick up a few skills, but I severly underestimated just how difficult that was."
    mc "Then... things just went downhill from there. As much as I could, I practiced and practiced."
    mc "As time went on, I realized my efforts were in vain. There's just no learning these things over night."
    mc "But even still... I just couldn't bring myself to confess."
    re "[mcname]..."
    mc "Heh. I'm sorry, I really hope you're not feeling sorry for me right now."
    mc "I know you're a nice girl, but I wouldn't hold it against you if you hated me right now. In fact, I deserve it."
    re "... You're the worst."
    re "Deceit on top of plagiarism. What you did was awful, and there's no doubt you deserve to be punished accordingly."
    "Up until this point, Reina has been relatively calm and emotionless."
    "Now, I could hear her voice shake slightly with each word."
    re "Ngh..."
    re "But even still, I... I just can't hate you."
    mc "...Huh?"
    "I lifted my head to look at her, eyes wide open in bewilderment."
    mc "But... why?"
    re "Well..."
    re "You worked... hard."
    mc "..."
    re "Day after day, I saw you work so hard."
    re "Sometimes you were serious. Other times you were frustrated. Every now and again you'd even look a bit sad."
    re "But no matter what kind of expression you had on your face, you were always working diligently, trying hard to improve."
    re "There's just no way I could hate someone like that."
    mc "Then... Then does this mean-?"
    re "I don't forgive you, and I'm still angry at you."
    re "You're going to have your current tasks stripped from you and you'll be confessing to the whole team within the week."
    mc "(Ouch. Don't know what I was expecting there.)"
    mc "Y-Yea, of course. That's to be expected."
    show re blush with dissolve
    re "... But, afterwards, I wouldn't mind... teaching you myself."
    mc "(?!?)"
    mc "H-Hold on. Are you serious..?"
    "Reina looked away sheepishly and nodded. I gawked in response."
    mc "But... why?"
    show re calm with dissolve
    re "W-Well... you may have done something bad, but you're not a bad person. At least I don't think you are."
    re "I... I want to try trusting you. A-And maybe, getting to know the real you, and not some made up prodigy."
    mc "..."
    mc "G-Geez... hah. I, I can't believe this is happening."
    re "D-Don't let it get to your head though! It's not like it's anything special or anything, and you're still not off the hook for everything you did!"
    mc "Oh no, I know that! Trust me, I do!"
    mc "I swear I'll work hard to make up for my mistakes!"
    mc "Once I've redeemed myself, I look forward to working with you. I really, really do."
    re "Hmph. That's more like it."
    "With a pout and her chin pointed upward slightly, I knew Reina was trying her best to seem upset."
    "Though, she couldn't hide the red that brushed her cheeks nor the slight smile that pulled at her lips."
    mc "(It may have been a rough start, but maybe there's still hope for a happy ending after all.)"
    scene bg black with fade
    ".:. Good Ending."
    stop music fadeout 1.0
    return

    #---------------------------------------------------------------------------------------------
     
     
     #[[BAD ENDING]]
label re_bad_ending:
    scene bg gameroom with dissolve
    "The game lab is mostly empty today."
    "I’m playtesting our project for a bit when the door to the lab slams shut."
    show md angry with dissolve
    md "[mcname], we need to talk pal."
    mc "(Gulp)"
    "Melody takes me outside. Reina is waiting for us."
    show md angry:
        linear 0.5 xalign 0.2
    show re calm with dissolve
    show re calm:
        linear 0.5 xalign 0.8
    "She seems to be on the verge of tears."
    re "The art you showed me at the beginning, it wasn’t yours was it."
    play music "/Audio Dumpster/Bad Ending.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Uhh…"
    md "Well?"
    "The two of them stare me down. No amount of lying or excuses can get me out of this one."
    mc "Yeah, I stole it. I lied and passed it off as my own. I just really wanted to be on the team."
    md "Un-flipping-believable."
    mc "I’m sorry."
    "I turn to Reina."
    mc "Reina, I didn’t mean to do any harm. I’m really, really sorry."
    re "You idiot! It’s not just that, you lied to us! You lied to me…"
    mc "I…"
    mc "Reina, you know me, I would never try to hurt you."
    re "Do I know you? What else did you lie about? Does the project even matter to you?"
    re "...Do I even matter to you?"
    mc "(Of course you do!)"
    mc "No, I--"
    mc "Reina, I’ve got your back. You mean the world to me."
    re "I’d rather you just let me fall that day instead of letting me down here like this.."
    re "What could you possibly have wanted so much that you would ruin your integrity like this?"
    "I hesitate. Before I can answer, she storms off."
    hide re calm with dissolve
    mc "(I wanted to be with you…)"
    show md angry:
        linear 0.5 xalign 0.5
    "I try to follow her, but Melody stops me."
    md "You’re in deep trouble, pal."

    #//Timeskip to later, main character is talking to Alex in the park
    scene bg park_2 with fade
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    "Because of my plagiarism, they kicked me off the team."
    "The president was going to drop me from the club entirely and report my actions, but someone convinced him to let me off with a stern warning."
    "I can’t join another team for the rest of the year, that’s not too bad."
    "But I don’t know if I can ever face Reina again, and that punishment will last forever."
    mc "So that’s where I am right now."
    show ax calm with dissolve
    ax "Wow."
    ax "You really messed up, my friend."
    mc "Yeah…"
    "Alex and I laying in the grass in Aldrich. I just really needed someone to talk to."
    mc "I have to wonder if things might have gone down another way if I had done things differently."
    mc "In any case, thanks for putting in a kind word to George. It means a lot that you backed me up there."
    show ax happy with dissolve
    "Alex smirks."
    ax "You know I’m happy to stick up for you…"
    ax "But it wasn’t me that had your back in the meeting."
    mc "Huh?"
    show ax calm with dissolve
    ax "Your guardian angel was someone else. Speak of the devil, here she comes."
    hide ax calm with dissolve
    "A blue-haired girl walks over to the two of us. If she were smiling, she’d have dimples."
    "I jump to my feet."
    mc "Reina."
    show re calm with dissolve
    re "It’s not like I forgive you, I don’t."
    mc "I’m sorry, I really am. I’ll say it a thousand times and a thousand more."
    "She continues."
    re "I liked you, I trusted you. But you lied to us just to join the team?"
    re "See this as a learning experience, practice. Make yourself better from the time you spent with me."
    re "After all, that’s all I was to you in the end."
    mc "That’s not…"
    re "I wish you luck in the future with VGDC, but I never want to talk to you again."
    re "Good bye."
    scene bg black with fade
    ".:. Bad Ending."
    $ MainMenu(confirm=False)()
    #return