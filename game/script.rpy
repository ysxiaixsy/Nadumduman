# characters
define renz = Character("Renz", color="#3b002d", base="boy")
define me = Character("Me", color="#2e2e2e")

# variables
default player_reason = ""  # reason for visiting leganes

label start:
    jump leganes_park

label early_ending:
    # early ending scene here
    return
