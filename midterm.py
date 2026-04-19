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
for i in range(len(heroes)):
    print(f" {i+1}. {heroes[i][0]:<10} [{heroes[i][1]}]")

print("==========================================\n")

# Initialize tracking variables
match_history = []
wins = 0
losses = 0
matches_played = 0
best_kda = -1.0
best_match_info = ""

# 3. Accept 4 match entries
for m in range(1, 5):
    print(f"--- MATCH {m} ---")
    hero_num = int(input("Hero number (0 to skip): "))
    
    if hero_num == 0:
        continue  # Skip this iteration
    
    # 4. If valid, ask for stats
    if 1 <= hero_num <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()
        
        matches_played += 1
        hero_name = heroes[hero_num - 1][0]
        
        # 5. Compute KDA
        denom = deaths
        if deaths == 0:
            denom = 1
        kda = (kills + assists) / denom
        
        # 6. Performance Tag
        tag = ""
        res_text = ""
        if result == "W":
            wins += 1
            res_text = "WIN"
            if kda >= 5:
                tag = "DOMINATION!"
            else:
                tag = "Team Effort"
        else:
            losses += 1
            res_text = "LOSS"
            if kda >= 5:
                tag = "Carried Hard"
            else:
                tag = "Better Luck Next Game"
        
        # Store match data for the log
        match_data = [matches_played, hero_name, kda, res_text, tag]
        match_history.append(match_data)
        
        # 7. Identify Best Match
        if kda > best_kda:
            best_kda = kda
            best_match_info = f"[{matches_played}] {hero_name}  (KDA: {kda:.2f})"
    
    print() # New line for spacing

# 8. Print Formatted Match Log
print("=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for match in match_history:
    # index 0: #, 1: Hero, 2: KDA, 3: Res, 4: Tag
    print(f"[{match[0]}] {match[1]:<10} | KDA: {match[2]:.2f}  | {match[3]:<4} | {match[4]}")
win_rate = 0
if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")
print(f"Best Match     : {best_match_info}")
print("=============================================")
