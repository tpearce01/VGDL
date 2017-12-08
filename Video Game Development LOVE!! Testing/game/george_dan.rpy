#DIALOGUE : 
#Scene 1: 
#setting:lecture hall
label gd_scene1:
    scene bg meeting_1 with dissolve
    mc "(So he's the guy I bumped into earlier...)"
    show gd calm with dissolve
    gd "Oh yeah, one more thing. This first meeting may not be too exciting, but I promise you that there will be invaluable experiences to gain,many joyous moments to come, and new friends to share those moments with."
    gd "So with that said, I hope that you will enjoy your journey here to the fullest."
    mc "(The way he speaks... it’s so familiar, but I can’t recall what it is.)"
    mc "(The way that he is able to captivate the audience...)"
    mc "(There is a weird, but definitely familiar feeling about him that that perplexes me and I can’t seem to figure out!!)"
    mc "(For some odd reason I can't stop gazing at him.)"
    mc "(He’s so cu...I MEAN ODD. Yes, very odd...)"
    hide gd calm with dissolve
    mc "(Oh well, I shouldn’t think too much about it. Too much curiosity is always troublesome.)"
    mc "(HUH?! Something poked me.)"
    show ren calm with dissolve
    ren "Hey, I didn't expect to see you here!"
    "This is Ren. I haven't seen her since high school, but she was like my bigger sister back then in high school. Always protecting me and taking care of me."
    mc "Ren! It's been awhile!"
    ren "Yeah, it has been awhile. I've missed you kiddo."
    ren "So how do you like it here so far?"
    mc "I like it a lot! The weather is nice, and the people are friendly!"
    ren "Anyway, I see that you are here now, so does that mean you are planning to join VGDC?" 
    mc "Yeah I was at their booth earlier and I wanted to check out their first club meeting."
    ren "You should definitely join!"
    ren "Are you going to pitch a game idea for the next meeting? I think you should!"
    mc "Yeah, I'm considering doing it, but will I have enough time or the ability to run a whole team?"
    ren "I believe you can do it. You are more than capable! And don't worry, if anything, I’ll personally be here to help you out."
    mc "Thanks Ren, I’ll definitely consider it now."
    mc "(I really do miss talking to Ren.)"
    mc "At that moment I saw him coming up towards us and Ren started to walk down towards him."
    show ren calm:
        linear 0.5 xalign 0.7
    show gd calm:
        xalign 0.3
    with dissolve
    gd "Hey Ren, I need to ask you something, can you come with me?"
    ren "Yeah, I can, but what's up with the speech? You know this was only a VGDC meeting, not a presidential inauguration... Who are you trying to impress anyway?"
    gd "I must make sure that the new members know how cool I am."
    ren "That's pretty...cringe."
    gd "Anyway come with me for a sec."
    ren "You got it..."
    hide ren calm with dissolve
    hide gd calm with dissolve
    mc "(So Ren knows him huh? Here’s my chance to have my curiosity satisfied! This is perfect!!)"
    mc "HEY YOU!!"
    mc "(...Wait where did they go?)"
    mc "(Why did everyone turn their heads? Is there something interesting behind me?)"
    crowd "?..."
    mc "(EHHH? WHY ARE THEY STARING AT ME?! WAS I THAT LOUD??)"
    mc "(I HAVE TO GET OUT OF HERE!!)"
    crowd "Who was that?"
    crowd "That was pretty weird.. Who was [they] calling for?"   
    crowd "Hey! Maybe [they] was calling for me because [they] thought I was cute!"
    crowd "No fool, you’re ugly."
    crowd "Waah... you’re so mean."
    return
    
#Scene 2:
#Setting: MC’s Apartment
label gd_scene2:
    scene bg mc_apartment_inside with fade
    mc "That was the most... EMBARRASSING MOMENT OF MY LIFE!!!"
    mc "That was so embarrassing. Everything felt so embarrassing!!"
    mc "Okay. Okay. Focus... I have to calm down and get work done. Get over it, let the past me worry about what happened."
    mc "Okay... time to get work done."
    "..."
    mc "(Uh...now I’m getting really hungry and I haven’t eaten anything all day too. But the meeting ended so late so I didn’t have time to make food.)"
    mc "Life at college..."
    "(your phone rings)"
    show phone with dissolve
    mc "Hello? Dad?"
    dad "Hi my wonderful child, it’s your amazing dad here. How was your first few days at school so far?"
    mc "I’m hungry..."
    mc "And you sound happy today, did something happen?"
    dad "Nothin’, your mom and I just had our anniversary today."
    dad "Oh yeah, if you’re hungry, there’s food in the fridge. We came up to your area to eat for our anniversary, and we dropped by to say hi, but you weren’t there so we just dropped off some food for ya."
    mc "No way?! You are officially my favorite dad!"
    dad "I am your only dad..."
    dad "But your fridge is pretty empty! You need to take care of yourself and be more responsible for your health!"
    mc "Yeah dad, I know. I’ve just been a bit tight on my schedule, but I’ll be sure to stock up the fridge with food later."
    dad "You know that boys won’t want you if you’re as skinny as a stick."
    mc "... No comment."
    dad "Talking about boys, did you find a boyfriend yet?! Or maybe a girlfriend..?"
    mc "...NO COMMENT!!"
    dad "Hahaha, I’m joking of course."
    mc "Oh yeah, there’s this boy, it’s weird, but I get a very familiar feeling coming from him as if I know him from somewhere long ago."
    mc "Do you think I should ask him about it?"
    dad "I knew it!! There’s a boy HAHAHA. It’s been a week and you already found someone."
    mc "...Seriously, you’re an annoying boy stuck in an old man’s body. AND I DON’T LIKE HIM, I JUST WANT TO KNOW HIM!!"
    dad "I'm only joking! And yea if he makes you that curious, then you should definitely meet him."
    mc "Anything else you want to say old man?"
    dad "I just want to say, firstly, good luck with school and keep warm, the weather is getting colder."
    mc "Thanks dad...Tell mo..."
    mc "He... JUST HUNG UP ON ME?"
    hide phone with dissolve
    mc "That rotten old man! Didn’t even let me finish my sentence and just hangs up on. What kind of dad does that..."
    "I headed to the fridge and grabbed the food that my parents brought for me."
    mc "Thanks Mom and Dad..."
    mc "After I finished eating, I took off my clothes, got into my bed, and put on my headphones. The soothing music starts to play, as I begin to do some of my homework."
    "Eventually, my eyes start to tire. I put my work aside, laid down on, looked at the window, and as I listened to the music, his voice...started to run through my mind.)"  
    mc "(I really want to ask him...)"
    mc "(Hey... you...)"
    "(*Beep Beep Beep*)"
    with fade
    mc "OH SHOOT!! IT’S 8:15!"
    mc "(I won’t make it to my 8 a.m class!! Damn... I forgot to set my alarm.)"
    "Disappointed and sad, I slammed my head back into my pillow."
    return

#Scene 3: 
#Setting: Anywhere on Campus
label gd_scene3:
    scene bg studentcenter_2 with fade
    mc "(I missed my first class class today, but that’s okay. The notes are online so I should be fine.)"
    mc "(What terrible luck... Whatever, I should find a place to study now.)"
    mc "(Oh! I know where! Ren told me that Ayala Library is a great place to study and I haven’t been there yet either.)"
    mc "(I think it should be around here somewhere...)"
    mc "(Oh! I see it. Wow, it looks so nice from the outside...)"
    with hpunch
    "Suddenly I bump into someone."
    unknown "Oh, sorry. My apologies."
    mc "Oops! Sorry, let me pick up the water bottle for you..."
    mc "(As I return the water bottle, I look up and the person that I bumped into is none other than him!! The president of VGDC.)"
    mc "(What should I do or say?!)"
    menu gd_menu1:
        "(What should I do or say?!)"
        #[Player Options 1]
        "Hand back the bottle,say nothing, and walk away": #(worst)
            "I immediately hand back the bottle and nervously walk off without saying a word."
            gd "Thank y..."
        "Get dramatic and tell him that he’s the worst kind of guy":  #(middle)
            mc "Wait a minute, why am I, a girl, picking up the bottle for you who obviously bumped into me??"
            mc "(WHAT AM I SAYING?! THIS IS NOT ME.)"
            gd "My apologies. You picked up my bottle so fast that I didn’t even have time to react."
            gd "Thank you very much though."
            mc "(He looks so tall and handsome close up... Wait what?)"
            mc "Uhhh you’re the worst kind of guys, just make sure to not get in my way next time Hmfph!"
            mc "(Next time?! What am saying!?)"
            "I start to quickly walk away."
        "Pretend to accidentally trip and sees if he catches you": #(best)
            mc "Here’s your bott..."
            "As I return the bottle to him, my legs start to feel weak. Suddenly, as if a ghost had possessed me, my legs stumble and I fell toward him."
            gd "Oi, Are you okay?"
            "My mind went blank and I just blocked out all the noises. The only thing that I can think of is how his arms are holding onto mine."
            mc "(He's so warm and his hands are soft. He smells nice too... Wait what?)"
            "Suddenly, I snap out of my delusional state and realize what had just happened."
            mc "Hahaha! I’m very sorry!"
            gd "It's oka..."
            "After nervously apologizing, I got up and quickly walked away."
    
    #cut
    #Setting: Outside
    scene bg park_1 with dissolve
    mc "I can’t believe that just happened!! That was extremely awkward..."
    mc "(Why did I do that... At first I wanted to meet him, and when I met him, I become a nervous wreck.)"
    mc "(It’s okay! It’s over now. I need to focus and get some work done.)"
    #Setting: ayala
    scene bg library_1 with dissolve
    mc "(This library is so nice. It looks so modern and it feels so comfortable.)"
    mc "(Hmmm, now to find a table to sit at... oh there’s another room in here.)"
    "I sat down and then as I unpack my stuff, I look across from me and he was there again!"
    show gd calm with dissolve #Maybe?? Consider an expression where he's not looking
    mc "He’s reading his book so he doesn’t notice me yet. What should I do?!)"
    "I quickly hid my face behind my textbook before he could notice me."
    mc "(Okay, no problem. This is fine. It’s not awkward at all. We’re just two people studying at the same table.)"
    mc "(A few minutes pass by as I try to study.)"
    mc "(This feeling is so tense... how am I supposed to focus?! I wonder if he’s looking at me. Should I peek to see if he is or should I just leave??)"
    menu gd_menu2:
        "(This feeling is so tense... how am I supposed to focus?! I wonder if he’s looking at me. Should I peek to see if he is or should I just leave??)"
        #[Player Options 2]
        "Definitely peek": #(best)
            mc "(Okay. Just a really, really brief peek.)"
            "(you peek at him)"
            mc "(Wow.... His face, resting gently on his silky fingers. He looks so elegant...)"
            mc "(STOP PEEKING THIS IS NO TIME TO CHECK HIM OUT!!)"
            mc "(You’re right myself... but I must peek again!!)"
            mc "(He’s not looking at all, or maybe he is indirectly looking and he can actually see me peeking at him! This guy is so sly.)"
            mc "(AH! I know a way to test this.)"
            "I gently put my book down, with my face looking down. I then softly yawn."
            mc "(If he yawns then that means that he’s definitely looking at me! Hehe, I’m a genius!)"
            "He then yawns almost instantly!"
            mc "HA I KNEW IT!"
            "(gd gives a slight chuckle)"
            mc "(Did he just smirk at me?)"
            "Before I noticed, the people in the room were all staring at me except for him."
            mc "(Wait... Why is everyone looking at me?)"
            mc "(OH NO, I DID IT AGAIN!! ME AND MY BIG MOUTH. I NEED TO LEAVE.)"
            "(You quickly exit the room.)"
            mc "(That was so embarrassing! I got played by that fool!!)"
        
        "Hell no, get the heck out of there!!": #(worst)
            mc "(I can’t believe he’s here again. I’m definitely leaving.)"
            "I get up and leave"
    
    #cut
    #library
    scene bg library_2 with fade
    mc "(That guy thinks he’s so cooool, but he’s so annoying and that dumb smile of his...)"
    mc "(I need to get back on track though and study...)"
    mc "(I’ll definitely get him back for this.)"
    "I studied for awhile until I was caught up."
    mc "(I think that’s enough studying for today. I caught up with my class so that’s a relief.)"
    mc "(I’m getting kinda hungry though. Oh yeah, VGDC is having a fundraiser and they’re selling food at their booth.)" 
    mc "(I should drop by and support them. Maybe Ren will give me a discount hehe.)"
    mc "(Hopefully he’s not there running the booth or something. I can’t stand seeing him again.)"
    #outside anywhere
    mc "(I think the booth is on ring road somewhere... )"
    mc "(Oh there it is!)"
    "I walked towards the VGDC booth."
    show ren calm with dissolve
    ren "Hey! What the? Why do you look like a starving child! I can’t have that. Here, take this. I already paid for it"
    "Ren handed me a plate full of freshly made food!!"
    mc "Ren... thank you so much!!!"
    ren "Hahaha, no worries kiddo."
    mc "(For some reason, I had a feeling that he was going to be here, but thank goodness he’s not.)"
    mc "(What am I saying?? Why should it matter to me if he’s here or not.)"
    mc "(Anyway, I kinda wanna get some exercise today. I wonder if there’s a park near by.)"
    mc "Oh by the way Ren, is there a park near here?"
    ren "Yeah, there’s a park one mile going that way. Are you planning to chill there?"
    mc "Yeah, I had a long, stressful, and embarrassing day."
    mc "Okay thank you Ren, I’m going to head over there, and thank you for the food!"
    ren "No problem kiddo."
    mc "(The park is on the way to my apartment, that’s perfect.)"
    hide ren calm with dissolve
    #player’s apartment
    scene bg mc_apartment_inside with irisin
    mc "(Let’s see... I should change first into something more comfortable.)"
    mc "(Okay, that’s done, now I just need to grab my basketball and then I can head to the park.)"
    
    #park
    scene bg park_1 with dissolve
    mc "(This park is amazing, there’s even a pond here! It’s so empty and quiet. Everyone must be too busy with school to have time to come here.)"
    mc "(The quietness of the park creates such a relaxing atmosphere compared to the liveliness on Ring Road...)"
    mc "(But sometimes I do prefer the solitude that quietness brings.)"
    mc "(Wait... There’s actually someone here. Who is that over there?)"
    mc "(Aww, that’s cute. It seems like they’re feeding the ducks.)"
    mc "(No freaking way, it can’t be... It’s him again!? Why is he always at the same place that I am. Is he stalking me??)"
    mc "(Should I confront him this time?)"
    menu gd_menu3:
        "(Should I confront him this time?)"
        #[Player Options 3]
        "Yes, and make sure you show him who’s boss": #(Best Choice + Bonus)
            "I walk up to him to confront him."
            mc "Hey you!!"
            "He then looks at me."
            mc "(Oh crap! Maybe this is a bad idea. It’s too late now though!)"
            mc "Why are you stalking me? You’ve been following around the whole day!"
            mc "What is your purpose!?"
            gd "Oh, it’s you, the one that yelled out loud at the library."
            mc "I DID NOT DO..."
            mc "So you ARE stalking me!!"
            gd "I mean... I can’t be the one stalking you if I’m always the one here before you."
            gd "So are YOU stalking me?"
            mc "(He’s smiling at me! He’s ridiculing me! This guy pisses me off so much!!!)"
            mc "Why you..."
            mc "So you do notice me!"
            gd "Of course I would notice my stalker."
            mc "(I swear this guy’s only job in life is to piss me off.)" 
            mc "I’ll make you eat your words you smart ass!!"
            mc "Play me one on one in basketball. If I win, you leave here immediately!"
            gd "That’s fine. And if I win, you tell me your name, Stalker."
            mc "(That smirk of his, I’ll make sure to slam this ball onto his face.)"
            "With force, I pass the ball to him."
            mc "Here! Take this. You start."
            gd "Nice pass."
            gd "Are you ready?"
            mc "(Yeah, I’m ready to kick your ass.)"
            mc "(As I nod my head, a faint clap of thunder passes by.)"
            gd "Thunder..."
            gd "Hey, I guess we’ll have to postpone our game."
            mc "(DAMN IT! Is it really going to rain. Cursed luck, I didn’t even bring an umbrella either.)"
            mc "(Actually, if I run, I might be able to make it back before the rain hits!)"
            mc "(What the?! It’s raining already! What a splendid day... It couldn’t get any worse.)"
            mc "(Something is covering me from the rain...)"
            "He's holding an umbrella over my head."
            mc "(This guy... what does he want. He’s probably going to ask me if he can walk me home.)"
            gd "I’ll walk you home."
            mc "(Who does this guy think he is?? He didn’t even ask me, he just demands that I walk home with him.)"
            mc "No thanks. I’d rather stay in the rain."
            gd "Then I will stay here in the rain, together, with you."
            mc "(Huh??..."
            "Unexpected were his words as I turned my head to look at him."
            mc "Who... is this guy."
            
            #settings: road?
            "It was turning night. We walk home in silence as the rain falls. The sound of the rain brought a soothing quietness, but it did not bring solitude." 
            "He stood next to me, with his umbrella above us as we walk through our reflection on the concrete."
            "(he quietness wasn’t awkward between us, but instead it felt... comforting, as if two friends had reunited after years of isolation..."
            "No words needed. The sound of the rain spoke for us."
            "Once we arrived in front of my place, I turn to look up at him."
            mc "Uh-um.. Thanks for walking me home."
            "He looks me in the eyes and smiles."
            "As I turned around, I can see that annoying but beautiful smile of his from the corner of my eye."
            gd "By the way. May I ask for you name?"
            #[Player Option 3.1(bonus)]
            menu gd_menu3_1:
                "Run at him and whisper in his ears": #(1st best)
                    "I turned around and walked up to him. With my hands on his shoulders I whispered...)"
                    mc "My name is [mcname]."
                    gd "[mcname]..."
                
                "Nah. You haven’t beaten me yet.": #(2nd best)
                    mc "You haven’t beaten me yet."
                    mc "(I turn around and smile.)"
                    mc "My name is [mcname]."
                    gd "[mcname] ..."

                "Tell him your name from afar": #(3rd best)
                    mc "My name is [mcname]."
                    gd "[mcname]..."
                    #inside prot apartment
                    show bg mc_apartment_inside with fade
                    mc "(It’s so cold in here!! I need a warm bath so badly!)"
                    "I turn on the heater and headed for the showers."
                    mc "What an eventful day today... "
                    mc "(He’s... he’s actually not as bad as I thought. Thinking about the events that happened within the last few hours, I couldn’t help but to smile.)"
                    mc "This bath feels so good!"
                    mc "Oh right! Pitch day is coming soon, I need to come up with a game idea soon..."

        "Nah, just play ball and ignore him": #(Worst Choice) (3.2)
            mc "(I can’t believe he’s always at the same location that I am in.)"
            mc "(Whatever, I should just ignore him, he’s not worth my time.)"
            gd "Hey do you need someone to play against?"
            mc "(He wants to play?)"
            mc "So you’re stalking me aren’t you?"
            gd "I was here first, so I couldn’t have!"
            mc "(This guy...)"
            mc "Fine, if I win, you leave."
            gd "Don’t worry, you won’t will."
            mc "(THIS GUY!!!)"
            mc "(Was that thunder?)"
            mc "(What the... it’s raining!? What is with the bad luck today! I didn’t even check the weather and I don’t even have an umbrella...)"
            gd "Hey!"
            mc "Yes?"
            gd "Do you need an umbrella?"
            mc "No... I’m good, I’d rather walk in the rain. Thanks for the offer."
            gd "Are you sure?"
            mc "Yeah. Stop bothering me!"
            gd "Okay. By the way, may I ask for your name?"
            mc "(What the? Why does he want to know my name for!?)"
            mc "My name is [mcname]"
            gd "Nice to meet you today [mcname]"
            mc "(So he did notice me... Maybe I should’ve taken his offer. I sounded pretty rude too...)"
            mc "You idiot... now you’re gonna be going home dripping wet."
            #Setting your apartment
            mc "(It’s so cold in here!! I need a warm bath so badly!)"
            mc  "(I turn on the heater and headed for the showers.)"
            mc "What an eventful day today... "
            mc "Maybe I shouldn’t have been so cold towards him..."
            mc "Aiyah... I totally shouldn’t have done that."
            "I slowly sunk my head under the water."
            mc "Oh and I still need to come up with a game idea soon..."
    return
        
#Scene 4
#Setting: Lecture Hall, Anywhere On Campus
#DIALOGUE:
label gd_scene4:
    scene bg meeting_1 with fade
    show gd calm with dissolve
    gd "Alright everyone, today is the big day. Let's hear those pitches."
    "(*The crowd claps*)"
    mc "(Today is already pitch day... I hope I don’t choke up there.)"
    mc "(I'm getting so nervous even though this is a small presentation...)"
    gd "Up next we have a game called Find the Faker by [mcname]."
    hide gd calm with dissolve
    scene bg meeting_2 with dissolve
    mc "Hi everyone. My name is [mcname] and my game is called Find the Faker."
    mc "So my game is a text based game with animation where the player plays as the main character and as the story develops, the player are provided with evidence and clues."
    mc "There will be an abnormal villain within your group of characters that can morph itself into anyone."
    mc "The goal of this game is for the player to find the kidnapper as soon as possible..."
    mc "(Okay, you got this, everything is going smoothly, just stall it out for a few more minutes...)"
    mc "That's the gist of it. Thank you for listening, and once again, the name of my game called Find the Faker."
    "(The crowd claps)"
    mc "(It’s over...What a relief.)"
    show ren calm with dissolve
    ren "Hey, you did great! I expected nothing less from you kiddo."
    mc "Yeah... Thank goodness it’s over."
    mc "Oh Ren, you’re not gonna pitch an idea?"
    ren "Nope. I’ve decided to join your group! Well, if that’s cool with you!"
    mc "Of course!"
    ren "Anyway, we'll find out who will be in our group in the next meeting. I have to head out now, but I'll catch you later."
    mc "Bye Ren!."
    ren "See ya!."
    hide ren with dissolve
    with Pause(0.5)
    show gd with dissolve
    gd "You did a nice job up there."
    mc "(That voice...)" 
    mc "Hey, you shouldn’t sneak up on people like that!"
    gd "Long time no see."
    mc "Too scared to go to the park and get beaten?"
    gd "Don’t worry, I won’t lose to a stalker."
    mc "(Stalker!? Why you... no I shouldn’t fall for his taunts.)"
    menu gd_menu4:
        #[Player Option 4]
        "Then come and challenge me today!": #(Best)
            mc "Instead of talking big, how bout you come out and play me tonight!"
            gd "I would love to, but you’ll just have to wait a bit for your that L."
            mc "Hmph. At this rate I guess I’ll just have to wait two lifetimes before I get to beat you."
            gd "Hahaha, one day, when there’s enough time. Bye."
            mc "(That’s... the first time I heard him laugh.)"
        "Ignore him and walk away": #(Worst)
            mc "Scaredy-cat."
            gd "Maybe soon!"
            mc "(Whatever. I should go home, it’s getting late.)"
    
#Scene 5
#Setting: Lecture Hall
#Characters: MC, Ren, gd
#Dialogue:
#Outside
label gd_scene5:      
    scene bg sslh with fade
    ren "Heya!"
    mc "Oh, Hi ren!"
    ren "Are you excited? We find out our team members today."
    mc "(Hopefully I don't get him on my team... but for some reason I feel like I will.)"
    ren "Okay, let's go to the meeting!"
    #lecture hall
    scene bg meeting_1 with dissolve
    mc "(WHAT?! HE'S ON MY TEAM AS THE GROUP SUPERVISOR?!)"
    mc "(I bet he purposely put himself into my group...)"
    show gd calm with dissolve
    gd "Hey everyone. It's an honor to be working with you guys and supervising the team."
    gd "Everyone please introduce yourself to the group and write your contact info down and your availability."
    gd "Once you guys finish, please give the information to the group leader and I’ll get back to you guys as soon as possible."
    gd "I have to talk to the board, but I’ll be back."
    hide gd calm with dissolve
    mc "What a great supervisor. He ditches us to wander off and he’ll never come back."
    show ren calm with dissolve
    ren "That’s gd for ya. Hahaha. Let’s have an introduction everyone!"
    hide ren calm with dissolve
    mc "(After introductions, we exchanged details. I then told my members the general information about the project.)"
    mc "(Hmmm it's getting late, I should head back soon.)"
    mc "Okay guys, let's call it a day and head home."
    show gd calm with dissolve
    gd "Hey, sorry about that."
    gd "I'll message you later to get the information that I missed."
    mc "But of course my amazing supervisor!"
    gd "Thank you."
    gd "I’ll see you later, Stalker."
    hide gd calm with dissolve
    mc "(This guy gets on my nerves so much.)"
    mc "(Maybe that’s his plan! I’m falling for him.. I mean his trap, falling for his trap!)"
    mc "(Anyway, I should start heading home.)"
    return
    
#Scene 6
#Setting: Player’s Apartment
#Characters: MC and gd(Phone)
label gd_scene6:
    scene bg mc_apartment_inside with fade
    show phone with dissolve
    mc "(I suddenly wake after hearing a message notification. It's 1 a.m!!)"
    mc "(Why is he texting me at 1 a.m?! Why am I so awake now...)"
    gd "Hey, this is me Jeorge, sorry for messaging you this late, but I was wondering when you wanted to meetup to discuss about the game?"
    mc "(Mhhmm should I wait till the morning and answer or should I answer it now..." 
    mc "(WHY DOES THAT MATTER. I'll just answer it now.)"
    mc "Uhh yeah I can meet up whenever after 6p.m tomorrow."
    gd "Okay, where do you want to meet up?"
    mc "Wherever is fine."
    gd "My apartment?"
    mc "Yeah sure."
    mc "(Wait. What did he say? WAIT, WHAT DID I SAY? HOW DID THIS HAPPEN.)"
    gd "Okay, sounds good. I’ll send you my address tomorrow"
    gd "Goodnight."
    mc "(I am so careless... I can’t even fall asleep now.)"
    mc "(It's 3 a.m...)"
    mc "(I'm going to be so tired tomorrow but I can't sleep. All because of him...)"
    
    #Setting: gd’s apartment
    scene bg gd_apartment_inside with fade
    mc "So this is where the president lives huh?"
    show gd calm with dissolve
    gd "Yeah, it's pretty empty inside"
    mc "It's so clean..." 
    mc "Your apartment is so clean, but you're a guy..."
    mc "It's so sad when a guy's apartment is cleaner than yours..."
    gd "I just like to keep things clean I guess."
    gd "Would you like anything to drink or eat?"
    mc "Yeah, sure. What do you have?"
    gd "Well the fri... I guess you found the fridge."
    mc "(I opened up his fridge and there was so much food inside! I really wanted to cook too because I haven’t cooked in so long.)"
    mc "So much fresh ingredients in here... You mind if I cook?"
    gd "Cook?! Are you really going to cook right now?"
    mc "Why? Is that a problem, huh?"
    gd "Uhh no, feel free to cook yourself anything."
    gd "I’ll help you out."
    mc "Okay, thanks."
    mc "(I haven’t eaten anything all day and he said I can use his stuff to cook myself a free meal hehe.)"
    gd "You’re pretty comfortable around strangers huh?"
    mc "You’re not a stranger... You’re a freaking stalker."
    gd "Hahaha, I see."
    mc "Can you pass me the bowl over there and cut up the tomatoes."
    gd "Yeah."
    gd "You’re pretty good at cooking, but why did you suddenly want to cook?"
    mc "I don’t cook often, but since I have all these ingredients and someone to test my cooking, I can’t let go of such opportunity."
    mc "(He just smiled and did not say anything back.)"
    mc "(We cooked for an hour or so and the food came out great.)"
    gd "It smells great, thanks for cooking me dinner."
    mc "What? Don’t think this is free. You owe me a dinner too."
    gd "Then I’ll have to come to your apartment and use your ingredients."
    mc "Nevermind. I take that back."
    gd "Hahaha. Let’s eat!"
    mc "(As we ate, I noticed a weird outfit on his table.)"
    mc "Is that your halloween costume?"
    mc "This is one good detective costume! Where did you get it?"
    gd "Oh, I made it."
    mc "You made that by yourself? I guess you have some skill after all."
    mc "(I stood up to get a better look at the costume, but as I stood up, the bottom of my shirt catches the sharp corner of the table.)"
    mc "Damn it, my shirt... it ripped"
    gd "Here, take off your shirt."
    mc "WHAT?! HUH?! YOU PERVERT."
    gd "Here take this shirt, put it on, and give me your shirt, I won't look."
    mc "(This guy... what is he up to. I took off my shirt, put on the other one and handed it to him.)"
    mc "Here."
    mc "(He pulls out his sewing kit and starts to sew my shirt together... he does know how to do a lot of things...)"
    gd "Here ya go, sorry I wasn't able to do a better job."
    mc "You sure know how to do everything huh..." 
    gd "It's called being a responsible adult." 
    mc "So you're saying I'm not an adult because I can’t sew?"
    mc "That's insulting..."
    gd "I meant that there are many different kinds of adults..."
    gd "Well it's late, we weren't able to discuss much, but we can talk about the game another day."
    mc "Let’s at least plan out the first group meeting first!"
    gd "Sounds good."
    
    #Club Meetings
    #Setting: Lecture Hall? Or  Game lab?
    #Characters: gd, ren, MC
    #player’s apartment
    scene bg black with fade
    "(*Beep Beep Beep*)"
    mc "(I shouldn’t have stayed up so late last night... I’m so tired now.)"
    mc "(Today is our VGDC group’s first meeting! I’m so nervous but excited at the same time. Leading a group is such a big task, hopefully I’ll be able to manage.)"
    mc "(I got up and got ready. Hmm I think I should dress a little nicer today...)"
    #Outside anywhere
    scene bg park_1 with fade
    mc "(It’s almost time for the meeting... Thinking about it makes my stomach want to curl up.)"
    mc "(I’ll be fine! Let’s go in.)"
    #inside meeting place
    scene bg library_1 with dissolve
    show ren calm with dissolve
    ren "Wow! Look at that everyone, our leader looks so pretty today! You look good kiddo."
    mc "(I’m... seriously about to faint. Everyone is actually here, including him and they’re all looking!! Maybe I shouldn’t have looked extra nice today.)"
    mc "Thanks Ren... Hi everyone, welcome to the first meeting. Let’s all work hard and do our best!"
    mc "I’ll give everyone the full details of the game and then we can start by having the programmers set up gitHub."
    mc "I’ll need to talk to the artist and the writer to plan out the characters and stories."
    mc "Audio boy, you work your magic! Sounds good everyone?"
    team "Yea!"
    mc "Then let’s get to work!"
    mc "Hey gd, since we don’t have any writers... do you mind being our main writer?"
    show ren calm:
        linear 0.5 xalign 0
    show gd calm at right with dissolve
    gd "Yeah, I don’t mind."
    mc "Thanks!"
    mc  "By the way..."
    gd "Yeah, what’s up?"
    mc "Oh nevermind..."
    mc "(I wanted to thank him for the meal last night, but I’m sure I don’t need to say anything.)"
    mc "Okay Ren and gd so about the characters, can you guys talk to each other and come up with designs for the characters...."
    gd "That shouldn’t be hard. But knowing ren, I’ll end up coming up with the characters all by myself."
    ren "That’s not true! You’re the one that relied on me for all the characters last project!"
    ren "That reminds me! You owe me a dinner for the characters I drew for your group last project since you guys didn’t have an artist!"
    gd "Oh yeah, I totally forgot about that! My bad Ren. I’ll cook you dinner tonight and bring it over."
    hide gd calm with dissolve
    show ren calm:
        linear 0.5 xalign 0.5
    mc "(ren and Jeorge get along so well.)"
    mc "(We worked on the project for an hour. Throughout the hour of our meeting, I discussed my vision of the projects and questions that the members had.)"
    mc "Alright everyone! Thank you for coming to today’s meeting. I’ll see everyone next meeting!"
    mc "(That meeting went well...)"
    ren "Good meeting today kiddo!"
    ren "By the way, do you want to join us for dinner? It would be nice to have you and gd both come!"
    ren "My place has been a bit empty and boring lately..."
    mc "(I shouldn’t...)"
    mc "Sorry Ren, maybe next time! I have something that I have to do."
    ren "I see. No worries! You’re welcome to come if by if you change your mind!"
    mc "Thank you."
    mc "(Boy am I tired. I feel like I’m gonna...)"
    ren "Hey! Can you hear me??"
    mc "(Is that ren? Why do I feel so light-headed)"
    mc "ren? Is that you? What happened..."
    ren "You passed out right in front of me!"
    mc "Oh... I guess I did. Just a bit tired, I’ll be okay."
    ren "No way, you are not okay. You need to take better care of yourself."
    ren "Here, hold onto my shoulders, I’ll carry you back home."
    mc "No, I’m okay really... "
    mc "(She gave me a stare that is similar to that of a worried mother’s expression towards her child.)"
    mc "...Thank you, Ren."
    hide ren calm with dissolve
    #player’s Apartment
    show bg mc_apartment_inside with dissolve
    show ren calm with dissolve
    ren "You’ve been working too hard on yourself..."
    mc "Maybe just a little."
    mc "(I smiled and she gives me a long sigh.)"
    ren "Alright, you just lay down and close your eyes. I’ll cook you something to eat right now."
    mc "Wait, I’ll be okay. You have dinner plans with someone and you can’t miss that!"
    ren "Oh that? Don’t worry about it, he’ll understand. Rest up, I’ll cook you dinner tonight."
    mc "(Ren...)"
    mc "(Why do you do this... for me?)"
    ren "Okay, the food is ready, let’s eat!"
    ren "Come on you lazy pig, get up."
    mc "Hey wait! Hey that tickles!"
    mc "(ren picked me up and carried me to dinner table.)"
    mc "Wow! You cooked all of this for me??"
    ren "For US. I’m gonna eat your food with you! Oh yeah, make sure you sleep early tonight and not stay up late."
    ren "I’m cooking your dinner so you better listen to what I say... OR else MUWAHAHA."
    mc "Already roleplaying as a witch for Halloween I see."
    ren "What did you say?"
    mc "N-nothing!"
    mc "(We both laughed...  I’m so grateful to have such a good friend like you in this life...)"
    
    #Player’s Apartment Part 1235332
    #Setting: apartment
    #player’s apartment
    scene bg mc_apartment_inside with fade
    ren "Hey! Wake up! I’m here to cook you breakfast!"
    mc "(It’s 8 a.m and she’s already here knocking at my door....)"
    show ren calm with dissolve
    mc "Why are you here so early!?."
    ren "I must make sure that you are okay!"
    mc "I've been okay..."
    ren "Better safe than sorry! Anyway, my apartment is lonesome, so I’m gonna crash here and hang out with you for the day!"
    mc "(Even though it’s 8 a.m on a Saturday, I’m happy that Ren came. It does get pretty lonely sometimes.)"
    mc "Okay, okay I’m going back to bed. Please, Just 10 more minutes. Or better yet, wake me up when you finish cooking. Thank you!"
    ren "...."
    mc "(It's almost the end of the quarter and the club meetings are going well. We made a lot of progress so far and we’re on track to finish it by winter break.)"
    mc "(ren and I have also been getting extremely close.)"
    mc "After the incident where I fainted in front of her, she would always check up on me and take care of me.)"
    mc "(And as for George Dan, I would always see him at club meetings and he would always make the meeting fun, interesting, and productive for everyone.)"
    mc "(As I felt the stitches on the shirt that he sew back for me, the memories of when I first met him at the park came back.)"
    mc "(I haven’t seen him at the park since our first encounter...)"
    ren "Hey sleepyhead, wake up!"
    mc "The quarter is ending soon…"
    ren "Yeah, time does fly by when you’re too busy."
    ren "That’s why you have to take time away from your busywork and spend a little time enjoying ya self!"
    mc "That’s easier said than done… being an adult requires us to uphold a lot of responsibilities. We actually have to worry about the future ahead of us now."
    mc "Work hard now and enjoy life later! That’s my motto."
    mc "Besides, it’s impossible for me to make time for relaxing since finals and projects are coming up."
    ren "Well… that’s why I’m here! To find the time for you to relax instead of over studying. Haven’t you heard?? Too much studying is equal to ‘student dying’."
    mc "Haha, real funny. I’m gonna fail my exams because of you…"
    ren "You’re not wrong though. We do have a life ahead of us to worry about and we’re given great opportunities in life to do many great things…"
    ren "But sometimes we forget the things that are also important in our life, and sometimes we don’t realize it until it’s too late."
    mc "(Tears started to fall down her gentle face as she spoke. I can sense feelings of sincerity and regret coming from her.)"
    mc "(What she said weren’t merely just words, but experiences. Experiences that she had gone through. Experiences that shouldn’t be taken lightly. Ren…)"
    ren "Work hard and enjoy life along the way with others! That’s my motto for sure."
    ren "You also better take care of your health too! You can’t work hard or enjoy life if you’re always out of energy!"
    mc "ren… fine, let’s relax then! You prepare the food and I’ll prepare… the Netfix!"
    ren "That’s what I like to hear!"
    mc "How about you come back tomorrow night and I’ll cook you dinner to repay ya for all those times that you took care of me?"
    ren "That sounds great, but we’ll have to do it another day! Sadly, I’m going to be busy tomorrow. George Dan and I made plans to go somewhere."
    mc "George Dan huh… that’s fine! We’ll do it next time…"
    ren "Sorry about that kiddo!"
    mc "No worries!"
    ren "Lunch is ready though! Let’s eat."
    mc "Thank you, Ren."
    #--black--
    "Ren left. The place feels a bit empty again. I guess humans are social animals… it does suck feeling lonely."
    "I guess ren is right. You’re enjoying their company so much that when they leave, you just can’t help but get a little sad."
    "Our group’s last meeting is coming up… We finished the project and it’s works amazingly thanks to everyone’s hard work."
    "Oh, I know! I’ll cook everyone something nice and the last meeting can just be a hangout!"

    #Last Club Meeting
    #setting: apartment
    scene bg mc_apartment_inside with fade
    mc "The last meeting… I can’t believe it’s been a whole quarter already. Everyone worked so hard and the game came out nicely."
    mc "I hope they’ll enjoy my cooking. I mean, why wouldn’t they? I’m a pretty damn good chef. George Dan seemed to enjoy it the last time I cooked for him..."
    #setting: outside/lobby
    "As I walk towards the room, I start to get that indescribable feeling… the feeling that you get when you know that a story is coming to an end." 
    "I mean, it’s a good ending… but this might be the last time I’ll really get to be this close to everyone."
    "Then everyone will be going off to another group or doing their own thing next quarter. I know that we will all keep in touch, but we won’t be as close as we are now."
    #Enters the room
    "Well, that’s part of the journey I guess. Let’s enjoy this last moment…"
    show gd calm with dissolve
    mc "WHY ARE YOU THE ONLY ONE HERE??"
    mc "Where’s everyone else??"
    gd "Didn’t you see the group chat?"
    "I pulled out my phone to check"
    hide gd calm with dissolve
    show phone with dissolve
    mc "Hey [mcname], Alex, me, and Melody are all going to be busy. We will not make it to the last meeting! Sorry! But we can hangout after finals! - Love ya, Ren"
    mc "(Why didn’t I check my messages earlier…ughhh.)"
    hide phone with dissolve
    show gd calm with dissolve
    gd "You didn’t plan anything special before the meeting, did you?"
    "I walked up to him and placed the box of food in front of him."
    mc "You’re eating all of that. By yourself."
    mc "I can’t believe that they all ditched the meeting… I really wanted to thank them for their hard work you know."
    "He starts to eat my food."
    gd "You’ll get to do it later, when we hang out after finals."
    mc "You’re… actually eating my food."
    show gd smile with dissolve
    gd "It’s pretty good. Your cooking tastes even better the second time. It’s a shame that the group’s not here to try it."
    mc "(Why am I blushing!?)"
    #Player Option 
    menu why_am_i_blushing:
        #option 1: Asks him if he really likes your cooking.
        "Ask him if he really likes my cooking":
            mc "Is it really that good?"
            gd "Yeah, I love it."
            mc "Thanks."
            mc "...Why did you come if you knew that everyone else wasn’t coming?"
            gd "I am the group’s main buddy officer so it’s my duty to be here at this final meeting to thank you for an amazing quarter and congratulate you for your hard work."
            gd "Also... I didn’t want you to be here alone all by yourself."
            mc "I… Thanks."
            "I sat down, across from him."
            mc "Since no one is here, I guess I’ll just give you my thanks. Good luck on your finals."
            gd "Hey."
            "I turned back around and looked at him."
            gd "Let’s finish our one on one match today."
            mc "Now you finally want to lose?"
            gd "Let’s see if you’ll still say that after the game."
            mc "You’re on."
            gd "Before that, here."
            "He hands me a wooden double picture frame."
            gd "I always get it for everyone in the group that I’m in. It’s like a souvenir... to remind them that they were a part of a wonderful journey."
            gd "The other one is special. I got it for you as a personal thank you for holding the team together and creating a memorable experience for all of us." 
            "I hadn’t expected this at all… I was awed. I looked at him in the eyes and he gently smiles back."
            mc "Thanks…"
        #option 2: Try to invite him over to your place. #Best
        "Try to invite him over to my place":
            mc "Is it really that good?"
            gd "Yeah, I love it."
            mc "Anyway… why did you come if you knew that everyone else wasn’t coming?"
            gd "I am the group’s main buddy officer so it’s my duty to be here at this final meeting to thank you for an amazing quarter and congratulate you for your hard work."
            gd "Also... I didn’t want you to be here alone all by yourself."
            mc "Thanks... actually, come with me!"
            gd "Where do you want to go?"
            mc "We’re going to my place."
            gd "Huh… What??"
            mc "Come on, let’s go. I want you to try something."
            "Like a spirit had possessed, I grabbed him by the hand and dragged him to come with me"
            gd "Hey wait! We can take my car, it’ll be faster..."
            #--black--
            #Player’s apartment
            scene bg mc_apartment_inside with fade
            show gd calm with dissolve
            gd "So this is your apartment... It’s so empty, don’t you get a bit lonely?"
            mc "So will putting a giant teddy bear in that corner make it less lonely, huh??"
            mc "(This guy… already criticizing my place. He’s getting me angry again.)"
            mc "(No s**t it gets a bit lonely when you live by yourself.)"
            gd "I like it actually. Simple and spacious, yet elegant. But I think it needs a little something…"
            "He pulls out an object and then places it on my table next to my laptop."
            gd "Some objects are good to keep around. It reminds you that you are never alone in this world."
            mc "Since when did you get that?"
            "The item that he placed on my table was a picture of our group together."
            gd "I always get it for everyone in the group that I’m in. It’s like a souvenir... to remind them that they were a part of a wonderful journey."
            gd "This one... is special."
            mc "(There’s something behind it…)"
            "He opens the the second frame underneath the first frame to reveal another picture. It was a double picture frame."
            mc "That’s.... us…"
            "It was a picture of me staring at him angrily during a group meeting. My irritated eyes glaring at him and his subtle posture. Ren took this picture."
            show gd smile with dissolve
            gd "I like this one. I got it for you as a personal thank you for holding the team together and creating a memorable experience for all of us." 
            "I was shook. Words did not come to me. I did not expect this. As I stare at the pictures, I wanted to thank him, but I couldn’t say a word. I only shed a few tears."
            show cd calm with dissolve
            gd "Oh yeah, did you want to show me something? Sorry for stealing the show."
            "I finally snapped out of my trance and wiped the few tear drops off my face."
            mc "Sorry, I got a bit distracted. Thank you very much for the gift…"
            mc "Okay! Sit down and relax. I’m going to make food for you to repay you for the meal at the start of the year."
            gd "This is rare so I guess I’ll accept your offer."
            "I looked at him in the eyes and he gently smiles back. As the night went on we talked to each other endlessly as we ate. I was getting to know him more and… it was nice."
            gd "That was really good. Thank you for the meal."
            mc "No worries."
            gd "It’s been a whole quarter already huh?..."
            mc "Yeah… are you leaving now?"
            gd "Is that your basketball over there?"
            mc "Yeah."
            "He didn’t answer my question but instead grabs my hand."
            show gd smile with dissolve
            gd "Let’s go, I want you to see something."
            mc "Huh?"
            "He picks up the basketball."
            gd "I wanna show you what a real winner looks like."
            "He passes the basketball to me."
            mc "Ah I see. You’re on. We’ll finish our match tonight."
            "Our eyes crossed and this time… I smiled back at him."
    #----------END OF OPTION-----------
    #Park Scene
    #Setting: Park
    scene bg park_1 with fade
    show gd calm with dissolve
    gd "Are you ready to lose? You start."
    "He passes the ball to me."
    mc "You’re gonna eat those words."
    mc "(He’s playing extremely aggressive. I guess he really wants to win. I won’t let him.)"
    "It felt refreshing as we played.  I don’t want to lose… I don’t want this day to end."
    mc "(There! An opening.)"
    gd "Not even close."
    "He predicted my movements and blocks me."
    mc "Not bad…"
    gd "Try to defend this."
    mc "(He’s fast!)"
    "I was able to catch up and defend him from going to the rim but then he pulls up and makes a jump shot."
    gd "1-0."
    mc "That was pretty lucky. I didn’t expect you to make that."
    "Once get got the ball back he quickly" 
    mc "You know what they call me… the Handle God."
    "I quickly crossed him over with ease and laid up the ball into the basket."
    mc "Too easy. You can’t guard me!"
    gd "Let’s see you do that again."
    "I did the same thing once again, but this time he swiftly moved back and tries to block me, but this time I reversed my layup and scored once again."
    "Our bodies made contact during the shot and as I landed I felt a stinging pain coming from my left foot and I yelled out in pain."
    gd "Hey are you okay??"
    mc "Scored and one."
    "He just slightly laughs and carried me over to a bench. We sat down on the bench."
    gd "Let me see your foot."
    mc "It’s fine, just a tiny sprain, I get them all the time. I can still walk fine, it just hurts a little."
    gd "Well, I guess the game is over..."
    mc "Then I win."
    gd "Then I guess you win the bet. I’ll leave you alone in here now."
    "I grabbed him by the arm. He turns and looks me in the eyes."
    mc "So you’re just going to leave me here, at night, after you injured me?!"
    gd "I’m joking, I’m joking. Hahaha."
    gd "It’s been a whole quarter already huh? Sorry it took this long for our rematch."
    mc "Don’t worry, I understand. Ren told me that you’re always busy so it only makes sense."
    mc "So what are you going to do during winter break? Are you gonna go home?"
    gd "This place is like home to me so I’ll be staying here for the break. How about you?"
    mc "I live up north so I’ll be heading back there to my family during the break..."
    "We sat on the bench silently for the next minute. He then broke the silence."
    gd "How’s your dad like?"
    mc "(Huh? That’s a weird question…)"
    mc "Uhmm… he’s just a uhhh… regular, nosy, old fool that always try to piss me off!!"
    mc "(Thinking about him is making me annoyed.)"
    gd "Oh I see. Hahaha."
    mc "But I guess he’s wise and caring… sometimes."
    mc "(I wonder why he’s asking about my dad… I should ask him about his dad.)"
    mc "How’s your dad like?"
    gd "We were never close..."
    mc "Oh… I’m sorry to hear that. Maybe you can use this winter break to get closer to him."
    gd "If you tried your best to help someone but they refuse to accept your help, will you ever give up on them?"
    mc "If you know that you will never forgive yourself for giving up on them… then you should never let go of them."
    mc "Maybe they’re lonely… and they need someone to clear those gray clouds of loneliness."
    gd "I see…"
    "He then grabs my arms and put them around his neck."
    gd "I’ll take you home."
    mc "I can walk on my own you know..."
    gd "I know."
    "He carried me on his back. My arms around his warm neck. His warm body against mine. The weather is getting colder."
    mc "(Always playing the prince while I play the princess in distress…)"
    "Just like then… quiet but comforting. I couldn’t help but to smile as I rest my head onto his shoulders."
    #--black-- 
    "Suddenly, a black car stops in front of us, blocking us from moving forward."
    "A man around my dad’s age came out of the car. Exiting the passenger side was a woman... "
    show gd calm:
        linear 0.5 xalign 0.8
    show ren calm at left with dissolve
    show ren calm:
        linear 0.5 xalign 0.2
    mc "(It’s Ren!)"
    "George Dan looks at the man. Their eyes met, a cold stare that I have never seen before, came from George Dan. Serious wouldn’t describe the look in his eyes, it was more of hatred."
    "I wanted to ask him about the situation… but I couldn’t. It wasn’t my place to say anything."
    gd "ren, can you take [mcname] home."
    ren "Yeah."
    "ren then came over and took me from George Dan’s shoulders."
    hide gd with dissolve
    show ren calm:
        linear 0.5 xalign 0.5
    mc "It’s okay ren, I can walk."
    ren "Nope. I got you!"
    "She wrapped my arms around her neck and carried me on her back."
    mc "(Stubborn just like George Dan… I’m thankful for friends like you guys.)"
    ren "Don’t worry, I’ll explain everything once we get home."
    hide ren calm with dissolve
    "I looked at George Dan and the mysterious man. Their eyes still glaring at one another without a single word. Is it his father? Why was ren with him…?"
    #Apartment Scene 9000x
    #Setting: MC apartment
    scene bg mc_apartment_inside with fade
    show ren calm with dissolve
    ren "How’s your foot? Here let me get you some ice."
    mc "I’m okay, thank you Ren."
    ren "You’re probably wondering who that guy was. You probably guessed it though… he’s our father."
    mc "Yeah, I had a feeling… wait WHAT?!?! ‘Our father’??"
    ren "Yeah, George Dan and I are siblings… well, he’s my stepbrother."
    ren "Why? Did you think we were… perhaps, lovers?"
    "She starts so laugh. I on the other hand, was shook. I couldn’t believe what she had told me."
    mc "You guys are siblings?? You never told me this!!"
    ren "I thought you knew… hahaha."
    mc "You told me you had plans with him so I thought you two… like each other…"
    ren "Oh that… we were just planning to visit our mom in the hospital like usual. Here, sit down, drink some water, and I’ll explain to you everything…"
    return
# END SCENE 6