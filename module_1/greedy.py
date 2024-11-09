change_input = float(input("How much change is owed? "))

while change_input < 0:
        change_input = float(input("Please Input Valid number (>0)"))

change_cents = int(round(change_input*100))

coins = 0

# No lists, can't do loops through them :(

coins += change_cents // 25
change_cents = change_cents % 25

coins += change_cents // 10
change_cents = change_cents % 10

coins += change_cents // 5
change_cents = change_cents % 5

coins += change_cents // 1
change_cents = change_cents % 1

print(coins)
