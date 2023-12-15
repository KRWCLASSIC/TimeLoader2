screen choose_route:
    add "bg/bg_choose.png"
    hbox:
        xalign 0.5
        yalign 0.45
        yoffset 30
        spacing 20

        imagebutton:
            auto "acts/act1_%s.png"
            action Jump("act1")
        imagebutton:
            auto "acts/act2_%s.png"
            action Jump("act2")
            sensitive persistent.act1 == True
        imagebutton:
            auto "acts/act3_%s.png"
            action Jump("act3")
            sensitive persistent.act1 == True and persistent.act2 == True
        imagebutton:
            auto "acts/act4_%s.png"
            action Jump("act4")
            sensitive persistent.act1 == True and persistent.act2 == True and persistent.act3 == True  

        imagebutton:
            auto "acts/act5_%s.png"
            action Jump("act5")
            sensitive persistent.act1 == True and persistent.act2 == True and persistent.act3 == True and persistent.act4 == True 