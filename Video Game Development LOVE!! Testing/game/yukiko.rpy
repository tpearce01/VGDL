## YUKIKO ROUTE ##
# INTRO SCENE
label yu_scene1:
    play music "/Audio Dumpster/Waiting Music.mp3" fadeout 1.0 fadein 1.0 loop
    mc "(Programming sounds like my cup of tea, so I'm going to try to talk to the programming officer.)"
    mc "(She's the cheerful girl who forcibly escorted me to the club yesterday.)"
    mc "(She seems the most approachable out of all the officers, but that might serve as a double-edged sword.)"
    "I look for her on the stage."
    "From afar, I can see a large crowd of prospective members are circling around her."
    "Justifying my laziness with the excuse of giving her one less person to deal with, I decide to talk to her tomorrow."
    "Not feeling like meeting people and knowing what to now, I just allow the bustling of the lecture hall to fill my senses."
    mc "(The group of lively people clamoring while sharing one common interest.)"
    mc "(The energetic officers who express their passion for their field in different ways.)"
    mc "(I hear a lot of good and bad advice from the students here, like attending the first meeting of a lot of clubs lets you get a feel for if the club is a good fit for you.)"
    mc "(At least they're right about that.)"
    "With nothing particularly eventful happening for the rest of the meeting, I decide to call it a night."
    pause 5.0
    scene bg park_2 with dissolve
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    "I walk out of my boring lecture into the fair weather and stifle a yawn."
    mc "(I know I shouldn't, but I stayed up last night again.)"
    "I pull out my phone while walking slowly and aimlessly on the park's paths."
    mc "(Yesterday's club meeting was interesting.)"
    "The programming officer's name is... Yukiko?"
    mc "(Oh well. If I want to learn how to program, then she would be the best officer to talk to.)"
    "I clutch my phone hopefully and shuffle weakly over to the game lab."
    scene bg black with dissolve
    pause 5.0
    "There's a large sign on the door to the game lab indicating that food and drink are forbidden."
    #play sound "knock.ogg"
    #door opening
    scene bg gameroom with dissolve
    show re calm with dissolve
    mc "Hi, is the programming officer here right now?"
    re "Sorry, Yukiko isn't here right now..."
    mc "Oh, that's okay."
    mc "(Ugh, maybe I should've tried to talk to her yesterday after all.)"
    mc "I'll come back later."
    hide re with dissolve
    "I take my leave while shutting the door at the same time."
    mc "(I actually feel like crashing on the nearest soft surface right now.)"
    "I attempt to drag myself back home."
    scene bg park_1 with dissolve
    stop music fadeout 1.0
    "... and I end up collapsed in the park on the grass."
    mc "(I can't do it anymore...)"
    mc "(I'll rest my eyes, just for a little...)"
    scene bg black with fade
    "My vision fills with black as sleep overtakes me."
    pause 5.0
    mc "Ngh........... nnn."
    mc "Just five more minutes..."
    "I allow my eyes to peek open ever so slightly."
    "An unpleasant orange immediately stains my vision as I realize I am facing the sunset."
    "I turn over onto my other side away from the light."
    "As I prepare to shut my eyes to return to my slumber, I notice the sight of a faint purple."
    "Opening my eyes further reveals a rather unexpected scene before me."
    mc "Whoa!"
    scene bg park_1
    "I bolt upwards to a sitting position in surprise."
    "Right in front of me is a girl sleeping peacefully on her back."
    "Her long, straight purple hair is slightly astray with strands wavering in the wind."
    mc "(Actually, this wind is getting really strong.)"
    #play sound "wind.ogg"
    #play sound "snap.ogg"
    "A relatively large branch suddenly falls towards her."
    mc "Get out of the way!"
    "She began to stir."
    "Without thinking, I dash into a standing position with her between and below my legs with my back towards the falling branch's trajectory."
    show yu calm with dissolve
    show yu calm:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 0.5
    "Her crimson eyes flicker for a moment before dilating and meeting mines, seemingly lasting forever due to the adrenaline."
    "As if she understood just by our brief exchange of gazes, her sleepy face snaps to one of urgency as she suddenly jumped up and tackled me."
    play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
    mc "OOHOUGH!"
    "I wasn't prepared for a hit by a surprising amount of force from the front, so I toppled backwards onto the grass, disheveled but out of harm's way."
    "The branch hits the ground with a loud crack."
    "We sit there in surreal silence for a few moments before the girl sitting on top of me finally speaks."
    show yu nervous with dissolve
    yu "Gosh, what are you doing?"
    yu "That branch almost hit you!"
    "Her girly, singsong voice comes out light but worried."
    mc "Wait, what?!"
    mc "That's my line!"
    mc "A branch fell towards you while you were sleeping and I was trying to block it."
    show yu calm with dissolve
    yu "Hmm, that's what happened?"
    mc "Yes, it did..."
    mc "(Why did I even try?)"
    show yu happy with dissolve
    yu "C'mon, cheer up!"
    yu "Sorry, I was just teasing you."
    "I put my hand on my forehead in exasperation and suddenly wince in pain."
    show yu calm with dissolve
    yu "Oh, you have a cut on your hand."
    "She fumbles around in her pocket for a moment before pulling out two bandaids."
    show yu happy with dissolve
    yu "which one would you like?"
    mc "Uhh.."
    yu "Bzzt, time's up; you get both!"
    show yu calm with dissolve
    "Her face resets into one of pure concentration."
    yu "Oh wait, I should probably clean this first."
    "She pulls out a handkerchief and gently wipes the blood and dirt from my injury."
    yu "I'm sure I should have put some antiseptic on first, but we don't have that right now..."
    "She tears open a bandaid and carefully places it over my cut, her hands working with an unexpected speed and precision."
    mc "You seem like you're used to this."
    yu "..."
    "She repeats the process except with another bandaid, forming a cross pattern on the back of my hand."
    show yu happy with dissolve
    "Admiring her work, she smiles to herself in satisfaction while still sitting on me."
    show yu calm with dissolve
    mc "Could you move of--"
    yu "Sorry, did you say something earlier?"
    mc "Oh, uh, you seem like you're used to this."
    show yu nervous with dissolve
    yu "Ah, I tend to get little cuts and bruises a lot."
    yu "Sometimes, when I'm walking around and thinking about something, I bump into a whole lot of stuff!"
    mc "Is that why you carry bandaids on you?"
    show yu happy with dissolve
    yu "Yep!"
    show yu calm with dissolve
    yu "Did they help you feel better?"
    mc "Sure, but why two?"
    yu "It's cooler that way."
    yu "Don't you think it's like some cool symbol thingy on your hand?"
    show yu happy with dissolve
    yu "Everyone knows crosses are cooler than straight lines."
    yu "Like, paths having crossed once is more charming than being parallel lines who are always besides each other but will never touch?"
    mc "But couldn't you just use one bandaid though?"
    mc "(God, I'm letting myself get caught up in this girl's pace.)"
    yu "But one bandaid by itself will get lonely."
    show yu calm with dissolve
    "The girl directs her eyes upwards and rests an index finger on her chin, as if thinking."
    "I expect another eccentric line out of her but she quickly subverts my expectations again."
    yu "Hey, aren't you [mcname]?!"
    show yu happy with dissolve
    "Contrary to what I expected, her face lights up with the intensity of a thousand suns."
    mc "I was looking for you."
    mc "(To be honest, I've never had anyone so earnestly happy to see me before.)"
    mc "(That, and I'm beginning to become more conscious of her weight on me.)"
    "I can feel my face begin tinting a light shade of crimson."
    show yu calm:
        ease.5 zoom 2.0
    "She leans in a bit closer despite already sitting on me."
    yu "What can I do for you today?"
    mc "You can get off me first."
    show yu calm:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 1.0
    show yu nervous with dissolve
    yu "Oh, sorry."
    "She whispers that rather quietly."
    mc "(That was surprisingly meek of her.)"
    stop music fadeout 1.0
    "We dust the dirt and plant matter off ourselves."
    show yu calm with dissolve
    show yu calm:
        ease .5 zoom 1.0
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Why were you napping next to me?"
    yu "Well, I walked to the game lab and Reina described a male student who was looking for me."
    mc "(I wonder what Reina said about me...)"
    yu "I remembered I abduct -- I mean persuaded a guy matching the description yesterday to join the club."
    #change to happy sprite in the middle of the line? "I mean persuaded"
    mc "(No, you totally kidnapped me.)"
    yu "I was walking back and noticed you napping on the grass."
    yu "You looked so peaceful, I didn't want to wake you."
    show yu calm with dissolve
    yu "I sat down and waited, but the weather was so nice and cool."
    yu "The birds were chirping, and the rays of the sun were so warm!"
    mc "Don't worry, I understand. I would have napped too."
    show yu happy with dissolve
    yu "Riiiiiight?"
    mc "Now why was I looking for you again?"
    yu "Programming?"
    yu "It's the only thing I do."
    mc "Oh, right, programming!"
    show yu calm with dissolve
    yu "What's your experience level?"
    mc "I'm a complete beginner."
    "I look away rather sheepishly."
    show yu happy with dissolve
    yu "Don't worry! Learning is what this club is for."
    yu "Everyone starts somewhere."
    mc "When did you start?"
    show yu nervous with dissolve
    yu "Uhh..."
    mc "Hmm?"
    yu "When I was... six."
    mc "Oh."
    yu "Sorry, I didn't mean to get you down."
    yu "Don't worry [mcname], what we do here is for everybody to learn!"
    show yu happy with dissolve
    yu "I'll teach you personally!"
    yu "Or if you would prefer something else, there are a lot of tutorials online on how to get started with Python!"
    yu "Python is what they teach here in the introductory class and it's the easiest to get started with, and--"
    "The school bell chimes."
    mc "Oh crap, I'm gonna be late for my evening lab!"
    show yu sad with dissolve
    yu "Oh..."
    "She looks a bit disappointed, but I don't have a choice."
    mc "I'll see you at the programming workshop, okay?"
    mc "(I tell that her gently as if somehow consoling her.)"
    show yu happy with dissolve
    yu "Yep!"
    mc "(Well, she got better quickly.)"
    yu "See you later!"
    mc "Bye!"
    yu "By the way, thanks for protecting me!"
    hide yu happy with dissolve
    "She scurries off before I could say anything else."
    "I turn around and walk away with what must have been a smile on my face."
    "It then occurs to me that I forgot to ask her when the workshop will be."
    scene bg black with fade
#end of intro

#scene1 programming workshop
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "A week later in the game lab..."
    scene bg gameroom with dissolve
    show yu nervous with dissolve
    yu "A-and so, for testing code, they say that ninety percent of the work goes into the last ten percent of software, so it's like ten times the effort for a tenth of the fun..."
    "She says all this with strange inflections in her tone of voice."
    yu "(She's so nervous..)"
    "Yukiko proceeds to drop all her notes onto the floor."
    yu "Ahh! I'm so sorry everyone!"
    mc "(Wow, she's a mess right now.)"
    mc "(I don't know much about programming to be able to say anything to help her out.)"
    "A few other students and I stand up to help her gather her dropped papers."
    scene bg black with dissolve
    "The rest of the meeting went shakily but steadily."
    "Much to Yukiko's dismay, a lot of students had questions for her afterwards."
    "I waited until everyone dispersed to approach her."
    scene bg gameroom with dissolve
    show yu sad with dissolve
    yu "Uuuu..."
    show yu sad:
        parallel:
            ease .5
        parallel:
            linear 0.5 yalign 1.7
    "She slumps down onto a desk in the corner."
    mc "Hey, Yukiko."
    show yu sad:
        parallel:
            ease .5
        parallel:
            linear 0.5 yalign 1.3
    "From the top of the desk, she directs a cute upward gaze against me as if projecting a telepathic barrier with her eyes to prevent any further inquiries."
    "I almost felt like a criminal walking up to her."
    mc "That must have been stressful."
    "Her eyes give up on arresting me and face forward into empty space."
    show yu calm with dissolve
    yu "I wish it wasn't."
    mc "What do you mean?"
    yu "I always get like this with large groups."
    yu "The way the saying goes is to picture everyone in their underwear, but really, how would that help?"
    yu "If anything, I would feel like I'm the one who's out of place being the only one wearing clothes."
    "Yukiko sighs."
    yu "Two is great, three's a party, but any more than that.. I.."
    mc "Get overwhelmed?"
    "She gives a slight nod with her head as much as being on a flat surface would allow."
    mc "You were so talkative when you met me though."
    show yu nervous with dissolve
    yu "I just woke up from a nap so I was refreshed and the adrenaline of almost being hit by a branch and you seemed like a good person and--"
    "I might be imagining it, but it looks like her eyes are spinning in circles from the speed at which she is looking around."
    mc "Thanks. It wasn't what I expected when I took a nap in the park, but I had fun talking to you."
    show yu calm with dissolve
    "Her eyes lock onto me again."
    yu "Really?"
    "She utters that word timidly."
    mc "I mean it. I mean, you seem like a person who would have a lot of friends."
    "As the words left my mouth, I immediately regret speaking before thinking."
    show yu sad with dissolve
    "My fears are justified as her hopeful expression unravels."
    yu "That's not true, though."
    yu "I've talked to a lot of people here, but I don't have many people I can call a friend."
    yu "At this school, maybe only Reina."
    mc "Maybe?"
    #play sound "knock.ogg"
    "As if we spoke of the devil, Reina suddenly enters the game lab."
    show re calm at left with dissolve
    "As she scanned the room for a place to sit, Reina's expression changes from a slight smile upon spotting Yukiko to a slight frown upon seeing me."
    re "Yuki... is he bothering you?"
    "I involuntarily flinch at the timid girl's uncharacteristically sharp words."
    mc "(Now that I think about it, standing over and talking down to Yukiko like this looks like I'm trying to intimidate her.)"
    mc "Oh sorry, I was just.."
    show yu happy:
        parallel:
            ease .5
        parallel:
            linear 0.5 yalign 1.0
    show re surprised with dissolve
    show re surprised:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.2
    show yu happy:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.0
    "Yukiko stands up and suddenly glomps Reina."
    show re blush with dissolve
    re "Kyah!"
    show re blush:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.1
    pause .5
    show re blush:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.3
    pause .5
    show re blush:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.1
    pause .5
    show re blush:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.2
    #Reina blush and wriggling a bit
    "Reina wriggles around a bit like a captured animal, but quickly lets out a sigh of resignation to her fate."
    yu "Don't worry Reina. He was just comforting me after my big workshop flop."
    show re calm with dissolve
    re "Yuki, you know the only reason they always have questions is because they aren't getting what you're saying during your presentation."
    show yu sad with dissolve
    yu "Uuuu..."
    show re calm with dissolve
    re "That being said... if you have any worries... you can just come to me."
    "Yukiko seems speechless for a moment, but quickly turns into sunshines and rainbows in response to Reina's encouragement."
    show yu happy with dissolve
    yu "Reina!"
    show yu happy:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.1
    "She holds onto Reina even tighter."
    show re surprised with dissolve
    re "Agh.. I'm choking.."
    "I couldn't help but fail at surpressing a laugh at such a heartwarming scene."
    show re calm wth dissolve
    "Reina seems to be uncomfortable but I couldn't shake the feeling that she looks slightly happy."
    re "Well? What's on your mind?"
    yu "I... don't have many friends here."
    re "And that bothers you, right?"
    yu "Yeah."
    show re calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 yalign 1.2
    "Reina shrinks down a bit deeper into Yukiko's embrace."
    re "I know... I'm the worst person you could ask for advice about this but..."
    re "I see you talking to a lot of people all the time."
    show yu sad with dissolve
    yu "Right?"
    re "Wait.. I'm not finished."
    re "At least from my perspective... when you talk to them..."
    re "It looks like you're not being yourself."
    show yu calm with dissolve
    yu "Really?"
    mc "(I wonder if the Yukiko who bandaged me is the same as the Yukiko sitting in front of me right now.)"
    re "So what you can do is..."
    re "At least for me.. I don't want many friends."
    re "But if you're not satisfied with your amount of friends, you should go out and talk to people."
    re "Not like talking, but... connecting."
    yu "You mean like speaking what's on my mind, or..?"
    re "Not exactly that..."
    mc "I've kind of read a book about this before."
    mc "Maybe you have to stop being polite and start being real?"
    mc "Not everyone will like you so you have to show people who you really are so they can decide to like you or not?"
    "They both stare at me."
    mc "Oh sorry, that sounds silly, doesn't it?"
    yu "No, it doesn't."
    re "If you backpedal now... you would be a hypocrite."
    yu "Since [mcname] would be denying what he just said?"
    mc "(Ack, they got me there!)"
    mc "I was just mentioning something I read; it doesn't mean I necessarily believe in it."
    yu "True..."
    mc "But then again, knowing about the books someone reads probably tells a lot about them..."
    scene bg black with fade
    stop music fadeout 1.0
    "We continue to discuss how to make friends for a good hour."
    scene bg park_2 with dissolve
    show yu happy
    show re calm
    with dissolve
    show yu happy:
            linear 0.5 xalign 0.4
    show re calm:
            linear 0.5 xalign 0.6
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    "Even while walking back in the park, Yukiko clings to Reina."
    "We walk for a while in comfortable silence."
    "Fortunately for me, right after I begin pinning myself as the third wheel, Reina speaks up."
    re "This is where I'm turning... so..."
    show re calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 yalign 1.8
    pause 0.5
    show yu calm with dissolve
    show re calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 1.2
    pause 1.0
    show re calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 yalign 1.0
    "Reina effortlessly slips out under Yukiko's arms by simply kneeling down and sliding out of her embrace."
    re "See you later, Yuki..."
    show re calm:
        linear 2.0 xalign 2.0
    hide re calm with dissolve
    show yu calm:
        linear 0.5 xalign 0.5
    "Reina scampers off without another word."
    yu "Poor Reina must be really exhausted from all that socializing."
    "I thought that Yukiko would be sad, but it seems like she had her fair share of Reina today."
    yu "She doesn't usually talk that much at all."
    mc "How did you become friends?"
    show yu happy with dissolve
    "She poses her arms on her hips and puffs her chest out proudly."
    yu "I caught her alone in the game lab one day and the rest was history."
    mc "(You caught her..?)"
    mc "I'd like to hear more about that potentially incriminating evidence you just--"
    #play sound "phone.ogg"
    "Before I can investigate the dangerous potential predator standing in front of me, my phone interrupts me."
    mc "Sorry, can I take this?"
    yu "Of course!"
    "I answer my phone to the voice of a friend I made at school."
    mc "What's up? Yeah. Oh, I'm just walking back from around the computer science building. Sounds fun! Okay. Alright, see you then."
    "I was about to hang up when an idea abruptly pops into my head."
    mc "Actually, wait..."
    define yu_hang = 0
    menu yu_menu1:
        "What should I do?"
        "Invite Yukiko to hang out with us":
            $ yu_hang = yu_hang + 1
            play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
            "I put down my phone for a moment."
            mc "Hey Yukiko, wanna go grab a bite with us?"
            show yu nervous with dissolve
            "She begins fidgeting and hesitates to answer until I give her an encouraging smile."
            yu "Um, sure."
            scene bg foodcourt with dissolve
            "We head to the food court and I grab some overpriced fish tacos."
            "Yukiko just asks for a water cup."
            "....."
            "Time passes as we just chat together about nothing in particular."
            "....."
            "It was a bit awkward, but Yukiko's true personality shined through here and there."
            "My friends part ways for class while getting the wrong idea about Yukiko and I, goading me as they left."
            show yu calm with dissolve
            mc "I swear they're nice people."
            yu "You all seem to get along very well."
            show yu sad with dissolve
            yu "... I was just being weird."
            mc "No, you weren't being weird. You were fine."
            mc "It's only natural to be a bit reserved when you first meet people."
            show yu nervous with dissolve
            yu "Um, [mcname], can I ask you a question?"
            mc "You just did."
            yu "Can I ask you another question after this question?"
            mc "Shoot."
            yu "Um, I just had a feeling, so if I'm totally wrong, just correct me, but..."
            mc "Mmhmm?"
            yu "You seemed like you were making an extra effort involve me in the conversations."
            mc "What made you think that?"
            yu "You were being pretty awkward yourself."
            mc "Ugh..."
            "I feel like I had just been stabbed in the chest."
            mc "So that's how it looked to you."
            show yu happy with dissolve
            yu "Thank you, [mcname]."
            "I can't stop my face from flushing slightly as I deny it."
            mc "Nah, I didn't do anything..."
            "I quickly change the subject."

        "Hang out with just Yukiko":
            #[Neg. Option] "No"
            mc "Something came up today. I have to pass this time."
            mc "Mmhm, talk to you later. Bye."
            #cell phone beep
            mc "Now, where were we?"
            show yu calm with dissolve
            yu "Who was that?"
            mc "Just some friends seeing if I want to hang out."
            yu "Shouldn't you go hang out with them?"
            mc "I don't feel like it today."
            show yu happy with dissolve
            yu "Uwaaah, [mcname] sure is mean to his friends!"
            mc "Okay, the real reason is that when I meet a new friend, I like to spend time to get to know them."
            yu "Who's that? Have I met them before?"
            "I flash a smile at Yukiko who returns a confused smile."
            mc "(Wait, is she serious?)"
            show yu calm with dissolve
            yu "..."
            mc "It's you."
            yu "..."
            yu "Oh! I didn't think of that."
            show yu happy with dissolve
            "She rests a fist on the back of her head, flashes a smile, and sticks her tongue out while winking."
            mc "(I'm not sure if I find that cute or disturbing.)"
            show yu calm with dissolve
            mc "Wanna go grab a bite?"
            yu "Okay."
            hide yu calm with dissolve
            scene bg black with fade
            play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
            "We head to the food court and I grab some overpriced fish tacos."
            "Yukiko just asks for a water cup."
            scene bg foodcourt with dissolve

    show yu calm with dissolve
    mc "Hey Yukiko, what kind of food do you like?"
    yu "I don't really like food."
    "I stop eating."
    mc "What."
    mc "How can you not like food?"
    show yu happy with dissolve
    yu "Aha, sorry. I phrased that wrong."
    show yu calm with dissolve
    yu "I try to go as long as possible without eating."
    yu "When I do have to eat, I just inhale the minimum amount of food I need to function and I hurry back to my computer."
    "She picks up one of my fish tacos and devours it one bite to demonstrate."
    mc "MY TACO!!!"
    "I melodramatically agonize over the death of my beloved taco."
    yu "What's in a fish taco?"
    mc "Didn't you just eat it?"
    yu "I didn't taste anything though."
    mc "What a waste..."
    "I grit my teeth and clutch my fist while staring downwards to observe a moment of silence for the wasted food."
    yu "You know, I do love water though."
    "I couldn't help but stare at her curiously."
    yu "I just have to take a sip and I already feel refreshed."
    yu "I can also keep a bottle next to me at my desk all the time."
    mc "So you're saying bottled water is the best thing to happen since sliced bread?"
    show yu happy with dissolve
    yu "No, [mcname], I'm saying programming is the best thing to happen since bottled water!"
    mc "Or is bottled water the best thing to happen since programming?"
    show yu calm with dissolve
    yu "Ehh? I haven't thought about it that way."
    yu "....."
    mc "....."
    show yu happy with dissolve
    yu "Pfft.."
    mc "Hahahaha!"
    "We both laugh to ourselves and have a good time until we part for class."
    scene bg black with fade
#end of scene1
    pause 5.0
#scene2 player gets a team and help with programming
    stop music fadeout 1.0
    "I haven't seen Yukiko since we had lunch together, but we exchanged numbers before we left."
    "We texted each other mostly about random crap, like how four hours of sleep isn't a lot, but a four hour nap is."
    "I sheepishly grin to myself walking to the building where the club meeting is taking place again."
    scene bg sslh with dissolve
    mc "(I would be lying if I said I don't look forward to our weird exchanges.)"
    scene bg meeting_1 with dissolve
    "I enter the lecture hall in the middle of someone's game pitch and get a few looks from the packed audience."
    "I hasten my walk of shame and plop down into the first random seat I could find."
    "The current pitch doesn't catch my interest so my eyes inevitably begin wandering around the room."
    "I notice that most of the officers sit together on the stage, maintaining an air of professionalism."
    mc "(What's Yukiko doing?)"
    show yu calm with dissolve
    "I see Yukiko listening to the pitches like the good officer she is."
    mc "Wait..."
    "Now that I look more closely, I notice she is actually staring in the podium's general direction. Her eyes aren't focused."
    "She seems to be silently drumming her fingers on her leg."
    mc "Poor Yukiko..."
    "I silently offer a prayer for her."
    "Her eyes suddenly dart towards my direction."
    mc "(It's just a coincidence, right? Or she could be looking at someone else.)"
    "Her eyes quickly shift back to the direction of the podium."
    "I remind myself that the students pitching the games are putting their ideas out there and deserve respect."
    hide yu calm with dissolve
    "I shift my attention back to the speaker."
    "The current student's pitch describes programming in lua for a game mod."
    mc "(It can't be THAT game, can it?)"
    "As the pitch goes on, the student never mentions the name of the game, but all the clues point to a game I hold dear to my heart as part of my childhood."
    scene bg meeting_1 with vpunch
    mc "Larry's Mod!"
    "In my fit of nostalgia, I accidentally blurt that out rather loudly and attract the attention of nearby audience members and the officers."
    show kd angry
    show md angry at right
    show gd serious at left
    with dissolve
    "I receive a lot of sideway looks for my interruption. Some of the officers appear to be arresting me with their gazes."
    hide kd angry
    hide md angry
    hide gd serious
    with dissolve
    pause 2.0
    show yu calm with dissolve
    "Yukiko is trying in vain to give me a disciplinary look, but her quivering features indicates she appears to be preoccupied with suppressing a smile."
    "I mutter a meek apology dispersed in no one's direction in particular and remain dead silent for the rest of the presentations."
    "It's fine though, because I know which project I want to work on."
    scene bg black with fade
    play music "/Audio Dumpster/Large Room Background.mp3" fadeout 1.0 fadein 1.0 loop
    "The rest of the pitches finish and I head towards the stage to join the other students asking officers and game pitchers questions."
    scene bg meeting_1 with dissolve
    show yu nervous with dissolve
    "Most of the members are programmers, so a rabid pack of students are swarming Yukiko with questions."
    mc "(Wouldn't Reina help Yukiko right now?)"
    hide yu nervous with dissolve
    pause 2.0
    show re calm with dissolve
    "I look for Reina, but she is occupied with her own group of students."
    mc "Right, then."
    hide re calm with dissolve
    mc "(Plus, trying to help Yukiko out would be considered coddling her, wouldn't it?)"
    mc "(But helping out just a little bit wouldn't hurt, right?)"
    "I wrack my brain for ideas."
    mc "(Yukiko said she's bad with big groups...)"
    mc "(Wait, duh! If they asked one-by-one, it would be easier on her! Why aren't they doing that to begin with?)"
    show yu nervous with dissolve
    "I stride over and break through Yukiko's circle of interviewers."
    "I clear my throat and prepare my best voice of authority."
    mc "Hey guys, I think everyone would get their questions answered a lot faster we asked one at a time!"
    stop music fadeout 1.0
    "Everyone observes a moment of silence during which I imagined being lynched by the mob."
    "Yukiko looks at me surprised like everyone else for a moment, but gives an almost invisible nod to show that she got my cue."
    show yu happy with dissolve
    yu "I think that's a great idea, w-would everyone form a neat, single-file line for me please?"
    "It's as if everyone suddenly remembers that they're mature, adult college students."
    "A line forms in front of Yukiko and she tackles their inquiries one-on-one with the speed of an experienced officer."
    "I watch her proudly like a mother bird witnessing her young flying for the first time."
    "Yukiko continues answering questions without missing a beat."
    scene bg black with dissolve
    "Like a knight mowing down a goblin army with a sword, she whittles the crowd down until it was time to vacate the hall."
    scene bg sslh with dissolve
    show yu calm with dissolve
    yu "I'm so done."
    mc "You need anything? Food? Water?"
    yu "My computer."
    mc "Right, priorities."
    yu "I should head back now."
    yu "See you later..."
    "She begins shuffling away..."
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.6
    pause 0.5
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.7
    pause 0.5
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.8
    pause 0.5
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.9
        pause 0.5
    show yu nervous:
        linear 0.5 xalign 0.6
    #move Yukiko sprite to the side quickly and change to nervous expression while bicycle bell sound plays twice
    "... and narrowly avoids a collision with a speeding biker."
    mc "You know what, I'm walking you back."
    scene bg black with fade
    pause 2.0
    "After I walked her home, I immediately started teaching myself how to program."
#end of scene2
    pause 5.0
#game lab scene where Yukiko is programming with absolute focus

#scene3 midterms vs project help
    play music "/Audio Dumpster/Waiting Music.mp3" fadeout 1.0 fadein 1.0 loop
    "It's a nice, sunny day on the weekend. Birds are singing, flowers are blooming."
    "I got onto my dream project team, but..."
    scene bg mc_apartment_inside with vpunch
    mc "This is so hard!!!"
    "I remember Yukiko said that people usually learn Python first, but I jumped into another language."
    "Since the deadline for me to complete my portion of the work is next week, I've been bugging my project leader about the intricacies of lua at least every ten minutes while working."
    mc "(He's been very reliable and patient with me, but that's exactly why I shouldn't keep bothering him.)"
    mc "(He has his own life and midterms too...)"
    mc "Maybe Yukiko could help me with this."
    "I rub my forehead in frustration and let my gaze wander over to a stack of textbooks on my desk."
    mc "(Wait, midterms!)"
    mc "Is this what they call being between a rock and a hard place?"
    "I don't want to turn in crap, but I don't want to fail my classes either..."
    define yu_midterms = 0

    menu yu_menu2:
        "What do I do?"
        "Study for midterms":
            $ yu_midterms = yu_midterms + 1
            #Choice B1 - Study for midterms
            mc "I can't change the dates of the midterms but I can just work harder later to make up my part for the project."
            "I nod to myself confidently."
            "I spend the rest of the day with my face buried in textbooks."
        "Get programming help from Yukiko":
            #Choice B2 - Get help from Yukiko
            mc "(Is it okay for me to ask her for help?)"
            mc "(Guess I'll try...)"
            "I call Yukiko."
            #play audio "phone.mp3"
            "This is my first time calling her."
            "The phone keeps ringing, but it doesn't seem like she's going to pick up."
            "I almost hang up when her voice suddenly caresses my eardrums."
            yu "Hello?"
            mc "Hey, do you have some spare time?"
            mc "I could really use a hand with programming in lua."
            yu "I'm at my apartment right now."
            mc "Should we meet in the game lab?"
            yu "No, going outside is a pain; just come over."
            "She casually invites me over with a bored tone."
            "Normally I would be very ecstatic, but her attitude makes it difficult to let my thoughts sidetrack into less than pure territory."
            yu "Do you have a laptop?"
            mc "Yes, I'm on my way."
            yu "Kay, bye."
            scene bg black with dissolve
            pause 5.0
            scene bg yu_apartment_outside with dissolve
            stop music fadeout 1.0
            "I text her to let her know I'm outside."
            show yu calm with dissolve
            play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
            "She opens the door with her hair slightly disheveled."
            yu "Hi."
            mc "Sup."
            hide yu calm with dissolve
            yu "Without giving me cue to follow, she shuffles back inside."
            scene bg yu_apartment_inside with dissolve
            "I follow her to find the living room void of furniture and a few filled trash bags lined up next to the door."
            show yu calm with dissolve
            yu "My room is this way. Well, it's pretty obvious, I guess."
            mc "Do you have any roommates?"
            yu "Nope."
            "She lets out a yawn while walking into her room."
            scene bg black with dissolve
            "I come in and see a bed, desk with a computer, and an office chair."
            "She leaves the light off and works in the darkness."
            mc "(I'm not sure how to put it, but it's very Yukiko.)"
            mc "Did you just wake up by any chance?"
            show yu calm with dissolve
            yu "Yeeeeeaaaaah."
            mc "Are you awake?"
            yu "Maybe."
            "I give her a very soft punch on the head."
            yu "Owie."
            show yu calm:
                parallel:
                    ease .5
                parallel:
                    linear 0.5 yalign 1.3
            "She falls back onto the cushion of her black office chair which let out a sigh as if it was just as tired as its owner."
            "From her desk, she picks up and tosses a paperback manual at my face that smacks me painlessly in the face and falls to the floor."
            mc "I'm suing you."
            yu "I'm pretty sure I can afford a better lawyer than you."
            mc "Fair enough, since you can afford to live in a 2 bedroom apartment by yourself."
            yu "With a little help from financial aid, I do enough freelance work to support myself."
            hide yu calm with dissolve
            "She turns her chair back to her computer and resumes her work."
            yu "I don't have any friends to room with here."
            mc "Couldn't you just find other female students?"
            yu "I only know Reina here and she doesn't really want to room with anyone."
            mc "Must be nice."
            yu "It gets lonely sometimes."
            "I peer over curiously at Yukiko who remains focused on her monitor."
            #something someting
            "I pick up the manual and read the title aloud."
            mc "Lua for Dummies."
            yu "Just use that as reference."
            "She says that without looking at me."
            mc "Um, is this really different from searching for it on the internet?"
            yu "I'll be here in case you don't get anything."
            "We just spend the rest of our day like that until midnight."
    scene bg black with fade
    pause 5.0
#end of scene3

#scene4 Confession Scene
    scene bg night with dissolve
    "Actually managing to call her out here still feels like a dream."
    "The cool breeze flowing through the azure night reminds me of time passing by."
    "It lulls a me into a reverie of emotional procrastination as I put off processing my feelings of excitement and anxiety."
    "The growing sound of rhythmical tapping of boots on concrete breaks me out of my trance."
    mc "Hey, Yukiko."
    yu "Hey, [mcname], you know I've been wondering for the whoooooooooole day what important thing you could possibly have to tell me at the dead of night."
    mc "Oh yeah, sorry about calling you out this late."
    yu "Don't worry, I don't mind."
    yu "I usually stay up working past this hour anyways!"
    mc "You sure work as hard as ever, huh?"
    yu "When I get in the zone, it I just forget that things are moving around me."
    mc "I really like that about you."
    show yu happy with dissolve
    yu "Thanks!"
    #Yukiko tries to make small talk
    stop music fadeout 1.0
    mc "U-um, let's get to what I came out here to talk to you about!"
    yu "Right, right; sorry for sidetracking."
    mc "Well... you see..."
    show yu calm with dissolve
    yu "Yes?"
    mc "I like yu..."
    play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
    mc "... mmy fish tacos."
    yu "Me too."
    mc "You didn't even taste -- wait, that's not what I meant!"
    mc "I mean I like you!"
    yu "I know."
    "I tried to pick my jaw off the floor."
    mc "You do?"
    show yu happy with dissolve
    yu "I like you too!"
    "I'm so taken aback that I can't think of anything to say, so I stammer something stupid instead."
    mc "T-that's good."
    "She stares at me smiling as I fry my brain on what to do next."
    "She's probably expecting something, so I move forward automatically."
    show yu calm:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 0.5
    yu "Is there something on my face, [mcname]?"
    "Her confused, innocent line manages to knock out all the courage I mustered in one foul swoop."
    show yu calm:
        parallel:
            ease .5 zoom 1.0
        parallel:
            linear 0.5 yalign 1.0
    "I back off dejectedly."
    mc "Oh, nothing of the sort."
    "It suddenly hits me that she might not know what I'm getting at."
    mc "(But really, even in this kind of situation..?)"
    mc "Hey, Yukiko?"
    yu "Yes?"
    mc "So you like me, right?"
    show yu happy with dissolve
    yu "A lot, yeah!"
    mc "Do you like Reina too?"
    yu "Even more!"
    mc "(Okay, that stings a little, but I have to go on.)"
    stop music fadeout 1.0
    mc "I like you in a romantic way."
    yu "Oh."
    mc "..."
    yu "....."
    show yu calm with dissolve
    mc "......."
    yu "........."
    show yu nervous with dissolve
    mc "..........."
    yu "............."
    show yu embarassed with dissolve
    play music "/Audio Dumpster/Piano Solo 1.mp3" fadeout 1.0 fadein 1.0 loop
    yu "Wait what when did this start I can't believe you would fall for someone like me oh but there were a lot of boys who gave me attention when I was growing up but I never got back to them so I don't really know how this works and--"
    "She loses control of her intonation so her voice oscillates between various pitches just like when she gets nervous in front of groups."
    mc "Yukiko--"
    yu "I'm not really against the idea but you know wouldn't it be weird if people at the club noticed us together or maybe they already see us that way and I don't really care in the end but oh my gosh what would Reina do to you after she finds out--"
    mc "Yukiko!"
    show yu blush with dissolve
    yu "I wanna crawl back to my computer right now but at the same time I don't so it's a really big issue for me right now right now but oh my gosh that was an attempt at kissing me earlier and I completely missed what you were getting at and--"
    show yu embarassed:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 1.0
    "I decide to speak through actions instead of words, pulling her into a secure, yet gentle embrace."
    yu "....."
    "Yukiko's panicked rambling trails off into quiet murmurs, and finally, into muffled breaths as she rested her face onto my chest."
    show yu calm with dissolve
    "The tension of her body fades away as she leans her weight on me in silent consent..."
    scene bg black with fade
#end of scene4
    pause 5.0
#possible hackathon scene

#scene5 normie date
    play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
    "Yukiko and I may be official now, but our relationship didn't really change from before."
    "We text each other dumb, pretty standard couple stuff."
    "Well, one little thing might have changed..."
    scene bg night with dissolve
    show yu happy with dissolve
    yu "Hi [mcname]!"
    mc "Hey!"
    "She's even more beautiful than before."
    show yu calm with dissolve
    "Or at least in my eyes, she is."
    "However, there's been something gnawing away at the corner of my mind lately, so I pop the question."
    mc "Hey Yukiko, why does everyone around here seem to wear the same clothes everyday?"
    yu "Are you familiar with no outfit november?"
    mc "Is that a thing?"
    yu "Yeah, [mcname], you need to get with the times if we're gonna be together."
    mc "Whaaaat? How was I supposed to know this?"
    show yu happy with dissolve
    yu "Don't worry, I'm just messing with you."
    mc "(You little...)"
    show yu calm with dissolve
    yu "Sometimes, it's best not to pry into things too closely and just enjoy the journey."
    mc "How can I enjoy the journey if I don't understand it?"
    yu "Some things don't need to be understood, [mcname]."
    show yu happy with dissolve
    "She grabs my hand and leads me along towards the plaza."
    mc "Where are we going?"
    show yu calm with dissolve
    yu "I don't know."
    "I stare at her rather confusedly, but I realize she can't see my expression as she was scanning the plaza to pick out a restaurant."
    yu "How about this place?"
    mc "A ramen restaurant? Have you tried it before?"
    show yu nervous with dissolve
    yu "I've had a lot of the instant kind at home."
    "I smile wryly at her mainstream college student tendencies."
    mc "I don't think that counts, Yukiko."
    show yu calm with dissolve
    #play audio "chime.mp3"
    "Still holding hands, we clumsily stumble over each other's feet into the store."
    scene bg black with dissolve
    pause 5.0
    #play audio "chime.mp3"
    scene bg night with dissolve
    yu "That was soooo good!"
    mc "I'm surprised you can taste anything wolfing it down like that."
    show yu happy with dissolve
    yu "I'm surprised you can taste staring at me eat my food."
    mc "In my defense, I was captivated."
    show yu nervous with dissolve
    yu "Is this the start of a cheesy line?"
    mc "No, it was like watching a wild lioness devour her prey without a second thought."
    yu "Did you just call me a wild animal?"
    show yu sad with dissolve
    "Yukiko feigns sadness and turns away from me in protest."
    "I decide to play along."
    mc "Yukiko, I'm sorry!"
    mc "Yukikoooo?"
    show yu sad:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 0.5
    "I get close enough to whisper in her ear."
    mc "Yuki..."
    show yu embarassed with dissolve
    "With my shenanigans, I manage to start her into jumping a few feet away from me as her face flushed red."
    show yu embarassed:
        parallel:
            ease .5 zoom 0.8
        parallel:
            linear 0.5 yalign 1.1
    yu "Reina might assault you if she hears you calling me that."
    mc "Does it bother you?"
    mc "I think it's a really cute nickname."
    yu "No, that name is part of Reina's intellectual property, so you can't plagiarize it."
    mc "Sweety? Maybe honey? Or how about darling?"
    show yu nervous with dissolve
    yu "Actually, I think I'm starting to feel kind of nauseous."
    mc "Kidding. Teasing you is just really fun."
    mc "Can't spell Yukiko without the 'ko.'"
    mc "The k stands for kind and the o stands for outgoing."
    show yu embarassed with dissolve
    yu "There you go with the cheesy lines again..."
    show yu calm with dissolve
    yu "[mcname], I'm not feeling very well..."
    mc "What's wrong? Did the food not sit well with you?"
    stop music fadeout 1.0
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.4
    pause 0.5
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.6
    pause 0.5
    show yu calm:
        parallel:
            ease .5
        parallel:
            linear 0.5 xalign 0.5
    "She takes small, unsure steps into random directions."
    mc "(Wait...)"
    mc "(This could be disorientation due to food poisoning..!)"
    yu "I'm feeling... feeling..."
    show yu calm:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 0.5
    "I grab her shoulders to steady her."
    mc "Feeling?"
    "Yukiko lets out a big yawn."
    yu "A strong food coma."
    "I poke her on the forehead."
    mc "Don't scare me like that, dummy."
    "She stares at me with hazy eyes."
    mc "You wanna go home?"
    yu "Yeah..."
    show yu calm:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 xalign 1.8 yalign 0.5
    "While saying that, she latches onto my arm and leans her weight on me."
    "I walk her home gently."
    scene bg black with dissolve
    pause 5.0
    scene bg yu_apartment_outside with dissolve
    "We arrive to the familiar outside of an apartment."
    mc "Hey Yukiko, need help getting your keys?"
    yu "Nah, I think I'll be okay..."
    "She lets go of my arm, straightens her posture, and adopts a focused gaze."
    "Yukiko fishes her hand inside of her bag for a while as I watched."
    "After a short period of rustling, she stands triumphantly with a glistening ring of metal in her hand."
    show yu happy with dissolve
    "She unlocks the door while the corners of her mouth curve upwards somewhat mischievously at me."
    mc "For someone who was just sleeping on my arm, you sure got better fast."
    yu "Your arm has magical healing properties."
    "She walks inside without giving me an opportunity to respond."
    "I shrug and follow her in."
    scene bg yu_apartment_inside with dissolve
    "The inside is still barren, but the rubbish adorning the living room from the last time I visited are all gone."
    mc "(Did she expect me to come over today?)"
    show yu calm with dissolve
    "Yukiko gestures to her room."
    yu "Come in."
    "I don't know what I'm getting into, but I can only obey my girlfriend being strangely assertive."
    "I scamper inside with my tail tucked between my legs."
    yu "Sit down."
    mc "Okay."
    #sitting noises? pomf?
    yu "I'm gonna go shower."
    mc "I see."
    hide yu calm with dissolve
    "I sit there calmly doing nothing for the next 15 minutes."
    pause 5.0
    show yu calm with dissolve
    "She returns with an air of sweet shampoo wafting from her still slightly damp hair."
    yu "I haven't done it in a while because of work, but I guess I can spare enough time today."
    mc "Doing what?"
    play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
    yu "Video games."
    mc "Oh."
    yu "What?"
    mc "Nothing."
    "....."
    mc "I just didn't see a console in your room so I thought we were doing something else."
    yu "There are games on PC too."
    mc "Oh, I usually play most games on console with a controller."
    show yu happy with dissolve
    yu "Then today's the day for you try out the games I have on my computer!"
    mc "Are you gonna be playing with me?"
    show yu calm with dissolve
    yu "Yeah, you can use controllers with the keyboard, or just use the controllers by themselves."
    mc "Heck yeah! As long as I have controls I'm used to, I can mop the floor with you."
    show yu happy with dissolve
    yu "Is that a challenge?"
    show yu nervous with dissolve
    yu "I wanted to play co-op games, but if you want to throw down, then..."
    scene bg black with dissolve
    "Yukiko proceeds to decimate me in every game genre possible, even first-person shooters and fighting games, the ones I thought I was good at."
    pause 5.0
    scene bg yu_apartment_inside
    show yu calm with dissolve
    mc "No way..."
    "Outside of fighting games, Yukiko wasn't even trying."
    show yu happy with dissolve
    "In fact, she spent a lot of her time watching me and giggling at my dismay every time she scored a headshot on me in , wiped out my base in Mooncraft, or "
    yu "Do you want to play co-op games yet?"
    "She says that with a genuine innocence that my pride embellishes with mocking intent."
    mc "I think I can live with just one more rematch on Tori Faiter."
    "I'm determined to win at least once against Yukiko, so I put on my game face."
    show yu calm with dissolve
    mc "Good Queen of Cats, nothing but one of your nine lives, that I mean to make bold withal, and, as you shall use me hereafter, dry-beat the rest of the eight."
    mc "Will you pluck your controller out of his pilcher by the ears? Make haste, lest mine be about your ears ere it be out."
    "Yukiko plays along without missing a beat."
    show yu happy with dissolve
    yu "I am for you."
    show yu calm with dissolve
    "I might be good enough to defeat her in Tori Faiter with a bit of luck."
    "At least in this game, she has to try in order to beat me."
    "....."
    "She's beating me again."
    mc "(Instead of accepting my character's inevitable defeat, maybe I should try a change in strategy.)"
    "I'm currently at 85 points of health. While adopting a defensive playstyle to stall out the game, I take brief side glances at Yukiko."
    "The light emitted from the monitor highlights her long eyelashes and big eyes. Her glossy lips remain slightly parted in concentration."
    "She chunks about 20 points of my character's health due to me taking one hand off the controller in order to poke her on the cheek."
    "She mumbles something in response."
    yu "What are you doing, dummy?"
    "Satisfied that she wasn't ignoring me, I try something more bold."
    show yu calm with dissolve
    show yu calm:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 0.5
    "With my character at 65 health, I lean over and give her a peck on the cheek."
    show yu calm with dissolve
    show yu calm:
        parallel:
            ease .5 zoom 1.0
        parallel:
            linear 0.5 yalign 1.0
    show yu embarassed with dissolve
    "She stops beating my fighter up for a fleeting moment to send me a cute, panicked look."
    show yu calm with dissolve
    "Yukiko immediately snaps back to the game and somehow increases the severity of her assault on my virtual self."
    "She begins whittling me down from 65 to 50... 50 to 35... and 35 to 15."
    "Realizing the gap in our skill levels at this point, I concede that winning is a faraway dream."
    mc "(But, I don't want to lose at least..!)"
    "In a final desperate bid to avoid defeat, I tear my gaze from the screen showing my limping 1 health character and I begin standing up--"
    show yu embarassed with dissolve
    show yu embarassed:
        parallel:
            ease .5 zoom 1.5
        parallel:
            linear 0.5 yalign 0.5
    stop music fadeout 1.0
    "... and Yukiko pushes me down onto the bed to stop me from doing anything else to her."
    "Aside from the game's background music, it was so quiet that we could hear both of our controllers fall onto the rug with a quiet thud."
    "Mirroring our bodies, our characters in Tori Faiter remain still and cycle through their idle animations, as if refusing to hurt each other."
    yu "[mcname], do you want to win that badly?"
    mc "Now that I think about it, no, not really."
    show yu calm with dissolve
    mc "I think I just wanted you to notice me."
    "I give her a dry, self-deprecating laugh."
    mc "I'm lame, aren't I?"
    show yu happy with dissolve
    yu "No, I think that's really cute."
    mc "(Now I'm the one who's blushing.)"
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    yu "[mcname], I'm the one who's lame."
    yu "I thought if you kept trying to beat me, you would end up staying longer."
    "Yukiko's lovely smile remains but her round eyes begin filling with melancholy."
    yu "Studying at this school and living here..."
    yu "Even if I was fortunate enough to start what I love doing since I was a kid..."
    yu "Even if I can ace the classes in my major while sleeping in lecture..."
    yu "Even though I could probably comfortably live off working from home like I do right now..."
    show yu sad with dissolve
    mc "Yukiko..."
    yu "It doesn't change the fact that I'm all alone in this cold, drafty apartment when I wake up late in the afternoon."
    show yu sad:
        parallel:
            zoom 1.7
        parallel:
            linear 0.5 yalign -0.5
    "I embrace her close to me."
    mc "Are you cold right now?"
    "She shakes her head as she nuzzles into my chest."
    mc "Yukiko."
    yu "Hmm?"
    mc "I'll stay as long as you want."
    yu "Is that a promise?"
    mc "Yes."
    yu "What if I want you to stay until morning comes?"
    mc "Fine with me."
    yu "....."
    "Yukiko peeks her head up and stares into my eyes. She looks like she has something to say."
    mc "What is it?"
    yu "What if... I want you to stay until I say otherwise?"
    mc "Okay."
    show yu nervous with dissolve
    yu "Are you serious?"
    mc "I'll pay rent too, of course."
    yu "You don't have a job, right?"
    show yu happy with dissolve
    yu "You're really thoughtful [mcname], but you can't even afford half of this rent."
    mc "Oh, that's right."
    mc "I was so caught up in the moment that I forgot about the financial implications."
    yu "That's something I like about you."
    show yu calm with dissolve
    yu "You can just pay me what you're currently paying for your current place."
    mc "Really? That's really generous. I even get a whole room to myself."
    yu "I think I'm coming out on top for this one. I get a whole [mcname] to myself!"
    mc "Maybe I can contribute in other ways. I've got the stamina for the most strenuous chores and I can cook pretty decently."
    yu "That would be really helpful, thank you."
    mc "Is there anything else I can do for you?"
    "Yukiko mulls over her options for a moment and reddens."
    show yu blush with dissolve
    yu "Can you close your eyes?"
    mc "... sure."
    scene bg black with fade

#scene6 Projects showcase CHANGE to "my project sucked, Yukiko's was good"
    scene bg dbh_outside with dissolve
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "It's been a month since I moved in with Yukiko."
    "Today was the day for our projects to be showcased."
    "My project did painfully average."
    "First of all, the fact that people needed to own or purchase Larry's Mod in order to experience it served a crucial barrier discouraging people from trying it."
    "Secondly, the development team, including me, was collectively caught up in the nostalgia of Larry's Mod and didn't consider how much appeal it would have for gamers who prefer more modern titles."
    "It was definitely suited for a very niche audience."
    "Lastly, our mod of Larry's Mod neither executed a known concept exceptionally well or really offer any new, innovative features that made it stand out from the other available mods."
    "It was a good learning project for the programmers on the team, but in the end, that's all we could afford to make it turn out to be within our capabilities at the time."
    show yu calm with dissolve
    "I sigh dejectedly next to Yukiko."
    yu "Cheer up, [mcname]. I liked your project. I saw how much effort went into the programming."
    mc "Hearing someone like you tell me that makes me feel a little better."
    yu "Forget my qualifications. Anyone could tell you guys were really passionate about your work."
    show yu happy with dissolve
    yu "As long as you guys learned something, you can always use those skills to make something better in the future."
    mc "Right, right. That was the point."
    "Her smile is contagious, so I can't help but smile too."
    yu "Oh right, I had something important to tell you today."
    mc "Is it about your project?"
    show yu calm with dissolve
    yu "I actually signed up for a commercial project with an experienced team. We're also not sponsored by the club."
    mc "I see."
    yu "We didn't get much reception after release..."
    mc "Oh..."
    show yu happy with dissolve
    yu "But once the internet caught wind of it, our game blew up overnight."
    mc "OH?!"
    mc "That's great! We have to go celebrate."
    show yu calm with dissolve
    stop music fadeout 1.0
    yu "I'm not really feeling it today."
    mc "Oh, how come?"
    yu "What I just told you coincides with what I actually have to tell you today."
    mc "What is it?"
    play music "/Audio Dumpster/Melancholy.mp3" fadeout 1.0 fadein 1.0 loop
    "She starts slowly walking facing away from me with her arms behind her back. I follow suit."
    yu "I wasn't satisfied with my life here. So I thought that focusing on my career would help me find the spark in my life that I was looking for."
    yu "They say that the degree is the minimum that you need to get a job."
    yu "Sometimes you don't even need the degree."
    yu "Networking and your portfolio and capabilities are what really get you the job."
    mc "Sounds about right to me."
    yu "I couldn't do the networking part. I just couldn't."
    yu "It wasn't that I had anything against networking."
    yu "Some people might see networking as a selfish thing because they consider it as a means to an end instead of an end within itself."
    yu "You know, just a handful of people helping each other out."
    yu "I gave up early. I didn't want to go back to trying to talk to people, not to mention people who I might emd up working with. It was scary."
    yu "I took the easy way out and worked really hard for my talents to get noticed."
    yu "Sometimes things just don't work out if you avoid reality and keep trying to play by your rules."
    yu "That was okay. I decided I was content with what I had. A really sweet guy even wandered his way into my heart one day."
    yu "But now, just when I thought I was at my happiest, my work gets noticed."
    yu "I printed out the job offer they gave me."
    "Without looking at me still, she holds out a 2-page document in my direction."
    "She doesn't say anything else. Even without seeing her face, I can tell she's crying."
    "I'm not daft enough to not know what kind of question she's asking without her actually saying it. I know what I have to do."
    "I take the stapled paper from her small hand and hastily skim over the contents in order quickly formulate a response to ease her fears, to put her at rest."
    mc "Overseas..?"
    "I stop walking and read over the whole description carefully again. Yukiko continues walking farther and farther from me."
    mc "THAT bigwig company?"
    "The moment I finish reading, I realize what the scope of dilemma I'm facing."
    "I can't find any appropriate words. Maybe it's better to say something rather than nothing. But maybe some things are best left unsaid?"
    hide yu calm with fade
    "Yukiko's back is growing increasingly fainter in the distance."
    "I start disassociating. I begin seeing myself and my actions from a third-person point of view. It feels almost as if I'm dreaming."
    "The voice in the back of my head telling me to chase after her fails to break through to my senses. It fades away just like Yukiko's figure in my view."
    scene bg black with fade
    pause 5.0
#scene7 Final
    scene bg yu_apartment_inside with dissolve
    stop music fadeout 1.0
    "It wasn't as if Yukiko disappeared, but today is the third day that she's locked herself in her room."
    "And it's finals week."
    "When I go check up on her, she tells me to leave her alone."
    "At least she takes the food that I leave by her door, so I know she's not starving herself."
    "But even a girl with grades as immaculate as hers will fail her classes if she skips the final exams."
    "Her first final is tomorrow morning."
    "I've been giving her time to herself, but it's harmful for her if I keep this up."
    mc "(I'm not your dad, you know...)"
    mc "(You just have to take them, Yukiko...)"
    mc "(Don't be so selfish...)"
    mc "(... no. That's not right.)"
    mc "(The one who's really selfish is me. What if I had just told her how I felt that day...)"
    if yu_hang < 1:
        jump yu_bad
    menu yu_menu3:
        "What should I do?"
        "Tell her to stay with me":
            label yu_normal:
            mc "(I wanted her to stay with me.)"
            #play sound knock.mp3
            "I knock on her bedroom door and receive no response."
            mc "Yukiko! I realized it. I knew it all along. I just couldn't bring myself to say it!"
            "My passion is greeted by silence, but I keep going. I have to say this for the both of us."
            "I don't want you to leave! You're the most special person in my life right now!"
            "Even if it means turning down an opportunity like that..!"
            "I can't stop the waterworks."
            "I choke back my tears of guilt and sadness."
            mc "You said that you were happy with what you have right now right?!"
            mc "No one can say for sure whether you'll be more happy carrying on here or moving away to chase your dreams..."
            mc "And I certainly don't have a right to decide that for you, but I want you to know..."
            mc "There are lots of ways to define success! There isn't any one way to reach happiness. And I want to keep sharing the happiness we have now with you!"
            mc "I love you!"
            "....."
            "......."
            "........."
            mc "(Was she asleep?)"
            mc "Yukiko..?"
            mc "(If she's really asleep, I feel like the dumbest person on earth right now.)"
            "The door finally opens just a little."
            show yu calm with dissolve
            yu "[mcname], I was sleeping. Did you need something"
            "My mouth flaps between open and closed in shock as the tears flow out of my eyes."
            mc "Sorry..."
            yu "Just kidding... I heard everything."
            hide yu calm with dissolve
            scene bg black with dissolve
            "She opens the door all the way and makes her appearance in the hallway."
            "I still can't really see that well with the tears impeding my vision."
            "I feel a soft cloth and gentle hand drying my tears."
            show yu sad with dissolve
            "It's Yukiko using her sleeve to wipe away the residue of my weeping."
            mc "Don't scare me like that."
            "With two tilts of my head, I wipe away the rest of my tears on my shoulders."
            play music "/Audio DumpsterSomber Music.mp3" fadeout 1.0 fadein 1.0 loop
            scene yu_apartment_inside with dissolve
            show yu calm with dissolve
            "Returning my gaze to her, I notice her eyes are rather moist and bloodshot."
            show yu happy with dissolve
            "Noticing that I was looking at her, she pushed herself to perk up."
            yu "I was just finishing my email to follow up with the job offer."
            mc "I see... if you want to go ahead with it, I have no right to stop you."
            yu "What are you saying, silly?"
            yu "I'm turning them down. I think I would be much happier here. I don't think I could handle losing the few friends I've worked so hard to get here."
            yu "If they want me that bad, they can let me telecommute somehow. If not, I'm finishing my degree here to hopefully land a local job."
            mc "Not hopefully, you're amazing at what you do. You'll find a job. In fact, you already kinda work, so..."
            show yu nervous with dissolve
            yu "Oh yeah, that. Right."
            yu "Once they notified me about that opportunity, I couldn't think about anything else, so I totally forgot about the stuff I had due."
            mc "You don't have to study for finals, right?"
            show yu calm with dissolve
            yu "I skim some stuff I don't know for 30 minutes and I'm good."
            mc "Okay, you do that and I'll start on the freelance work you haven't done yet."
            yu "Uhh, I don't think..."
            mc "Can I come in?"
            yu "Sure."
            "Yukiko lets me skim the assignments she has in her work email."
            mc "Alright, I have no idea how to do this!"
            show yu calm:
                parallel:
                    ease .5
                parallel:
                    linear 0.5 yalign 1.3
            "Yukiko rewards my effort with a faux exasperated sigh as she plops down in her chair."
            mc "I'll keep handling the chores and cooking. I'll bring you whatever you need."
            yu "So you'll keep doing what you've always been doing?"
            mc "You didn't have to put it that way..."
            "She snickers amusedly as my voice trails off."
            yu "And I'll keep doing what I've always been doing too. Nothing will change."
            "Yukiko puts her hand on her mouse and hovers the cursor over the send button."
            mc "Is this really okay, Yukiko?"
            show yu happy with dissolve
            yu "Like you said [mcname], there are many ways to happiness."
            show yu calm with dissolve
            "Her voice sounds brave, but her hand on the mouse is shaking."
            "I give her a reassuring smile and put my hand on top of hers."
            "From today on, we forge forward to our uncertain future."
            #play sound "mouse.ogg"
            scene bg black
            ".:. Normal Ending."
            $ MainMenu(confirm=False)()

        "Tell her to go":
            stop music fadeout 1.0
            mc "(I wanted her to stay with me.)"
            mc "(... but I also want her to chase her future.)"
            "I knock on her bedroom door and receive no response."
            mc "(If you love something, let it go, and if it loves you back, it will always come back to you, right?)"
            "I make a poor effort of comforting myself with a platitude before steeling my heart in preparation for what I'm about to do."
            "I begin audibly packing anything I had that would fit into my suitcase, serious or not."
            "I still sense no signs of life from Yukiko's room."
            "I shout at her bedroom door."
            mc "Yukiko, this is the last time I'm gonna try. Let's talk about this like grown-ups."
            "No response."
            mc "I don't want to make any assumptions before we talked, but..."
            "I see and hear the door shake a little."
            mc "Yukiko, if you're going to keep running away from this, I'm leaving right now."
            "The doorknob turns frantically right before the door swings open abruptly, narrowly missing my face."
            show yu nervous with dissolve
            yu "[mcname], you can't be serious."
            mc "Just take the job. You don't have to lose me. We can make this work!"
            show yu sad with dissolve
            "Yukiko stares at me for a bit while biting her lower lip anxiously for before speaking."
            yu "Long distance relationships are really hard [mcname]."
            yu "We even just started officially dating a month ago."
            yu "Couples who have been together longer than us have been broken apart by distance."
            yu "I want to believe that we can be different, [mcname], but it just doesn't feel like two silly college students like us are capable of doing any different."
            if yu_midterms >= 1:
                scene bg black with dissolve
                "I close my eyes and bite my lip while wracking my brain for a solution."
                "As much as I hate to admit it, Yukiko's worries hold a strong foundation within reality."
                scene bg yu_apartment_inside with dissolve
                show yu calm with dissolve
                play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
                mc "Yukiko..."
                "I practically crush my lower lip with the weight of my front teeth before finally speaking."
                mc "I... think you're right, as much as it pains me to admit it."
                yu "..."
                show yu sad with dissolve
                mc "(She's the one who said that we can't continue our relationship like this, but she looks so sad.)"
                "Of course, I know that's not her fault because she's just describing the situation as it is. She's not happy with this either."
                mc "(Things change; life happens. These circumstances aren't really anyone's fault.)"
                yu "[mcname], is this really okay?"
                show yu sad:
                    parallel:
                        ease .5 zoom 1.5
                    parallel:
                        linear 0.5 yalign 0.5
                "I move close to her and place my hands gently on top of her fragile shoulders."
                mc "... I can't answer that question for you, Yukiko."
                mc "This might sound cheesy, but if you have even a tiny part of you who wants to take the job, just go for it. Even if it's scary."
                mc "I don't subscribe to the romantic belief that couples complete each other."
                mc "Instead, I think it's two people who are whole looking to come together to make something special."
                mc "I don't think it's two halves coming together to become a whole."
                mc "In other words, we should prioritize trying to complete ourselves over leaning on each other."
                "Feeling silly, I scratch my head."
                yu "I don't really know what I'm doing."
                mc "I think you do. You just making a really hard decision."
                show yu calm with dissolve
                yu "I don't know how to talk people."
                mc "But you really do know how to talk to a person enthusiastically about bottled water and fish tacos."
                yu "I was just born with my talent."
                mc "I find it really hard to believe that you can nonchalantly rent out a $2000 apartment while going to school without working hard at all."
                show yu happy with dissolve
                "Yukiko gives me a smile riddled with melancholy."
                yu "I'm selfish, [mcname]. I don't want to pick to begin with. Between taking the job and staying with you, I mean."
                show yu sad with dissolve
                yu "Not to mention I spent three days sulking indecisively while you took care of me. I'm sorry about that."
                mc "It's a tough decision. Also, I think it's my job to help my girlfriend make tough decisions, right?"
                show yu calm with dissolve
                mc "And... you're not selfish, Yukiko. I was really blown away when you tackled me out of harm's way while I was trying to bodyblock a branch for you in the park."
                mc "You could say that you really left an impact on me."
                show yu happy with dissolve
                "Yukiko tries in vain to prevent a giggle from slipping out."
                show yu nervous with dissolve
                yu "D-don't make me laugh in such as serious situation."
                show yu calm with dissolve
                "I chuckle to disguise the nostalgia-induced sadness welling up in my eyes."
                mc "The point is that I believe in you. Whatever you decide to do, you have my support."
                "Yukiko pauses for a moment before abruptly removing my arms from her shoulders."
                mc "(Did I make her mad?)"
                show yu blush with dissolve
                show yu sad:
                    parallel:
                        zoom 1.7
                    parallel:
                        linear 0.5 yalign -0.5
                "She swiftly rushes forward and squeezes me tight in a hug with her face nestled into my chest. I embrace her gingerly in return."
                "Just like the time we became official not so long ago, we just stand like that for a while, both knowing what's going to come next."
                scene bg black
                yu "I'm going."
                pause 5.0
                stop music fadeout 1.0
                mc "(When we consider the other billions of people living on this planet, it is hard to believe that you could conveniently meet the one person you were destined to be with.)"
                mc "(However, let's say that the conditions determining a soulmate include how near they are to you.)"
                mc "(But then, what kind of measurement would you have to use for that?"
                mc "(Are they the best match for you within the same nation? The same state? 50, 20, or 5 miles?)"
                mc "(Even if you meet and marry someone and stay with them for the rest of your life, are they really your soulmate?)"
                mc "Maybe you would be happier with someone from Dubai who is completely compatible with you. How about China, Russia, or Europe?)"
                mc "(That's not even considering time periods. Maybe Marie Curie of the 20th century was your ideal.)"
                mc "(If I call the person I'm with my soulmate, it seems to contradict soulmates' own romantic interpretation of being star-crossed lovers.)"
                mc "(I'm sure many would disagree, citing the many valid flaws of such an interpretation. Maybe all of what I just described doesn't even matter on a practical basis.)"
                mc "(Still, when I think about the overwhelming amount of factors we can consider, I don't believe in fate.)"
                mc "(Although most people would balk at the notion that the relationships we hold so closely to our hearts are largely determined by physical proximity, there are plenty of studies within the realm of social psychology that support the idea.)"
                mc "(In other words, although we forge genuine friendships through love and connection, circumstances and continual interaction fosters more of it than we like to realize.)"
                mc "(In the end, all we can do is march forward against nature's undiscriminating winds which threaten to knock us down or blow us off our paths.)"
                mc "(We try to remain close to those we hold dear, lest we lose them trying to navigate the twists and turns of the bittersweet maze that we call life.)"
                mc "(I figured all this out after I graduated college.)"
                mc "(I met a lot of people along the way. Some friends, I end up keeping, even the ones I least expect. Some friendships are torn apart for the wrong reasons. Others decay slowly but certainly, until they have long withered away.)"
                mc "(Yukiko was one of those who faded into obscurity.)"
                "The summary goes as follows: after we spent our remaining time together, I saw her off at the airport."
                "At first, I texted her a lot to reassure her and she texted me about the new things she experienced that day, but our lives became increasingly busy."
                "We just broke off at some point. One day, on a whim, I sent her a text checking up on her, but it didn't send."
                "She must have finally changed her number to avoid international fees from service within her own country."
                "Neither of us used social media. I had no way to reach her. I had work and social events plastered all over my week and the rest of my calendar. Life went on."
                "It's been two whole years since I graduated from university."
                "I worked hard and earned an entry-level position at an international game development company desperate to staff their brand new North American branch."
                scene bg office with dissolve
                play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
                "Today's my first day on the job and I'm just playing armchair psychologist and philosopher while waiting to meet the head of my department."
                "I've been sitting in expensive, new posh waiting chair for around 20 minutes already."
                "It's definitely far from the worst of fates, but I have to keep my mind active so that I don't fall asleep because of how comfortable this chair is."
                "The early period of my new coworkers bustling about and smiling and greeting me has already passed, and I'm just a sitting mascot that they acknowledge at this point."
                "I can't get to work before what is basically my briefing. I don't even know where my work area is."
                "The secretary at the front desk just told me to have a seat here."
                "I let out a quiet sigh."
                su "Hi, you must be the new hire."
                "I snap back to reality and professional mode as a figure in an expensive looking suit greets me."
                "Based on my impression of the work environment I got at my interviews, I decide to head straight for the casual route."
                mc "Hi, you must be my boss!"
                "Them returning my greeting with a warm smile reassures me of my choice."
                su "Not exactly. In our company's work environment, we encourage equal collaboration."
                su "No one's your boss. But of all the people who aren't your boss, I'm the MOST not your boss, if you get what I'm saying."
                mc "Is that from the company handbook for new hires?"
                su "Yes, it is. I never thought anyone actually read that. We even have joke illustrations inside of it."
                mc "Wow... so much for me trying to take my job seriously."
                su "You *should* take your job seriously. Being serious at what you do is good."
                su "Though, I would say that the nature of our job as game developers requires us to be able to not take ourselves too seriously to a certain extent."
                mc "Work hard and play hard."
                su "Exactly."
                mc "By the way, I'm only going to be doing programming right?"
                su "What I've noticed working in the game industry is that big companies often split the departments up properly in order to ensure a continuous workflow, but smaller companies tend to be a free-for-all."
                su "Right now, it's not as clear-cut as what I just described, since we're a big company with a branch just beginning to bloom with the few hires we managed to carefully pick out of the local talent pool."
                su "Our branch right here has the manpower of a small company at the moment."
                su "What that means is that a programmer like you only does programming related work on paper, but anything else you can bring to the table makes you a huge asset."
                su "I would recommend working on our odd tasks even though you're not experienced in the field. We don't expect you to be either. It can be a good learning experience."
                mc "I'll do my best. I wanted to work in this industry, after all."
                su "That sounds fantastic. I actually have some remaining paperwork for you to fill out in my office before you get started."
                su "My office is just down the hall."
                "The supervisor begins walking down the hall with me in tow."
                scene bg black with dissolve
                "No one else is around."
                play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
                su "Consider what I'm about to ask you a personal question, since I'm requesting a personal answer. I don't want to hear any corporate pandering, and you don't have to answer if you don't want to."
                mc "Go ahead, shoot."
                su "What made you want to work in games?"
                "For a short period of time, the only sounds around us are my footsteps and the click-clatter of high heels down the corridor."
                mc "When I went to college, a girl entered my life as quickly as she left it."
                "My voice echoes in the spacious hallway we're walking in."
                su "Oh, I'm sorry..."
                "I flash an amiciable smile."
                mc "Don't worry, it wasn't like that."
                mc "To say she really liked programming would be an understatement. She loved games too."
                mc "Even after a couple years in college, I still didn't know what I was doing. I didn't know where I wanted to go, or what I wanted."
                mc "When I met her, she didn't have many friends. But I knew she had her stuff together. I believed in her."
                mc "She was a person who shined so brightly that she illuminated the path forward for me, even if she didn't mean to."
                mc "I had to let her go shine because I didn't have the capacity to follow her. It just wasn't the right place or the right time for us."
                mc "I don't regret it. I do regret never letting her know how big a role my stint with her had in shaping my future though."
                "My supervisor smiles and nods understandingly as they listen to my story."
                mc "I must be going off a tangent."
                su "No, it's fine. I can tell you really cared about her. It was a good answer, and a really personal one at that."
                "I notice that their eyes seem to be rather moist."
                su "Thank you for sharing with me."
                mc "No problem."
                "We finally reach the outside of the closed office."
                su "Come in, have a seat."
                mc "I think I'm learning a lot today so far. Sitting in all these chairs is a valuable learning experience for my ass."
                "My supervisor spares a laugh for my crude joke while sitting down."
                su "You might want to avoid that kind of humor if the producer comes around. He's a pretty serious fellow."
                mc "I was just making sure you still find my bad jokes funny."
                scene yu_end_1 with dissolve
                su "I actually didn't recognize you until you started telling me that story."
                "Fixing a stray strand of hair on my head, I chuckle self-consciously."
                mc "I guess I did change a lot over the years."
                mc "Why did you come all the way over here?"
                su "They needed senior level employees who speak good English to run things around here."
                scene yu_end_2 with dissolve
                su "Naturally, I fit the bill quite well."
                "I'm at a loss for words, so I just say what's on my mind."
                mc "Welcome back."
                scene yu_end_3 with dissolve
                yu "It's good to be home."
                mc "(I don't believe in fate, but... I don't have to.)"
                mc "(Fate found me instead.)"
                scene bg black with fade
                ".:. Good Ending."
                return
            else:
                label yu_bad:
                hide yu sad with dissolve
                stop music fadeout 1.0
                "I stare down at my feet, unable to look her in the eye. Unable to face the truth."
                "As much as I hate to admit it, Yukiko's worries hold a strong foundation within reality."
                play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
                mc "Yukiko, I... I think we're special, and..."
                "I try to find some sensible words to reassure her with, but I just end up stumbling over my own desperate thoughts."
                mc "(My trembling voice must not sound very encouraging to her.)"
                yu "I think we're special too but... maybe not as much as you think we are."
                "I still can't look her in the eyes."
                mc "How could you say that? I'm really trying here, Yukiko."
                "Her voice cuts at me from a few paces from the wooden floor I'm staring at."
                yu "I'm trying too, [mcname]."
                mc "Is that why you've been sitting in that room by yourself all day?"
                stop music fadeout 1.0
                "Before could hold my tongue, those vile words fueled by frustration left my mouth."
                "I look up impulsively to assess the damage."
                show yu calm with dissolve
                "Yukiko's unflinching face greets my vision."
                yu "Do you really think that was what I was doing?"
                yu "I was writing up a follow-up email to the company declining their offer."
                mc "Why didn't you just tell me then?"
                yu "I was still deliberating..."
                mc "You took three days sitting in there by yourself to deliberate?"
                "My voice rises together with my anger."
                show yu nervous with dissolve
                yu "I-I just needed some time to myself..."
                mc "Why didn't you just talk to me about it instead of hiding like a kid?"
                show yu sad with dissolve
                yu "I didn't mean..."
                mc "Do you know how worried I was sitting out here? I was--"
                "I finally manage to stop myself at the sight of her tears."
                mc "Yukiko, I'm sorry, I didn't mean to--"
                yu "L-long distance or not, t-this isn't going to work out."
                "Yukiko tries to communicate through her tears."
                yu "If you want me to go s-so bad, I'll do it. I'll just forget about you."
                yu "We're breaking up."
                "I give her a bitter smile."
                mc "Sure."
                "With what felt like a pained expression on my face, I quickly stride out of her apartment, disappearing into the cold night."
                hide yu sad with dissolve
                scene bg black with fade
                pause 5.0
                scene bg park_2 with fade
                stop music fadeout 1.0
                "It's been an academic quarter since I last saw her."
                "Since then, I sent her texts apologizing and encouraging her, but she never responded."
                "I still go to the club, but I never catch a glimpse of her, even during official events."
                "I don't think about it everyday."
                mc "(I wake up. I go to school. I study. I sleep. Life goes on.)"
                mc "(However, my body grows weary merely from carrying out its routine.)"
                mc "(I function as an automaton. When I talk to other people, I behave as I normally do. I look people in the eye while greeting them. We make friendly small talk.)"
                mc "(It feels all like an act to me. What I'm doing, what I feel, and what I say.)"
                "My introspection ends early as I end up walking mindlessly into someone familiar."
                show re calm with dissolve
                re "..."
                "She stares at me blankly before continuing on her way."
                "I turn in her direction and greet her back with a friendly smile."
                mc "Hi Reina, how's it going?"
                "She mechanically turns her torso back towards me without a change in expression."
                re "... hi."
                mc "Maybe you've forgotten me from back then, but we talked for a bit."
                re "... I remember."
                mc "Oh."
                re "....."
                mc "........."
                "............."
                "We share awkward silence until Reina shifts her body as if about to leave."
                mc "Hey, have you seen..."
                "My voice tapers off the end of my question as Reina briefly looks as if I had just asked her if I could defecate on her shoes in public."
                re "You don't even know..?"
                "I start to feel a little annoyed at her rudeness."
                mc "I don't. Tell me. What am I missing?"
                "Taking note of the angle of the corners of my mouth, my smile must have dropped off a long time ago in this conversation."
                "Reina begins walking away. I stride after her in what must have appeared to outsiders as in an intimidating manner."
                mc "Tell me!"
                "The voice that leaves my throat surprises me with its harshness."
                "In a single swift motion, Reina twirls around with her hand raised."
                #play sound "slap.ogg"
                "The freshly throbbing pain in my cheek pales in comparison to the news Reina delivers to me immediately after."
                play music "/Audio Dumpster/Bad Ending.mp3" fadeout 1.0 fadein 1.0 loop
                re "She doesn't go here anymore."
                "With the pragmatism of her tone to set the mood, Reina begins cutting me with her short statements."
                re "She cried to me on the phone. She flunked her finals by not going."
                re "She didn't take the job. She moved back home."
                "I daftly remain still."
                re "Are you even listening? You're the one who asked me."
                "Bearing a famine for words, I have no words to offer her."
                re "Whatever."
                "Reina starts walking away, taking glances back to make sure I'm not stopping her again."
                re "There were plenty of things she wasn't satisfied with before you barged in. Don't give yourself too much credit."
                re "You just happened to be the final lock to seal away her heart."
                hide re calm with dissolve
                "As Reina disappears into the rays of morning sunshine, I carry my body away back into the park to rest on the grass."
                #blurring out
                "I lie down weighed heavily in hardship. My body drifts away into the sea of slumber, anchoring my my mind with it."
                "Afraid of drifting away into loneliness, afraid of navigating through an uncharted future, I remain floating here where we first met, calling out your name."
                mc "Yukiko..."
                scene bg black with fade
                "But you never come."
                ".:. Bad Ending."
                $ MainMenu(confirm=False)()
