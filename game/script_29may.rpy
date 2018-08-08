label may29:
    image afterCrash = "cg/afterCrash.png"
    image afterCrashOutside = "cg/afterCrashOutside.png"
    image nightSkyAfterCrash = "cg/nightSkyAfterCrash.png"
    image fullMoon = "cg/fullMoon.png"
    image zaryaFades = "cg/zaryaFades.png"
    image zaryaOnGrass = "cg/zaryaOnGrass.png"
    image twoShadows = "cg/twoShadows.png"
    image date text = Text(_("29 Мая. Мир Зари. Темный лес. Полнолуние."), size=30)
    image black = "#000000"

    transform datepos:
        xalign 0.05
        yalign 0.05

    scene afterCrash
    show date text at datepos
    empty ""
    play sound "sounds/openDoor.mp3"
    empty ""
    play sound "<from 0 to 1.5>sounds/zaryaAC.mp3"
    scene afterCrashOutside
    zsub "Твою мать..."
    zsub "Специально выбирала маршрут как можно дальше от населенных пунктов. И вот как всё обернулось…"
    play sound "sounds/nervousLaugh.mp3"
    zsub "Уверена, здесь даже никто не ездит."
    scene nightSkyAfterCrash
    empty ""
    scene fullMoon
    empty ""
    scene zaryaFades
    empty ""
    play sound "<from 0 to 1.5>sounds/fallingHuman.mp3"
    scene zaryaOnGrass
    empty ""
    play sound "<from 0 to 3>sounds/grassSteps.mp3"
    scene twoShadows
    empty ""
    play sound "<from 0 to 3>sounds/elevation.mp3"
    scene black
    empty ""

return
