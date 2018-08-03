# Определение персонажей игры.
define zarya = Character('Заря', color="#361136")
define slowdissolve = Dissolve(1.0)
define esubtitle = Character(None, 
                            what_white_color="#ffffff", 
                            what_xalign=0.5, 
                            what_text_align=0.5, 
                            what_size=26,
                            window_background=None, 
                            window_yminimum=300, 
                            show_say_vbox_properties=dict(xalign=0.5),
                            what_layout='subtitle')

label start:

    # 29 мая, мир Зари, темный лес, полнолуние

    # кадр 1 - Заря с травмой головы лежит на руле
    # scene bg ____
    # play sound "открытие дверей машины"

    # кадр 2 -  Из последних сил выползает, садится, облокотившись на машину
    scene bg broke_car

    esubtitle "{color=#ffffff}Боль дикая. Я в полной жопе{/color}"
    esubtitle "{color=#ffffff}Специально выбирала маршрут как можно дальше от населенных пунктов. И вот как всё обернулось…{/color}"

    # play sound "нервный смешок"

    esubtitle "{color=#ffffff}Уверена, здесь даже никто не ездит{/color}"

    # кадр 3 - Крупным планом Заря смотрит на небо
    scene bg night_sky with slowdissolve

    # кадр 4 - Полная луна
    #scene bg full_moon with slowdissolve
    # или конструкция вида image ... = .... ("1.jpg", 2.0,
    #                                        "2.jpg, 2.0")

    esubtitle "{color=#ffffff}Я обречена?{/color}"

    #Кадр 5. Заря теряет сознание.
    #Кадр 6. Исчезает машина, дерево остаётся без повреждений.
    # play sound *падающее тело*
    #Кадр 7. Заря лежит на земле.
    #Кадр 8. Две тени возле Зари. Мужчины и Женщины.
    #Кадр 9. Тёмный экран.

    # play sound *поднимают тело*
    # play sound *шаги по траве*

    hide bg night_sky
    
    "Женский голос" "Мы нашли её! Нашли! Заберём ладушку домой?"

    zarya "М-меня кто-то несёт? Глаза открыть не могу..."

    "Мужской голос" "Нет, сегодня не успеем. Петухи уже скоро."

    # 30 мая, мир Руси, дом упырей