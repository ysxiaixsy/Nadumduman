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
default persistent.katunggan_unlocked = False

image balintawak_statue_bg = "statue02_bg.png"
image saad_park_bg = "saad_park2_bg.png"
image bebot_millas_bg = "bebot_millas_bg.png"
image katunggan_bg = "katunggan_bg.png"
image katunggan_final_view = "katunggan_final_view.png"

init python:
    def unlocked_main_menu_background_name():
        unlocked = []

        if persistent.church_unlocked:
            unlocked.append("church")
        if persistent.balintawak_unlocked:
            unlocked.append("balintawak")
        if persistent.saad_unlocked:
            unlocked.append("saad")
        if persistent.bebot_unlocked:
            unlocked.append("bebot")
        if persistent.katunggan_unlocked:
            unlocked.append("katunggan")

        if not unlocked:
            return gui.main_menu_background

        return "home_menu_{}_unlocked.png".format("_".join(unlocked))

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
