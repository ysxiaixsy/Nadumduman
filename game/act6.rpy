label katunggan_eco_park:
    scene katunggan with fade
    "Katunggan Eco Park."
    "Leganes Integrated Katunggan Eco Park, also known as LIKE."
    "The mangroves creep from the muddy waters and form pretty foliage as a result."
    "What a beautiful place, nature at its finest."

    show renz_smile at sprite_fit as renz with dissolve
    renz "This place is amazing."
    show renz_neutral_explaining as renz
    renz "I was told it was just a fish pond at first, but a typhoon damaged it, causing the owner to have to repair it."
    renz "As a result, we have this amazing eco park now, with more than 50 species of animals and plants, including endangered ones."
    show renz_melancholy as renz
    renz "Shows how much time can change something... or someone."
    show renz_neutral_explaining as renz
    renz "I remember volunteering in cleanup and tree-planting projects here."
    renz "This park is at the heart of many environmental communities."
    renz "Its health, as well as the eco-tourism it brings, sustains the livelihoods of the people."
    show renz_thinking as renz
    renz "Lately there have been a few illegal trespassers and issues on waste management that threaten the welfare of this reserve."
    show renz_smile as renz
    renz "I hope we can continue to protect and preserve this place."

    "We continue our walk, spotting more birds, reptiles, and different native flora and fauna."
    "My legs start to tire, so we find a spot where we can sit down and stare at the sea."

label katunggan_good_ending:
    scene katunggan_final with fade
    "Renz and I stare into the lush and vibrant greenery of the mangrove forest and wetlands."
    "The golden shine of the afternoon rays make the whole scenery glow brighter than it would've."
    me "I've seen this place before."
    me "I've been here."
    me "Why can't I remember?"
    "Renz seems more quiet than usual, looking into the sunset."
    "Is he remembering something too?"

    show renz_melancholy at sprite_fit as renz with dissolve
    renz "The memories."
    renz "They've come back to me."
    renz "But tell me, did they come back for you too?"
    show renz_thinking as renz
    renz "I'm not the only one who's been here before."

    me "Renren?"
    show renz_melancholy as renz
    renz "You finally remember."
    renz "How long has it been since I last saw your face?"

    window hide
    stop music fadeout 1.0
    pause 1.0
    window show
    # Suggested music cue if a licensed audio file is added: an OPM ballad with the mood of "Multo".

    "It all comes back to me."
    "All the places we've been to."
    "We've gone there together. The two of us."
    "How long has it been?"
    "We were close, very close."
    "We shared every thought in our hearts and walked around this park."
    me "Does that mean..."
    me "The reason I ran into him..."

    scene leganes_park_intro with fade
    "Flashback. Leganes Plaza."

    show renz_thinking at sprite_fit as renz with dissolve
    renz "Hey... that person..."
    show renz_shocked as renz
    renz "I've seen them before."
    renz "Huh! It can't be!"
    show renz_questioning as renz
    renz "I gotta follow them!"
    show renz_sad as renz
    renz "But... it's so hot..."
    renz "I feel so light headed."
    show renz_shocked as renz
    renz "Hey... wait up!"
    "*THUMP*"

    scene black with fade
    pause 1.0

    scene katunggan_final with fade
    show renz_melancholy at sprite_fit as renz with dissolve
    me "Renren- I..."
    renz "I know."
    renz "You have to go soon again, right?"
    renz "Back to your job in the big city."
    show renz_smile as renz
    renz "It's okay. I won't be lonely here."
    show renz_pout as renz
    renz "I still have friends other than you, you know!"
    show renz_melancholy as renz
    renz "But promise me."
    renz "Promise me you'll come back every now and then, even if it's just for Saad Festival."
    me "I-"
    renz "Please."

    menu:
        "Okay. I promise.":
            me "Okay. I promise."

    show renz_smile as renz
    renz "... Panumduma lang ako."

    $ persistent.katunggan_unlocked = True
    $ renpy.save_persistent()

    scene black with fade
    call ending_credits
    return

label ending_credits:
    window hide
    play music "music/Eva Eugenio - Maalaala Mo Kaya.mp3" fadein 2.0
    call screen ending_credits_roll
    stop music fadeout 2.0
    return

transform credits_scroll:
    xalign 0.5
    ypos 1.18
    linear 40.0 ypos -1.8

screen ending_credits_roll():
    tag credits

    add Solid("#000000")

    vbox:
        at credits_scroll
        xalign 0.5
        spacing 42

        text "Nadumduman":
            xalign 0.5
            size 92
            color "#f0c76a"

        text "Good Ending":
            xalign 0.5
            size 48
            color "#ffffff"

        null height 80

        text "Starring":
            xalign 0.5
            size 54
            color "#f0c76a"
        text "Frederick Renz Banas":
            xalign 0.5
            size 42
            color "#ffffff"

        null height 50

        text "Writer & Director":
            xalign 0.5
            size 54
            color "#f0c76a"
        text "Yuan Birondo":
            xalign 0.5
            size 42
            color "#ffffff"

        null height 50

        text "Devs":
            xalign 0.5
            size 54
            color "#f0c76a"
        text "Dejel Cyrus De Asis":
            xalign 0.5
            size 42
            color "#ffffff"
        text "John Romyr Lopez":
            xalign 0.5
            size 42
            color "#ffffff"
        text "JP Salomeo":
            xalign 0.5
            size 42
            color "#ffffff"

        null height 50

        text "Design & Assets":
            xalign 0.5
            size 54
            color "#f0c76a"
        text "JP Salomeo":
            xalign 0.5
            size 42
            color "#ffffff"    

        null height 100

        text "Special Thanks To":
            xalign 0.5
            size 54
            color "#f0c76a" 

        text "Everyone who made Nadumduman possible!":
            xalign 0.5
            size 42
            color "#ffffff"

        null height 1000

    timer 44.0 action Return()
