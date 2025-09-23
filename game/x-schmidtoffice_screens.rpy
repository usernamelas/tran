screen SchmidtOffice():
    zorder 150
    add "hospital/Scenes/day_1/30-11 doctors office anna.jpg"
    imagebutton auto "hospital/Scenes/day_1/computerscreen_%s.png":
        focus_mask True
        action [Hide("tooltip_example"), Jump("hospitalcomputercheck")]
        tooltip "Computer"
        hovered Show("tooltip_example")
        unhovered Hide("tooltip_example")
    imagebutton auto "hospital/Scenes/day_1/vase_%s.png":
        focus_mask True
        action [Hide("tooltip_example"), Jump("hospitalvasecheck")]
        tooltip "Vase"
        hovered Show("tooltip_example")
        unhovered Hide("tooltip_example")
    imagebutton auto "hospital/Scenes/day_1/paperstack_%s.png":
        focus_mask True
        action [Hide("tooltip_example"), Jump("hospitalpaperstackcheck")]
        tooltip "Stack of Papers"
        hovered Show("tooltip_example")
        unhovered Hide("tooltip_example")
    imagebutton auto "hospital/Scenes/day_1/cupboardone_%s.png":
        focus_mask True
        action [Hide("tooltip_example"), Jump("hospitalcupboardcheck")]
        tooltip "Cupboard"
        hovered Show("tooltip_example")
        unhovered Hide("tooltip_example")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
