def crisis_handler(filename: str, routine: bool = False) -> None:
    label = "ROUTINE ACCESS" if routine else "CRISIS ALERT"
    print(f"{label}: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as vault:
            data = vault.read().strip()
            print(f'SUCCESS: Archive recovered - "{data}"')
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly - {e}")
        print("STATUS: Crisis handled, system stabilized")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt", routine=True)
    print()
    print("All crisis scenarios handled successfully.  Archives secure.")
