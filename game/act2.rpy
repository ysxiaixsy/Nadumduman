label visit_church:
    scene outside_church with fade
    "Leganes Church."
    "The current Kura Paroko of the church is Father Tababa."
    "His words fill the room as the devotees listen intently."
    "As I try to listen in as well, Renz taps me on the shoulder."

    show renz_questioning at sprite_fit as renz with dissolve
    renz "Hey, quick question, are you Catholic?"

    menu:
        "Yes":
            me "Yes."
            jump church_candles

        "No":
            me "No."
            jump church_not_catholic

label church_not_catholic:
    show renz_thinking as renz
    renz "Uh, well are you fine with coming with me to light some candles?"

    menu:
        "Sure":
            me "Sure."
            jump church_candles

        "I don't feel like it":
            me "I don't feel like it."
            jump church_wait_outside

label church_wait_outside:
    show renz_looking_away as renz
    renz "Huh. Okay."
    show renz_sad as renz
    renz "You can just wait outside."
    jump church_visit_done

label church_candles:
    show renz_smile as renz
    renz "Great! Come with me, let's light some candles."

    "We both went to a nearby vendor."
    "He picked out two red candles, one for him and one for me."
    "Then we lit the candles and put our hands together for a prayer."

    show renz_questioning as renz
    renz "What did you pray for?"

    menu:
        "For safe travels":
            me "For safe travels."
            jump church_renz_prayer

        "For you to be okay":
            me "For you to be okay."
            jump church_prayed_for_renz

label church_prayed_for_renz:
    show renz_bashful as renz
    renz "Really? >///<"
    jump church_renz_prayer

label church_renz_prayer:
    show renz_neutral_explaining as renz
    renz "I prayed for help in figuring this situation out."
    renz "I've been here with my family a lot."
    renz "During Holy Week and the Saad Festival, there's the palapag, or palapak, a practice where a statue of the town's head saint, Saint Vincent Ferrer, is tapped on the head of a devotee."
    show renz_melancholy as renz
    renz "Thanks for coming with me here."
    renz "I haven't been here ever since-"
    show renz_shocked as renz
    renz "OW, my head still hurts."
    show renz_sad as renz
    renz "Let's head out."
    jump church_visit_done

label church_visit_done:
    $ persistent.church_unlocked = True
    $ renpy.save_persistent()
    scene outside_church with fade
    "A few minutes later, we found ourselves outside the church again."

    show renz_smile at sprite_fit as renz with dissolve
    renz "The plaza is just nearby."
    show renz_questioning as renz
    renz "Do you want to keep walking for a bit?"
    me "Yeah, let's go."
    jump balintawak_statue
