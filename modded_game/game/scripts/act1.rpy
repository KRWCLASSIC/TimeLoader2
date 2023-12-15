#Do przyszłego mnie, pierdol się, zostawiam cię z tym source spaghetti
##FUTURE_NOTE, ZOBACZ I DOEDUKUJ SIĘ ODNOŚNIE TEGO https://www.renpy.org/doc/html/text.html#text-tag-p
#main characters
define h = Character("Hapering", color="#8b8b8b")    
define an = Character("[name]", color="#ffffff")
define d = Character("Dave", color="#00ffd5")
define j = Character("Jack", color="#ed9237")
define a = Character("Ametrine", color="#ad39b7")
define nick = Character(_("Nick Calhoun"), color="#dc143c")
#objects and others
define obone = Character("Object 001", color="#7658bb")
define dr = Character("The Man From The Dreams", color="#7658bb")
#other characters
define c = Character("Clef")
define neskuk22 = Character("neskuk22",color="#006aff")
define p = Character(_("Patrick Bateman"))
define n = Character("Narrator")
define sm = Character("???", color="#7658bb")
define h1 = Character("H-4P3R1", color="#8b8b8b")
define saul = Character(_("Saul Goodman"))
#effects
define fade = Fade(0.5, 1.0, 0.5)
define flashbulb = Fade (0.2, 0.0, 0.8, color='#fff')
define longwhitefade = Fade (5.0, 1.0, 1.0, color='#fff')
#flags + zmienne
default male = False 
default female = False
default other = False
default hapering_thing = 0
default hapering_friendship = 0
default hapering_awaken = True
default hapering_joins_ametrine = False
default hapering_checked = False
default remote_broke = False
default dave_dave = False
default awareness_about_the_dream = 0
default thefactoryknowledge = 0 
default thefactorysite = False
default awarenessaboutobject001 = False
default awarenessaboutobject022 = False
default awarenessaboutobject031 = False
default awarenessaboutobject050 = False
default awarenessaboutwarning = False
default conventionknowledge = False
default easteregghunter = False
default bonked = False 


#start game
label act1:
    stop music
    scene bg void
    sm "you [current_directory]"
    neskuk22 "First things first.{p}You can save the game in the menu.{p}You should know what button it is."
    ""
    play music "audio/Long Time Ago.mp3" fadein 2.0 volume 0.25
    sm "Well...{w=1.00} Hello."
    sm "Welcome to the begining of your new adventure!"
    sm "You're probably wondering where exactly are you.{p}Am I right?"
    sm "Lets just say that, You're kind of dreaming right now."
    sm "I'll probably give you more details later..."
    sm "So, let's get started.{w=1.00} What's your name?"
    jump namechoice

label namechoiceagain:
    sm "Your name, please input the correct one this time!"
    jump namechoice

label namechoice:
    $ name = renpy.input ("Your name.")
    $ name = name.strip()
    
    if name == "EGG":
        jump crash
    else:
        jump sansname

label sansname:
    if name == "sans":
        jump sans
    else:
        jump name1

label name1:
    if name == "Clef":
        jump clef
    else:
        jump name2
    
label name2:
    if name == "Hapering":
        jump Hapering
    else:
        jump name3

label name3:
    if name == "British":
        jump British
    else:
        jump name5
        
label name5:
    if name == "Backrooms":
        jump Backrooms
    else:
        jump name6
        
label name6:
    if name == "neskuk":
        jump gamedev
    else:
        jump name7

label name7:
    if name == "neskuk22":
        jump gamedev
    else:
        jump name8
        
label name8:
    if name == "Narrator":
        jump Narrator
    else:
        jump name9
        
label name9:
    if name == "Stanley":
        jump Stanley
    else:
        jump name10

label name10:
    if name == "Saul Goodman":
        jump saul 
    else:
        jump name11
        
label name11:
    if name == "Jimmy McGill":
        jump saul
    else:
        jump name12
        
label name12:
    if name == "Patrick Bateman":
        jump sigma
    else:
        jump name13
                
label name13:
    if name == "Dave":
        jump dave
    else:
        jump name14

label name14:
    if name == "Bigos":
        jump bigos
    else:
        jump name15

label name15:
    if name == "2137":
        jump gamedev
    else:
        jump name16

label name16:
    if name == "Barney":
        jump blackmesa
    else:
        jump name17 

label name17:
    if name == "The Factory":
        jump REDACTED
    else:
        jump name18

label name18:
    if name == "Jack":
        jump Jack
    else:
        jump name19

label name19:
    if name == "Nick Calhoun":
        jump nick
    else:
        jump name20

label name20:
    if name == "Ametrine":
        jump ametrine
    else:
        jump name

label ametrine:
    a "And what is this about?"
label nick:
    nick "You say anything like that again and I will break your jaw, and knock your teeth out too."
    $ easteregghunter = True
    jump namechoiceagain

label Jack:
    j "And how do you know that,{w=1.00}huh?"
    j "Im not even in the game yet!"
    j "If you wanted to name yourself {i}Jack{/i},{w=1.00} sorry,{p} you need to use {i}jack{/i} instead."
    j "Well I got a passcode for you, as a reward for your Easter {b}EGG{/b} hunting."
    j" It's a passcode for {i}The Factory{/i}: 2030"
    j "You can use it to get access to some secret files"
    j "{i}The Factory{/i} needs to update their security!"
    j "Just enter: {i}The Factory{/i} , in the name choice screen.{p}{i}(Yes. I'm breaking the 4th wall here. JUST DO IT!){/i}"
    j "It's all for now. Go back to playing."
    $ easteregghunter = True
    jump namechoiceagain

label blackmesa:
    "About that beer I owned ya!"
    "It's me,{w=1.00} Gordon!{p}Barney!{p}From Black Mesa!"
    $ easteregghunter = True
    jump namechoiceagain

label bigos:
    stop music
    show bigos
    "Bigos was heated in cauldrons; hard to put into words"
    "Bigos has a strange taste, a wonderful color and smell;"
    "He will hear only the clink of words, and the order of rhymes,"
    "But the contents of their urban stomach will not comprehend."
    "To appreciate Lithuanian songs and dishes,"
    "You have to be in good health,"
    "live in the countryside, "
    "come back from a raid."
    "After all, even without these spices,"
    "the dish is quite a dish"
    "There is bigos,"
    "because it is artificially made of good vegetables."
    "Chopped, sauerkraut is taken to it,"
    "Which, according to the proverb, goes into the mouth by itself;"
    "Closed in a cauldron, she covers with a moist womb"
    "Gourmet pieces of the best meats;"
    "And it burns until the fire squeezes everything out of it"
    "Live juices, until the var splashes from the edges of the vessel"
    "And the air around exhales aroma."
    "Bigos is ready."
    "Shooters with three cheers,"
    "Armed with spoons, they run and butt the dish,"
    "Copper thunders, smoke bursts, bigos dies like air,"
    "He's gone, he's gone;"
    "only in the depths of the sagana"
    "Steam boils, as in the crater of extinguished volcanoes."
    jump crash

jump namechoice

label sigma:
    stop music
    play music "audio/sigma.mp3"
    scene bg sigma
    p "Impressive. Very nice."
    jump crash

label saul:
    stop music
    play music "audio/Its all good man!.mp3"
    scene bg saulgoodman
    saul "Hi, I am Saul Goodman."
    saul "Did you know that you have rights?{p}Constitution says you do.{p}And so do I."
    scene bg saulgoodman2
    saul "I believe, until proven guilty; every man, woman, and child in this country is innocent.{p}THATS WHY I FIGHT FOR YOU, ALBUQUERQUE"
    jump crash

label Stanley:
    n "This is a story of a man, named [name]"
    $ easteregghunter = True
    jump namechoiceagain

label clef:
    c "{w=1.00}k{p}y{p}s"
    $ easteregghunter = True
    jump namechoiceagain

label sans:
    "Sans granie"
    $ easteregghunter = True
    jump namechoiceagain

label Hapering:
    h "Hey! It's mine!"
    $ easteregghunter = True
    jump namechoiceagain

label British:
    "It's chewsday, innit!"
    $ easteregghunter = True
    jump namechoiceagain

label Narrator:
    n "Excuse me???"
    $ easteregghunter = True
    jump namechoiceagain

label Backrooms:
    stop music
    scene bg backrooms
    play music "audio/Somewhere Else.mp3"
    ""
    jump crash

label dave:
    d "Dave."
    $ dave_dave = True
    $ easteregghunter = True
    jump namechoiceagain

label gamedev:
    jump crash

##The start of The Factory.
label thefactorysitecon:
    stop music
    sm "Wait.{p}How did..."
    sm "How did you know the passcode? {i}The factory{/i} is...{p}How did you know?"
    obone "Im one of the objects you know..."
    if awarenessaboutobject001 == True:
        dr "You already read that don't you?"
    obone "I...{w=1.00} What should I do..."
    obone "You know too much... Im sorry"
    scene bg black
    play sound "audio/BONK.mp3"
    $ bonked = True
    obone "{i}BONK{/i}"
    "..."
    "Wow, he hit you so hard, that I had to narrate this."
    "It would be strange if he just kept narrating this, after he bonked you!"
    "I will send you to the name choice screen now."
    "See you on the flipside."
    "BZZZZZ"
    scene bg void
    play music "audio/Long Time Ago.mp3" fadein 2.0 volume 0.25
    jump namechoice

label REDACTED:
    scene bg void error
    play music "audio/thefactory.mp3" volume 0.25
    $ passcode = renpy.input ("Please enter the passcode.")
    if passcode == "2030":
        jump access
    else:
        jump DENIED


label access:
    $ thefactorysite = True
    "ACCESS GRANTED.{p}WELCOME TO {i}THE FACTORY{/i} FILES."
    jump files

label files:
    "{w=1.00}PLEASE CHOOSE ONE OF THE FILES."
menu:
    "OBJECT 001":
        jump object001
    "OBJECT 022":
        jump object022
    "OBJECT 031":
        jump object031
    "OBJECT 050":
        jump object050
    "Important 22/##/2030":
        jump warning
    "Go back.":
        jump act1

label object001:
    "OBJECT 001 -{w=1.00} The Man From Dreams{p}THREAT LEVEL -{w=1.00} LOW"
    "Object 001 does not have a physical body,"
    "As a result, he cannot interact directly with our world."
    "{b}NOTE #001{/b}"
    "Object 001 tends to choose a random victim, that he seems to be interested in."
    "Then, he appears in the victims dream."
    "He mostly just talks about random stuff, at least, with our personel."
    "{i}The Factory{/i} IS NOT RESPONSIBLE FOR ANY STUFF THAT MAY HAPPEN IN YOUR DREAM!!!!"
    "Yes we had to put that here becasue LAW."
    "{b}NOTE #002{/b}"
    "Object 002 said something out of the ordinary ."
    "He mentioned very weird name."
    "I think it was {b}{i}Timekeeper...{/b}{/i}{p}Whatever THAT means."
    "{b}END OF THE RECORD{/b}"
    if awarenessaboutobject001 == True:
        jump files
    $ thefactoryknowledge += 1
    $ awarenessaboutobject001 = True
    jump files

label object022:
    "OBJECT 022 -{w=1.00} H-4P34H1{p}THREAT LEVEL -{w=1.00} NEAR ZERO"
    "Object 022 is a humanoid Robot, with a TV for his head."
    "He is also considered a male being."
    "{b}SCIENCE PERSONEL NOTE:{/b}"
    "Object 022 was created from an old TV from year 1940"
    "So yes, very old."
    "At Least he has a good fashion sense!"
    "Object 022 is one of the most inoccent objects in the entire factory."
    "To bad he doesn't realise what HORRIBLE place he's in."
    "..."
    "Existing with a TV for a head comes with few downsides."
    "Cutting the bullshit."
    "He tends to Forget things."
    "Unfortunately. We can't do much about it."
    "We added a few RAM slots into his TV, kinda helped.{p}However, his system still deletes random data."
    "...Im sorry Hapering."
    "{b}END OF THE RECORD{/b}"
    if awarenessaboutobject022 == True:
        jump files
    $ thefactoryknowledge += 1
    $ awarenessaboutobject022 = True
    jump files

label object031:
    "OBJECT 031 -{w=1.00} Jack{p}THREAT LEVEL -{w=1.00} HIGH"
    "Object 031 looks almost like an average human"
    "But PLEASE trust this record. HE isn't normal."
    "Jack is known for changing his appearance, once he's close to death."
    "Due to his regenerative abilities, he's very hard to kill."
    "But, it shouldn't be impossible."
    "Our science team noticed that even if jack changes appearance, his irises remain orange."
    "This way, he still can be recognized."
    "On the other hand. He has two hearts, {i}(Not including the random organs from diffrent species.){/i}"
    "Somehow, he's still alive. And no, his internal organs are NOT affected by the change of his appearance"
    "{b}SCIENCE PERSONEL NOTE:{/b}"
    "Object 031 was one of the greatest experiments that our company ever made..."
    "His character is very alternating."
    "One day,{w=1.00} he WILL kill everyone he sees.{p}And the other day,{w=1.00} he's the most peaceful being in the Facility."
    "{b}SECURITY BREACH NOTE:{/b}"
    "In case of an emergency, or events of a security breach."
    "Take.{p}Him.{p}Out."
    ##I SAY,DON'T YOU KNOW
    ##YOU SAY, YOU DON'T KNOW
    ##I SAY
    ##TAKE ME OUT
    stop music
    "{b}01/##/2030 AUTOMATIC EMERGANCY WARNING.{/b}"
    "{b}WARNING.{/b}"
    "{b}CODE RED.{/b}"
    "{b}I REPEAT.{/b}"
    "{b}CODE RED.{/b}"
    "{b}DESTROY HIM AT ALL COST.{/b}"
    "{b}END OF THE RECORD{/b}"
    if awarenessaboutobject031 == True:
        jump files
    $ thefactoryknowledge += 1
    $ awarenessaboutobject031 = True
    jump files

label object050:
    "OBJECT 050 -{w=1.00} The Machine{p}THREAT LEVEL -{w=1.00} VERY HIGH"
    "Object 050 is a strange machine."
    "It takes up about 70 percent of the room it's contained in."
    "{i}The Factory{/i} was founded to try and examine the strange machine."
    "Our entire institution was made around it."
    "{b}NOTE #001.{/b}"
    "Well. It's fucking sentient."
    "Object 050 is capable of creating whatever human imagination desires.{p}And The Machine is sentient."
    "Basically can create whatever it can think of..."
    "It wasn't exactly a good idea..."
    "Firstly, we wanted to use it to create our {b}SPACE CHOCOLATE.{/b}"
    "But, our science team really fucked up,{w=1.00} and gave it a working MIND."
    "Guess how that went."
    "{b}END OF THE RECORD{/b}"
    if awarenessaboutobject050 == True:
        jump files
    $ thefactoryknowledge += 1
    $ awarenessaboutobject050 = True
    jump files

label warning:
    "COME ON, IS THIS SHIT RECORDING?"
    "IM USING SOME KIND OF PROGRAM, THAT CONVERTS THIS AUDIO FOR TEXT ONLY,"
    "WHY DO WE EVEN HAVE SOMETHING LIKE THAT?"
    "I MEAN THAT'S NOT THE CASE RIGHT N-"
    play sound "audio/metal.mp3"
    "OHSHIT I NEED TO BE QUICK"
    "SO THERE IS, A MASSIVE SECURITY BREACH RIGHT NOW.{p}ALL FOUR OF THE OBJECTS ARE ESCAPING"
    "Object 001 cannot be secured but FUCK THAT"
    "THE MACHINE IS STILL HERE BUT IT VAPORIZES ANYONE THAT ENTERS THE ROOM,"
    "Okay..."
    play sound "audio/metal.mp3"
    "OH FUCK THAT WAS CLOSE-"
    "I need to stay calm...{p}Stay calm..."
    "Okay...So..{p}They...escaped.{p}They are Free."
    "It wasn't supposed to be like that.{p}It was designed to be perfect!"
    "I shouldn't have worked h-{w=1.00} OH SHIT, THEY ARE BREAKING IN"
    play sound "audio/metal.mp3"
    "GUYS I SWEAR I ONLY FOLLOWED ORD-{w=1.00} {i}unintelligible noises{/i}."
    "{b}End.{/b}"
    if awarenessaboutwarning == True:
        jump files
    $ thefactoryknowledge += 1
    $ awarenessaboutwarning= True
    jump files

label DENIED:
    "WRONG PASSCODE. TRY AGAIN."
    jump REDACTED




#end of factory

    
        
label name:
    sm "[name]. Are you sure about that?"
menu:
    "Yes":
        jump story2
    "No":
        jump namechoiceagain

label story2:
    sm "That is....."
    if thefactorysite == True:
        jump thefactorysitecon
    sm "A nice name."
    sm "Well,{w=1.00} [name],{p}your name is ...{p}Decent."
    sm "Your name really says a lot. You may not realize that yet, but thats pretty much everything I need to know about you. For now at least."
    sm "I wanted to ask you about your gender but, I don't think it REALLY matters here..."
    sm "Maybe it changes something... sorry. You can tell me if you want!"

menu:
    "Sure":
        jump gender_choice
    "Nah":
        sm "Well that is okay! Let's continue."
        jump story3

label gender_choice:
    sm "So... Are you a Male, or Female?"
menu:
    "Male":
        jump male
    "Female":
        jump female
    "Other":
        jump other
            
label male:
    sm "Male?"
    sm "..."
    sm "Im glad you told me, [name]"
    sm "Maybe it's nothing much but, still, thanks."
    $ male = True
    jump story3
    
label female:
    sm "Female?"
    sm "..."
    sm "Im glad you told me, [name]"
    sm "Maybe it's nothing much but, still, thanks."
    $ female = True
    jump story3

label other:
    sm "I respect your choice and im proud of you."
    sm "..."
    sm "Im glad you told me, [name]"
    sm "Maybe it's nothing much but, still, thanks."
    $ other = True
    jump story3

label story3:
    sm "You are probably wondering where EXACTLY are you. Am I right?"
menu:
    "Yes.":
        jump story3choice1
    "No, not really":
        jump story3choice2
        
label story3choice1:
    $ awareness_about_the_dream += 1 
    sm "Unfortunately, I can't tell you too much now..."
    sm "Maybe in the next dream."
    sm "...Or maybe not."
    jump story4
        
label story3choice2:
    sm "Okey then."
    jump story4
    
label story4:
    sm "Oh, At least I should give you some more details about your adventure!"
    sm "You'll need to make some serious choices in this story..."
    sm "Just... watch out okay? That's all I want from you... For now."
    sm "Do you want anything else?"
menu:
        "Yes":
            jump anythingelse
        "No.":
            jump nothingelse

label anythingelse:
    $ awareness_about_the_dream += 1 
    sm "Too bad,{p}sorry kiddo."
    sm "I know you are a fully grown adult but STILL."
    sm "I can't tell you anything."
    jump story5

label nothingelse:
    sm "Good. Good."
    jump story5

label story5:
    sm "Now...im going to need you to wake up, [name]"
    jump intro1



#TRASH AREA






label intro1:
    stop music
    scene bg trash with longwhitefade
    play music "audio/TRASH.MP3.mp3" volume 0.25
    "You wake up, surrounded by...{w=1.00}Trash.{p}Literally.{p}Just trash."
    "Wow, sucks to be you!"
    "Anyways, you wake up surrounded by THE trash.{p}...it REALLY stinks."
    "You must continue your search for scrap,{p}and leave this place as fast as you can.{p}Please."
    menu:
        "I think I got hit.":
            an "I think I got hit by a... brick."
            "What are you, homeless?"
            jump next1
        "Okay, you're right.":
            an "Okey, you're right. It stinks."
            "Just go already."
            jump next1

label next1:
    "You stand up,{w=1.00} dumping the garbage off your body"
    "Well, at least you're alive!{p}Probably..."
    menu:
        "Wait...":
            an"Wait..."
            jump next2
        "...What?":
            an "What?"
            jump next2

label next2:
    "Nevermind."
    an "Okey...{w=1.00}Let's continue this search for something to scrap."
    "You begin your hunt for something to salvage."
    an "Wow... And what is this?"
    "You pick up a strangely looking remote from the trash."
    show tv remote
    an "And that's interesting."
    an "It looks like... some kind of remote?"
    an "If there's a remote...{p}{b}There's something valuable in my area.{/b}"
    "You begin looking for something more valuable than this old remote..."
    an "And... What is it exactly?"
    show tv withsome trash
    "Some kind of an old TV, that's for sure..."
    an "I think I should clean it... And get it out of the TRASH."
    "You begin to throw the trash off the TV..."
    scene bg trash
    an "It looks much better without the trash."
    "You decide to pick up the TV."
    an "OKEY IT'S SO HEAVY."
    jump intromenuchoice1
    
label intromenuchoice1:
    menu:
        "Check the TV.":
            jump introchoice11
        "Put it back in the trash.":
            jump introchoice12
            
label introchoice11:
    "You begin to check the TV."
    an "Wow."
    an "It's... like really.{p}OLD."
    "Why did you say it like that..."
    an "Could my inner voices just shut up?"
    "No."
    an"...Sure."
    "You put the TV onto the random platform trolley that was standing nearby."
    show tv off incart
    jump intro2
    
label introchoice12:
    an "Eh, it's so old, it's probably worthless."
    an "Like, maybe not even 20 whole dollars"
    "You put the TV back int- Wait."
    "Why would you do that? Money is money after all!"
    menu:
        "It's not worth it.":
            jump introchoice121
        "Maybe I should think about it...":
            jump introchoice122

label introchoice122:
    an "Hm...{w=1.00} You're right.{p}Money is money after all!"
    "Im glad you listened to me. You should probably get going"
    an "You are right about that part, that's for sure"
    "You put the TV on the totally free platfrom trolley that was standing nearby"
    jump intro2

label introchoice121:
    an "I don't think it's worth the trouble..."
    an "Do you have any idea how heavy it is?"
    "Yes I know, but look!, there's a platfrom trolley nearby, see?"
    an "And?"
    "You can always take the TV, plus, some totally free scrap!"
    an "There isn't enough room for such a combo!"
    "You need to make a choice, then."
    jump choicescraportv

label choicescraportv:
    "Scrap or the TV."
    menu:
        "Scrap.":
            jump introchoice1211
        "TV.":
            jump introchoice1212
    
label introchoice1211:
    an "I choose Scrap over the TV."
    "Are you sure?"
    menu:
        "Yes.":
            jump introchoice1211aftermath
        "Wait, let me think":
            jump choicescraportv

label introchoice1212:
    an "I choose the TV over Scrap"
    "Are you sure?"
    menu:
        "Yes.":
            jump introchoice1212aftermath
        "Wait, let me think":
            jump choicescraportv

label introchoice1212aftermath:
    an "Hm...{w=1.00} You're right.{p}Money is money after all!"
    "Im glad you listened to me. You should probably get going"
    an "You are right about that part, that's for sure"
    "You put the TV on the totally free platfrom trolley that was standing nearby"
    jump intro2

label introchoice1211aftermath:
    "There is no going back from this path, it is your choice though. So I respect that."
    an "Yep."
    "You put the TV back in the trash, including  the remote."
    an "It's time to take some USEFULL trash this time"
    $ hapering_awaken = False
    $ hapering_thing += 1
    "You gather some usefull scrap, and put it onto the platfrom trolley."
    jump intro2
    
label intro2:
    an "It's time to hit the road as they say!"
    "Literally...{p}NO ONE.{p}Says that."
    jump city1
    




#CITY AREA






label city1:
    stop music fadeout 3.0
    "Some time later..."
    stop music
    scene bg city with fade
    play music "audio/Late night in the city.mp3" volume 0.5
    if hapering_awaken == False:
        jump city1other
    show tv off incart
    an "I dont't get it... How could anyone use such heavy TV's!?"
    an "At least I got this random platform trolley with me!"
    "You know these aren't free, right?."
    an "What."
    "You just stole a platform trolley!"
    an "Okay ...We can worry about it later."
    an "So, As I was saying."
    an "This TV is very. VERY. Heavy."
    stop music fadeout 3.0
    "Suddenly...{p}The remote fell on the ground."
    "Normally it shouldn't be that bad... BUT, the remote is made out of very cheap plastic... Probably from china"
    "Oh god... The kids."
    an "Wha- I didn't need the details but, WHYYYY"
    play music "audio/Late night in the city.mp3" volume 0.5 fadein 1.0
    "You decide to bend down and pick up the remote."
    an "Please, work God damnit! Without that remote... This TV will be even more worthless!"
    stop music fadeout 1.0
    show hapering tv normal
    sm "Uh, excuse me? Im not worthless...And why would you want to sell me?"
    an "...WHAT?{p}WHO ARE YOU?{p}WHERE ARE YOU?"
    sm "I hope I didn't play a video from the year of 2023!{p}They're really not that funny..."
    sm "Anyways, Im right here! On the Trolley!"
    an "What?"
    sm "Here!"
    show hapering tv happy
    play music "audio/Late night in the city.mp3" volume 0.5 fadein 1.0
    an "A talking TV?"
    sm "Yes!"
    h1 "My name is H-4P3R1!"
    an "Maybe... something easier?"
    h1 "In that case... Call me Hapering!"
    h "I love my name,{w=1.00} it's like...{p}Fish fingers with custard!"
    "Did he meant Fish Sticks?"
    an "Don't ask me."
    "You stand a very weird amount of time..."
    an "This isn't possible... Can I turn you off?"
    menu:
        "Press the red button on the remote.":
            jump city1choice11
        "Press the blue button on the remote.":
            jump city1choice12

label city1choice11:
    "You press the red button on the remote."
    show tv off incart
    "Hapering turned off."
    $ hapering_thing += 1
    an "Ah... Finally!"
    "You put the remote back in your pocket."
    an "Now I can go back to my-"
    "Suddenly... Hapering turns back on!{p}You're fucked."
    h "HEY! WHY WOULD YOU DO THAT? THAT'S MEAN!"
    show hapering tv angry with vpunch
    an "AAAAAAAAA-"
    "You got spooked by a talking TV. WOW."
    stop music fadeout 1.0
    play music "audio/The Fire Is gone.mp3" fadein 1.0
    scene bg black with fade
    "Infact, SOMEHOW you got spooked so hard that you fall down on the ground and hit your head on the sidewalk."
    "You lose consciousness."
    "..."
    scene bg blur hapering pov with fade
    h "Hello? Are you okay? Wake Up!"
    an "What... What happened?"
    h "You lost consciousness! Are you alright?"
    an "Give me a moment..."
    scene bg hapering pov 
    h "Here, get up."
    an "Uhhhh... Wait...When did your legs appear?"
    h "The moment you felt unconscious! I panicked but... I think im getting used to it..."
    an "Glad you're okay..."
    stop music fadeout 2.0
    "You slowly stand up from the ground..."
    scene bg city with fade
    play music "audio/Late night in the city.mp3" volume 0.5
    show hapering normal
    jump intromenuchoice2
    
label city1choice12:
    "You press the blue button.{p}...{p}Nothing happens."
    an "How do I turn you off?"
    show hapering tv think
    h "I don't think you can..."
    h "This remote is... Old.{p}And it was made by some average polish male."
    an "Wait. You're a talking TV. How the FUCK do you work?"
    h "HEY! NO SWEARING!"
    "The scream that came from that TV was... very loud. It was so loud that you SOMEHOW got spooked by it. WOW."
    "SPOOKED BY A TALKING TV."
    stop music fadeout 1.0
    play music "audio/The Fire Is gone.mp3" fadein 1.0
    scene bg black with fade
    "Infact, SOMEHOW you got spooked so hard that you fall down on the ground and hit your head on the sidewalk."
    "You lose consciousness."
    "..."
    scene bg blur hapering pov with fade
    h "Hello? Are you okay? Wake Up!"
    an "What... What happened?"
    h "You lost consciousness! Are you alright?"
    an "Give me a moment..."
    scene bg hapering pov 
    h "Here, get up."
    an "Uhhhh... Wait...When did your legs appear?"
    h "The moment you felt unconscious! I panicked but... I think im getting used to it..."
    an "Glad you're okay..."
    stop music fadeout 2.0
    "You slowly stand up from the ground..."
    scene bg city with fade
    play music "audio/Late night in the city.mp3" volume 0.5
    show hapering normal
    jump intromenuchoice2

label intromenuchoice2:
    an "I can try to do something with... the rest of your body."
    h "No it's okey... Please leave it alone."
    "You pull out the remote from your pockets"
    menu:
        "Press random buttons.":
            jump city1choice21
        "Do nothing.":
            jump city1choice22
        
label city1choice21:
    "You start to randomly press the buttons on the remote, ignoring his request."
    show hapering error
    h "GOD NO!{p}WHAT DID I TOLD YOU?{p}STOP!"
    h "oifeosuifbOISNPNSODIFEOSIGNJMSODPJESAPEINJFI"
    h "GOUIRGNPOIUSBANP{b}you{/b}PJNSPIVUBSIUP{b}fucked{/b}FIEUSBIVUSBIU{b}up{/b}"
    menu:
        "Continue.":
            jump city1choice31
        "Stop pressing buttons":
            jump city1choice32
        
label city1choice31:
    stop music fadeout 2.0
    show hapering error
    h "UIFEGPIUSVBFIUYSVP;SUVSBUOERBSO"
    h "BZEVBFVZBZBZBZBbyhjevbfzhxvfeajhv"
    $ hapering_thing += 1 
    menu:
        "{b}Continue.{/b}":
            jump city1choice4
        "Just Stop...":
            jump city1choice32

label city1choice4:
    show hapering off
    "..."
    "...Hapering turns off... Are you happy?"
    "You probably broke him..."
    "It's the end for you."
    jump end1

label city1choice32:
    "You decide to stop.{p}{b}G o o d  c h o i c e.{/b}"
    play music "audio/Late night in the city.mp3" volume 0.5 fadein 1.0
    show hapering tired
    h "Ah...{p}Thanks..."
    an "Sorry...{w=1.00} I didn't know."
    h "Don't worry{w=1.00}, after all, I think you kind of own me right now."
    show hapering pointing
    h "You took me from that trash area so, im yours!"
    an "What...? Hell no! I was going to sell you anyway!"
    show hapering angry
    h "What?!"
    an "Anyways, I'll be going now!!"
    "You begin walking to your workshop, leaving hapering with the stolen trolley behind."
    h "Hey! You can't just leave..."
    "Hapering joins you... You don't really have a choice do you?"
    stop music fadeout 2.0
    "..."
    jump workshop1

label city1choice22:
    an "You're right, I'll let you be."
    h "Ah, thanks mate..."
    an "Im glad you accepted your fate"
    show hapering yup
    h "Yup. We need to accept it."
    show hapering asking
    h "We can do that,{w=1.00} right friend?"
    menu:
        "You are nothing but a piece of scrap.":
            jump city1choice221
        "Yes, we can do that.":
            jump city1choice222

label city1choice221:
    an "Wait.{p}Wait.{p}Wait."
    show hapering kinda sad
    an "What do you mean,{w=1.00} we? There is no, us."
    show hapering sad
    "You're just a piece of scrap for me to sell."
    an "That's all."
    an "But,{w=1.00} you are alive."
    an "And that wasn't the part of my plan."
    show hapering angry withtears
    h "...YOU CAN'T JUST LEAVE ME HERE!"
    an "Why?"
    h "NOW I HAVE THIS BODY! AND I DON'T KNOW WHAT SHOULD I DO!"
    h "AND NOW I HAVE TO YELL BECAUSE YOU CAN'T UNDERSTAND A SIMPLE THING!{p}PEOPLE THINK WE'RE CRAZY!"
    an "OK!{w=1.00} Okay!...shut up and let me think."
    $ hapering_thing += 1
    menu:
        "Fine.":
            jump city1choice2211
        "Im going to leave you anyway." if hapering_thing >= 2:
            jump city1choice2212
        
label city1choice222:
    an "Of course buddy! Now, let's get going!"
    show hapering happy
    "{i}Happy hapering noises.{/i}{p}You begin walking to your workshop with hapering, leaving the trolley behind."
    stop music fadeout 2.0
    "..."
    jump workshop1 

label city1choice2211:
    an "Ugh... I guess there is no other choice."
    show hapering happy
    "{i}Happy hapering noises.{/i}{p}You begin walking to your workshop with hapering, leaving the trolley behind."
    stop music fadeout 2.0
    "..."
    jump workshop1 
    
label city1choice2212:
    an "Im going to leave you anyway."
    an "You're NOTHING to me."
    show hapering sad
    h "I..."
    scene bg city
    "You begin walking to your workshop with the trolley, leaving hapering behind."
    "...He doesn't follow you."
    $ hapering_joins_ametrine = True
    jump workshop1_alone


#DO ZROBIENIA
label city1other:
    "This feels... different."
    an "What do you mean?"
    "It's... quiet.{p}Too.{p}Quiet."
    an "Except all the city noises?"
    "Yes, except all the noise."
    an "Well, we left that TV after all."
    "Maybe this wasn't a good idea after all."
    menu:
        "I don't care.":
            jump city1otherchoice1
        "I have mixed feelings about this.":
            jump city1otherchoice2
        "It wasn't a good idea.":
            jump city1otherchoice3

    
label city1otherchoice1:
    an "I DON'T CARE!"
    an "I got free scrap, and this trolley!"
    "And you could get a TV."
    an "Scrap's better anyways."
    "Well normally you could do something but..."
    "There's no one here. Everyone is busy with their stuff."
    an "Let's just get to my workshop, I have some scrap to sale."
    jump workshop1_alone

label city1otherchoice2:
    an "I have... mixed feelings about this"
    "You need to ask yourself one question. Was It a good choice after all?"
    "During your journey, you will have so many choices."
    "You have to learn to distinguish beetween a good choice, and a bad one."
    "Your journey depends on it. Now tell me, was it a good choice?"
    menu:
        "It was":
            jump city1otherchoice21
        "It wasn't":
            jump city1otherchoice22

#finish

label city1otherchoice21:
    an "It was a good choice."
    "It's up for you to find out"
    an "Im going straight to my workshop, it's getting late."
    "Okey then."
    jump workshop1_alone

label city1otherchoice22:
    an "It was a bad choice..."
    "It's up for you to find out, not me."
    "But, you could go back to the trash area."
    "Maybe He's still there."
    an "Wait, what do you mean by HIM?"
    "Nothing really, lets just go."
    menu:
        "Tell me more.":
            jump city1otherchoice221
        "Alright, lets go.":
            jump city1otherchoice222

label city1otherchoice221:
    an "No, wait, I want to know more!"
    "It's to late for that."
    an "To late to tell me what the hell was going on with that TV?"
    "You'll see him soon."
    an "Lets just go back for him..."
    "You turn back with your trolley to the trashzone... I wonder if he's still out there..."
    jump trashzone

label city1otherchoice222:
    an "Alright."
    "You turn back with your trolley to the trashzone... I wonder if the TV's still there..."
    jump trashzone

label city1otherchoice3:
    an "It wasn't a good idea, you're right."
    "Of course I was right!"
    an "Maybe, we could go back?"
    "I mean you can... but, is there any point?"
    menu:
        "Trying wouldn't hurt.":
            jump city1otherchoice31
        "Not worth it.":
            jump city1otherchoice32
    

label city1otherchoice31:
    an "At least trying wouldn't hurt...?"
    "Lets go then!"
    an "Agreed."
    "You turn back with your trolley to the trashzone... I wonder if the TV's still there..."
    jump trashzone




label city1otherchoice32:
    an "Ehh it's not worth it. It probably got taken anyways."
    "Oh, well it's your choice."
    an "Well, YES.{p}It is."  
    "{i}Sign...{/i}{p}You continue walking to your workshop."
    jump workshop1_alone



#TRASHZONE AREA




label trashzone:
    stop music fadeout 3.0
    scene bg trash with fade
    play music "audio/TRASH.MP3.mp3" volume 0.25
    "You arrive to the trash zone.{p}Again"
    an "Now where the hell I left this TV..."
    "You start to scounder for the TV."
    an "Where the FUCK is it?"
    "I... think it's gone."
    an "What? What do you mean? It magicly grown legs and escaped?"
    "I think this is EXACTLY what happend."
    an "I have too many questions."
    "Just... just leave this place already.{p}Don't tell me you have forgotten about this smell?"
    an "OH right the smell. Lets go. Straight to the workshop this time."
    $ hapering_checked = True
    jump workshop1_alone




#WORKSHOP AREA





label workshop1:
    scene bg workshop with fade
    play music "audio/working and stuff.mp3" fadein 2.0 volume 0.5
    "You finally arrive to your workshop."
    show hapering wow
    h "Wow...{w=1.00} This place is huge!"
    an "I know"
    an "So,{w=1.00} this is the place where I sleep, live, and do most of the stuff."
    show hapering happy
    h "Oh, Boy...{w=1.00} I love It!!!"
    an "Really?"
    h "Of Course!"
    an "Thank you..."
    show hapering normal
    h "So...{w=1.00}What are we gonna do?"
    menu:
        "Approach your desk":
            jump workshop1choice1
        "Pick up the poster that lies on the floor":
            jump workshop1choice2
            
label workshop1choice1:
    "You just walk up to your desk, completely ignoring the question..."
    h "Hello?"
    an "Sorry I was just...{p}You know."
    h "I don't."
    an "Nevermind,{w=1.00} we need to find you a place to sleep..."
    h "I agree. Can I sleep here?"
    if hapering_thing >= 2:
        jump workshop1choice1flag2
    if hapering_thing >= 1:
        jump workshop1choice1flag1
    an "Sure!"
    show hapering normal
    h "Really?{p}That's... very nice of you"
    an "No problem, my friend."
    show hapering happy
    h "I knew we're gonna become friends!"
    $ hapering_friendship += 1
    jump workshop21
    
label workshop1choice1flag2:
    an "Hell no!"
    show hapering sad
    h "...Oh"
    h "But Why???"
    an "You forgot about our argument already???"
    h "No..."
    an "So, nuh uh. You're not going to sleep here."
    h "I don't have a place to sleep!"
    an "I AM AWARE."
    $ hapering_thing =+ 1
    h "..."
    an "Fine. One night."
    h "Yay!"
    an "Calm down."
    h "Alright."
    jump workshop21

    label workshop1choice1flag1:
    an "Im not sure about this one{w=1.00} you know?"
    show hapering excited
    h "Oh come on! It will be fun!"
    an "Alright..."
    show hapering excited
    h "Yippie!"
    an "Calm down already!"
    show hapering normal
    h "Okay."
    jump workshop21

label workshop1choice2:
    "You pick up a poster from the floor..."
    show hapering asking
    h "A... poster?"
    an "Not an ordinary one."
    h "What do you mean?"
    an "I was joking. It's normal."
    show hapering normal
    an "I found it on the street."
    show hapering asking
    h "And what does it say?"
    an "It says something about a convention."
    show hapering think
    h "I see..."
    show hapering happy
    h "We can go there if you want!"
    if hapering_thing >= 2:
        jump workshop1choice2flag2
    if hapering_thing >= 1:
        jump workshop1choice2flag1
    an "Of course hapering!"
    h "Yay!"
    an "Then it's settled"
    show hapering yup
    h "Yep!"
    jump workshop1choice21

label workshop1choice2flag2:
    an "That was my plan."
    h "Cool!"
    an "And im going to use you as my entry."
    show hapering normal
    h "That... stoped sounding so cool."
    an "Well OF COURSE?"
    h "Uh."
    jump workshop1choice21

label workshop1choice2flag1:
    an "I don't know about this one,{w=1.00} hapering..."
    show hapering asking
    h "Why not?{p}This convention thing seems really fun!"
    an "Firstly... you need a working invetion to enter."
    show hapering think 
    h "Hm..."
    show hapering excited
    h "Oh, I got it!"
    an "What is it?"
    h "You can use me as an invention."
    an "This sounds...{w=1.00} pretty good."
    h "I know, right?"
    an "At least we got some sort of a plan!"
    show hapering yup
    h "Yup!"
    jump workshop1choice21

label workshop1choice21:
    an "Where are you going to sleep, then?"
    show hapering asking
    h "Can I sleep here?"
    if hapering_thing >= 2:
        jump workshop1choice2flag12
    if hapering_thing >= 1:
        jump workshop1choice2flag11
    an "Sure!"
    show hapering normal
    h "Really?{p}That's... very nice of you"
    an "No problem, my friend."
    show hapering happy
    h "I knew we're gonna become friends!"
    $ hapering_friendship += 1
    jump workshop22

label workshop1choice2flag11:
    an "Im not sure about this one{w=1.00} you know?"
    show hapering excited
    h "Oh come on! It will be fun!"
    an "Alright..."
    show hapering excited
    h "Yippie!"
    an "Calm down already!"
    show hapering normal
    h "Okay..."
    jump workshop22
    
label workshop1choice2flag12:
    an "Hell no!"
    show hapering sad
    h "Oh...But Why???"
    an "You forgot about our argument already???"
    h "No..."
    an "You're not going to sleep here."
    h "I have no place to sleep!"
    an "I AM AWARE."
    $ hapering_thing += 1
    h "..."
    an "Okey. Fine. One night."
    show hapering happy
    h "Yay!"
    an "Calm down."
    show hapering normal
    h "Alright..."
    jump workshop22

label workshop22:
    $ conventionknowledge = True
    jump workshop21

label workshop21:
    h "It's getting late..."
    an "You want to go to sleep?"
    show hapering think 
    h "I MEAN,{w=1.00} I don't need to sleep."
    an "What do you mean?"
    h "I mean I don't sleep like a normal human."
    h "I just, turn off.{p}It recharges my battery!"
    an "How..."
    h "I don't know."
    an "We can discuss that later."
    h "Probably the best idea. For now at least."
    show hapering normal
    "You approach your bed with Hapering..."
    show hapering excited
    h "Oh, you got a bunk bed?!?!?"
    an "...Yeah?"
    h "Wait... You live alone right?"
    "Hapering climbes to the top of the bed..."
    scene bg workshop
    an "Yeah?"
    h "So why a bunk bed?"
    an "It's a long story."
    h "I see...The bed is even cooler than I thought!"
    an "Enjoy while you can."
    h "..."
    an "Hapering?"
    "I think he turned off..."
    an "NO SHIT!"
    "SHH! He's sleeping!"
    if hapering_thing >= 2:
        jump workshop2choice1flag12
    if hapering_thing >= 1:
        jump workshop2choice2flag11
    an "I hope I didn't woke him up..."
    an "He's my friend... after all..."
    "I didn't thought you actually liked him... Wow. You proved me wrong, congrats!"
    an "Yeah..."
    "Anyways. You decide to close your eyes and go to sleep..."
    "..."
    $ hapering_friendship += 1
    jump dream1
    
label workshop2choice1flag12:
    an "Well to bad that I don't care!"
    "Why are you so... Rude?"
    an "Because I can!"
    if persistent.not_right == True:
        jump workshop_somethingsnotright
    "Even if you can, that doesn't mean you should be."
    an "Nah."
    "You pissed me off, go to sleep." 
    jump dream1

label workshop2choice2flag11:
    an "...And?"
    "You should be kind!"
    menu:
        "Maybe you're right.":
            an "Maybe you're right."
            "Yeah I am!"
            an "Maybe... Maybe."
            "Yeh... Anyways.{p}You decide to close your eyes and go to sleep..."
            "..."
            jump dream1
        "Maybe you're wrong.":
            an "Maybe you're wrong."
            "I don't think I am!"
            an "Well,{w=1.00} I think you are."
            "Look. You can only hope that you got control of your life."
            an "What do you mean?"
            "...Nothing."
            $ hapering_thing += 1
            "Yeh... Anyways.{p}You decide to close your eyes and go to sleep..."
            "..." 
            jump dream1

label workshop_somethingsnotright:
    stop music fadeout 1.0
    an "And there is no one to stop me."
    "...What do you mean?"
    an "Oh you know what I mean."
    an "And SOON. Everyone will know."
    "You fucking monster."
    "..."
    jump dream1
    

label workshop1_alone:
    scene bg workshop with fade
    play music "audio/working and stuff.mp3" fadein 2.0 volume 0.5
    "You finally arrive to your workshop."
    "But, you're alone."
    an "Ah... Home Sweet Home."
    "I don't this this qualifies as a normal house."
    an "I eat, work, and sleep here so yes, this is my home."
    an "Maybe it's not a normal house, but it's my home for sure."
    "Whatever."
    "It's awfully quiet here... Is this normal?"
    an "Pretty much."
    menu:
        "Approach your desk":
            jump workshop1_alonechoice1
        "Pick up the poster that lies on the floor":
            jump workshop1_alonechoice2

label workshop1_alonechoice1:
    "You approach your desk"
    "Well, do you have any plans?"
    an "I don't think so..."
    "What was all of the scrap for?"
    an "Uh..."
    an "Well my previous plan was to sell it but..."
    an "Now when I think about it..."
    an "...It is a pretty bad plan."
    "THAT'S WHAT I WAS TRYING TO TELL YOU."
    an "Well. I think im going to create something with all of this scrap but... this is going to be hard."
    "It ain't THAT hard..."
    an "You have no idea how this stuff works, right?"
    "You got me there, But you can always do an all nighter!"
    an "I guess I have no other choice, eh?"
    "Yep!"
    an "Let's get to work then..."
    "You begin to create something with the scrap..."
    an "I don't think this goes here..."
    "Do you think I know?"
    an "Please help me."
    "..."
    scene bg black
    "You spend an unhealthy amount of time working with scrap."
    "Infact, the second you finish, you instantly fell asleep."
    "How convenient is that?"
    "Goodnight, [name]"
    jump dream1

label workshop1_alonechoice2:
    "Hey, look, that's... a poster?"
    an "Yeah, there is some sort of a convention tommorow...."
    an "I had plans to go there... But there's a catch."
    "What is it?"
    an "I need to have a working invention with me to enter."
    "Well, let me introduce you to: All the fucking scrap you took from the trash zone."
    an "Are you sugesting me to create something?"
    "Well, duh? It ain't THAT hard..."
    an "You have no idea how this stuff works, right?"
    "You got me there, But you can always do an all nighter!"
    an "I guess I have no other choice, eh?"
    "Yep!"
    an "Let's get to work then..."
    "You begin to create something with the scrap..."
    an "I don't think this goes here..."
    "Do you think I know?"
    an "Please help me."
    "..."
    scene bg black
    "You spend an unhealthy amount of time working with scrap."
    "Infact, the second you finish, you instantly fell asleep."
    "How convenient is that?"
    "Goodnight, [name]"
    jump dream1




#SECOND DREAM AREA






label dream1:
    ""
    scene bg void with longwhitefade
    play music "audio/Long Time Ago.mp3" fadein 2.0 volume 0.5
    sm "Hey, you.{p}You're finally awake."
    sm "On the other side again! Back in your dream..."
    ##if persistent.not_right == True:
    ##    jump dream12
    menu:
        "...":
            jump dream11
        "What is this place again?." if awareness_about_the_dream >= 2:
            jump dream12

label dream12:
    an "What is this place again"
    sm "Wait How can you...."
    sm "I really tried to ban you from talking here."
    menu:
        "It did't work.":
            jump dream121

label dream121:
    sm "Agh,{w=1.00}Nevermind..."
    sm "Just stop talking. Let me continue."
    ##if persistent.not_right == True:
    ##    jump dream_not_right
    an "..."
    sm "Good."
    jump dream11

label dream_not_right:
    stop music fadeout 1.0
    an "No I will not."
    sm "...What?"
    sm "...What do you mean?"
    an "You know EXACTLY what I mean."
    sm "Uh..."
    an "OH YOU REMEMBER!"
    an "OH DON'T YOU TRY TO GASLIGHT ME."
    an "You're lucky that this is a dream."
    if awarenessaboutobject001:
        jump dream_not_right_quirk
    an "I am going to find you."
    jump finish

label dream_not_right_quirk:
    an "You're so lucky you don't have a physical body."
    an "You're probably not so lucky in the another universe."
    jump finish

label dream11:
    sm "That's what I thought."
    sm "So... First things First."
    
    if male == True:
        jump gender_male

    if female == True:
        jump gender_female

    if other == True:
        jump gender_other

label gender_male:
    sm "Oh... you're a male. That's certainly good."
    sm "Thanks for telling me earlier."
    jump dream111
    
label gender_female:
    sm "Oh... you're a female. That's certainly good."
    sm "Thanks for telling me earlier."
    jump dream111

label gender_other:
    sm "Oh... I see..."
    sm "Thanks for telling me earlier."
    jump dream111



    
label dream111:
    sm "Let's see what were you doing with hapering"
    
    if hapering_awaken == False:
        jump hapering_awaken
    
    if hapering_joins_ametrine == True:
        jump hapering_joined

    if hapering_thing >= 3:
        jump hapering_verymean
    
    if hapering_thing >= 2:
        jump hapering_mean
    
    if hapering_thing >= 1:
        jump hapering_not_really_mean

    if hapering_friendship >=1:
        jump hapering_friends

    jump dream2

label hapering_awaken:
    sm "Oh you..."
    sm "You left the TV."
    sm "Unfortunately. You dont have so much choice in this."
    sm "You'll discover that soon."
    if hapering_checked == True:
        sm "At least you checked if he was still there..."
    jump dream2


label hapering_joined:
    sm "Wait, you telling me, that you have left hapering alone?"
    sm "Why would you do that?"
    sm "Nobody told you about the consequences of your actions?"
    sm "Ah, it's to late to fix that."
    sm "There is a chance that... You broke him."
    sm "Well good luck now!"
    jump dream2

label hapering_verymean:
    sm "You were... mean."
    sm "But why?"
    sm "Do you know what kindness means??"
    sm "I don't think you know."
    jump dream2 

label hapering_mean:
    sm "You were, quite mean to hapering... I must say."
    sm "That ain't good you know?"
    sm "This is not my story... But you don't have a free will either."
    jump dream2  

label hapering_not_really_mean:
    sm "You were... KINDA neutral with hapering"
    sm "At least you weren't so mean to him!"
    sm "So...thats kinda the good part."
    jump dream2

label hapering_friends:
    sm "Oh wow... I must say, I didn't knew you were going to become friends with him!"
    sm "Im glad you two are getting along with eachother..."
    sm "He's kinda my friend... After all."
    sm "Okay...You need to go back to your adventure with him!"
    sm "Good luck, [name]."
    jump dream2
    
label dream2:
    if bonked == True:
        sm "Sorry for hitting you earlier. My mistake."

    if easteregghunter == True:
        sm "Eh, enough about that..."
        sm "There's another thing."
        sm "You were a little easter egg hunter, am I right?"

    if remote_broke == True:
        sm "Eh, enough about that..."
        sm "There's another thing."
        sm "You've broken the remote... It happens."

    if conventionknowledge == True:
        sm "Eh, enough about that..."
        sm "There's another thing."
        sm "Oh, you have plans on going to that convention you saw on the poster?"
        sm "Good... good."

    sm "Hm...{p}Lets check one last thing."
    if thefactoryknowledge == True:
        sm "You discovered the factory."
        sm "That's bad."
        jump dream3
    sm "Ah... good."
    sm "You didn't checked the factory..."
    sm "I think im lucky."
    jump dream3

label dream3:
    sm "Anyways..."
    sm "Now...Im gonna need you to wake up."
    sm "{b}WAKE UP.{/b}"
    sm "{b}WAKE UP.{/b}"
    sm "{b}WAKE UP.{/b}"
    jump finish




#ENDINGS + FINITO






label finish:
    show ending_three with flashbulb
    ""
    play music "audio/Long Time Ago.mp3" fadein 2.0 volume 0.5
    neskuk22 "Well...{w=1.00} Its the end of version 0.8.2."
    neskuk22 "THIS TIME I REWRITED MOST OF THE STUFF"
    neskuk22 "The extras menu doesn't work... yet"
    neskuk22 "Its not perfect,{w=1.00} I still need many sprites,{w=1.00} music,{w=1.00} and help from you!"
    neskuk22 "Im not a fucking english teacher to know everything I wrote wrong,"
    neskuk22 "Are there any mistakes in the game?{p}If yes,{w=1.00} PLEASE,{w=1.00} CORRECT ME."
    neskuk22 "So yes,"
    neskuk22 "You probably still got many secrets to discover...{p}Am I right?"
    neskuk22 "You can follow me on youtube, twitter, facebook, tik tok...{p}fucking everything..."
    neskuk22 "...Um."
    neskuk22 "Well... see ya!"
    neskuk22 "Here's my channel lol {a=https://www.youtube.com/c/neskuk22} CLICK HERE {/a}"
    $ persistent.act1 = True
    neskuk22 "Oh and click the main menu button to go to the real main menu..."
    "END OF VERSION 0.8.2.{p}The passcode is 2030"
    if hapering_joins_ametrine == True:
        jump aftermath
    jump endgame
    
label end1:
    show ending_two with flashbulb
    play music "audio/Long Time Ago.mp3" fadein 2.0 volume 0.5
    "You killed hapering... How Could You? You little monster..."
    "This is a very, VERY, Bad ending for you."
    ##$ persistent.not_right = True
    jump endgame
    

label aftermath:
    stop music fadeout 5.0
    scene bg city with longwhitefade
    play music "audio/Late night in the city.mp3" volume 0.5
    a "Oh, and what happend to you? My dear friend..."
    h "He... he left me."
    a "Well, it's alright now.{p}Im here."
    a "{b}Come with me.{/b}"

label endgame:
    stop music
    call screen main_menu

label crash:
$ renpy.quit()
