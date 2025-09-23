screen AndrewRoomScreen():
    zorder 150
    add "hospital/imagemap/hospitalandrewroom.jpg"
    imagebutton auto "hospital/imagemap/hospitalandrew_%s.png":
        focus_mask True
        action NullAction()
        tooltip "Andrew"
        hovered Show("tooltip_example")
        unhovered Hide("tooltip_example")
    imagebutton auto "hospital/imagemap/tohospitalhall_%s.png":
        focus_mask True
        action [SetVariable("isActivePlace", 15),
        Hide("tooltip_example"),
        Hide("AndrewRoomScreen"),
        Play("sound", "audio/sounds/door2.ogg"),
        Jump("hospitalScreen")]
        tooltip "To Main Hall"
        hovered Show("tooltip_example")
        unhovered Hide("tooltip_example")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
