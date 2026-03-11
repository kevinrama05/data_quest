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
    players = []
    active_regions = []
    for i in players:
        players.append(i["player"])
        active_regions = [i["region"]]
    print(f"Unique players: {set(players)}")
    print(f"Unique achievements: {}")
