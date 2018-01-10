define md_affection = 0
# max affection = 8

#DIALOGUE:
#--Scene 1:--
#SETTING: Outside (Night)
label melody_scene1:
    scene bg night with fade
    show ax calm with dissolve
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    ax "Hey Bro! How’d I do up there?"
    mc "You got the girls giving off giggly noises if that’s the answer you’re expecting…"
    show ax happy with dissolve
    ax "HAHAHA! Yes, YES!"
    "With his fist clenched and raised in the air, he gives off an excited grin as he knew that he had accomplished his goal."
    "Yeah, this… is definitely Alex. He lives in the moment just to impress girls…"
    "As we continue to walk he brings up an interesting topic…"
    show ax calm with dissolve
    ax "Did you see that girl, Melody?"
    mc "The one with the red streaks and the headphones? Audio girl, right?"
    ax "Yeah! Was she looking at me when I was speaking?"
    mc "No, she had an uninterested look the whole time. I don’t even think she even glanced at you."
    show ax sad with dissolve
    ax "What?!? Are you serious…?"
    "He has a hopeless look on his face that can probably make any girl go ‘Awww, Alex’."
    mc "Yeah, but why does that matter? You like her or something?"
    ax "You don’t understand… I’ve been trying to get at her for the longest time..."
    mc "Since When!?"
    show ax calm with dissolve
    ax "Since last week."
    "I raised my hand and smacked him on the head lightly."
    mc "You freaking player. I thought you were serious."
    ax "Oww, that hurts... Just kidding!"
    ax "But no, for reals… I want to try and get at her. I’ve known her since last year, but we didn’t talk much."
    ax "Well, she didn’t talk to anyone much really, she’s always doing her thing. Like a lonewolf…"
    mc "I see…"
    ax "I like lonewolfs."
    mc "..."
    ax "She’s also notorious for being a bad girl. Like the ones that can seduce you to do whatever she wants..."
    mc "I don’t think she has any bad intentions though..."
    ax "I like bad girls."
    mc "... I am speechless. You will never change. I take that back. You will never grow up!!"
    show ax happy with dissolve
    "He starts to laugh hysterically."
    ax "Comeeee on… good girls ain’t no fun, am I right?"
    mc "I wouldn’t know…"
    show ax calm with dissolve
    ax "But yeah, she’s the ‘Hard to get’ kinda girl, so I really, reaaally want to impress her."
    ax "You don’t understand how many guys tried to get at her last year…"
    ax "And did you not see the look on their faces this year?! She’s more desirable than ever!"
    mc "You talk about her as if she’s an object…"
    show ax happy with dissolve
    ax "Hahaha, did it sound that way? My bad, I meant to say that she’s… one of a kind you know. And maybe that’s why a lot of the guys like her."
    mc "She is cute… I guess."
    show ax calm with dissolve
    ax "Right?! But hey, she’s fair game. Though… you’re up against me if you want to snatch her away."
    mc "You’re a lunatic. I’m not interested in her."
    ax "Reaaaally? I can already read the fattest lie on your face."
    mc "Why… you!"
    show ax calm:
        linear 0.5 xalign 1.5
    hide ax calm with dissolve
    "Alex starts to laugh uncontrollably and runs away as I try to chase him."
    "Suddenly, I realized that I didn’t have my phone on me."
    show ax calm with dissolve
    mc "Alex! I lost my phone, can you call it, please?"
    ax "OH shoot, yea."
    "Alex called my phone but no one picked up."
    ax "No answer… I think you might’ve left it in the lecture hall."
    mc "Damn… I’ll be right back."
    hide ax calm with dissolve
    stop music fadeout 1.0
    "As I start running to the lecture hall, I accidentally bumped into someone on the shoulder. They gave off an angry expression."
    with hpunch
    show kd angry with dissolve
    kd "Watch where you're going, Kid."
    mc "My bad…"
    kd "Pst. Get out of my way..."
    mc "Damn... isn’t he the production guy? What an ass..."
    "I got to the lecture hall and luckily the doors were still open...."

    #SETTING: Lecture Hall
    scene bg meeting_2 with dissolve
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    "When I entered the lecture hall, the board was covered in graffiti and then I saw Melody drawing graffiti on the far wall. ‘VGDC sucks.’ was one of the messages on the wall."
    "She turned around with a blank expression on her face, like a deer when you shine your high beams at it."
    show md angry with dissolve
    md "Damn… I forgot to lock the doors."
    "I felt frozen in place. What should I do?"
    #----------Player Choice 1---------------#
    menu md_menu1:
    #option 1: Apologize and tell her that you’re just here to look for your phone. (Worse)-----
        "Apologize and tell her that I'm just here to look for my phone":
            mc "Uh, I'm really sorry. I, um, well, I-"
            show md calm with dissolve
            md "You’re looking for your phone right?"
            mc "Yes… how’d you kn-?"
            md "Here. Catch."
            "She tosses the phone across the lecture hall to me."
            mc "(I barely caught it… this girl is crazy.)"
            mc "Uh… thanks."
            show md angry with dissolve
            md "Close the door on the way out, will ya kiddo. And one more thing. If you tell anyone this, I’ll make sure you’ll regret ever coming to UCI."
            "Her words sent shivers throughout my whole body and soul. She’s so aggressive… I felt as if I was the deer being hunted…"
            mc "Of c-course!"
            md "Good… now get out."

    #-----#option 2: Look for your phone and ignore her (Best):-----
        "Look for my phone and ignore her":
            $ md_affection = md_affection + 1
            md "Hey!"
            mc "(Pull yourself together. She's not going to jump you.)"
            mc "(...)"
            mc "(...or will she?)"
            mc "(It doesn’t matter! I should just ignore her and look for my phone.)"
            show md calm with dissolve
            md "Looking for this?"
            "In her hand was my phone."
            mc "Y-yeah…"
            md "Since you ignored me..."
            md "I’ll tell ya what. Tell me your name, then kneel on the floor and beg for your phone… and MAYBE I’ll give you it back."
            mc "(Pft… does she really think I’m going to be her dog? Play fire with fire.)"
            mc "What if I don’t… and instead I tell the board members what you’re doing right now."
            show md angry with dissolve
            md "You dare threaten me…?  Hmfph… this arrogant punk."
            "She gave off an angry and aggressive smirk."
            mc "Alright… you win."
            "She tosses the phone across the lecture hall to me."
            mc "(I barely caught it… this girl is crazy.)"
            md "If you tell anyone about this, I’ll make sure you’ll regret ever coming to UCI."
            "Her aggressive tone and words sent shivers throughout my whole body and soul."
            "I felt as if I was the deer being hunted. I’m wasn’t playing with fire… I was sinking in the middle of the ocean!"

    #----------End of Player Choice 1----------
    hide md calm with dissolve
    stop music fadeout 1.0
    "Right before I left Alex came running through the door."
    show ax calm with dissolve
    mc "(Oh no!! This is bad…)"
    ax "Hey dude, slow down next ti..."
    "He gazed around the room with a shocked expression on his face…"
    ax "You.. didn’t do this in like 10 seconds did you...?"
    mc "No…"
    "I pointed my finger towards her."
    play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
    "Alex formed his hand into a gun-like formation with his index finger pointing towards her."
    show ax calm:
        linear 0.5 xalign 0.2
    show md calm at right with dissolve
    show md calm:
        linear 0.5 xalign 0.8
    ax "Hey… Melody..."
    mc "(This is so awkward…)"
    "Alex then quietly whispers to me."
    ax "Omg dude! This is my chance!"
    md "Great… don’t worry, Alex, it’s not permanent…"
    show ax happy with dissolve
    "Alex instantly smiles and then whispers to me."
    ax "OMG!! She said my name!!"
    "I slammed my hand against my face."
    "With a cool and calm posture he turns towards Melody."
    ax "Yo, no worries… I won’t tell the board or anyone, I promise!"
    ax "I only have one favor to ask you though…"
    md "What."
    ax "Uhh… do you want to.. eat lunch with us tomorrow?"
    md "No."
    mc "(Us?? And damn she rejected his ass quickly.)"
    ax "But… I… uh need to ask you questions about audio… effects? I mean… since you did say that you’ll help people out if they have questions for ya."
    "I closed my eyes. I was cringing at every B.S word that he said."
    md "Fine."
    "I slammed my hand against my face again. I can’t believe it worked..."
    show md angry with dissolve
    md "Now get out of my lecture hall. And if any of you tell anyone, I’ll-"
    ax "Yeah! Don’t worry… we won’t."
    "With a great sigh we looked at each other and exited the hall."

    #SETTING: Outside (night)
    scene bg night with dissolve
    show ax calm with dissolve
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    ax "Speaking of the devil… awkward."
    mc "You had to come in at the worst time…"
    ax "I scored us a lunch date with her though!"
    mc "US?! Why did you drag me into this…"
    ax "Because! Because... it would be awkward to have a 1 to 1 conversation with a beast like that!"
    "He points to me and pokes me."
    ax "And because. You. Are. My. Wingman!"
    "I let out a big sigh."
    mc "Fine, whatever."
    mc "What a stressful and awkward situation… Let’s go home now."
    ax "Forreal…"

    #--Scene 2--
    #SETTING: Student Center
    scene bg studentcenter with fade
    play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
    "It’s the next day. Alex and I have a ‘lunch date’ with Melody. I’m pretty sure this is gonna end up badly somehow..."
    show ax calm with dissolve
    ax "Hey dude!"
    mc "Why are you so... dressed up?"
    mc "Is that... cologne?"
    show ax happy with dissolve
    ax "No girl can resist my beautiful physique."
    ax "HAHAHA!"
    mc "Please stop."
    mc "When is she coming?"
    "As I speak, someone snatches my lunch right before my eyes."
    show ax calm:
        linear 0.5 xalign 0.2
    show md calm at right with dissolve
    show md calm:
        linear 0.5 xalign 0.8
    md "Mmmh! This looks good!"
    mc "Hey wa-!"
    mc "..."
    show md happy with dissolve
    md "Thanks for lunch! So nice of you to offer it to me!"
    mc "I… whatever."
    mc "(She did find my phone I guess…)"
    ax "Hel-."
    "Before Alex can finish a word, she instantly dives into my food like a barbarian."
    md "This is sooo good! Did you cook it!?"
    mc "Yeah…"
    md "Waah! You have to invite me over to your place sometimes."
    "She looks at me and smiles innocently and then Alex looks at me and rolls his eyes."
    mc "(So that’s how she wants to play it. The innocent, seductive girl that tries to get the two friends to fight over her...)"
    show md calm with dissolve
    md "Oh hi there Alex! Didn’t see you earlier!"
    ax "You seem awfully happy this afternoon…"
    show md happy with dissolve
    md "That’s because I, the most beautiful and smart girl, aced my quiz."
    mc "(Alex is right… she’s totally different from the night before. She’s… much happier now.)"
    show md calm with dissolve
    md "Oh yeah Alex, what kind of music related, audio-thingy, did you want to talk about?"
    ax "Well-uh…"
    mc "(Alex you fool… you didn’t prepare a subject to talk about did you…)"
    ax "How about… you join my group this year? Hehe?"
    md "Alex…"
    md "No."
    show ax sad with dissolve
    "Alex’s face turns extremely mellow as Melody rejects his offer."
    ax "Huh!? Why not…"
    md "I’m not going to join your group just because you ask me to. I can do whatever I like."
    md "But…"
    "Melody then gives Alex a very distressed look. A kind of innocent and seductive look, kinda like a maiden in distress."
    "Her voice too, started to sound fragile and sincere. She then holds up both of her index fingers and quietly taps them together."
    md "...If you get me a something nice to drink… I might consider helping you out here and there."
    show ax happy with dissolve
    "Alex instantly stood up without hesitation."
    ax "Yes! Of course! Whatever drink you want, I shall buy it and deliver it you!"
    "She then pretends to be charmed by Alex’s hospitality."
    show md happy with dissolve
    md "Ohhh Alex… you’re such a sweet guy. No wonder why all the girls like you so much."
    "Flattered by her over exaggerated words, Alex starts to pad his shoulders and straighten out his outfit."
    mc "(Goodness sake… she got him to make that ‘I’m the best’ face…)"
    mc "(Alex you one gullible fool. You got played by her so hard.)"
    md "I would like a caramel macchiato, hot, with 2 shots of espresso and make it a venti as well!"
    show ax calm with dissolve
    ax "I’ll be right back!"
    hide ax calm with dissolve
    "He bolts off towards the food court."
    show md calm with dissolve
    show md calm:
        linear 0.5 xalign 0.5
    md "Soo… how did I do? That was pretty good, eh?"
    mc "He is the only person, in this universe, who would fall for that."
    md "I know."
    show md happy with dissolve
    "She looks at me and starts to laugh."
    mc "(The way she laughs… it’s pretty charming. I can’t help but to look at her.)"
    show md calm with dissolve
    md "Don’t worry… I’m not trying to use Alex or anything."
    md "I just think it’s cute. Like having a little kid brother."
    show md happy with dissolve
    "With her elbow on the table and one side of face against her curled up hand, she looks at me and smiles."
    "She slowly starts to scan my body with her eyes, from the heads down."
    md "You’re a pretty good looking."
    mc "(I’m not gonna lie… she’s… cu-)"
    mc "(Control yourself man!! You’re falling for the oldest trick in the book!!)"
    show md calm with dissolve
    md "Oh yeah, we haven’t introduced ourselves to each other yet."
    "She extends her hand out towards me."
    md "I’m Melody, nice to meet you [mcname]!"

    #----------Player Choice 2---------
    menu md_menu2:
        "Tell her that I'm not going to fall for her tricks":
            #-----option 1: Tell her that you’re not going to fall for her tricks (Bad)
            mc "Pft. I’m not going to fall for your tricks."
            md "Aww...  you’re no fun."

    #-----option 2: Wait. How did you know my name? (Decent)
        "Wait. How did you know my name?":
            $ md_affection = md_affection + 1
            mc "(How did you know my name?)"
            "She gives a slight grin and remained silent."
            mc "Whatever."
    #-----option 3: Alex told you my name, huh? (Good)
        "Alex told you my name?":
            $ md_affection = md_affection + 2
            mc "(Damn that Alex…)"
            mc "Alex told you my name, huh?"
            "I grabbed her hand with mine and with a firm grip, I shook her hand."
            md "Ahhh… I see. I can’t fool you."
            mc "..."
    #---------End of option 2---------

    show md calm:
        linear 0.5 xalign 0.8
    show ax calm at left with dissolve
    show ax calm:
        linear 0.5 xalign 0.2
    show md happy with dissolve
    "Just as fast as he had left, Alex came back with her order and she pats him on the head and smiles at him."
    md "Thank you Alex."
    show ax happy with dissolve
    mc "(The expression on his face when she patted him… yup. He’s definitely gone now. Dreaming in his own little world…)"
    show md calm with dissolve
    md "Oh yeah, [mcname], are you planning to pitch a game for the club meeting next week?"
    mc "I’ll have to see… I’m not sure if I have time to manage a whole team."
    md "I think you should… the more the merrier!"
    show ax calm with dissolve
    "Suddenly, both Alex’s and Melody’s phone vibrated at the same time."
    mc "Hey you dimwit!"
    "I gently smack Alex on the head as he intensely stares at Melody."
    ax "Huh?"
    mc "Your phone..."
    show ax sad with dissolve
    stop music fadeout 1.0
    "He looked down at his phone and a few seconds after reading the message his mood and tone changes."
    ax "Melody, we have to go. Now."
    md "Yeah… I know."
    hide md calm with dissolve
    show ax calm:
        linear 0.5 xalign 0.5
    ax "Sorry [mcname], but we gotta go. We’ll talk to you later!"
    mc "(Something’s wrong. Something serious…)"
    "I quickly grabbed Alex’s wrist."
    mc "Call me after."
    ax "Yeah."
    hide ax calm with dissolve
    mc "..."
    
    #Scene 3
    #SETTING: Player’s apartment
    scene bg mc_apartment_inside with fade
    "I waited for hours. Waiting for Alex’s call."
    mc "What’s taking him so long… something happened with VGDC."
    show phone with dissolve
    "My phone rang! I quickly grabbed it and picked up."
    mc "Alex! What happened?"
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    ax "...We’re in big trouble."
    mc "What do you mean."
    ax "The whole VGDC board got called in… and not just us… the Dean staff and professors got involved too."
    mc "The Dean… you mean the student affairs people??"
    ax "Yeah…"
    ax "Sooo… it seems that Melody’s work of art from the other day was not liked by the professors too much…"
    ax "The professors weren’t able to give their lectures today because there was graffiti all over the chalkboard. They called us in to clean it up."
    mc "What!? I thought she cleaned up after herself?"
    ax "Well… she didn’t."
    ax "It’s okay though! She didn’t get caught. They don’t have any evidence as to who did it."
    "I let out a big sigh of relief."
    ax "The only evidence that they have is that person probably really, really hates VGDC because a lot of the graffiti was dissing the club."
    mc "Then Melody will be fine as long as she doesn’t do it anymore?"
    ax "Yeah… about that. You know the production officer, Kendrick?"
    mc "Yeah, the guy with the attitude?"
    ax "He’s… accusing Melody of being the one that did it and the two of them got in a big fight. Melody then bolted out the door after."
    mc "That bastard… why does he have to be like that?"
    ax "Well… I probably would’ve done the same thing if I were him."
    play music "/Audio Dumpster/Waiting Music.mp3" fadeout 1.0 fadein 1.0 loop
    "Alex starts to giggle."
    mc "What do you mean and why are you giggling?"
    ax "Let’s just say that the board didn’t believe Kendrick because he’s… a little bit bias."
    ax "So last year, our boy Kendrick had a little crush on Melody…"
    mc "WHAT!? No way! Him and Melody??"
    ax "Yeah he was obsessed with her. He would try to do everything to impress her."
    ax "Finally, one day, he decided to ask her to a school dance in front of EVERYONE at the meeting."
    ax "I was there, front row, when Melody flat out rejected him and embarrassed him in front of everyone!"
    ax "The fool, he already knew that she wasn’t interested in him or anyone, yet he still set himself up for that one."
    "Alex starts to hysterically laugh."
    ax "Duuuude you should’ve seen it. Okay… most of the people felt bad, but I laughed my ass off."
    mc "..."
    ax "I tried to hold it in though, but I couldn’t... and it just bursted out. And then others laughed after too."
    ax "I think that’s probably why Kendrick also hates me as well, but oh well, what can you do."
    ax "That’s also the reason why I think Melody hates the club… Kendrick makes her life so much harder."
    ax "Hey… you still there? Hellooo?"
    mc "Yeah, I’m just a bit shook…"
    mc "(Everything makes sense… the day that I bumped into Kendrick…)"
    ax "Well, that’s basically it. Talk to Melody about it if you see her around and keep our little secret about her artistry low key or else it might escalate to more drama."
    mc "Gotcha. Thanks Alex."
    mc "Wait. One more thing Alex."
    ax "Yeah?"
    mc "Do you think she’ll do it again?"
    ax "I’m… I’m not sure. Keep an eye on her if you can."
    mc "Yeah."
    hide phone with dissolve
    mc "Melody…"
    
    #-------------Scene 4-----------------
    #SETTING: Player’s apartment
    scene bg mc_apartment_inside with fade
    "A few has passed since the incident. I’ve submitted my pitch online and now I’m planning out the game, preparing for the actual pitch next meeting."
    "I haven’t seen or talked to Melody yet…"
    "I took my phone out of my pocket and called Alex."
    show phone with dissolve
    ax "Yo, what’s up."
    mc "Hey, I have a question. Do you know where I can find a piano at school?"
    ax "Yeah there’s a public piano room and concert hall right behind the VGDC club meeting place."
    mc "Alright, thanks."
    ax "Doing a piano lesson or what?"
    mc "Yea-"
    ax "If you’re teaching piano lessons to a girl… and you’re not telling me about it…"
    hide phone with dissolve
    "Without hesitation, I instantly hung up on him."
    mc "Haiyah. That boy and his obsession with girls… unreal."
    
    #SETTING: Piano Concert Hall
    scene bg piano with fade
    stop music fadeout 1.0
    mc "Wow… this room is so beautiful! There’s no one here either…"
    "A grand piano sat on the middle of the wooden stage, surrounded by the warmth of the incandescent lights."
    "The concert hall isn’t enormous, but the mood and the atmosphere is very subtle and cozy."
    "I went on the stage, sat down on the stool, and started to feel the keys on the piano."
    mc "Soft and beautiful as always… I want to test something."
    play music "/Audio Dumpster/Piano Solo 1.mp3" fadeout 1.0 fadein 1.0 loop
    "I started to play a few notes."
    mc "(I’m not a professional pianist, but I know enough to impress a few girls.)"
    mc "(EHhheh…That was pretty cringe... I sounded kinda like Alex for a bit.)"
    "The keys on my fingers felt natural even though I haven’t touched a piano in months. The empty hall was filled by the sound of my creation."
    stop music fadeout 1.0
    mc "That’s enough testing for now…"
    unknown "That was pretty good."
    mc "(A girl’s voice?)"
    "I turned towards the empty stalls to see who it was."
    show md calm with dissolve
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    md "Hey."
    mc "Melody? What are you doing here?"
    md "I should ask you the same question."
    "She got up and walked towards the stage, towards me."
    mc "Just testing something. Don’t worry, you’ll soon see."
    md "Ahhh. Interesting."
    "She stood next to me, while I sat, and slowly starts to move her hand across the surface of the piano keys."
    md "This piano… it’s nice."
    md "Well, nice seeing you again, [mcname]. I’ll see you around."
    show md happy with dissolve
    "She gave me a smile before turning and leaving."
    hide md happy with dissolve
    mc "Something or someone is bothering her… I can feel it."
    mc "Can it be… that Kendrick guy?"
    mc "Hmm. Maybe I’m over thinking it. I should just mind my own business."
    "I got up and before leaving the concert hall, I turned around and gave it one last glance."
    "As I left the room, I turned to my left and saw the president of VGDC next to me. Surprised by his appearance, I took a few step back."
    "He looks at me and gives me a slight, but beautiful smile."
    show gd calm with dissolve
    gd "That was a beautiful piece that you played there."
    mc "(How did he hear me?? I didn’t remembering seeing him in there.)"
    mc "Oh-uh, thanks."
    "He hands me a basic flier."
    gd "It’s a small piano competition here, in a couple of weeks."
    gd "You should come and watch."
    "He walks away while whistling the tune that I just played."
    hide gd calm with dissolve
    mc "What a weird guy..."
    mc "Piano competition? I’ve never watched one before… this might be interesting."
    mc "Pitch day is tomorrow. I gotta get ready ASAP…"
    
    #Scene 5
    #SETTING: anywhere on campus
    scene bg mc_apartment_inside with fade
    mc "Today is pitch day. I’m already getting some massive butterflies…"
    "I nervously walk around my room thinking about project idea."
    mc "What if I stutter up there… no what if I don’t remember what to say. What if I can’t handle it and start to-"
    "My phone rang before I can finish my thought."
    show phone with dissolve
    mc "Hello?"
    ax "Yo. Bad news."
    mc "What happened?"
    ax "Someone told me that Melody plans on publishing her artwork again… so if you see her, keep an eye on her will ya?"
    mc "What is that girl thinking…"
    
    #SETTING: outside anywhere (pref outside lecture hall)
    scene bg sslh with fade
    "I head towards the lecture a few hours before the meeting started."
    mc "(I’m pretty sure she’ll be here…)"
    mc "(There’s no way she’ll be doing it after the meeting. She’ll definitely do it before.)"
    "Once there, I tried opening the doors but they were all locked except for one on the far side. I entered."
    
    #SETTING: lecture hall
    scene bg meeting_1 with dissolve
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    "Instantly, as I entered, she turns around and looks at me."
    show md calm with dissolve
    "I wave at her."
    mc "Hey…"
    "I point and look towards the door."
    mc "You, uh, forgot to lock this door."
    md "How did you know I was here."
    md "Let’s not worry that. You need to get out."
    "She turns back around and continues to vandalize the board."
    md "And what if I don’t."
    "I start to walk towards her."
    mc "Well, if you don’t… First they’ll probably make you clean the board, then kick you out of the club…"
    "I slowly walk up next to her and lightly yank the graffiti pen out of her hand."
    mc "And finally, they’ll probably kick you out of the school."
    "She turns, looks at me and smiles."
    md "Only if I get caught."
    "She pulls out another pen and continues her artistry."
    "I let out a big sigh and continue to observe her ‘artwork’."
    mc "Wow. You must really hate this club. Why not just leave?"
    md "You don’t understand. And anyway, I’m planning to leave this dumpster place soon."
    "I look at the pen, unlocked the cap, and started drawing on the wall."
    mc "This is a nifty pen."
    md "Yup. It’s not permanent. It just takes a reaaaally long time to scrub it of-"
    "Before she can finish her sentence, she turns and looks at me confused, with one eyebrow raised higher than the other."
    md "What are you doing??"
    mc "I’m making your artwork better."
    mc "I think this mierable looking guy needs some cat ears..."
    mc "There! Perfect."
    "I turn to look at her and smile. With her hands on her stomach she suddenly bursts out laughing."
    "That laughter quickly dissolved as noises outside of the lecture hall can be heard and the locked doors start to crackle."
    mc "I think they’re here."
    md "What do you mean, the meeting doesn’t start for another hour."
    mc "No, they’re here for you!"
    mc "We gotta go!"
    "As fast as our feet can move, we went for the closest door near us. As I opened and held door, I took in a breath of fresh air."
    "But there was only one way leading to the main road and as soon as I took a step I catch a glimpse of a silhouette turning at the corner."
    "I quickly pushed Melody back inside and quietly closed the door."
    mc "Go to the other side and leave! They’re already here, I’ll stall for you!"
    md "No… you’ll get caught!"
    #----------Player Choice 3---------
    menu md_menu3:
        "What should I do?"
        #-----option 1: Ask her to trust you. (BEST)
        "As her to trust me":
            $ md_affection = md_affection + 1
            mc "I didn’t do the graffiti so I can make up an excuse, but you’ll get kicked if they find out!!"
            mc "Trust me on this one…"
            md "It doesn’t matter, I’m going to leave anyway!"
            mc "It does matter! I don’t want you to leave. Now go!"
            "I was surprised as she was when I had said those words to her."
            hide md calm with dissolve
            "Speechless, she turns and starts to run for the other door."
        #-----option 2: Tell her to go now and that she’s annoying.(WORSE
        "Tell her to go now and that she's annoying":
            mc "Go now! You’re so annoying, just go! You’ll get both of us caught."
            hide md calm with dissolve
            "She didn’t say anything, but her eyes started to get red. She then turns and heads for the other door."
            mc "(Damn… maybe I shouldn’t have said that.)"
    #----------End of Player Choice 3----------
    "Instantly, as she turns, I headed out once more."
    #SETTING: Outside Lecture Hall
    scene bg sslh with dissolve
    stop music fadeout 1.0
    "In front of me were Jeorge Dan and Kendrick. I froze still as their eyes gaze at mine."
    show kd calm at left with dissolve
    show kd calm:
        linear 0.5 xalign 0.2
    show gd calm at right with dissolve
    show gd calm:
        linear 0.5 xalign 0.8
    kd "Well, well, well. What are you doing out here kid?"
    "He gave off a vicious and cold grin."
    mc "Oh-hey, you guys are from VGDC right? I was just in there looking for my wallet because I had class this morning and I had lost it earlier this morning as well."
    mc "You guys should definitely look inside though… someone has been vandalizing the lecture hall again."
    kd "Again? Interesting how you would know that..."
    mc "(CRAP!!! I didn’t mean to say again, his is bad!!)"
    mc "Well yeah, I heard someone was vandalizing the lecture hall the other day… I guess they did it again."
    "My body couldn’t move. It felt less of a talk and more of an interrogation. I was trapped."
    kd "Then if say that you didn’t do it, did you see who did?"
    mc "I didn’t see anyone when I entered the room from this door."
    show kd angry
    "Irritated by my answer, Kendrick lunges forward with anger and grabs the torso of my shirt with two hands."
    kd "Tell me who did it! I know that you know! Talk!"
    show kd angry:
        linear 0.3 xalign 0.0
    show gd calm:
        linear 0.4 xalign 0.5
    with Pause(0.3)
    show md angry at right with dissolve
    stop music fadeout 1.0
    md "Hey! What’s going on around here. Why are the doors locked as well?"
    "It was Melody. She walked towards us and the two of them turn to look."
    kd "Mind your own business. This kid is a suspect here."
    md "Really? What proof do you have?"
    "Jeorge Dan turns and looks at me."
    gd "Open your hands and show me the pinky side of it."
    "I push Kendrick away and did what Jeorge Dan told me."
    gd "There’s no markings or ink. You’re fine to leave."
    show md calm with dissolve
    kd "What? Are you serious Jeorge Dan?! I’m sure this guy did it or knows who did it."
    gd "Unless there’s evidence or we catch them in the act, then we can’t accuse him."
    gd "Let’s go, Kendrick, we have to clean the hall before the meeting starts."
    hide gd calm with dissolve
    show md calm:
        linear 0.5 xalign 0.8
    show kd angry:
        linear 0.5 xalign 0.2
    "Kendrick stares at Melody with an irritated expression."
    kd "Annoying girl."
    hide kd angry with dissolve
    show md calm:
        linear 0.5 xalign 0.5
    "I moved aside and they entered the hall."
    "I look up at Melody. Our eyes met and I let out a big sigh."
    md "Let’s go."
    hide md calm with dissolve
    "We walk towards the main road."
    
    #SETTING: Ring Road
    scene bg studentcenter_2 with dissolve
    show md calm with dissolve
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    mc "That… was so close."
    md "I’m sorry I got you into that…really."
    #----------Player Choice 4---------
    menu md_menu4:
        "What should I do?"
        #-----option 1: Laugh. (BEST)
        "Laugh.":
            $ md_affection = md_affection + 2
            "I look at her and start to laugh uncontrollably. I then collapsed onto the floor and laid down."
            show md angry with dissolve
            md "What?! What’s so funny?"
            mc "It’s nothing."
            "She gives off an irritated look. I smiled at her."
            mc "I’m just happy that we both got away. But don’t do it again next time!"
            show md calm with dissolve
            md "Yeah… I’ll stop."
            "I raised both my hands in the air. She came over and helped me up."
            mc "Let’s find something to eat until the meeting."
            "After taking a few steps, Melody grabs my hand."
            "I turn around and face her."
            show md happy with dissolve
            md "I… thank you."
            mc "Don’t worry about it..."
            
        #-----option 2: Tell her it’s whatevers.(WORSE)
        "Tell her it's whatevers.":
            mc "It’s whatevers."
            mc "I’m just happy that we both got away. But don’t do it again next time..."
            md "Yeah… I’ll stop."
            mc "Let’s find something to eat until the meeting."
        
        #-----option 3: It’s fine.(MEDIUM)
        "It's fine.":
            $ md_affection = md_affection + 1
            mc "Oh, it’s fine! I still got away…"
            mc "I’m just happy that we both got away. But don’t do it again next time!"
            md "Yeah… I’ll stop."
            mc "Let’s find something to eat until the meeting."
    #----------End of Player Choice 4----------
    
    #SETTING: Lecture Hall
    scene bg meeting_1 with fade
    stop music fadeout 1.0
    mc "My stomach is going to explode… I knew I shouldn’t have eaten before my pitch. Now I have food and butterflies in my stomach."
    "The crowd claps as a girl finishes pitching."
    show gd calm with dissolve
    gd "Next up we have [mcname] who will pitching a game called Gentle Keys."
    mc "Thats me… oh this is not good."
    hide gd calm with dissolve
    "The crowd claps as I slowly walk up to the stage."
    scene bg meeting_2 with dissolve
    mc "(There’s so many people… my stomach…)"
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    mc "(Phewww. Okay. Let’s go.)"
    mc "Hi everyone, my name is [mcname]. My game is called Gentle Keys."
    mc "This game is a rhythm slash music video game. If you’ve ever played Guitar Hero or Osu, it’s similar to that."
    mc "The game is fairly basic, and well be sticking to using piano songs…"
    "I continued to talk until the time ran out."
    mc "Thank you for listening! My game is called Gentle Keys if you guys and ladies are interested."
    "The crowd claps once more and I headed towards the exit to get some fresh air."
    
    #SETTING: Outside Lecture Hall (Night)
label test_md_0:
    scene bg sslh with dissolve
    mc "Phewww… that wasn’t as bad as I thought."
    md "So that’s why you were at the concert hall…"
    mc "Sneaking behind someone is not nice…"
    show md calm at right
    show md calm:
        xalign 1.5
    show md calm:
        linear 0.5 xalign 0.5
    "I turn around to face Melody."
    md "Does it look like I’m a nice person??"
    md "Anyway, I’ve decided… I-"
    unknown "[mcname]!!"
    "Before Melody could finish her sentence, someone screamed out my name behind her."
    show md calm:
        linear 0.5 xalign 0.2
    show ren calm at right with dissolve
    show ren calm:
        linear 0.5 xalign 0.8
    mc "Ren?!"
    ren "Heya! Long time no see."
    "This is Ren. She’s… well kinda like an older sister to me back in high school. She’s a year above me and I only knew her for one year."
    "But we became really close and she treated me like her little sibling."
    mc "(W-wow. Ren’s so different! Her hair… her outfit. She looks so much older and pretti-)"
    md "Hey! You’re not gonna even say hi to me?"
    ren "Oops! Sorry Melody, I got too caught up seeing [mcname] again."
    md "You still didn’t even say hi to me yet…same old Ren."
    "Both Ren and Melody looked at each other and laughed."
    "Ren then runs up to me and with her arms around me, she started to squeeze me tightly with the side of her face on my torso."
    mc "Hey, wait! Get off me, Ren! I smell! I just presented and I’m soaked."
    "Ren started to sniff my torso."
    ren "Liar! You smell so nice! Mmm! It reminds me so much of the good old days."
    ren "I missed you so much!"
    md "Good old days?"
    "One of Melody’s eyebrows raises as she glares at me with a stern and curious look."
    "I start to shake my head violently as Ren continues to squeeze me in her arms."
    mc "(She’s not my ex! She’s not my ex! She’s not my ex!!)"
    mc "Oh HAHAHA! Ren and I are just friends! We’ve known each other back in high school! She would always treat me like a kid, right Ren?"
    "Ren continued to hug me with her cheek rubbing against my body."
    ren "Ohhh... mmmm… uhhh. My precious little Angel."
    "I start to nervously laugh"
    show md angry with dissolve
    "Melody let out a long and sigh and started to shake her head."
    show md calm with dissolve
    md "Oh boy… this is gonna be long."
    mc "Ehhehehe! Okay, I’ll catch up with you more later, Ren! I’ve got to discuss something with Melody."
    ren "Awww… alright. I’ll talk to guys later then! I’ll make sure to join your group too [mcname]!"
    ren "Bye guys!"
    hide ren calm with dissolve
    show md calm:
        linear 0.5 xalign 0.5
    "After waving us good-bye, Ren headed out."
    mc "Ohhh boy… that was unexpected."
    show md angry with dissolve
    "I looked at Melody and she gave me a very, very irritated and impatient look."
    mc "(What should I say now?)"
    menu md_menu5:
        "What should I say now?"
        #----------Player Option 5------------
        #option 1: "It’s not what you think." (Middle)
        "It's not what you think.":
            $ md_affection = md_affection + 1
            mc "I promise you… it’s not what you think!"
            mc "We’re just friends! She’s just a touchy person!"
            show md happy2 with dissolve
            "With her hand on her stomach she bursts out laughing."
            mc "Why are you laughing??"
            md "Because that was too cringy to watch."

        #option 2: "I swear, she’s not my ex girlfriend." (Best)
        "I swear, she's not my ex girlfriend.":
            $ md_affection = md_affection + 2
            "I turn to look at Melody."
            mc "I swear, she’s not my ex girlfriend."
            mc "She’s just a touchy person!"
            show md happy2 with dissolve
            "With her hand on her stomach she bursts out laughing."
            mc "Why are you laughing??"
            md "Because that was too cringy to watch."

        #option 3: "She’s kinda cute, don’t ya think." (Middle)
        "She's kinda cute, don't ya think?":
            $ md_affection = md_affection + 1
            mc "She’s kinda cute, don’t ya think?"
            md "You know what I think?"
            "Melody starts to curl her fingers into a fist."
            md "I think you need a big fat punch!"
            mc "EH? Why?!"
            "She tosses her punch half way, but then stops and cross her arms instead."
    #--------End of Option-----------
    show md calm with dissolve
    md "Anyway, I’m still mad and annoyed because you ignored me earlier."
    mc "Huh? I did?"
    show md angry with dissolve
    "When I said those words, her eyebrows started to arc and she looked even more annoyed."
    md "Hpmph. I’ve decided to join your group. Don’t tell anyone."
    mc "Eh?! Really??"
    "With her arms crossed and a stern look on her face, she starts to walk away."
    hide md angry with dissolve
    mc "Oi! Wai-"
    mc "(Is she… angry at me? There’s no way it’s my fault.)"
    mc "(She’s probably having one of those moody days of the month...)"
    mc "Yup. That’s probably it."
    mc "But damn… Ren got a lot cuter than before…"
    mc "Shoot… I should get home, it’s getting kinda late."
    
    #SCENE 6

    #SETTING: Anywhere outside, ring road
    scene bg studentcenter_2 with fade
    stop music fadeout 1.0
    "It’s been a week since pitch night. Melody said she wanted to meet up today to talk about the game. I still couldn’t believe that she wanted to join my group…"
    "She asked me to meet her up at the piano room. I’m guessing she wants me to record her a few pieces in order to create the audio for the game."
    with hpunch
    "Suddenly, as I walk towards the piano room, a random guy bumps into me."
    mc "My bad, sorry."
    show kd calm with dissolve
    kd "If it isn’t the rat again."
    play music "/Audio Dumpster/Bad Ending.mp3" fadeout 1.0 fadein 1.0 loop
    "It was Kendrick and he has a malicious smirk on his face."
    mc "What do you want?"
    show kd angry with dissolve
    kd "What do I want? I WANT YOU TO TELL ME WHO DID IT!"
    kd "I know you know."
    "He grabs me by my shirt. I coldly look at him in the eyes."
    mc "I don’t know."
    show kd angry:
        linear 0.5 xalign 0.2
    show md calm at right with dissolve
    show md calm:
        linear 0.5 xalign 0.8
    md "Let him go."
    show kd calm with dissolve
    kd "Ahhh… your little princess to the rescue again?"
    kd "I wonder how long she’ll be around to help you."
    kd "I hoping she does leave. She doesn’t deserve to be here at all."
    show kd calm:
        linear 0.5 xalign -1.5
    hide kd calm with dissolve
    show md calm:
        linear 0.5 xalign 0.5
    "He starts to laugh wickedly and walks."
    stop music fadeout 1.0
    mc "(I really wanted to punch him…)"
    md "Hey, are you okay?"
    mc "Yeah. I’m fine. I handle bullies all the time."
    mc "Oh yeah, what did you want to talk about?"
    md "Follow me!"
    "She grabs my hand and started to run towards the piano room."
    mc "Hey! Wait!..."
    #SETTING: Piano Room
    scene bg piano with dissolve
    show md calm with dissolve
    md "We’re here."
    md "I wanted you to..."
    mc "Play the piano for you to record for the audio?"
    show md happy with dissolve
    "She nods her head and smiles."
    mc "Yeah, that’s no problem at all!"
    show md calm with dissolve
    "I turn to look towards the stage."
    mc "Well… I guess we’ll have to wait our turn. There’s someone here before us."
    "Melody turns and looks at the stage."
    hide md calm with dissolve
    md "Oh… him."
    show gd calm with dissolve
    play music "/Audio Dumpster/Piano Solo 1.mp3" fadeout 1.0 fadein 1.0 loop
    "As we both look, he started to play."
    mc "Wow… Jeorge Dan’s pretty good. He’s really good!"
    hide gd calm with dissolve
    "I look towards Melody and she looked unimpressed and annoyed."
    show md angry with dissolve
    md "Yeah he’s good, but does he have to take up our spot."
    mc "(Our?)"
    md "Let’s just go to the other piano room…"
    mc "I think he’s almost done..."
    hide md angry with dissolve
    stop music fadeout 1.0
    "As Melody starts to walk away, Jeorge Dan stopped playing and claps from one person can be heard."
    mc "Is that Ren??"
    show md angry with dissolve
    "Irritated, she turns and looks at me."
    md "Let’s go."
    #PLAYER CHOICE 6----------
    menu md_menu6:
        "What should I do?"
        
        "Tell her that we should go down there to meet them":
            #-------option 1---------: Tell her that we should go down there to meet them. (Worse)
            mc "Let’s go down there and meet them instead!"
            "Her irritated expression turned for the worse."
            md "Do whatever you want."
            "She starts to leave the building."
            hide md angry with dissolve
            mc "Hey wait!"
            "I quickly followed her as she exits."

        "Listen and go with her":
            #-------option 2---------: Listen and go with her. (Good)
            $ md_affection = md_affection + 1
            mc "Okay, let’s go."
            "I quickly followed her as she exits."
    #------------End of choice 6------------
    #SETTING: OUTSIDE
    scene bg park_1 with fade
    "We recorded the music that Melody needed and then she left… I wonder why she seemed so irritated back at the concert hall…"
    "Was it because of Jeorge Dan? Well… I guess she really does hate the club. But why is she still in it if she hates it?"
    "Tonight is the club meeting and also results… I wonder if Melody is actually in my group."
     
    #SCENE 7 
    #Setting: Outside
    scene bg dbh_inside with fade
    "Today’s our first group meeting."
    "Yesterday was the club meeting and I was pretty surprise to see the results. I totally did not expect it all…"
    #Setting: Meeting place
    scene bg gameroom with dissolve
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "I walk inside to our meeting place and the first thing I noticed was Alex holding her hands between his."
    show ax calm at left with dissolve
    show ax calm:
        linear 0.5 xalign 0.2
    show ren calm at right with dissolve
    show ren calm:
        linear 0.5 xalign 0.8
    ax "Ren, ohhh Ren! I still can’t believe I’m this lucky to be in a group with such a beautiful girl."
    ren "Awww, thank you Alex! You’re such a sweetheart!"
    md "Oh buddy… you fall victim to girls way too easily. I feel bad for you."
    "Ren was the first one to notice me."
    ren "[mcname]!!"
    "She dashes toward me and wraps her arms around me."
    show ax happy with dissolve
    ax "Hey dude! You finally made it!"
    show ax calm with dissolve
    show ax calm:
        linear 0.4 xalign 0.0
    show ren calm:
        linear 0.3 xalign 0.5
    show md calm at right with dissolve
    md "The leader is the last one to be here huh?"
    mc "Hey everyone…"
    "I look around the room to get a good look at everyone."
    "This is my team… the four of us."
    "Alex is our designer/programmer, Ren is our artist, Melody is our audio girl, and I’m the producer."
    "I guess our team is solid for this game project."
    "It was pretty unexpected. I thought that Alex was going to have his own group since he was pitching…"
    "But it turns out that no one wanted to join his project so he chose to be in mine. That’s good though, because we don’t really have that many members."
    "I didn’t think Ren would be in our group, but I guess after seeing me, she really wanted to be in my group."
    "I guess she thinks I’m pretty cute!"
    "And Melody… well I knew she was going to be in my group but it still feels like a dream."
    "She looks so beauti…"
    mc "By the way! I just realized… how come we have 2 officer buddies for such a small group?"
    ax "Wait, Melody, you didn’t tell [mcname]?"
    md "Oh yeah… I dropped the board gig. I’m not a board member anymore."
    md "It didn’t suit me anyway."
    mc "Oh… that makes sense."
    "I had a feeling that she was going to drop the board position, but it was a surprise to see her do it so early…"
    mc "Well then… "
    "Everyone stares at me intensely as I spoke."
    mc "Firstly… can you all stop staring at me!!"
    md "Oh yeah, let me just stare at a wall while you talk!"
    show ax happy with dissolve
    "Alex and Ren start to laugh uncontrollably."
    mc "..."
    show ax calm with dissolve
    mc "Okay guys! This game should be pretty simple and straightforward! We also all know each other so this will be easy for us to collaborate."
    mc "I sent you guys a work schedule and your roles. Let’s get to work everyone!"
    ax "Sounds good!"
    md "Yup."
    ren "Wait!!"
    "Instantly everyone turns to look at Ren."
    ren "Before we start, I have a gift for everyone!"
    "She pulls out 3 slips of paper and hands them to everyone."
    ren "They’re tickets to the Fall Fair this week!"
    ren "I’m volunteering there and they gave out free tickets, so as a gift, I’m giving one to each one of you!"
    ax "Ren!!! I can’t accept this… unless…"
    ren "Unless?"
    ax "Unless I can go with you."
    mc "EHHH?"
    "I quickly moved my hands to cover my eyes."
    mc "(This is embarrassing… I can’t watch him get rejected.)"
    ren "Of course Alex! I’m free on the weekends at night!"
    mc "(No way…)"
    show ax happy with dissolve
    ax "Yes!!! This has to be my luckiest day ever!"
    md "That was… unexpected."
    mc "Alright Alex, you fool, get to work before I kick you out of here!"
    show ax calm with dissolve
    ax "Sorry! Sorry!"
    "I couldn’t help but to laugh a little… everyone felt the same."
    "This group is... perfect. Hopefully we don’t run into any dilemmas."
    
    #SCENE 8
    #SETTING: Player’s Apartment
    scene bg mc_apartment_inside with fade
    stop music fadeout 1.0
    "The first group meeting went well the other day… It was so much fun working with everyone. Alex, Ren, and especially Melody all looked pretty happy."
    mc "What should I do today… it’s the weekend and I guess I should take my mind off school."
    "As I ponder, my eyes took notice of the piece of paper that Jeorge Dan had handed to me that one time."
    mc "The piano competition huh?"
    mc "I wonder if he’ll be there… I guess I’ll check it out."
    mc "He was pretty good when I watched him that one time. I wonder if he’s even better in a competition."
    #SETTING: Concert Hall
    scene bg piano with fade
    play music "/Audio Dumpster/Large Room Background.mp3" fadeout 1.0 fadein 1.0 loop
    mc "There’s actually a lot more people than I had expected. The hall’s almost filled up!"
    "I went to find a seat and sat down as the competition begins."
    stop music fadeout 1.0
    unknown "Hi everyone, welcome to our this year’s competition!"
    unknown "We’ll start off right away with our first contestant, Miss Melody!"
    mc "Melody… WHAT?!"
    mc "It can’t be the same Melody??"
    "I focused my eyes heavily towards the stage to see the first contestant walk onto the stage."
    show md calm with dissolve
    mc "It’s her!!! No way, she knows how to play the piano?!?"
    mc "That dress… she looks amazing..."
    "She was wearing an extremely beautiful dress. And her sheer beauty alone had many of the guys in the audience screaming out her name."
    "The crowd of excited college boys started to quiet down as she begins to play."
    play music "/Audio Dumpster/Piano Solo 2.mp3" fadeout 1.0 fadein 1.0 loop
    mc "She’s really good…"
    "The way she plays the piano… it wasn’t natural, It wasn’t formal…"
    "It was aggressive and exciting almost to point where you would want to just stand up and cheer."
    "Her style of aggression... played perfectly."
    mc "Beautiful…"
    play music "/Audio Dumpster/Applause.mp3" fadeout 1.0 fadein 1.0 loop
    "As she finishes up, the crowd ejected from their seats while claps and screams of her name travel throughout the audience."
    "As the cheering continues, I settle my eyes towards her. Not once did I blink."
    mc "Melody… she didn’t tell me that she can play the piano."
    mc "I should go backstage and meet her!"
    hide md calm with dissolve
    "My phone rings. I took a step outside to answer it."
    show phone with dissolve
    play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Yeah, what’s up Alex?"
    ax "Ren… she’s busy!! So she can’t go to the fair with me!!!"
    "I started to hear sobbing noises coming from the phone."
    mc "Are you… crying? Man up!!"
    ax "I can’t… I- I had the perfect chance and now it’s gone."
    mc "Well… you can always go later with her…"
    ax "I’m already here…"
    mc "Oh dear… I guess I’ll come…"
    ax "Really?"
    mc "Well… I can’t leave you all by yourself…"
    hide phone with dissolve
    scene bg black with fade
    "I hung up and started to walk towards the fair."
    mc "This guy is like a child...."
    #SETTING: Fall Fair
    scene bg fair with fade
    mc "Yo."
    show ax happy with dissolve
    ax "You made it! This is gonna be a fun friend date!"
    mc "If you put it that way, I’ma go home."
    ax "Joking! Joking!"
    show ax calm with dissolve
    "We went up to a stall and we decided to play their game in order to win a prize. Then two familiar faces showed up from a distance."
    "Alex turns his eyes towards the two of them and his excitement quickly returned to a depressed state."
    ax "So that’s what she meant by ‘busy’…"
    "Ren was walking aside the president of VGDC, Jeorge Dan."
    mc "It’s okay buddy, there are more fish in the ocean for you to catch."
    "I continued to play the game and landed a hoop onto the tip of the glass bottle."
    "The lady hands me my prize of a stuffed animal and a bracelet."
    mc "Here take this. I call her Ren."
    "I handed him the teddy bear that the lady handed me."
    ax "Real funny…"
    "I started to laugh."
    "We hung out and checked the stalls out a little bit more and then headed home."
    ax "Hey… thanks for hanging out with me."
    mc "I had to… your date bailed on you."
    ax "..."
    mc "I’m joking Hahaha. Alright, laters Alex."
    ax "See ya."
    hide ax calm with dissolve
    stop music fadeout 1.0
    "I held the bracelet in my hand as I start to walk home. The bracelet had a music note on it as a design."
    mc "I should give this to Melody… she’ll like it."
    
    #--------Player Choice 7-----------
    menu md_menu7:
        "What should I do?"
        
        "Call her.":
            #Option 1(good): Call her.
            $ md_affection = md_affection + 1
            "I took out of my phone and started to call her."
            show phone with dissolve
            md "What’s up?"
            mc "Where are you?"
            md "I’m at the concert hall at school."
            mc "This late?"
            md "Yeah, I’m just chilling here by myself."
            mc "Do you need company?"
            md "No…"
            mc "Hmmm…"
            md "But I do need someone to play the piano so I can record it for our game."
            "I started to laugh."
            mc "I’ll be there in a few."

        "Nah, don't call her.":
            #-----Option 2: Nah, don’t call her.------
            mc "Maybe next time…"
            mc "Watching her today was very refreshing…"
            mc "She made me want to play."
            "I start to head back to the school, towards the concert hall."

    #END OF CHOICE 7-----------------

    #SETTING: Concert Hall
    scene bg piano with fade
    show md calm with dissolve
    mc "Don’t you get lonely being here by yourself?"
    md "I prefer the loneliness most of the time."
    "I walk towards her as she sits on the piano stool."
    mc "Here. I got this for you."
    "Reaching for my pocket I took out the bracelet and handed it to her."
    md "It’s a cute bracelet. I like the design."
    mc "An interesting thing happened today."
    md "Hmm?"
    "I sat myself down on the stool beside her. And started to touch the piano keys."
    md "Hey… wait! Did I say you can sit next to me?!"
    mc "One sec, let me finish. So I went to this event, and there was this girl, in a beautiful dress, sitting in this exact spot, and beautifully played this song."
    play music "/Audio Dumpster/Piano Solo 2.mp3" fadeout 1.0 fadein 1.0 loop
    "I started to dance my fingers on the keys and played the similar song that she played earlier this morning."
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    "I then turn to look at her. Her eyebrows started to curl inward and her cheeks started to turn red."
    md "You were watching me?!"
    mc "Yeah… and so were like 50 other guys screaming your name Hahaha."
    mc "you’re pretty popular."
    md "I just play for fun…"
    mc "I was shook when I heard your name and saw you play… you didn’t tell me that you play the piano."
    md "It’s not a big deal."
    mc "You’re really good."
    show md happy with dissolve
    md "Thanks…"
    show md calm with dissolve
    "We sat there, together, silently for a minute."
    md "I was planning to leave the club at the start of this year..."
    md "But after meeting you, I thought it would be fun to stick around a little bit longer, until our project is done."
    mc "Hmm…"
    mc "Is there a reason… for why you’re leaving, if you don’t mind?"
    md "Not my place to be I guess…"
    mc "Kendrick? Alex told me about you two."
    md "Oh that little thing?"
    md "Sort of... We were pretty good friends back then, but he just took everything the wrong way."
    md "But that’s not the main reason."
    md "I guess you can say that I’m a little similar to Kendrick…"
    mc "What do you mean?"
    md "I… I was pretty close to someone as well. But it’s hard to be around someone who doesn’t feel the same way."
    mc "One way love, I assume?"
    "She starts to smile, but sadness can be seen within that smile."
    md "You’re good at catching on."
    mc "Nothing is ever the same once you confess your feelings for the person you love..."
    mc "It can either be reciprocated with the start of a beautiful chapter-"
    md "Or rejected with an end to a friendship."
    md "And the love that you have for that person… it will hurt you more than ever."
    mc "The most beautiful love is the one that is not forced…"
    mc "So that’s why you’re leaving…"
    md "Yeah… I just have to accept things for what they are and move on."
    mc "(The person she loves…)"
    mc "We should leave soon! It’s getting way too late."
    md "Mmm. You go first, I’m going to stay here for another minute."
    mc "I’m sorry to hear about that…"
    show md happy with dissolve
    "She shakes her head and smiles."
    hide md happy with dissolve
    "As I turn to walk away, she grabs me by my jacket sleeve."
    show md calm with dissolve
    "I turn around towards the girl who’s sitting in front of me with her head down."
    "With one hand on my sleeve, and the other holding the bracelet, her tears started to fall… hitting the ground as they fall…"
    #SCENE 9
    #SETTING: player’s apartment
    scene bg mc_apartment_inside with fade
    stop music fadeout 1.0
    "Last night… that incident with Melody."
    "I can’t keep her off my mind… and him."
    "She’s leaving after this project. I need to talk to her today, after the group meeting."
    "My phone rang as I ponder around my thoughts."
    show phone with dissolve
    mc "Alex?"
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    ax "Come to the lecture hall, now!!"
    mc "What happened?"
    ax "Melody is in trouble!"
    hide phone with dissolve
    "I hung up the phone and instantly dashed out my door."
    #SETTING: Lecture Hall
    scene bg meeting_1
    "Instantly, after entering the lecture hall, my body froze in place as I observe the the walls and boards had graffiti all over it."
    "At the bottom of the lecture hall, near the podium, were Alex and Melody, next to each other, and facing them, across a table, were Kendrick, and Jeorge Dan."
    "After observing the situation, I quickly rush to them."
    mc "What’s going on?!"
    show kd angry with dissolve
    kd "None of your business, brat."
    "My eyes met with Kendrick as he spoke to me. I can see a spiteful happiness coming from his face."
    hide kd angry with dissolve
    "Ignoring me, Jeorge Dan looks directly towards Melody."
    show gd serious at left with dissolve
    show gd serious:
        linear 0.3 xalign 0.2
    show md angry at right with dissolve
    show md angry:
        linear 0.3 xalign 0.8
    gd "As you can see, the room has been vandalized by someone. This person has been causing the club quite a lot of trouble."
    gd "Kendrick found this object, here, at the lecture hall, and Kendrick identifies it to be yours, Melody."
    gd "Is this your bracelet?"
    "He tosses the object onto the table."
    "It was the bracelet with the music note design that I gave to Melody..."
    mc "(She couldn’t have done it! She was with me last night!! Someone has to be framing her.)"
    mc "If this is about Melody being the person vandalizing the room, I can tell you that it’s not her! She was with me last night!"
    mc "Melody! Tell them!"
    "She stood there, with her head down, without saying a word."
    gd "Melody, I ask you again, is this your bracelet?"
    "She looks up and their eyes met. Sadness filled her eyes as Jeorge Dan confronts her."
    "She then looks at the bracelet that I gave to her."
    show md calm with dissolve
    md "Yes."
    show gd serious:
        linear 0.4 xalign 0.0
    show md calm:
        linear 0.3 xalign 0.5
    show kd calm at right with dissolve
    "Pleased from hearing Melody say those words, Kendrick gives off a nasty smirk."
    kd "Finally caught the vixen."
    mc "(I need to shut this guy up!!)"
    show gd serious:
        linear 0.5 xalign -1.5
    show md calm:
        linear 0.4 xalign -1.5
    show kd calm:
        linear 0.3 xalign -1.5
    with Pause(0.3)

    show ax sad
    show ax sad:
        linear 0 xalign 1.5
    show ax sad:
        linear 0.3 xalign 0.5
    "As I move barely an inch towards Kendrick, Alex quickly grabs me and locks me down."
    ax "Sorry… but you shouldn’t make the situation worse."
    mc "Let me go Alex!"
    ax "I’m sorry, just wait till it’s over first. Please keep your cool."
    "Alex holds me down as I struggle to get loose."
    show ax sad:
        linear 0.5 xalign 1.5
    hide ax sad with dissolve
    
    show gd serious:
        linear 0.5 xalign 0
    show md calm:
        linear 0.4 xalign 0.5
    show kd calm:
        linear 0.3 xalign 1.01
    gd "Then Melody, were you the person responsible for the vandalism that happened the past few times?"
    kd "Come on Jeorge Dan, she already confessed that she’s the person. Just report her to the school and get it over with."
    md "Yes…"
    mc "No… no…"
    "Kendrick turns to Jeorge Dan and starts to laugh comfortably."
    kd "I told you! I knew it."
    "Ignoring Kendrick, and with a subtle, but somber expression, he looks at Melody."
    gd "Leave the club, Melody, and I won’t report this to the school."
    kd "What?! You’re letting her off too easily! Just report her to the Dean so she can get expelled for this atrocious act."
    stop music fadeout 1.0
    "Jeorge Dan and Melody, their heavy-hearted eyes met once more."
    md "I’m sorry... for saying those words."
    hide md calm with dissolve
    "Suddenly, Melody turned and bolted towards the door, with her tears falling as she ran past me."
    "Shook by the event that just happened, my whole body and mind froze in place as I stare at Jeorge Dan."
    kd "I can’t believe you let her go that easily… well at least she’s gone now. She never deserved to be in our club anyway."
    "Alex’s hold on me suddenly loosened. As I noticed his release, I ceased my eyes from staring at Jeorge Dan and turned it towards Alex..."
    show gd serious:
        linear 0.5 xalign -1.5
    show kd calm:
        linear 0.3 xalign -1.5
    with Pause(0.3)
    hide kd calm with dissolve
    hide gd calm with dissolve

    show ax sad at right 
    show ax sad:
        linear 0 xalign 1.5
    show ax sad:
        linear 0.3 xalign 0.5
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    "It wasn’t the joyful Alex, full of life Alex, or the cool headed Alex that I was looking at…"
    ax "Hey... [mcname]... grab the bracelet and find her will ya."
    ax "Don’t…"
    hide ax sad with dissolve
    show kd calm with dissolve
    "Suddenly, without warning, he lunges forward towards Kendrick and punches him in the face with his right hand."
    show ax sad at right
    show ax sad:
        linear 0 xalign 1.5
    show ax sad:
        linear 0.3 xalign 0.5
    with Pause(0.2)
    show kd angry
    show kd angry:
        linear 0.3 xalign 0
    with hpunch
    kd "OUGHHH!"
    ax "DON’T EVER TALK TO HER LIKE THAT YOU SWINE!!!!"
    "Alex then turns and looks at me with pure anger in his eyes."
    ax "What are you doing!?"
    ax "GO!! I’ll hold them back!!"
    hide ax sad with dissolve
    hide kd angry with dissolve
    "I quickly ran past them, towards Jeorge Dan, and grabbed the bracelet."
    show gd serious with dissolve
    "Our eyes met… He didn’t stop me…"
    hide gd serious with dissolve
    "With God’s speed, I turned and ran out of the lecture hall."
    mc "Don’t leave… please."
    
    if md_affection >= 6:
        jump md_good_ending
    else:
        jump md_bad_ending
        
    #SCENE 10
    #Setting: outside
label md_good_ending:
    #Good Ending--------------
    scene bg park_1 with dissolve
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Hey…"
    show md angry with dissolve
    "Standing a couple of yards away from me, she turns and looks."
    "Her somber eyes met mine as I approach her."
    "Without saying anything, I open my hand with the bracelet inside it."
    "Looking at the bracelet, she touches it…"
    mc "I-"
    "Tears started to fall from her eyes once again."
    "As the first of many tears hit the ground, she suddenly lunges towards me."
    show md calm with dissolve
    "With her hands grabbing the torso of my shirt, and the side of her face resting against my chest she began to cry helplessly."
    "I slowly place my arms around her… holding her tightly."
    mc "I will follow you… wherever you go."
    #----Black------
    scene bg black with fade
    "The night at the concert hall, after the festival, when I gave Melody the bracelet…"
    "I saw him as I left."
    #SETTING: Outside at night
    scene bg night with dissolve
    show gd calm with dissolve
    "We both stared at each other, neither one moving a muscle."
    gd "How was the performance at the concert hall today?"
    mc "You… you knew Melody would be there… and the flier."
    gd "Follow her. Wherever she goes… follow her."
    gd "And give her what I couldn’t."
    scene bg black with fade
    ".:. Good Ending."
    return

    #Bad Ending---------------
label md_bad_ending:
    scene bg park_2 with dissolve
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Hey…"
    "Standing a couple of yards away from me, she turns and looks."
    show md angry with dissolve
    "Her somber eyes met mine as I approach her."
    "Without saying anything, I open my hand with the bracelet inside it."
    show md calm with dissolve
    "Looking at the bracelet, she touches it…"
    "Tears started to fall from her eyes once again."
    md "I’m sorry [mcname]... my feelings for him… have not gone away."
    "She turned and ran."
    "She ran away… farther and farther away… from my grasp."
    scene bg black with fade
    ".:. Bad Ending."
    $ MainMenu(confirm=False)()
    #return
