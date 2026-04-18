# Mobile Legends Match Tracker

heroes = [
    ("Layla",   "Marksman"),
    ("Tigreal", "Tank"),
    ("Gusion",  "Assassin"),
    ("Kagura",  "Mage"),
    ("Chou",    "Fighter"),
]

# --- Player Info ---
ign  = input("In-game name (IGN): ")
rank = input("Current rank: ")

# --- Hero Roster ---
print()
print("==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")
for i, (name, role) in enumerate(heroes, 1):
    print(f" {i}. {name:<10} [{role}]")
print("==========================================")

# --- Match Entries ---
matches = []

for match_num in range(1, 5):
    print(f"\n--- MATCH {match_num} ---")

    while True:
        try:
            hero_num = int(input("Hero number (0 to skip): "))
            if 0 <= hero_num <= 5:
                break
            print("  Please enter a number between 0 and 5.")
        except ValueError:
            print("  Invalid input. Enter a number.")

    if hero_num == 0:
        continue  # skip this slot

    hero_name, _ = heroes[hero_num - 1]

    while True:
        try:
            kills   = int(input("Kills: "))
            deaths  = int(input("Deaths: "))
            assists = int(input("Assists: "))
            break
        except ValueError:
            print("  Invalid input. Enter whole numbers.")

    while True:
        result = input("Result (W/L): ").strip().upper()
        if result in ("W", "L"):
            break
        print("  Please enter W or L.")
    denominator = deaths if deaths > 0 else 1
    kda = (kills + assists) / denominator

    if kda >= 5 and result == "W":
        tag = "Better Luck Next Game"

    matches.append({
        "hero":   hero_name,
        "kda":    kda,

# --- Summary ---
matches_played = len(matches)
wins   = sum(1 for m in matches if m["result"] == "W")
losses = matches_played - wins
win_rate = int(wins / matches_played * 100) if matches_played > 0 else 0

best = max(matches, key=lambda m: m["kda"]) if matches else None
best_idx = matches.index(best) + 1 if best else None

# --- Match Log ---
print()
print("=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for i, m in enumerate(matches, 1):
    result_str = "WIN " if m["result"] == "W" else "LOSS"
    print(f"[{i}] {m['hero']:<10} | KDA: {m['kda']:<6.2f} | {result_str} | {m['tag']}")

print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")
if best:
    print(f"Best Match     : [{best_idx}] {best['hero']}  (KDA: {best['kda']:.2f})")
print("=============================================")        "result": result,
        "tag":    tag,
    })
        tag = "DOMINATION!"
        tag = "Team Effort"
    else:
    elif kda >= 5 and result == "L":
        tag = "Carried Hard"
    elif kda < 5 and result == "W":

