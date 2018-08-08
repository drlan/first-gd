# Определение персонажей игры.
define z = Character('Заря', color="#FF4500")

define zsub = Character(None,
                            what_white_color="#FF4500",
                            what_xalign=0.5,
                            what_textalign=0.5,
                            what_size=28,
                            window_background=None,
                            what_layout='subtitle')
define empty = Character(None,
                            what_white_color="#ffffff",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            what_size=26,
                            window_background=None,
                            what_layout='subtitle')

# Игра начинается здесь:
label start:
    jump may29
    return
