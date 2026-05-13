label leganes_park:
    scene leganes_park_intro with fade
    "A hot day at Leganes Plaza."
    me "This is too much, I can't deal with this summer heat."
    "It's so hot that I end up finishing the entire bottle of water I was holding."
    me "Time to throw it in the trash."

    scene leganes_park with fade
    me "Wait... is that?"

    scene renz_yamcha with fade
    me "Someone passed out!"
    "After shaking him a bit, he finally woke up."
    
    scene leganes_park with fade
    me "Are you okay?"
    show renz_thinking at sprite_fit as renz with dissolve
    renz "My memory is a little hazy."
    menu:
        "What happened to you?":
            jump renz_what_happened
        "Let's get you checked up.":
            jump renz_checkup

label renz_what_happened:
    show renz_thinking as renz
    renz "Well, like I said, my memory is a little hazy."
    renz "I don't remember a single thing."
    renz "Might've been the heat."

    jump renz_checkup_merge

label renz_checkup:
    show renz_smile as renz
    renz "I'm okay!"
    show renz_bashful     as renz
    renz "I think I just fainted from the heat a bit."

label renz_checkup_merge:
    me "That's even more concerning!"
    show renz_pout as renz
    renz "I said I'm fine!"
    show renz_annoyed as renz
    renz "I'm a tough guy, you know?"
    menu:
        "I can't just leave you alone.":
            jump renz_cant_leave
        "I'll leave you alone then.":
            jump renz_leaving

label renz_leaving:
    show renz_shocked as renz
    renz "Oh, okay."
    show renz_bashful as renz  
    renz "Not like I needed any help or anything.."
    show renz_sad as renz
    renz "OW– my head still hurts.."
    jump renz_geez

label renz_cant_leave:
    show renz_annoyed as renz
    renz "I said I'm fine!"
    show renz_sad as renz    
    renz "OW– my head still hurts.."
    jump renz_geez

label renz_geez:
    show renz_looking_away as renz
    renz "Geez, okay I get it."
    show renz_thinking as renz    
    renz "Don't you have anything better to do though?"
    show renz_questioning as renz    
    renz "What are you doing here anyway?"
    menu:
        "I'm on vacation.":
            $ player_reason = "vacation"
        "I'm visiting some relatives.":
            $ player_reason = "relatives"
        "Just taking a walk.":
            $ player_reason = "walk"
    show renz_questioning as renz
    renz "Hm, I'm guessing you haven't been here before, right?"
    show renz_smile as renz    
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
    show renz_smile as renz
    renz "Great!"
    scene outside_church with fade
    me "Leganes Church?"
    show renz_smile at sprite_fit as renz with dissolve
    # ALWAYS REAPPLY SPRITEFIT AFTER A SCENE CHANGE

    renz "That's what we call it around here."
    renz "But its official name is the Archdiocesan Shrine of Saint Vincent Ferrer."
    show renz_looking_away as renz    
    renz "Now let's not waste any time! It's so hot out here, let's go!"
    jump visit_church
