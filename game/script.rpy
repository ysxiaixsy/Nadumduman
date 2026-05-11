# characters
define renz = Character("Renz", color="#3b002d")
define me = Character("Me", color="#2e2e2e")

# variables
default player_reason = ""  # reason for visiting legasnes

label start:
    jump leganes_park

label leganes_park:
    scene leganes_park with fade
    me "Are you okay?"
    show renz thinking with dissolve
    renz "My memory is a little hazy."
    menu:
        "What happened to you?":
            jump renz_what_happened
        "Let's get you checked up.":
            jump renz_checkup

label renz_what_happened:
    show renz thinking
    renz "Well, like I said, my memory is a little hazy."
    renz "I don't remember a single thing."
    renz "Might've been the heat."
    jump renz_checkup_merge

label renz_checkup:
    show renz smile with dissolve
    renz "I'm okay!"
    show renz bashful
    renz "I think I just fainted from the heat a bit."

    label renz_checkup_merge:
    me "That's even more concerning!"
    show renz pout with dissolve
    renz "I said I'm fine!"
    show renz tsun
    renz "I'm a tough guy, you know?"
    menu:
        "I can't just leave you alone.":
            jump renz_cant_leave
        "I'll leave you alone then.":
            jump renz_leaving

label renz_leaving:
    show renz shocked with dissolve
    renz "Oh, okay."
    show renz bashful
    renz "Not like I needed any help or anything.."
    show renz pain
    renz "OW– my head still hurts.."
    jump renz_geez

label renz_cant_leave:
    show renz tsun with dissolve
    renz "I said I'm fine!"
    show renz pain
    renz "OW– my head still hurts.."
    jump renz_geez

label renz_geez:
    show renz geez with dissolve
    renz "Geez, okay I get it."
    show renz thinking
    renz "Don't you have anything better to do though?"
    show renz question
    renz "What are you doing here anyway?"
    menu:
        "I'm on vacation.":
            $ player_reason = "vacation"
        "I'm visiting some relatives.":
            $ player_reason = "relatives"
        "Just taking a walk.":
            $ player_reason = "walk"
    show renz question with dissolve
    renz "Hm, I'm guessing you haven't been here before, right?"
    show renz smile
    renz "Why don't I just show you around then?"
    menu:
        "Sure!":
            jump renz_agree
        "I'll pass.":
            jump renz_decline

label renz_decline:
    renz "Hah? Okay then."
    renz "We're done here. See you never."
    jump early_ending

label renz_agree:
    show renz smile with dissolve
    renz "Great!"
    scene leganes_park with fade
    me "Leganes Church?"
    show renz smile
    renz "That's what we call it around here."
    renz "But its official name is the Archdiocesan Shrine of Saint Vincent Ferrer."
    show renz geez
    renz "Now let's not waste any time! It's so hot out here, let's go!"
    jump visit_church

label early_ending:
    # early ending scene here
    return