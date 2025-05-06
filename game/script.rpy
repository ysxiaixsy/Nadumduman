# characters
define renz = Character("Renz", color="#3b002d")
define me = Character("Me", color="#2e2e2e")

# variables
default player_reason = ""  # reason for visiting leganes
default saad_patron_answered_correctly = False
default persistent.church_unlocked = False
default persistent.balintawak_unlocked = False
default persistent.saad_unlocked = False
default persistent.bebot_unlocked = False

image balintawak_statue_bg = "statue02_bg.png"
image saad_park_bg = "saad_park2_bg.png"
image bebot_millas_bg = "bebot_millas_bg.png"

transform sprite_fit:
    zoom 0.60
    yanchor 1.0      # anchor to bottom of image
    ypos 1.0         # place at bottom of screen
    xalign 0.5       # center horizontally

label start:
    jump leganes_park

label early_ending:
    # early ending scene here
    return
