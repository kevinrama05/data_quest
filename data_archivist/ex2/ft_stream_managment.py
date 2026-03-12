from sys import stdin, stdout, stderr

if __name__ == "__main__":
    stdout.write("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    stdout.write("\nInput Stream active: Enter archivist ID: ")
    stdout.flush()
    a_id = stdin.readline().strip()
    stdout.write("Input Stream active: Enter status report: ")
    stdout.flush()
    status_report = stdin.readline().strip()

    stdout.write("\n")
    stdout.write(f"[STANDARD] Archive status from {a_id}: {status_report}\n")
    stderr.write("[ALERT] System diagnostic: ")
    stderr.write("Communication channels verified\n")
    stdout.write("[STANDARD] Data transmission complete\n")
    stdout.write("\n")
    stdout.write("Three-channel communication test successful.\n")
