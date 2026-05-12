label balintawak_statue:
    scene balintawak_statue_bg with fade
    "Near the church, we found ourselves passing through the plaza again."
    "My eyes wander and find themselves on a large statue."
    "The figure depicted raises their hand in a marvelous stance."
    "He must be really important."

    show renz_questioning at sprite_fit as renz with dissolve
    renz "Hm? Are you curious about the statue?"
    me "Yes."

    show renz_thinking as renz
    renz "That's the..."
    show renz_smile as renz
    renz "Balintawak Monument!"

    me "Who is this statue depicting?"

    show renz_shocked as renz
    renz "OW- I'm trying to remember but my head still hurts."
    show renz_questioning as renz
    renz "Is there anybody you can think of?"

    menu:
        "Andres Bonifacio":
            me "Andres Bonifacio."
            jump balintawak_correct

        "Jose Rizal":
            me "Jose Rizal."
            jump balintawak_incorrect

        "Emilio Aguinaldo":
            me "Emilio Aguinaldo."
            jump balintawak_incorrect

        "Lapulapu":
            me "Lapulapu."
            jump balintawak_incorrect

label balintawak_correct:
    show renz_thinking as renz
    renz "Hmm..."
    show renz_wide_smile as renz
    renz "You got it!"
    show renz_smile as renz
    renz "I think that's right!"
    jump balintawak_explanation

label balintawak_incorrect:
    show renz_wide_smile as renz
    renz "There's no way that could be them!"
    jump balintawak_explanation

label balintawak_explanation:
    show renz_neutral_explaining as renz
    renz "Obviously, Andres Bonifacio!"
    show renz_thinking as renz
    renz "Ah! I remember now."
    show renz_neutral_explaining as renz
    renz "It's also called the Bonifacio Monument."
    renz "The statue also represents the Cry of Balintawak, when the Katipuneros tore the cedula and declared their defiance to the Spanish Empire."
    show renz_smile as renz
    renz "I really love this monument."
    renz "It honors our history and the Katipuneros that fought for our independence."

    "RUMMBBBLEEEE"

    show renz_shocked as renz
    renz "Looks like you're hungry!"
    show renz_smile as renz
    renz "Why don't we find a place to eat?"
    show renz_sad as renz
    renz "OW- My memory is still hazy."
    show renz_thinking as renz
    renz "Let's walk around. Maybe we'll find something."

    "We continue to walk around."
    "The sight of big cemented grounds catches me but..."
    "It's full of vendors."

    $ persistent.balintawak_unlocked = True
    $ renpy.save_persistent()

    show renz_questioning as renz
    renz "Wait, this place is not just a shortcut."
    show renz_melancholy as renz
    renz "The open grounds feel familiar too."
    me "The marketplace?"
    show renz_thinking as renz
    renz "Maybe. Let's take a closer look before we find food."
    jump saad_park
