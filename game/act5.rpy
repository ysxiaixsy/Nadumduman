label bebot_millas:
    scene bebot_millas_bg with fade
    "Bebot and Milla's."
    "The sign outside says Bebot and Milla's Talabahan."
    "The place's structure is unique, like a kubo with part of the place being on the beach."
    "The air is salty, smoky, and warm from the kitchen."

    show renz_wide_smile at sprite_fit as renz with dissolve
    renz "This is Bebot and Milla's!"
    renz "They have great talaba here!"
    show renz_questioning as renz
    renz "Before I order for us, what's your favorite seafood?"

    menu:
        "Pork":
            me "Pork."
            jump bebot_pork_choice

        "Squid":
            me "Squid."
            jump bebot_seafood_choice

        "Oyster":
            me "Oyster."
            jump bebot_seafood_choice

        "Shrimp":
            me "Shrimp."
            jump bebot_seafood_choice

label bebot_seafood_choice:
    show renz_smile as renz
    renz "Great! I'll order you some."
    show renz_wide_smile as renz
    renz "You know, I don't actually eat seafood here."
    renz "I just eat the Pork Kawali all the time."
    jump bebot_meal

label bebot_pork_choice:
    show renz_wide_smile as renz
    renz "What a coincidence!"
    renz "I just eat Pork Kawali all the time here, I don't usually eat seafood."
    jump bebot_meal

label bebot_meal:
    "The food arrives, steam curling up from the plates while the waves murmur nearby."
    "The smell is sooo good and its flavor melts in my mouth."
    "Tastes so much better when I have... him with me."

    show renz_wide_smile as renz
    renz "I'm so full. That felt amazing!"
    show renz_neutral_explaining as renz
    renz "Anyways, I remember why I thought of this place."
    renz "Other than the times I eat lunch and dinner here occasionally, I remember watching a festival here."
    show renz_smile as renz
    renz "It's called the Biray-Paraw Festival."
    renz "Everyone goes to the beach to celebrate Leganes and its sailing traditions."
    renz "There's even sailing races!"

    window hide
    pause 1.0
    window show

    show renz_melancholy as renz
    renz "..."
    renz "All the memories I have of this town are coming to me."
    show renz_thinking as renz
    renz "I'm starting to remember."

    "Renz turns to me, his eyes reflecting a sort of melancholy in him, like he's looking at the inevitable."
    "I wonder what it is that is so important for him to make that sort of face."
    "Did he remember something that's really important?"

    show renz_melancholy as renz
    renz "It's going to be late soon."
    show renz_neutral_explaining as renz
    renz "We should go to one last place before figuring out what to do next."
    show renz_smile as renz
    renz "And I know exactly where to go."

    "The next thing I knew, we were on another trike northward, this time to a little clearing near the waters."

    $ persistent.bebot_unlocked = True
    $ renpy.save_persistent()

    return
