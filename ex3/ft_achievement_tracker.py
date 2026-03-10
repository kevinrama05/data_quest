if __name__ == "__main__":
    alise = {'first_kill', 'level_10', 'treasure_hunter', "speed_demon"}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    print("=== Achievement Tracker System ===\n")
    print(f"Player Alise Achievements: {alise}")
    print(f"Player Bob Achievements: {bob}")
    print(f"Player Charlie Achievements: {charlie}")

    print("\n=== Achievement Analytics ===")
    uni = alise | bob | charlie
    print(f"All unique achievements: {uni}")
    print(f"Total unique achievements: {len(uni)}\n")
    print(f"Common to all players: {alise & bob & charlie}")
    print(f"Rare achievements (1 player): {(alise - bob - charlie) | (bob - alise - charlie) | (charlie - alise - bob)}\n")

    print(f"Alise vs Bob common: {alise & bob}")
    print(f"Alise unique: {alise - bob}")
    print(f"Bob unique: {bob - alise}")
    
