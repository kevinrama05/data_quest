if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    with open("vault.txt", "w") as vault:
        vault.write("Quantum encryption keys recovered\n")
        vault.write("Archive integrity: 100%\n")
        vault.write("New security protocols archived\n")

    with open("vault.txt", "r") as vault:
        print("Vault connection established with failsafe protocols\n")
        lines = vault.read().splitlines()

        print("SECURE EXTRACTION:")
        print(f"[CLASSIFIED] {lines[0]}")
        print(f"[CLASSIFIED] {lines[1]}")

        print("\nSECURE PRESERVATION:")
        print(f"[CLASSIFIED] {lines[2]}")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")
