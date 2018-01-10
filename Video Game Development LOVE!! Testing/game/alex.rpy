define ax_affection = 0
#define ax_max_affection = 6

label alex_scene1:
    #Scene 1 - Food Court
    scene bg foodcourt with fade
    play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
    "I hadn’t talked to Alex since finding out that he was a design officer in the VGDC."
    "I had so many questions."
    "I managed to meet up with him in the food court the next day."
    show ax happy with dissolve
    ax "Bonjour, [mcname]!"
    mc "Since when did you speak French?"
    show ax calm with dissolve
    ax "Since finding out it’s the language of love, and that chicks really dig bilingual guys."
    mc "(We were just friends, but it always hurt to hear him talk about other girls.)"
    mc "Um, okay. So, why didn’t you tell me that you were in the VGDC?"
    ax "I dunno. I wanted it to be a surprise."
    mc "It was a crappy surprise."
    ax "Sorry I made you feel that way, [mcname]."
    mc "I just feel like there’s a lot of things I don’t know about you anymore."
    show ax happy with dissolve
    ax "I think I can help with that, if you help me with something."
    mc "What are you talking about?"
    show ax calm with dissolve
    ax "So, I went out with the girl last night that I met at the Involvement Fair." 
    mc "What's her name?"
    ax "Naomi. Anyways, it uh, went south pretty quickly."
    mc "How’d you manage to screw it up so fast?"
    show ax sad with dissolve
    ax "I guess I have a ‘reputation’ for being a womanizer. And Naomi called me out on it."
    mc "Dude… that sucks."
    show ax calm with dissolve
    ax "Tell me about it. Anyways, this is where you come in."
    mc "What are you gonna make me do?"
    ax "I’ll need you to pretend to be in a fake relationship with me."
    mc "Um…"
    ax "Please say you'll help me, [mcname]."
    menu ax_menu1:
        "What should I say?"
        "Yes.":
            #Diverges into 2 options:
            #[Pos. Option] "Yes"
            $ ax_affection = ax_affection + 1
            mc "Okay, but how does it benefit me?"
            show ax happy with dissolve
            ax "You'll get the satisfaction of helping your best friend in his time of need."
            mc "That's it?"
            ax "I'll also help you with a pitch for the meeting next week."
            mc "(I did want to pitch something next week...)"
            mc "(And if I had the help of one of the official officers, I was sure to get accepted.)"
            mc "All right. As long as your plan doesn't involve anything super awful."
            show ax calm with dissolve
            ax "Nah! I’ll text you later about it."
        "No.":
            #[Neg. Option] "No"
            mc "I'm not comfortable with doing something like that."
            show ax sad with dissolve
            ax "So you're gonna abandon your friend in his time of need?"
            mc "I'm not 'abandoning' you..."
            show ax calm with dissolve
            ax "Look, help me with this, and I'll help you with your pitch for next week."
            mc "How'd you know that I wanted to pitch...?"
            ax "Just a good guess."
            mc "(I did want to pitch something next week...)"
            mc "(And if I had the help of one of the official officers, I was sure to get accepted.)"
            mc "Fine. I'll help, but I'm still not comfortable with all of this."
            ax "It won't be for very long, I promise. I'll text you later about it."

    #After Either Option -
    hide ax calm with dissolve
    "Although I thought that his revenge plan was an awful idea, I missed doing stuff with Alex."
    "He had changed. Whether or not for the better, I hadn’t decided yet."
    "But it didn’t really matter. He was my friend, and we were doing stuff together again, like old times."

    #Scene 2 - Starbucks Student Center
    scene bg black with fade
    play music "/Audio Dumpster/Waiting Music.mp3" fadeout 1.0 fadein 1.0 loop
    "We met up the next day to discuss the pitch."
    scene bg sturbacks with dissolve
    show ax calm with dissolve
    ax "Okay, so what’s our plan?"
    mc "I was thinking of a dating sim, but with cats."
    ax "So kind of like Hatoful Boyfriend?"
    mc "Yeah! But with cats."
    ax "Sounds weird, but its got cats, so…"
    stop music fadeout 1.0
    "Before Alex could continue, a girl in a demin jacket walked up to our table."
    show ax calm:
        linear 0.4 xalign 0.2
    show nm at right with dissolve
    show nm:
        linear 0.4 xalign 0.8
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    nm "Alex."
    ax "Naomi."
    nm "Who’s this?"
    mc "My name is [mcname]."
    nm "How do you two know each other?"
    mc "We’ve known each other since grade school."
    nm "Oh, is that so? How cute."
    show ax sad with dissolve
    ax "Can you please leave, Naomi?"
    "A shiver went down my spine as Naomi glared down at me, her arms crossed."
    nm "Don’t come back to me and say I didn’t tell you so."
    mc "How can I? You haven't told me anything."
    show nm:
        linear 0.4 xalign 0.85
    nm "I don't think you realize how popular your little boytoy here is around the campus."
    show ax calm with dissolve
    ax "What can I say? I get around."
    nm "He's what you might call a 'serial dater'."
    mc "I've never heard of that term before. Since when has Alex dated cereal?"
    nm "Ugh. No, 'serial' dater. He dates many women but never forms a deep bond or relationship with them."
    mc "Well, like I said, I've known him for a long time. Whatever kind of guy he is, I'm okay with it."
    show nm:
        linear 0.4 xalign 0.8
    nm "Do you love him?"
    "Alex looked at me expectantly."

    #Diverges into 2 options:
    menu ax_menu2:
        "What should I say?"
    #[Pos. Option] 
        "Of course!":
            $ ax_affection = ax_affection + 1
            mc "We're dating, so obviously I do."
            show nm:
                linear 0.4 xalign 0.85
            nm "That's so sweet. What cute little things has he told you?"
            ax "Our relationship isn't-"
            mc "He told me I have a cuter nose than you do."
            nm "That's obviously a lie."
            mc "I don't know - I'm looking at you right now, and I feel like your nose is gonna poke me in the eye. That's how big your nose is."
            nm "Ugh. Look - you're not foolilng anyone. Especially not everyone on campus who's talking about the two of you."
            mc "I..."

    #Neg. Option] 
        "Well...":
            mc "Uh... well, as a friend I do. If it's more, then... then I guess we'll find out."
            nm "Hm. Anyways, my point was that people have been talking. Like, a lot of people. Almost everybody. Watch yourself."

    #After Either Option -
    show ax sad with dissolve
    ax "Okay, seriously, Naomi - leave. Now."
    nm "You're digging yourself into a deep hole, [mcname]. Be wary of how far that hole goes. You may find yourself unable to get out."
    hide nm with dissolve
    show ax calm with dissolve
    show ax calm:
        linear 0.5 xalign 0.5
    stop music fadeout 1.0
    "Naomi left, and I sat there baffled."
    play music "/Audio Dumpster/Waiting Music.mp3" fadeout 1.0 fadein 1.0 loop
    mc "Everyone's talking about it?"
    ax "Don't worry. She's just trying to psyche you out."
    mc "If you say so."
    ax "I'm serious. Why are you even worrying about it now?"
    mc "Because I..."
    mc "(Because suddenly my feelings for you extend beyond the 'just friends' amount.)"
    mc "You know what? Nevermind."
    ax "Okay. Back to the game pitch. So, it's Hatoful Boyfriend with cats. What else?"
    mc "What... what do you mean, what else?"
    ax "How long do you want to work on it? Just for a quarter? Or longer?"
    mc "Uh... I dunno. Ask me another question."
    ax "Besides me, did you have anyone else you wanted to have join the group?"
    mc "Well, no. You're the only person I really know."
    ax "All right. What position did you want to be?"
    mc "The... the top position?"
    ax "What?"
    mc "I only know of two positions. Top and bottom."
    show ax blush with dissolve
    ax "Oh, god, no, not like... not \"bed\" position. Did you wanna be a writer, or a producer, or an artist, or-"
    show ax calm with dissolve
    mc "Designer. I want to be a designer."
    ax "I assumed that I would be the designer, but-"
    mc "No, no. I guess I meant junior designer. Assistant designer. You would, of course, be the main designer."
    ax "Are you actually interested in becoming a designer, or are you just trying to find an excuse to get closer to me?"
    mc "It could be a little of both."
    show ax happy with dissolve
    ax "If I didn't know better, I'd say that you were flirting with me."
    mc "You're reading too much into it. I want more coffee."
    show ax calm with dissolve
    ax "Then, I will go grab you more coffee, dear."
    "The word 'dear' made my stomach turn. He said it so... so casually."
    "Was this really just a revenge scheme, or was it quickly turning into something more?"

    #Scene 3 - Food Court
    scene bg black with fade
    play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
    "The conversation with Naomi yesterday made me realize that I didn't really know a lot about the \"new\" Alex."
    "Growing up, he was kind of a quiet guy. He was always super friendly, though."
    "And also, he was into sports, not art."
    "So, how did he become the Design leader of a Video Game Design Club?"
    scene bg foodcourt_2 with dissolve
    show ax calm with dissolve
    mc "I had no idea you were into the whole design thing."
    show ax happy with dissolve
    ax "Sure am! It's really pretty cool."
    mc "What exactly do you do?"
    show ax calm with dissolve
    ax "I do the aesthetics. Making sure it looks good and it’s all zen and lookin’ good. Things like that."
    mc "You were always into football. It’s so weird to think that you’re like, artsy now."
    ax "It was soccer, and it’s not an absurd idea."
    mc "But a self-proclaimed hardcore jock boy turning into a sensitive artist?"
    ax "I went to high school, broadened my horizons a little, and decided that I really enjoyed doing the whole design thing."
    mc "Is it something you just stumbled onto, or…?"
    ax "I was required to take a couple of electives, so I did a graphic design course one year. It was fun."
    mc "Huh."
    ax "You look confused. Do I need to explain it again?"
    mc "No, I’m just trying to figure out why, still."
    show ax happy with dissolve
    ax "There were a lot of cute chicks in the class that I wanted to impress. I worked hard, got good, and now here I am."
    mc "That makes a lot more sense. I thought that you'd have a more interesting story though."
    ax "You're right. I've been keeping the truth from you."
    mc "I... what?"
    ax "You see, the real reason I became a designer was because aliens abducted me, and-"
    mc "I'm just gonna stop you right there."
    show ax calm with dissolve
    ax "Too ridiculous?"
    mc "It sounds like something out of The Sims."
    ax "So do you actually have interest in learning the design aspect of video games, or are you just interested in designers?"
    mc "I... w-what?!"
    ax "You were never really into art either, growing up."
    mc "I liked it more than you did!"
    show ax happy with dissolve
    ax "You literally sneezed on a painting in a museum. On purpose. And got kicked out."
    mc "It was a modern art piece. It was just black rectangles on a canvas. It was awful, and it deserved it."
    ax "Mrs. Henderson wasn't happy."
    mc "What's your point?"
    show ax calm with dissolve
    ax "I guess I'm just trying to figure out why you're suddenly so into design."
    mc "I like learning. I ge to hang out with my best friend and learn at the same time. It's a win-win."
    ax "Hey, so, it’s five to three. We should probably get to class."
    hide ax calm with dissolve
    "Alex had changed so much… but at the same time, he hadn’t changed at all."

    #Scene 4 - SSLH
    scene bg meeting_1 with fade
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "A week passed, and the most important club meeting of the quarter was near - the Pitch Meeting."
    "I’ve never been a huge fan of speaking in front of huge crowds."
    "But with Alex at my side, we could conquer anything."
    show ax happy with dissolve
    mc "I hope we don't go first."
    ax "But if we go first, then we'll get it over with. We'll set the bar so high, that everyone else won't be able to reach it."
    mc "I dunno..."
    show ax calm with dissolve
    ax "Look, we'll be okay. Just breath. Most people here are very against public speaking. You're not the only one who's nervous."
    mc "I'm not sure that makes me feel better."
    "We ended up being the third group to go up."
    scene bg meeting_2 with dissolve
    show ax happy with dissolve
    ax "Hello everyone! My name is Alex, and this is my friend, [mcname]."
    mc "Hi! The game we're pitching is called 'Lovely Kitten Love'."
    mc "Uh... and so the basic gist of our game is that it's a dating simulator about cats."
    show ax calm with dissolve
    ax "Think 'Hatoful Boyfriend'."
    mc "But with cats."
    ax "Right. With cats.  So, me and [mcname] are going to head the design."
    ax "We're going to need everyone else though. Artists, writers, programmers."
    mc "Um, and the art style is going to be anime."
    ax "Yes, the art style! Anime. Shojo-style. 2D."
    mc "It, um, isn't meant to be a difficult project, so beginners are welcome."
    show ax happy with dissolve
    ax "Definitely. If you're new to the club, this is a good first project to do to learn the ropes."
    mc "And also, we do plan on finishing it this quarter."
    show ax calm with dissolve
    ax "This may depend on how many people join our group, though."
    mc "Yeah, so, if you have any questions, feel free to come and ask us."
    show ax happy with dissolve
    ax "[mcname] and I look forward to having you guys join our team!"
    scene bg meeting_1 with fade
    "As we went to sit back down, my heart was racing."
    "When everyone had finished pitching, Alex and I sat there. No one came up to us though."
    show ax calm with dissolve
    mc "It feels like everyone is avoiding us."
    ax "Nah. There were a lot of pitches this time. Ours wasn't very complicated, so people probably don't have questions."
    mc "I hope you're right."
    "The Audio Officer, Melody, showed up."
    show ax calm:
        linear 0.4 xalign 0.2
    show md calm at right with dissolve
    show md calm:
        linear 0.4 xalign 0.8
    md "Hey, you guys!"
    mc "Hi."
    ax "What's up, Melody?"
    show md happy2 with dissolve
    md "Nothin', nothin'. So, your game sounds like a furry simulator."
    ax "Thanks, Captain Obvious. What other insightful observations do you have?"
    show md happy with dissolve
    md "Oh, I'm soooo sorry if I offended you!"
    ax "Your sarcasm isn't necessary."
    show md calm with dissolve
    md "I'm just curious why you're choosing to do something so... basic. Is it because of [them]"
    mc "My name is [mcname]."
    md "But does Alex know that? He goes through girls on a weekly basis. Did he bother to learn your name?"
    show ax sad with dissolve
    ax "You should leave, Melody. There might be actual people with actual questions who want to talk with us, and you're scaring them away."
    show ax calm with dissolve
    md "Maybe I was interested in joining your little furry simulator."
    mc "It's not... really a furry simulator."
    ax "Are you actually interested?"
    md "No, but I could have been."
    ax "You're just wasting time now."
    show md happy with dissolve
    md "Whatever. Good luck getting anyone to join your lame little group. And enjoy your week-long relationship with Alex, [mcname]!"
    hide md happy with dissolve
    show ax calm:
        linear 0.4 xalign 0.5
    show ax sad with dissolve
    ax "Ugh. I'm so glad she's gone."
    mc "Did something happen between you and Melody?"
    ax "Just something stupid. You can't get along with everybody."
    mc "You didn't date her too, did you?"
    show ax calm with dissolve
    ax "God, no. The meeting's almost done. Wanna leave early to grab a burger across the street?"
    mc "Sounds great."

    #Scene 5 - Aldrich Park
    scene bg black with fade
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    "A couple days later, Alex and I finally had time to catch up in Aldrich Park."
    scene bg park_1 with dissolve
    show ax calm with dissolve
    ax "What do you think of the campus so far? It's not quite UCLA, but..."
    mc "Well, I think it's really, really green."
    ax "Is... is that good?"
    mc "Nature is good. And I like how like, you can get most places by going in a circle."
    ax "Ring Road?"
    mc "Yeah! Ring Road is super convenient."
    ax "What have you been up to the past few years?"
    mc "I'm... sorry, what?"
    ax "We haven't really had time to catch up. What's been going on in your life? Any boyfriends or girlfriends?"
    mc "Well... I did have a steady-ish relationship with someone my junior year of High School."
    ax "What were they like?"
    mc "Quiet. Artsy. Kind."
    ax "Sounds like a great person. Why'd you guy's break up?"
    mc "It just didn't feel right."
    ax "Is there a... particular type of person you're looking for now?"
    mc "I haven't really thought about it. Why, have you heard something?"
    show ax happy with dissolve
    ax "About someone liking you? No, not yet. But I do know a lot of people. I could help hook you up."
    mc "Ugh, no thanks. I just want to focus on school."
    show ax calm with dissolve
    ax "Same ol' [mcname]. Always the good student."
    mc "Hey! I like my A's."
    ax "I like your A's too! I was just wondering."

    menu ax_menu3:
        "What should I say?"
        "Ask about Alex's feelings.":
            $ ax_affection = ax_affection + 1
            #[Pos. Option] - Ask About Alex's Feelings
            mc "Maybe I'm reading too much into it, but it sounds like maybe you're getting feelings for me."
            show ax blush with dissolve
            ax "What!? No. I like Naomi. You're helping me get Naomi back."
            mc "I thought this was a revenge thing."
            ax "It started out that way, but I decided to try to get her back again."
            mc "After she was so rude the other day?"
            show ax calm with dissolve
            ax "I'm allowed to change my mind."
            mc "Just to make sure - you don't like me like that, do you?"
            show ax blush with dissolve
            ax "I... um... it's irrelevant."
            "Little did Alex know that maybe I was starting to have feelings for him too..."
        "Let it go.":
            #[Neg. Option] - Let It Go
            mc "I appreciate your concern for my love life, but I'm fine."
            ax "Are you sure? Are you really sure?"
            mc "If I'm still single at the end of the school year, then we can talk."
            ax "I'm going to hold you to that."
            mc "(Does he have feelings for me....?)"
            mc "(No... no we're just friends.)"

    #After Either Option -
    show ax calm with dissolve
    ax "Anyways, forget about it. We've got more important things - like Lovely Kitten Love."
    mc "Right. We have to make sure it's not a furry simulator."
    ax "It's gonna take some very careful writing, but we can do it."
    mc "Do you have any connections to a writer who could make it... not a furry simulator?"
    ax "I'll ask around after class. The club is huge - there has to be someone."
    hide ax calm with dissolve
    "As we walked to class, Alex looked like he was hiding something."
    "But, I didn't want to pry, so I just continued acting like we didn't have the conversation at all."

    #Scene 6 - Food Court
    scene bg foodcourt_2 with fade
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    "I had gotten a text from Alex early in the morning."
    show ax calm with dissolve
    ax "I'm really glad you're here."
    mc "Um... thanks? Did you find a solid writer that might want to join our group?"
    ax "This has nothing to do with the video game."
    mc "Is something wrong?"
    "Alex had become uncharacteristically quiet."
    show ax blush with dissolve
    ax "I've got a confession to make."
    mc "What happened? Is it about Naomi?"
    ax "Yes. No. Nothing. Nothing bad."
    mc "Whatever it is, it's not going to change our relationship."
    ax "I wouldn't be so sure about that."
    mc "Well, are you going to tell me? Or keep stringing me along?"
    ax "I'm sorry. I'm sorry."
    ax "..."
    ax "I don't want to pretend anymore."
    mc "Pretend what?"
    ax "This. Us. You and me. [mcname], I've liked you for so long. Since we were kids."
    mc "Are you serious?"
    ax "100\%."
    mc "I... don't know what to say..."
    ax "Say that we can stop pretending. Say that you feel the same way about me. I love you, [mcname]."

    menu ax_menu4:
        "How should I respond?"
        "I love you!":
            #CHOICE A [Neg] - "I love you!"
            mc "I love you too, Alex. Let's... let's stop pretending."
            show ax calm with dissolve
            ax "Phew... that was hard..."
            mc "Just… what about Naomi?"
            ax "Yeah, she's out of the picture. I can't stop ignoring these... feelings I have for you."
            mc "..."
            mc "So is that… that’s it?"
            ax "Besides the obligatory social media update spam, yeah. I guess that’s it."
            mc "I don’t feel any different."
            ax "Me neither. I think we just need time to let it sink in."
            "It all happened so fast, that I wasn't sure it had even happened at all."
            "But I'm glad it did."
            "I loved my best friend, and he loved me."
            #Goes to CHOICE A ROUTE.
            jump ax_choiceA1
        "Wait a second...":
            stop music fadeout 1.0
            #CHOICE B [Pos] - "Wait a second..."
            $ ax_affection = ax_affection + 1
            mc "I'm still not completely convinced, Alex."
            play music "/Audio Dumpster/Joke.mp3" fadeout 1.0 fadein 1.0 loop
            ax "Y-yeah... okay. Y'know, I was just kidding."
            mc "It sure didn't look like it."
            show ax sad with dissolve
            ax "Nah. You and me, officially a couple? If we were going to do that, we would have done it forever ago."
            mc "Yeah, I guess. Are you okay?"
            show ax calm with dissolve
            ax "Sure! Why wouldn’t I be okay?"
            mc "Again, you just seemed to take it super personally just then."
            ax "Nah, nah, we’re cool. Maybe we should um, just break up."
            mc "Break up? Oh, right - the whole fake revenge thing. You sure we've gotten revenge against Naomi?"
            show ax sad with dissolve
            ax "Doesn't matter. I don't want to lie like this anymore."
            mc "Are you okay, Alex?"
            show ax calm with dissolve
            ax "I'm okay. We’re good. Let’s finish eating."
            hide ax calm with dissolve
            "Lunch was awkward after that. Alex purposefully avoided eye contact with me."
            "We talked about Lovely Kitten Love, but he only gave one word answers."
            "He was acting like I had just punched him in the stomach or something."
            "I don't know what he wanted me to say."
            "We were friends - best friends - and I kind of wanted it to stay that way."
            #Goes to CHOICE B ROUTE.
            jump ax_choiceB1

label ax_choiceA1:
    #CHOICE A ROUTE
    #[scene 1 - Aldrich Park]
    scene bg park_1 with fade
    play music "/Audio Dumpster/Piano Solo 1.mp3" fadeout 1.0 fadein 1.0 loop
    "I had never been in a relationship until now."
    "Sure, there were crushes, but never anything serious."
    mc "(Now, though...)"
    show ax happy with dissolve
    "Alex and I were laying on the grass in Aldrich park, basking in the warmth of the sun."
    "His eyes crinkled as he laughed at a stupid joke he made. I couldn't help but giggle along with him."
    mc "(I couldn't be happier.)"
    #--black--
    "Nothing could get between us."

    #--Food Court--
    scene bg foodcourt
    show ax calm at left with dissolve
    show ax calm:
        linear 0.4 xalign 0.2
    show nm at right with dissolve
    show nm:
        linear 0.4 xalign 0.8
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    nm "Wow. It's week four and you two are still together. That's a first for you, isn't it, Alex?"
    mc "(Ech...)"
    "It's been a week since we'd gotten together."
    "We were discussing the game's progress over dinner when Naomi approached us."
    ax "What do you want this time?"
    nm "Can I talk to you? Privately?"
    show ax sad with dissolve
    ax "Anything you need to tell me, you can tell me here, in front of [mcname]."
    nm "No. No, I can't. Pleeease?"
    ax "Wow. Begging. That's a new low."
    show ax calm with dissolve
    ax "You know what? Fine. [mcname], we'll be right back."
    hide ax calm with dissolve
    hide nm calm with dissolve
    "Naomi took Alex aside, far enough to where I couldn't hear what they were saying."
    "I watched as Alex's initially gruff features grdually soften."
    "He laughed at one point, and I could feel my face getting hot from jealousy.."
    "By the time they returned, the two of them were all smiles."
    show ax happy at left with dissolve
    show ax happy:
        linear 0.4 xalign 0.2
    show nm at right with dissolve
    show nm:
        linear 0.4 xalign 0.8
    ax "Naomi wants to help with our game."
    mc "And you couldn't have that conversation with me?"
    ax "Sorry. She's going to help with the writing."
    mc "Do I get any say in this?"
    show ax calm with dissolve
    ax "[mcname], we need the help."
    mc "Ugh. Fine. Welcome aboard... I guess."
    nm "Such enthusiasm! You make me feel soooo welcomed!"
    mc "Is there ever a time when you aren't sarcastic?"
    nm "Sorry, [mcname], that's just how I roll."
    mc "Tch..."
    mc "(I really don't like this girl.)"
    "I make a mental note to myself to keep a close watch on her."

    #[scene 2 - SC Starbucks]
    scene bg black with fade
    play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
    "Weeks passed, and we were so happy."
    "We did everything together. Just like old times."
    scene bg sturbacks with dissolve
    show ax happy with dissolve
    ax "Come on, just a liiittle closer..."
    mc "Haha, stop it! We're in public!"
    ax "Oh, you know that doesn't stop me."
    mc "Geez..."
    "...Well, things are a bit different from what it was before."
    mc "(Still, I wouldn't change a thing.)"
    show ax happy:
        linear 0.4 xalign 0.2
    show nm at right with dissolve
    show nm:
        linear 0.4 xalign 0.8
    nm "Ah, Alex!"
    show ax calm with dissolve
    ax "Naomi! Hey, what's up?"
    nm "Can't say I'm up to anything, but I can see you two are fairly busy yourselves."
    show ax happy with dissolve
    ax "Haha! Yea, well..."
    mc "..."
    mc "(I take that back.)"
    "I sighed. Naomi and Alex had gotten into a full blown conversation."
    "I meddled with his fingers and focused entirely on my phone the whole time."
    stop music fadeout 1.0
    "When the conversation finally ended and Naomi was about to leave, I allowed myself to look up at her."
    show nm:
        linear 0.3 xalign 0.85
    nm "...Heh"
    mc "!!"
    mc "(Did she-- Did she just smirk at me?!)"
    "I stared at her back as she left the building."
    mc "That little..."
    show ax calm with dissolve
    ax "Hello..?"
    mc "Ugh... I can't stand her!"
    ax "Huh?"
    mc "The way you talk to her so easily too... I can't stand it!"
    "I turned to face my boyfriend, completely red in the face."
    mc "Tell me, Alex. Did you ever actually have feelings for Naomi?"
    ax "What?"
    mc "Did you ever LIKE her the way you like me?"
    ax "Why are you asking?"
    mc "I'm just trying to figure out how serious you two were."
    ax "[mcname]. We went on one date."
    mc "Okay, and how far did you two go?"
    show ax blush with dissolve
    ax "Uhh.. Haha, what do you mean?"
    mc "You know what I mean! Don't dodge the question."
    ax "..."
    "We stared each other down."
    "It was absolutely frustrating. Why couldn't he just answer me?"
    "After about half a minute, Alex let out a sigh, and started putting away his things."
    mc "What's this?"
    show ax sad with dissolve
    ax "I just remembered something. I've got to go."
    mc "What?!"
    "He slung his bag over his shoulder. He looked as though he was about to leave right there and then."
    "But, he paused and looked at me."
    mc "Alex?"
    play music "/Audio Dumpster/Bad Ending.mp3" fadeout 1.0 fadein 1.0 loop
    ax "..."
    ax "I'll see you around, [mcname]."

    #ENDING
    #[end- bad- Food Court]
    scene bg black with fade
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    "Our game was set to be completed in the following week."
    "Alex had stopped returning my texts. He didn't want to meet up for lunch..."
    "And then I found out the truth."
    scene bg foodcourt_2 with dissolve
    show ax calm with dissolve
    mc "Alex? I thought I’d find you here."
    ax "Oh. [mcname]. What are you doing here?"
    mc "You’re my boyfriend, and you’re basically acting like I don’t exist."
    ax "What? Nah."
    mc "I’ve texted you three times since this morning. A couple people dropped out, and the game needs to be finished by next week."
    show ax sad with dissolve
    ax "Sorry. I’ve been distracted."
    mc "Yeah, I get that. But that doesn’t give you the right to ignore me."
    ax "I wasn’t ignoring you."
    mc "You went back to Denim Jacket?"
    show ax calm with dissolve
    ax "She's got a name."
    mc "I don't care WHAT her name is. How could you do this to me?"
    ax "Everyone keeps on telling me how much I've changed. And maybe I have."
    show ax sad with dissolve
    ax "But so have you. It feels like you've been leaching off me."
    mc "Leaching? I’m leaching off you? What does that even mean?"
    ax "You used to be so independent, never took no for an answer."
    mc "You're really going to pin all of this on me?"
    ax "We didn't finish the game because of YOU."
    mc "How is it my fault!?"
    ax "Your constant nagging, dragging me to places instead of to the meetings so we could finish things."
    mc "That's what couples do!"
    ax "If you love someone, then you're not going to keep them from doing what they want to do."
    mc "I thought this was what you wanted to do!"
    ax "I changed my mind. I’m leaving."
    mc "Alex! Don't leave, please! I love you!"
    ax "Yeah, and I thought I loved you too."
    hide ax sad with dissolve
    "Looking back, the last few weeks had been a trainwreck."
    scene bg black with fade
    "I lost the love of my life."
    "I lost the best friendship I’d ever had."
    "Our cat dating sim never ended up getting finished."
    "I ended up all alone, and it hurt."
    "I tried to find a silver lining in the whole situation, but there wasn’t one."
    "There was nothing I could do. It was the death of the best friendship I’d ever had."
    scene bg black with fade
    ".:. Bad Ending."
    $ MainMenu(confirm=False)()
    #return

label ax_choiceB1:
    #CHOICE B
    #[scene 1 - Aldrich Park]
    scene bg park_2 with fade
    play music "/Audio Dumpster/Aldrich Park.mp3" fadeout 1.0 fadein 1.0 loop
    "A few days had passed since we 'broke up'."
    show ax calm with dissolve
    ax "Look, about the other day..."
    mc "Forget about it. Let's just work on our game, okay?"
    show ax sad with dissolve
    ax "No, I don’t want to forget about it. I want to talk about it."
    mc "What’s there to talk about?"
    ax "I… I know I said I was kidding when I said everything, but a small part of me wasn’t."
    mc "I kind of figured. You were always a bad liar."
    show ax calm with dissolve
    ax "Anyways, about the game..."
    mc "Ugh, I know. It gonna be tight with only one full-time writer, but I think we'll be okay."
    stop music fadeout 1.0
    ax "Yeah, about that..."
    play music "/Audio Dumpster/Tension.mp3" fadeout 1.0 fadein 1.0 loop
    "Naomi approached us."
    show ax calm:
        linear 0.4 xalign 0.2
    show nm at right with dissolve
    show nm:
        linear 0.3 xalign 0.8
    nm "[mcname]. Alex. Sorry to hear about you two breaking up. But, I did tell you so."
    ax "Hi Naomi. It's nice to see you, too."
    nm "So, did you tell [mcname] about the great news?"
    mc "What news?"
    nm "Alex and I got back together!"
    show ax blush with dissolve
    ax "No, we didn't. We're just going on a date tonight. That's it."
    "I felt betrayed. I mean, sure, I kind of turned him down the other day, but hearing Naomi's words still hurt..."
    mc "Um... he didn't tell me. But good for you. I'm happy."
    nm "Do you still need some writing help?"
    mc "Writing help?"
    ax "I may have... asked her to help since we're short a person on the team."
    mc "Are you even a part of the club?"
    show nm:
        linear 0.3 xalign 0.85
    nm "Not officially. But I do dabble in Creative Writing."
    mc "Hm... I don't think we'll need your help, Naomi. We'll be fine."
    nm "That's not what Alex was telling me last night."
    mc "What are you hiding from me?"
    ax "Nothing! We'll talk about it later. I'll talk to you about it later too, Naomi. In a separate conversation. Bye."
    hide nm with dissolve
    show ax blush:
        linear 0.4 xalign 0.5
    show ax calm with dissolve
    stop music fadeout 1.0
    "Naomi didn't look happy, but she still left, and Alex and I were alone again."
    mc "Okay, it's later! What are you hiding from me?"
    ax "It's been forty-five seconds, if that."
    mc "Can you please stop avoiding my question?"
    ax "We don't have a full team."
    mc "I know that part."
    ax "It's going to be hard to finish this quarter unless we get some outside help."
    mc "I know that, too."
    ax "And... and that's it, isn't it?"

    menu ax_menu5:
        "What should I say?"
        "Ask about feelings for Naomi.":
            #[Pos Option] - ("Ask About Feelings for Naomi")
            $ ax_affection = ax_affection + 1
            mc "So... so do you love Naomi?"
            show ax sad with dissolve
            ax "I don't love her, but I still have feelings for her, [mcname]."
            mc "But the whole plan was to get back at her for..."
            show ax calm with dissolve
            ax "She's still pretty. And right now, she can help us. So I'm gonna try to get on her good side, okay?"
            mc "She's just so mean..."
            ax "You're not jealous, are you?"
            mc "No! I'm just woried about your well-being. Be careful, okay?"
            "Hearing that Alex was going out with Naomi did hurt a little."
            "I don't know why. After all, we were just friends..."
        "Ask about relationship with Naomi":
            #[Neg Option] - ("Ask About Relationship With Naomi")
            mc "When did you guys get back together anyways?"
            ax "Last week."
            mc "I honestly didn't think she'd want you back after everything she thought about you."
            ax "Me neither. But then she found out about us and said that she decided to give me a second cahnge."
            mc "Why's that?"
            ax "She never really explained why, and I don't really care enough to question it."
            mc "As long as you guys are happy..."

    #Either Option Leads To -
    ax "Look, [mcname], forget about Naomi. She's not relevant right now."
    mc "Right. You're right."
    scene bg black with fade
    "Later that day, I got a weird text."
    show phone with dissolve
    "'Hey, it's Naomi.'"
    mc "'How did you even get this number?'"
    nm "'I asked Alex to give it to me.'"
    mc "'Oh.'"
    nm "'[mcname], if it's too uncomfortable for you, then I won't offer to help you guys out.'"
    mc "'What do you mean by 'uncomfortable'?'"
    nm "'If what's going on between me and Alex makes you uncomfortable...'"
    mc "'No, it's fine. But I am confused why you asked him out again.'"
    nm "'I think the first time we went out, I acted out of line. He's a nice guy.'"
    mc "'He really is. If you ever hurt him though, you'll have to deal with me.'"
    nm "'Yes, ma'am. ;)'"
    hide phone with dissolve
    "I told Naomi that Alex would contact her if we did need her help."
    "I was tired of dealing with her at this point."
    "Plus, I didn't want to be dragged into whatever would potentially happen between her and Alex again."

    #[scene 2 - SC Starbucks]
    scene bg black with fade
    play music "/Audio Dumpster/Food Court.mp3" fadeout 1.0 fadein 1.0 loop
    "Our game was set to be completed in the following week."
    "We still hadn't found a replacement writer and were really struggling."
    scene bg sturbacks with dissolve
    show ax calm with dissolve
    mc "We have four of the five routes done. We just have one more."
    ax "Which one?"
    mc "Tabby's."
    ax "Remind me again - what was that one again?"
    mc "Tabby is the flirty jock who gets around."
    ax "I... Did you just admit to giving me a fursona?"
    mc "Yeah. Sorry. But not sorry."
    ax "..."
    mc "So... I was hoping that you could write it. I've got a ton of schoolwork to catch up on."
    ax "Actually, I think we should have Naomi help us."
    mc "Does it work like that, where we can just get someone else on board that's outside the club?"
    ax "People who aren't students are allowed to work on projects. It's the same concept."
    mc "Is she going to have time to finish? Or, should we just scrap Tabby's route?"
    ax "I've been writing a little of it. All Naomi would need to do is polish some parts to make it... coherent."
    mc "Well, then I think we have our answer. Hit her up."
    show ax happy with dissolve
    ax "Cool. This way, we'll have time to finish the other parts!"
    mc "As long as it all gets done, it doesn't matter to me!"
    hide ax happy with dissolve
    "Alex and I were colelcting backgrounds for the game, since everyone else was busy."
    "Naomi texted me."
    show phone with dissolve
    nm "'Hey, it's Naomi again.'"
    mc "'Hey,  what's up?'"
    nm "'Alex texted me saying that you guys needed help.'"
    mc "'Yes, please. Neither of us are very good writers.'"
    nm "'It's cool. Did you have any requests about what you want in it?'"
    mc "'Nah, just make it make sense.'"
    nm "'Will do.'"
    hide phone with dissolve
    "A part of me regretted having Naomi finish Tabby's story."
    "I felt like she was going to write something akin to a lame, crappy romantic comedy movie plot."
    "I didn't have time to worry about it, though."

    #[scene 3 - VGDC Lab in DBH]
    scene bg gameroom with fade
    play music "/Audio Dumpster/Game Lab.mp3" fadeout 1.0 fadein 1.0 loop
    "Game testing day arrived, and I felt just as nervous as the day we had originally pitched the game."
    show ax calm with dissolve
    ax "Hey, breathe."
    mc "I am breating."
    ax "Well, do more of it. You look like you're gonna pass out."
    mc "I feel like passing out."
    ax "Everything's going to be fine. You don't need to be so nervous."
    mc "But what if people don't like it?"
    ax "It doesn't matter. This is a prototype, not the finalized version. There will be bugs.But we'll fix them."
    mc "Right. Just a prototype..."
    mc "Everyone looks like they're having a lot of fun! I'm getting jealous."
    ax "There's nothing against you playing the game now, too."
    mc "Yes! Come on, you've gotta help me make decisions."
    "Alex and I opeened up the game on his laptop."
    menu ax_menu6:
        "What should I do?"
        "Choose Tabby's path.":
            #[pos option] ("Choose Tabby's Path")
            $ ax_affection = ax_affection + 1
            ax "Tabby's route, huh?"
            mc "Thought I'd finally see how Naomi's writing holds up."
            ax "It's really pretty good, actually."
            "Alex and I played through the route together, making all the worse decisions possible."
            "Finally, when Tabby had to confess his feelings for the main character..."
            mc "'I can't love you, because I love somebody else.' What!? What the hell!?"
            ax "I have no idea what Tabby's doing. I didn't get this far."
            mc "You didn't even finish reading it?"
            ax "No! Click next."
            mc "'I'm sorry, but I love my best friend.' Dude, Tabby just rejected my feelings for him."
            show ax sad with dissolve
            ax "That sounds... oddly familiar."
            mc "Oh. Did you tell Naomi -"
            show ax calm with dissolve
            ax "No! I don't know why she chose to write it this way. Just click next."
            mc "Aw, the main character looks so sad! 'I understand. Can we still be friends?' Awwww!!"
            ax "Ugh!!!! Click next!!"
            mc "'Of course we can still be friends.' I wonder how long that's gonna last..."
            "Alex and I saw strange parallels between Tabby's route and the events that had happened over the past few weeks."
            "In the end, Tabby and the main character ended up together anyways."
            "Maybe... maybe, when given the chance, I need to be straightforward with Alex about my feelings..."
        "Choose a different path.":
            #[Neg Option] ("Choose A Different Path")
            ax "Cali's path, huh?"
            mc "Yup. Calico's are my favorite."
            ax "I thought for sure that you would have chosen Tabby's route."
            mc "And finally read the crap that Naomi came up with? No thanks."
            ax "You don't know that."
            mc "I don't. That just means you'll have to play through two routes with me."
            ax "You're a sneaky one."
            "Alex and I played through Cali's path. It was straightforward and kind of unmemorable."
            mc "That's it? After all that, and they break up?"
            ax "Who wrote this route?"
            mc "Some chick. I don't even remember her name. She was the one really into politics."
            ax "Next time, maybe we should get writing samples before we tell people to write for us."
            mc "That is an excellent idea. But, like you said, this is just a prototype. Maybe Naomi could fix it for us?"

    #Either Option Leads To - 
    ax "You know that Naomi and I broke up, right?"
    mc "Again?"
    show ax blush with dissolve
    ax "Yup. Well, kind of. We didn't really break up the first time, but... whatever. I had it coming."
    mc "You, um, kind of did. Sorry."
    show ax calm with dissolve
    ax "It's okay. I'll deal with it."


## JUMP TO ENDING ##
    if ax_affection >= 4:
        jump ax_end_good
    else:
        jump ax_end_normal
    #ENDING
label ax_end_normal:
    #[end - normal - student center]
    scene bg black with fade
    stop music fadeout 1.0
    "The rest of the quarter went on without a hitch."
    "Alex and I finished our game, and everything's been progressing nicely."
    "That is, aside from the awkward tension between me and Alex."
    "Everytime we met up, the atmosphere always became heavy, and neither of us could talk freely."
    "It was frustrating."
    "I wanted our old relationship back."
    scene bg studentcenter with dissolve
    "--phone buzz--"
    show phone with dissolve
    ax "'Hey, can we meet up at the food court?'"
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    mc "..."
    mc "'Sure. Be there in 5."
    "In my heart, I hoped Alex felt the same."

    #--food court--
    scene bg foodcourt with dissolve
    show ax sad with dissolve
    mc "..."
    ax "..."
    mc "Umm... So, what did you-"
    ax "I’m sorry." 
    ax "Listen, [mcname], I really regret what I did before, and I can't stand how things are between us."
    ax "Can't we... go back to being friends?"
    mc "..."
    mc "I feel the same way, Alex."
    mc "But, it’s gonna take some time."
    ax "Well, sure. Of course. But we’ve got all the time in the world."
    mc "Yeah. You’re right. Let’s start our friendship over."
    show ax calm with dissolve
    ax "The best way to do that is by grabbing coffee."
    mc "Haha. Sounds great."
    "Looking back, the last few weeks had been a trainwreck, the worst of it being I'd lost the best friendship I’d ever had."
    "But I was still standing, and I had the chance to win my best friend back."
    "Things could only go up from here."
    scene bg black with fade
    ".:. Normal Ending."
    $ MainMenu(confirm=False)()
    #return
    
label ax_end_good:
    #ENDING
    #[end- good- VDGC Lab in DBH]
    scene bg gameroom with fade
    show ax happy with dissolve
    play music "/Audio Dumpster/Somber Music.mp3" fadeout 1.0 fadein 1.0 loop
    ax "Thanks for everything, [mcname]."
    mc "It's what friends do!"
    ax "Then I'm super lucky to have a friend like you."
    mc "Do you ever think of like, what could have been?"
    show ax calm with dissolve
    ax "I’m not sure what you mean."
    mc "What if I had said that I loved you too a few weeks ago?"
    ax "I dunno. So much has happened that I haven't really thought about it."
    mc "Do you think things could have worked out between us?"
    ax "Romantically? I guess we'll never know."
    mc "Why don't we try it out?"
    show ax blush with dissolve
    ax "Is that your way of asking me out on a date?"
    mc "Hm. I guess I am!"
    show ax happy with dissolve
    ax "Okay, sure! Let's try it out."
    mc "Alex?"
    ax "Yeah?"
    mc "I love you. I'm sorry I didn't tell you a few weeks ago."
    show ax calm with dissolve
    ax "It's totally cool, [mcname]. I love you, too."
    scene bg black with fade
    ".:. Good Ending."
    return