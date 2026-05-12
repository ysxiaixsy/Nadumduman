label saad_park:
    scene saad_park_bg with fade
    "Saad Park."
    "The wide cemented grounds were busier up close."
    "Vendors lined the walkways, their tarps cutting bright patches across the heat."
    "Renz is just staring."
    "With a sad expression on his face."

    show renz_melancholy at sprite_fit as renz with dissolve
    me "Are you remembering anything?"
    show renz_shocked as renz
    renz "This is-"
    show renz_neutral_explaining as renz
    renz "I'm remembering all the festivals and events I went to and experienced here."
    show renz_melancholy as renz
    renz "But... it's being used as a marketplace while those events aren't happening yet."

    me "What kind of events did you have?"

    show renz_smile as renz
    renz "Have you heard of the Saad Festival?"
    renz "Saad means vow."
    renz "The festival was first held to celebrate the birth of the patron saint of this town."
    show renz_questioning as renz
    renz "You're a smart one, can you guess who that is?"

    menu:
        "Saint Vincent Ferrer":
            $ saad_patron_answered_correctly = True
            me "Saint Vincent Ferrer."
            jump saad_patron_correct

        "Saint Paul":
            $ saad_patron_answered_correctly = False
            me "Saint Paul."
            jump saad_patron_incorrect

        "Saint Peter":
            $ saad_patron_answered_correctly = False
            me "Saint Peter."
            jump saad_patron_incorrect

label saad_patron_correct:
    show renz_smile as renz
    renz "Correct!"
    renz "That was an easy question after all, pretty obvious if you've paid attention."
    jump saad_ritual_question

label saad_patron_incorrect:
    show renz_angry as renz
    renz "Really?"
    renz "It's not even that hard to figure out, unless you weren't listening at all."
    show renz_annoyed as renz
    renz "Pay attention next time."
    jump saad_ritual_question

label saad_ritual_question:
    show renz_neutral_explaining as renz
    renz "Moving on, it's not solely a religious festival."
    renz "Like most festivals here, traditional Filipino culture is integrated."
    show renz_smile as renz
    renz "I remember watching those ritual dances based on the Leganes folktales."
    show renz_questioning as renz
    renz "There's also one central ritual done here. Do you still remember?"

    menu:
        "patilaw":
            me "Patilaw."
            jump saad_ritual_incorrect

        "papila":
            me "Papila."
            jump saad_ritual_incorrect

        "palapak":
            me "Palapak."
            jump saad_ritual_correct

label saad_ritual_correct:
    show renz_wide_smile as renz
    renz "Glad you still remembered!"
    jump saad_palapak_explanation

label saad_ritual_incorrect:
    if saad_patron_answered_correctly:
        show renz_pout as renz
        renz "You should listen properly! It's palapak!"
    else:
        show renz_annoyed as renz
        renz "No, it's palapak."
        show renz_pout as renz
        renz "Try to keep that one in mind this time."
    jump saad_palapak_explanation

label saad_palapak_explanation:
    show renz_neutral_explaining as renz
    renz "Palapak is the ritual where the priest taps a small figure of San Vicente on the head of the devotee."
    renz "They then pray about things such as good health and fortune."
    show renz_thinking as renz
    renz "Speaking of festivals..."
    show renz_melancholy as renz
    renz "I remember something about my dad taking me to another one."
    renz "Something near the sea..."

    show renz_shocked as renz
    renz "Wait."
    show renz_wide_smile as renz
    renz "I know where we can eat!"

    "After a tricycle ride to the coastal road, we arrive at a building full of a fishy smell."

    $ persistent.saad_unlocked = True
    $ renpy.save_persistent()

    jump bebot_millas
