## PROLOGUE ##

# PROLOGUE SCENE1
label prologue_scene1:
    ## SCENE AUDIO ##
    $ renpy.music.set_volume(1.0, 0, channel="music")
    queue music "<loop 11.3609>/Audio Dumpster/Food Court.mp3" loop
    # !! Need to fadeout music before playing the next audio track
    ## END SCENE AUDIO ##
    scene bg black with fade
    "My name is [mcname]"
    "I'd consider myself a pretty good student. I attend class, get good grades, and ended the semester with an admirable GPA."
    "Though I wasn't entirely confident about it, I genuinely thought I had a shot at getting accepted into my dream school, UCLA."
    "\"To become a Bruin... Honestly, that'd be a dream come true.\" I'd think."
    "..."
    "Unfortunately, life tends to not go the way I want it to."
    "And today was no exception."
    #--Aldrich Park 1--
    scene bg park_1 with dissolve
    show ax calm with dissolve
    unknown "[mcname], this way! My club's booth is just up ahead!"
    mc "\"Alex, I told you, I'm not interested in joining any clubs this quarter! Just, let go of me already!\""
    ax "Hmm? Sorry, did you say something?"
    mc "\"Tch. You'd think someone would change after these years, but you haven't grown at all.\""
    mc "\"Well, not mentally, at least.\""
    ax "Hmm... You're not wrong there."
    mc "\"Oh, so you heard that?\""
    show ax happy with dissolve
    ax"Haha! Selective hearing, I guess!"
    mc "\"Selective hearing my ass\""
    show ax calm with dissolve
    "This guy is Alexander, or Alex for short."
    "As a result of our parents being close friends, he and I were introduced at a young age and pretty much grew up together."
    "For better or for worse, we became each others' confidants. I knew all his ins and outs, and he knew mine."
    "We did just about everything together, our bickering a result of how comfortable we are with each other."
    "That is, until his family moved to a different state, and we spent the last four years just chatting online whenever we could."
    mc "(It's been four whole years...)"
    "He was so ecsatic when he found out I would be attending UCI, he wanted to meet up as soon as we could."
    "Physically, Alex definitely changed over the years. Admittedly, for the better."
    mc "(But my feelings for him...)"
    ax "[mcname]. [mcname], look, over there."
    mc "\"What?\""
    "I turned to look in the direction he was pointing, only to see a group of girls chatting amongst themselves."
    ax "See that girl in the denim jacket?"
    mc "\"Yea...?\""
    ax "..."
    ax "I need her number."
    mc "..."
    mc "(My feelings for him definitely changed for the worse.)"
    ax "I'm sorry [mcname], but I have to-"
    mc "\"No no, by all means. Go ahead, I insist.\""
    ax "Really? You won't miss me?"
    mc "\"Absolutely not. In fact, please leave.\""
    ax "Haha, harsh!"
    "Letting out a little laugh, Alex let go of my arm and took out his phone, grooming his hair as he stared at his reflection."
    "Once he was satisfied, the corners of his lips pulled into charming smile, and he strode to his target."
    hide ax calm with dissolve
    mc "(Finally...)" 
    "I wrapped my hand around my arm, now free from the philanderer's grasp, and glanced around Aldrich Park."
    "Today was the Involvement Fair, so the area was filled with booths and students."
    mc "(Can't say this is my kind of scene.)"
    "I didn't want to go, but Alex was insitent on making me join his club."
    mc "(At least now, I can finally go back to my room...)"
    "I let out a sigh, and began following a road that would hopefully lead me out of here."
    unknown "Hey, you!"
    mc "..."
    unknown "Huh? Hellooo...?"
    mc "..."
    mc "(Just keep facing forward, and they'll just give up-)"
    with hpunch
    unknown "Boo!"
    show yu happy with dissolve
    mc "?!"
    "I jolted back, path now blocked by a grinning girl with purple hair."
    unknown "Haha, gotcha!"
    unknown "No escaping from me now, alright?"
    mc "(Damn. Foiled again...)"
    unknown "Hey, don't give me that look... Come on, just follow me for a sec, okay? There's this really cool club you should totally check out!"
    mc "\"Umm... Sorry, but I'm actually not interest-\""
    unknown "Nonsense! This way!"
    show yu calm with dissolve
    "And just like that, she placed a hand on my back, and whisked me away."
    hide yu calm with dissolve
    mc "(Why me...)"
    return
# END PROLOGUE SCENE1

# PROLOGUE SCENE2
label prologue_scene2:
    #--Aldrich Park 2--
    scene bg park_2 with fade
    show yu calm with dissolve
    unknown "Here we are!"
    show yu calm:
        linear 0.5 xalign 0.2
    show kd calm with dissolve
    show kd calm:
        linear 0.5 xalign 0.8
    unknown "Hmm..?"
    "The girl brought me to a booth with a video game themed banner. There was a guy wearing a suit sitting behind it."
    "He stared at me for a moment before turning to the girl."
    unknown "Yukiko, please tell me you didn't just abduct this person."
    show yu happy with dissolve
    yu "Tooootally not! [they_c] came here out of their own free will! Right?"
    mc "..."
    unknown "It certainly doesn't seem like it."
    yu "Oh lighten up! I know how much you love people, so I brought you one!"
    show kd angry with dissolve
    unknown "Tch."
    show yu calm with dissolve
    yu "Alright bud, I'll leave you in Kendrick's hands, alright? I've got some more hunting to do."
    mc "(Wait, you're just going to leave me here?!)"
    hide yu calm with dissolve
    show kd angry:
        linear 0.5 xalign 0.5
    "Before I got to voice my thoughts, the girl named Yukiko ran away, leaving me with this Kendrick guy."
    "He clicked his tongue."
    kd "How unprofessional." 
    mc "..."
    mc "\"Umm...\""
    kd "..."
    "He shot a sharp glance at me, and I awkwardly scratched my cheek."
    mc "\"Can I just... go..?\""
    kd "..."
    show kd thinking with dissolve
    "He looked away for a moment, probably contemplating something. But soon after, he sighed and walked around the table, making his way towards me."
    kd "I'm afraid not. I have a duty, and I am expected to fulfill it."
    "I couldn't help but let out a sigh." 
    kd "... Seeing as you're less than enthusiastic about this, I suppose there's no point in asking you what you'd like to know."
    kd "Please, bear with me while I go over the activities and goals of this club. I'll try to keep it short."
    mc "\"Alright... Fine by me, I guess.\""
    show kd calm with dissolve
    "He cleared his throat."
    kd "We are known at the Video Game Development Club, or the VGDC for short."
    kd "No matter the major of the individual, this club is open to anyone and everyone interested in producing video games."
    kd "There are six departments: programming, art, writing, audio, production, and design. I, personally, am part of the production department."
    mc "\"Unsurprising...\""
    kd "We- of different skill levels, both beginner and seasoned- gather and formulate teams. From there, each team creates their own game."
    mc "..."
    kd "And that's the main gist of it. Would you happen to be interested in joining?"
    mc "\"Hmm...\""
    mc "\"That... honestly sounds really cool.\""
    kd "Oh?"
    mc "\"But, I actually kinda planned to not join any clubs my first quarter here.\""
    kd "... I see."
    mc "\"Yea. I'm sorry, but I'm going to get going now.\""
    kd "DBH 1412"
    mc "\"Huh?\""
    kd "That's where the club meets. If you ever change your mind, there will likely be an officer there that can help you."
    mc "\"Oh. Uh, alright. Thank you...\""
    hide kd calm with dissolve
    "He gave a curt nod before returning back to his post, and I took this as my cue to leave."
    mc "\"He seemed... nice?\""
    mc "..."
    mc "(That suit is seriously overkill for a casual involvement fair, though...)"
    return
# END PROLOGUE SCENE2
    
# PROLOGUE SCENE3
label prologue_scene3:
    #--Student Center--
    scene bg black with fade
    "--A few days later--" 
    scene bg studentcenter with dissolve
    mc "..."
    "I've gotten through my first academic week here in UCI. Classes are faced paced, but nothing I can't work with."
    "I'm completing my work, attending my classes, and reading on my free time. The quarter is going smoothly, so everything should be fine as is. But..."
    mc "(I'm boored...)"
    "Everything is routine. The first week was so mundane, I actually regret not taking a closer look at the booths during the involvement fair."
    mc "(A club...)"
    mc "..."
    mc "(That suit guy said VGDC met in DBH 1412, right?)"
    "I thought for a minute. It wouldn't hurt to give it a shot, would it?"
    "Making up my mind, I picked my book up from the table and made my way towards the game room"
    return
# END PROLOGUE SCENE3
         
 # PROLOGUE SCENE4
label prologue_scene4:
    scene bg park_1 with fade
    mc "\"Let's see...\""
    "I was walking through Aldrich Park, inputing DBH on the Zotfinder app to guide me."
    "The park had been relatively empty, so I didn't bother looking up and see where I was going."
    mc "\"DBH... Ah, it should be up a- woa!\""
    with hpunch
    "Something hit my arm, hard."
    "Next thing I knew, I was on the floor, my phone and book joining me on the cold, hard ground."
    mc "\"Ow.. Who the heck..?\""
    mc "!!"
    show gd calm with dissolve
    "I looked up to find a tall boy staring down at me."
    "Our eyes met, and he immediately smiled, kneeling down to pick up the book that fell from my hand."
    mc "\"Umm.. Thank you..\""
    "I reached out, expecting him to hand me the book. But instead, he continued to stare at the cover."
    mc " ...?"
    show gd flustered with dissolve
    unknown ".. Oh, sorry."
    "He looked up and apologized, as if he only just remembered I was there."
    show gd calm with dissolve
    "Placing the book in my hand, he flashed a smile so beautiful, my heart skipped a beat."
    mc "(Holy shi-)"
    unknown "I apologize for bumping into you. And..."
    unknown "... you have really good taste for books."
    mc "..."
    hide gd calm with dissolve
    "With that, he simply stood up and left."
    "I turned and stared at his retreating form, completely under whatever spell the guy casted on me."
    mc "I have no idea who he is, but..."
    mc "...He's definitely easy on the eyes."
    "I probably sat there for half a minute until someone walked by, staring at me."
    mc "\"Oh.\""
    mc "Oh shoot-!"
    mc "(Right, I had somewhere to go!)"
    "I hurriedly picked up my phone and got up." 
    "After brushing myself off for good measure, I went on my way."
    return
# END PROLOGUE SCENE4
    
# PROLOGUE SCENE5
label prologue_scene5:
    #--Skip to DB lobby--
    scene bg dbh_inside with fade
    mc "\"DB 1412...\""
    "I entered the Donald Bren lobby and came across a map of the area."
    mc "(Oh. According to this, it should be just up ahead.)"
    "I set off for the club meeting room, and turned a corner."
    "To my left, there was a huge window that looked into the game room."
    mc "\"Hmm..?\""
    "Through the window, I saw a bunch of people sitting down. But, they were all turned toward something." 
    "I could see that they all had an angry expression on their face."
    mc "(Are they... staring at the door-?)"
    mc "!!"
    "An arm swung the door open, and out came a very enraged girl with red streaks in her hair."
    show md angry with dissolve
    unknown "Oh, cut the crap! I ain't changing for the likes of you all, got it?!"
    mc "..."
    unknown "!!"
    mc "(Oh shit...)"
    "The girl stopped in her tracks and looked me right in the eye."
    unknown "... Tch."
    "After a second, she just adjusted her backpack, and stormed out of the building."
    hide md angry with dissolve
    "I caught the door before it closed, nervously turning to watch students hastily moving out of the girl's way."
    "Then, I peeked inside the game room."
    return
# END PROLOGUE SCENE5

# PROLOGUE SCENE6
label prologue_scene6:
    #--Game room--
    scene bg gameroom with fade
    mc "(Ahh... I just have the greatest timing...)"
    "It was dead silent. Every member had a grim look on their face, and no one looked up from their screen."
    mc "(I don't even think anyone noticed me...)"
    mc "(But, I came all the way here. It'd be a waste if I just left.)"
    "Carefully, I closed the door as silently as possible, and scanned the room for someone approachable."
    mc "\"... Oh-\""
    "In the corner of the room, there was a girl with a ponytail drawing on a tablet"
    show re calm with dissolve
    "Unlike the rest of the room, she had a relaxed expression on her face, as if the events prior had never happened."
    mc "(Looks like my best bet...)"
    "I quietly stepped toward her."
    mc "\"Umm.. Excuse me-?\""
    show re surprised with hpunch
    unknown "Ah?!"
    mc "\"Woa-!\""
    "The girl jolted back, and pretty violently too."
    "The chair shook and teetered. Instincltively, I put my hand to the back of the chair to keep her from falling."
    unknown "!!"
    mc "\"That was my bad. Sorry for scaring you. Are you oka-?\""
    unknown "YES!"
    mc "..."
    unknown "..."
    show re blush with dissolve
    unknown "I, umm..."
    unknown "I'm- I'm thank y- FINE! I'm fine! And, umm..."
    unknown "... Thank you..."
    "Completely red in the face, she quietly mumbled the last part, then finally turned to look at me."
    unknown "So, uh... can I help you?"
    mc "\"Oh, yea.\""
    mc "\"Actually, I'm interested in joinging VGDC, and was told this was the place to go if I wanted to sign up.\""
    show re calm with dissolve
    unknown "Y-yes, it is... Um, I'll have you added to the newsletter. Can you give me your email...?"
    "After I told her, she inputted it and nodded."
    unknown "Alright. I added you and sent you the first message. You should be getting an email every week from here on out."
    unknown "Oh, and uh, the first meeting is tomorrow from 8:30 to 9:40 in SSLH 100."
    mc "\"Alright, got it. Thank you for your help.\""
    unknown" Mmm.."
    hide re calm with dissolve
    "She gave a small nod and turned away."
    mc "(Hmm..? Did I do something wrong?)"
    mc "\"Well, uh... Bye.\""
    unknown "..."
    return
# END PROLOGUE SCENE6

# PROLOGUE SCENE7
label prologue_scene7:
    #--DB hall--
    scene bg dbh_inside with fade
    mc "sigh..."
    mc "(Did I really make the right choice..?)"
    "I quietly closed the door to the game room and headed towards the exit."
    mc "(I mean I'm definitely interested in the club.)"
    mc "(But so far, everyone I've met besides Yukiko seemed really unapproachable.)"
    mc "\"Hmm...\""
    mc "\"Well, it'd be unfair to leave just for that. Might as well just give it a shot.\""
    "I nodded to myself and pushed through the doors of the building."
    return
# END PROLOGUE SCENE7

# PROLOGUE SCENE8
label prologue_scene8:
    #--Outside DB--
    scene bg dbh_outside with dissolve
    "The doors swung open"
    show ax calm with dissolve
    ax "Ah."
    mc "\"Oh.\""
    ax "..."
    mc "..."
    mc "\"Back inside I go...\""
    ax "[mcname]!"
    "He grabbed my arm."
    mc "\"Ngh...\""
    mc "\"Unhand me you philandering monkey.\""
    show ax happy with dissolve
    ax "Yikes. You're one brutal tsundere."
    mc "\"Oh no. These are my honest feelings.\""
    ax "So harsh..."
    show ax calm with dissolve
    ax "But hey, this is perfect timing. My club meeting room is actually really close by."
    ax "Come with me, let's finally get you joined!"
    mc "\"Thanks, but no thanks. I already joined a club, and I don't need any more than that this quarter.\""
    ax "Huh..?"
    "Alex let go of my hand."
    mc "...?"
    show ax sad with dissolve
    "There was an uncharacteristic frown on his face. It actually made me feel a little guilty."
    ax "Geez, really..?"
    ax "Alright, tell me what club this is. I'll beat up whoever took you away!"
    mc "\"The Video Game Development Club, or VGDC.\""
    ax "..."
    "His eyes widened a bit."
    show ax calm with dissolve
    mc "\"Alex?\""
    ax "The VGDC, huh..."
    "A small smile spread across his cheeks."
    mc "\"..? Yea, what about it?\""
    "He shook his head."
    ax "Nothing, nothing."
    ax "Well, I'll let it slide for now. See you tomorrow, [mcname]!"
    "Before I could respond, he spun on his heel and headed away from the building."
    hide ax  calm with dissolve
    mc "..."
    mc "\"Weirdo.\""
    return
# END PROLOGUE SCENE8
    
# PROLOGUE SCENE9
label prologue_scene9:
    #--Meeting room--
    scene bg meeting_1 with fade
    "Just before the first VGDC meeting.."
    mc "(Oh man... There's a lot of people.)"
    mc "(I didn't think it'd be this packed.)"
    "I looked around the room in awe, taking a seat close to the front of the hall."
    "Up on the stage, there was a guy setting up a powepoint on a computer."
    mc "(He must be the one leading the meeting.)"
    "I tilted my head to the side in an attempt to better see him."
    "Just then, he stood straight and faced the audience, a smile plastered on his face."
    mc "(... Hmm..?)"
    show gd calm with dissolve
    unknown "Good evening, everyone."
    "The chattering within the hall ceased, and all eyes fell on him."
    unknown "I'm very pleased to have you all here. It's very humbling to see such a great turnout."
    mc "(This... is the guy I bumped into!)"
    gd "Welcome to the first Video Game Development Club meeting. I'm the club president, Jeorge Dan. Though, you may call me Jeorge Dan if you wish."
    mc "(The club president? Seriously?!)"
    mc "(Geez... This really is a small world.)"
    "I took a deep breath, paying no mind to the rapid pacing in my chest."
    #--black--
    scene bg black with fade
    "The meeting went on."
    "Jeorge Dan went over the basics of the club, including activities, purpose, and history."
    "He spoke in a way that was confident yet calm. I'd like to say that his voice captured everyone in the hall."
    "Though... that may have just been me."
    return
# END PROLOGUE SCENE9
    
# PROLOGUE SCENE10
label prologue_scene10:
    #--back to hall--
    scene bg black with fade
    "About thirty minutes into the meeting..."
    scene bg meeting_1 with dissolve
    show gd calm with dissolve
    gd "And now, we move on to departments."
    gd "As you all know, we will be formulating development teams in the near future."
    gd "Each member will belong to a specified department, no matter their skill level."
    gd "If you have no experience, have no fear. We have seasoned officers at your disposal."
    gd "Now... if those officers could please come on stage and introduce themselves?"
    "Jeorge Dan directed a smile at the opposite end of the stage, causing a group of students to stir."
    "Soon enough, they all walked to the front of the stage and faced us all."
    mc "(....)"
    mc "(Talk about a huge coincidence.)"
    mc "\"... Huh?\""
    mc "\"Wait, is that-?!\""
    gd "Alright. Alexander, if you could start us off?"
    show gd calm:
        linear 0.5 xalign 0.0
    "The president spoke to the person who led the line of officers, none other than Alex."
    "In response, he straightened his posture and took a few steps forward, a charming grin on his face."
    show ax calm with dissolve
    ax "Heya! Name's Alexander, the design officer."
    ax "Probably not the most well known or popular department, sure. But that doesn't make it any less amazing."
    ax "If you're even the slightest bit curious about what it is I do, come talk to me." 
    ax "And to the girls out there, trust me, I'll make it worth your time~"
    "I could hear some girls nearby giggle."
    hide ax calm with dissolve
    mc "(God, Alex...)"
    "Before I could gather myself, the next person stepped forward."
    show kd calm with dissolve
    kd "My name is Kendrick, the production officer."
    kd "As a producer, you will be enforcing order and organization."
    kd "Straightforward, though the weak willed may find it difficult."
    kd "Please only take up this position if you fully intend on taking matters into your own hands."
    kd "I'd rather not waste my time cleaning up the mess of others."
    hide kd calm with dissolve
    "..."
    show yu calm with dissolve
    unknown "..."
    unknown "Oooookaaay..."
    unknown "Anyways!! Hey-ho everyone!"
    "The next officer's enthusiasm effectively dispelled the heavy atmosphere of the room."
    mc "(Bless your soul...)"
    show yu happy with dissolve
    yu "My name's Yukiko, and I'm the programming officer!"
    yu "This department's fairly straightforward. You write words into the computer and the engine does its thing!"
    show yu calm with dissolve
    yu "... Or, well, I guess it's a liiiitle more complicated than that."
    yu "But not to worry! I'll be here to help you if your code goes out of whack!"
    show yu calm:
        linear 0.5 xalign 1.0
    show md calm with dissolve
    unknown "Geez, you're as loud as ever."
    "A girl with headphones stepped forward, placing a hand on Yukiko's shoulder."
    unknown "(That's the girl who got into a fight with the club members the other day...)"
    yu "Heyy, wait your turn!"
    unknown "Shouldn't be a problem, right? You were just about done anyway."
    yu "Hmph."
    hide yu calm with dissolve
    "As Yukiko returned to her spot, Melody cleared her thoat and faced the room."
    md "Name's Melody. Audio officer."
    md "Not much t' say, really. We make music and sound effects and stuff."
    md "Really isn't all that hard. At least, not to me."
    md "If you need any help, uhhh... Message me, I guess, and we'll see if I have time."
    md "... And, uhhh...."
    "Melody scratched her head, unsure what else to say."
    gd "That should be enough. Thank you Melody."
    gd "Alright. That was four officers. That means we're missing..."
    md "Ah!"
    "Melody's eyes lit up."
    hide md calm with dissolve
    "She returned back to the line of officers pushed someone forward by their shoulders."
    show re surprised with dissolve
    unknown "Eeep!"
    unknown "M-Melody!"
    md "Alright, alright! Give 'em hell, Reina!"
    show re calm with dissolve
    re "Ahh... ummm..."
    "The girl clasped her hands together and kept her gaze lowered."
    re "I'm... Reina. Uhh, Art officer?"
    re "I- I draw and... and animate, aaand..."
    re "...."
    re "I-I'll be happy you help to!"
    mc "\"... huh?\""
    hide re calm with dissolve
    "Before I knew it, Reina bowed and ran behind the line of officers, Melody following her with a smile on her face."
    show gd calm:
        linear 0.5 xalign 0.5
    gd "Haha. A lively bunch, aren't we?"
    mc "(That's one way to put it...)"
    gd "Well then. That just leaves me."
    gd "My name is Jeorge Dan, as you all know. I am the head of the writing department."
    gd "Anyone can write words, true. But more goes into the script than one realizes."
    gd "If you take interest in conveying themes in a way that is eloquent yet subtle through the written..."
    gd "Consider joining the department. I'll do my best to assist you."
    hide gd calm with dissolve
    "As the officers wrapped up their introductions, the audience erupted into applause."
    "I clapped along, but at the moment, my mind was racing."
    mc "(So many departments, but...)"
    mc "(Which one interests me the most?"
    menu department_choice:
        "Which one interests me the most?"
        "Programming":
            call yu_route
        "Art":
            call re_route
        "Writing":
            call gd_route
        "Production":
            call kd_route
        "Audio":
            call melody_route
        "Design":
            call alex_route
    return
# END PROLOGUE SCENE10
