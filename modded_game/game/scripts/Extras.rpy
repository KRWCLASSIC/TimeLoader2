init python:
    gallery = Gallery()

    gallery.button("Hapering")
    gallery.image("hapering happy")
    gallery.unlock("hapering happy")

    gallery.button("Ending One")
    gallery.image("ending one")
    gallery.unlock("ending one LOCKED")

    gallery.button("Ending Two")
    gallery.image("ending two")
    gallery.unlock("ending two LOCKED")

    gallery.button("Ending Three")
    gallery.image("ending three ")
    gallery.unlock("ending three LOCKED")
screen extras:
    tag menu

    hbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        grid 2 2:
            add gallery.make_button(name="Ending One",unlocked="Extras/Endings/ending one small.png",locked="Extras/Endings/ending one LOCKED.png")
            add gallery.make_button(name="Ending One",unlocked="Extras/Endings/ending one small.png",locked="Extras/Endings/ending one LOCKED.png")
            add gallery.make_button(name="Ending Two",unlocked="Extras/Endings/ending two small.png",locked="Extras/Endings/ending two LOCKED.png")
            add gallery.make_button(name="Ending Three",unlocked="Extras/Endings/ending three small.png",locked="Extras/Endings/ending three LOCKED.png")
            spacing 15
        textbutton "Return" action Return()
    ##https://www.youtube.com/watch?v=p0XSPYYrlP8
    ##https://www.youtube.com/watch?v=R-DxSXKe4Aw&list=WL&index=141
    ##            add gallery.make_button(name="Hapering",unlocked="Extras/Gallery/hapering happy.png",locked="Gallery/LOCKED.png")