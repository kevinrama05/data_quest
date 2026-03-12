if __name__ == "__main__":
    players = [
        {
            "player": "alice",
            "score": 2300,
            "achievements": {"first_kill", "level_10", "boss_slayer", "speedrun", "pacifist"},
            "region": "north",
            "active": True
        },
        {
            "player": "bob",
            "score": 1800,
            "achievements": {"first_kill", "level_10", "boss_slayer"},
            "region": "east",
            "active": True
        },
        {
            "player": "charlie",
            "score": 2150,
            "achievements": {"first_kill", "level_10", "boss_slayer", "speedrun", "pacifist", "no_damage", "collector"},
            "region": "central",
            "active": True
        },
        {
            "player": "diana",
            "score": 2300,
            "achievements": {"first_kill", "level_10"},
            "region": "north",
            "active": False
        },
    ]
    print("=== Game Analytics Dashboard ===\n")
    print("\n=== List Comprehension Examples ===")
    high_score = []
    scores_doubled = []
    active_players = []
    for i in players:
        if i["score"] > 2000:
            high_score.append(i["player"])
        scores_doubled.append(i["score"] * 2)
        if i["active"] == True:
            active_players.append(i["player"])
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {}
    score_categories = {"high": 3, "mediuim": 2, "low": 1}
    achievement_counts = {}
    for i in players:
        player_scores[i["player"]] = i["score"]
        achievement_counts[i["player"]] = len(i["achievements"])
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")
    
    print("\n=== Set Comprehension Examples ===")
    players_name = []
    active_regions = []
    achievements = {}
    unique_achievements = []
    for i in players:
        players_name.append(str(i["player"]))
        active_regions.append([i["region"]])
    for i in players:
        for j in i["achievements"]:
            try:
                achievements[j] += 1
            except KeyError:
                achievements[j] = 0
    for key, value in achievements.items():
        if value == 1:
            unique_achievements.append(key)
    regions = [r[0] for r in active_regions]
    print(f"Unique players: {players_name}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {set(regions)}")
    
    print("\n=== Combined Analysis===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(achievements)}")
    total_score = 0
    for i in players:
        total_score += i["score"]
    print(f"Average score: {total_score / len(players)}")
    sorted_players = sorted(players, key=lambda x: (x["score"], len(x["achievements"])))
    print(f'Top performer: {sorted_players[-1]["player"]} ({sorted_players[-1]["score"]} points, {len(sorted_players[-1]["achievements"])} achievements)')
