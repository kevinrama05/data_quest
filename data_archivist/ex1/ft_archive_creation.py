if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", "x") as file:
            pass
    except FileExistsError:
        print("Storage already exists.")
    else:
        print("Storage unit created successfully...\n")
        entry_1 = "[ENTRY 001] New quantum algorithm discovered\n"
        entry_2 = "[ENTRY 002] Efficiency increased by 347%\n"
        entry_3 = "[ENTRY 003] Archived by Data Archivist trainee"
        with open("new_discovery.txt", "w") as file:
            print("Inscribing preservation data...")
            file.write(entry_1)
            print(entry_1, end="")
            file.write(entry_2)
            print(entry_2, end="")
            file.write(entry_3)
            print(entry_3)
        print()
        print("Data inspection complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
