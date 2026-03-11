if __name__ == "__main__":
    players = [
        {
            "player": "alice",
            "score": 2300,
            "achievements": ["first_kill", "level_10", "boss_slayer", "speedrun", "pacifist"],
            "region": "north",
            "active": True
        },
        {
            "player": "bob",
            "score": 1800,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "region": "east",
            "active": True
        },
        {
            "player": "charlie",
            "score": 2150,
            "achievements": ["first_kill", "level_10", "boss_slayer", "speedrun", "pacifist", "no_damage", "collector"],
            "region": "central"
            "active": True
        },
        {
            "player": "diana",
            "score": 2300,
            "achievements": ["first_kill", "level_10"],
            "region": "north"
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

