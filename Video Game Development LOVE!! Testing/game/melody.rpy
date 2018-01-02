define md_affection = 0
# max affection = 8

#DIALOGUE:
#--Scene 1:--
#SETTING: Outside (Night)
label melody_scene1:
    scene bg outside_night with fade
    show ax calm with dissolve
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
    show ax frown with dissolve
    ax "What?!? Are you serious…?"
    "He has a hopeless look on his face that can probably make any girl go ‘Awww, Alex’."
    mc "Yeah, but why does that matter? You like her or something?"
    ax "You don’t understand… I’ve been trying to get at her for the longest time..."
    mc "Since When!?"
    ax "Since last week."
    "I raised my hand and smacked him on the head lightly."
    mc "You freaking player. I thought you were serious."
    show ax calm with dissolve
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
    "He starts to laugh hysterically."
    show ax happy with dissolve
    ax "Comeeee on… good girls ain’t no fun, am I right?"
    mc "I wouldn’t know…"
    ax "But yeah, she’s the ‘Hard to get’ kinda girl, so I really, reaaally want to impress her."
    ax "You don’t understand how many guys tried to get at her last year…"
    ax "And did you not see the look on their faces this year?! She’s more desirable than ever!"
    mc "You talk about her as if she’s an object…"
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
    "As I start running to the lecture hall, I accidentally bumped into someone on the shoulder. They gave off an angry expression."
    with hpunch
    show kd concerned with dissolve
    kd "Watch where you're going, Kid."
    mc "My bad…"
    kd "Pst. Get out of my way..."
    mc "Damn... isn’t he the production guy? What an ass..."
    "I got to the lecture hall and luckily the doors were still open...."

    #SETTING: Lecture Hall
    scene bg meeting_2 with dissolve
    "When I entered the lecture hall, the board was covered in graffiti and then I saw Melody drawing graffiti on the far wall. ‘VGDC sucks.’ was one of the messages on the wall."
    "She turned around with a blank expression on her face, like a deer when you shine your high beams at it."
    show md calm with dissolve
    md "Damn… I forgot to lock the doors."
    "I felt frozen in place. What should I do?"
    #----------Player Choice 1---------------#
    menu md_menu1:
    #option 1: Apologize and tell her that you’re just here to look for your phone. (Worse)-----
        "Apologize and tell her that I'm just here to look for my phone":
            mc "Uh, I'm really sorry. I, um, well, I-"
            md "You’re looking for your phone right?"
            mc "Yes… how’d you kn-?"
            md "Here. Catch."
            "She tosses the phone across the lecture hall to me."
            mc "(I barely caught it… this girl is crazy.)"
            mc "Uh… thanks."
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
            md "Looking for this?"
            "In her hand was my phone."
            mc "Y-yeah…"
            md "Since you ignored me..."
            md "I’ll tell ya what. Tell me your name, then kneel on the floor and beg for your phone… and MAYBE I’ll give you it back."
            mc "(Pft… does she really think I’m going to be her dog? Play fire with fire.)"
            mc "What if I don’t… and instead I tell the board members what you’re doing right now."
            md "You dare threaten me…?  Hmfph… this arrogant punk."
            "She gave off an angry and aggressive smirk."
            mc "Alright… you win."
            "She tosses the phone across the lecture hall to me."
            mc "(I barely caught it… this girl is crazy.)"
            "If you tell anyone this, I’ll make sure you’ll regret ever coming to UCI."
            "Her aggressive tone and words sent shivers throughout my whole body and soul."
            "I felt as if I was the deer being hunted. I’m wasn’t playing with fire… I was sinking in the middle of the ocean!"

    #----------End of Player Choice 1----------
    hide md calm with dissolve
    "Right before I left Alex came running through the door."
    show ax calm with dissolve
    mc "(Oh no!! This is bad…)"
    ax "Hey dude, slow down next ti..."
    "He gazed around the room with a shocked expression on his face…"
    ax "You.. didn’t do this in like 10 seconds did you...?"
    mc "No…"
    "I pointed my finger towards her."
    "Alex formed his hand into a gun-like formation with his index finger pointing towards her."
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
    show ax calm with dissolve
    show ax calm:
        linear 0.5 xalign 0.2
    show md calm at right with dissolve
    show md calm:
        linear 0.5 xalign 0.8
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
    md "Now get out of my lecture hall. And if any of you tell anyone, I’ll-"
    ax "Yeah! Don’t worry… we won’t."
    "With a great sigh we looked at each other and exited the hall."

    #SETTING: Outside (night)
    scene bg outside_night with dissolve
    show ax calm with dissolve
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
    "It’s the next day. Alex and I have a ‘lunch date’ with Melody. I’m pretty sure this is gonna end up badly somehow..."
    show ax calm with dissolve
    ax "Hey dude!"
    mc "Why are you so... dressed up?"
    mc "Is that... cologne?"
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
    md "Oh hi there Alex! Didn’t see you earlier!"
    ax "You seem awfully happy this afternoon…"
    md "That’s because I, the most beautiful and smart girl, aced my quiz."
    mc "(Alex is right… she’s totally different from the night before. She’s… much happier now.)"
    md "Oh yeah Alex, what kind of music related, audio-thingy, did you want to talk about?"
    ax "Well-uh…"
    mc "(Alex you fool… you didn’t prepare a subject to talk about did you…)"
    ax "How about… you join my group this year? Hehe?"
    md "Alex…"
    md "No."
    show ax frown with dissolve
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
    md "Ohhh Alex… you’re such a sweet guy. No wonder why all the girls like you so much."
    "Flattered by her over exaggerated words, Alex starts to pad his shoulders and straighten out his outfit."
    mc "(Goodness sake… she got him to make that ‘I’m the best’ face…)"
    mc "(Alex you one gullible fool. You got played by her so hard.)"
    md "I would like a caramel macchiato, hot, with 2 shots of espresso and make it a venti as well!"
    show ax calm with dissolve
    ax "I’ll be right back!"
    hide ax calm with dissolve
    "He bolts off towards the food court."
    show md calm:
        linear 0.5 xalign 0.5
    md "Soo… how did I do? That was pretty good, eh?"
    mc "He is the only person, in this universe, who would fall for that."
    md "I know."
    "She looks at me and starts to laugh."
    mc "(The way she laughs… it’s pretty charming. I can’t help but to look at her.)"
    md "Don’t worry… I’m not trying to use Alex or anything."
    md "I just think it’s cute. Like having a little kid brother."
    "With her elbow on the table and one side of face against her curled up hand, she looks at me and smiles."
    "She slowly starts to scan my body with her eyes, from the heads down."
    md "You’re a pretty good looking."
    mc "(I’m not gonna lie… she’s… cu-)"
    mc "(Control yourself man!! You’re falling for the oldest trick in the book!!)"
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
            $ gd_affection = gd_affection + 1
            mc "(How did you know my name?)"
            "She gives a slight grin and remained silent."
            mc "Whatever."
    #-----option 3: Alex told you my name, huh? (Good)
        "Alex told you my name?":
            $ gd_affection = gd_affection + 2
            mc "(Damn that Alex…)"
            mc "Alex told you my name, huh?"
            "I grabbed her hand with mine and with a firm grip, I shook her hand."
            md "Ahhh… I see. I can’t fool you."
            mc "..."
    #---------End of option 2---------

    ### END OF UPDATES ###
    show md calm:
        linear 0.5 xalign 0.2
    show ax calm at right with dissolve
    show ax calm:
        linear 0.5 xalign 0.8
    "Just as fast as he had left, Alex came back with her order and she pats him on the head and smiles at him."
    md "Thank you Alex."
    mc "(The expression on his face when she patted him… yup. He’s definitely gone now. Dreaming in his own little world…)"
    md "Oh yeah, [mcname], are you planning to pitch a game for the club meeting next week?"
    mc "I’ll have to see… I’m not sure if I have time to manage a whole team."
    md "I think you should… the more the merrier!"
    "Suddenly, both Alex’s and Melody’s phone vibrated at the same time."
    mc "Hey you dimwit!"
    "I gently smack Alex on the head as he intensely stares at Melody."
    ax "Huh?"
    mc "Your phone..."
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
    "Without hesitation, I instantly hung up on him."
    mc "Haiyah. That boy and his obsession with girls… unreal."
    
    #SETTING: Piano Concert Hall
    mc "Wow… this room is so beautiful! There’s no one here either…"
    "A grand piano sat on the middle of the wooden stage, surrounded by the warmth of the incandescent lights."
    "The concert hall isn’t enormous, but the mood and the atmosphere is very subtle and cozy."
    "I went on the stage, sat down on the stool, and started to feel the keys on the piano."
    mc "Soft and beautiful as always… I want to test something."
    "I started to play a few notes."
    mc "(I’m not a professional pianist, but I know enough to impress a few girls.)"
    mc "(EHhheh…That was pretty cringe... I sounded kinda like Alex for a bit.)"
    "The keys on my fingers felt natural even though I haven’t touched a piano in months. The empty hall was filled by the sound of my creation."
    mc "That’s enough testing for now…"
    unknown "That was pretty good."
    mc "(A girl’s voice?)"
    "I turned towards the empty stalls to see who it was."
    show md calm with dissolve
    md "Hey."
    mc "Melody? What are you doing here?"
    md "I should ask you the same question."
    "She got up and walked towards the stage, towards me."
    mc "Just testing something. Don’t worry, you’ll soon see."
    md "Ahhh. Interesting."
    "She stood next to me, while I sat, and slowly starts to move her hand across the surface of the piano keys."
    md "This piano… it’s nice."
    md "Well, nice seeing you again, [mcname]. I’ll see you around."
    hide md calm with dissolve
    "She gave me a smile before turning and leaving."
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
    scene bg park_1 with fade
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
    "Irritated by my answer, Kendrick lunges forward with anger and grabs the torso of my shirt with two hands."
    kd "Tell me who did it! I know that you know! Talk!"
    show kd calm:
        linear 0.5 xalign 0
    show gd calm:
        linear 0.5 xalign 1
    show md calm with dissolve
    md "Hey! What’s going on around here. Why are the doors locked as well?"
    "It was Melody. She walked towards us and the two of them turn to look."
    kd "Mind your own business. This kid is a suspect here."
    md "Really? What proof do you have?"
    "Jeorge Dan turns and looks at me."
    gd "Open your hands and show me the pinky side of it."
    "I push Kendrick away and did what Jeorge Dan told me."
    gd "There’s no markings or ink. You’re fine to leave."
    kd "What? Are you serious Jeorge Dan?! I’m sure this guy did it or knows who did it."
    gd "Unless there’s evidence or we catch them in the act, then we can’t accuse him."
    gd "Let’s go, Kendrick, we have to clean the hall before the meeting starts."
    hide gd calm with dissolve
    "Kendrick stares at Melody with an irritated expression."
    kd "Annoying girl."
    hide kd calm with dissolve
    "I moved aside and they entered the hall."
    "I look up at Melody. Our eyes met and I let out a big sigh."
    md "Let’s go."
    hide md calm with dissolve
    "We walk towards the main road."
    
    #SETTING: Ring Road
    scene bg studentcenter_2 with dissolve
    show md calm with dissolve
    mc "That… was so close."
    md "I’m sorry I got you into that…really."
    #----------Player Choice 4---------
    menu md_menu4:
        "What should I do?"
        #-----option 1: Laugh. (BEST)
        "Laugh.":
            $ md_affection = md_affection + 2
            "I look at her and start to laugh uncontrollably. I then collapsed onto the floor and laid down."
            md "What?! What’s so funny?"
            mc "It’s nothing."
            "She gives off an irritated look. I smiled at her."
            mc "I’m just happy that we both got away. But don’t do it again next time!"
            md "Yeah… I’ll stop."
            "I raised both my hands in the air. She came over and helped me up."
            mc "Let’s find something to eat until the meeting."
            "After taking a few steps, Melody grabs my hand."
            "I turn around and face her."
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
    mc "My stomach is going to explode… I knew I shouldn’t have eaten before my pitch. Now I have food and butterflies in my stomach."
    "The crowd claps as a girl finishes pitching."
    show gd calm with dissolve
    gd "Next up we have [mcname] who will pitching a game called Gentle Keys."
    mc "Thats me… oh this is not good."
    hide gd calm with dissolve
    "The crowd claps as I slowly walk up to the stage."
    scene bg meeting_2 with dissolve
    mc "(There’s so many people… my stomach…)"
    mc "(Phewww. Okay. Let’s go.)"
    mc "Hi everyone, my name is [mcname]. My game is called Gentle Keys."
    mc "This game is a rhythm slash music video game. If you’ve ever played Guitar Hero or Osu, it’s similar to that."
    mc "The game is fairly basic, and well be sticking to using piano songs…"
    "I continued to talk until the time ran out."
    mc "Thank you for listen! My game is called Gentle Keys if you guys and ladies are interested."
    "The crowd claps once more and I headed towards the exit to get some fresh air."
    
    #SETTING: Outside Lecture Hall (Night)
    scene bg sslh with dissolve
    mc "Phewww… that wasn’t as bad as I thought."
    md "So that’s why you were at the concert hall…"
    mc "Sneaking behind someone is not nice…"
    "I turn around to face Melody."
    show md calm with dissolve
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
    Ren "Heya! Long time no see."
    "This is Ren. She’s… well kinda like an older sister to me back in high school. She’s a year above me and I only knew her for one year."
    "But we became really close and she treated me like her little sibling."
    mc "(W-wow. Ren’s so different! Her hair… her outfit. She looks so much older and pretti-)"
    md "Hey! You’re not gonna even say hi to me?"
    Ren "Oops! Sorry Melody, I got too caught up seeing [mcname] again."
    md "You still didn’t even say hi to me yet…same old Ren."
    "Both Ren and Melody looked at each other and laughed."
    "Ren then runs up to me and with her arms around me, she started to squeeze me tightly with the side of her face on my torso."
    mc "Hey, wait! Get off me, Ren! I smell! I just presented and I’m soaked."
    "Ren started to sniff my torso."
    Ren "Liar! You smell so nice! Mmm! It reminds me so much of the good old days."
    Ren "I missed you so much!"
    md "Good old days?"
    "One of Melody’s eyebrows raises as she glares at me with a stern and curious look."
    "I start to shake my head violently as Ren continues to squeeze me in her arms."
    mc "(She’s not my ex! She’s not my ex! She’s not my ex!!)"
    mc "Oh HAHAHA! Ren and I are just friends! We’ve known each other back in high school! She would always treat me like a kid, right Ren?"
    "Ren continued to hug me with her cheek rubbing against my body."
    Ren "Ohhh... mmmm… uhhh. My precious little Angel."
    "I start to nervously laugh"
    "Melody let out a long and sigh and started to shake her head."
    md "Oh boy… this is gonna be long."
    mc "Ehhehehe! Okay, I’ll catch up with you more later, Ren! I’ve got to discuss something with Melody."
    Ren "Awww… alright. I’ll talk to guys later then! I’ll make sure to join your group too [mcname]!"
    Ren "Bye guys!"
    "After waving us good-bye, Ren headed out."
    mc "Ohhh boy… that was unexpected."
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
            "With her hand on her stomach she bursts out laughing."
            mc "Why are you laughing??"
            md "Because that was too cringy to watch."

        #option 2: "I swear, she’s not my ex girlfriend." (Best)
        "I swear, she's not my ex girlfriend.":
            $ md_affection = md_affection + 2
            "I turn to look at Melody."
            mc "I swear, she’s not my ex girlfriend."
            mc "She’s just a touchy person!"
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
    md "Anyway, I’m still mad and annoyed because you ignored me earlier."
    mc "Huh? I did?"
    "When I said those words, her eyebrows started to arc and she looked even more annoyed."
    md "Hpmph. I’ve decided to join your group. Don’t tell anyone."
    mc "Eh?! Really??"
    "With her arms crossed and a stern look on her face, she starts to walk away."
    mc "Oi! Wai-"
    mc "(Is she… angry at me? There’s no way it’s my fault.)"
    mc "(She’s probably having one of those moody days of the month...)"
    mc "Yup. That’s probably it."
    mc "But damn… Ren got a lot cuter than before…"
    mc "Shoot… I should get home, it’s getting kinda late."
