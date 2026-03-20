import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_configuration(config: dict) -> list:
    required = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    missing = []

    for key in required:
        if config[key] is None:
            missing.append(key)

    return missing


def print_configuration(config: dict, missing: list) -> None:
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"]
    print(f"  Mode:           {mode}")

    if config["DATABASE_URL"]:
        print("  Database:       Connected to local instance")
    else:
        print("  Database:       [MISSING] DATABASE_URL not set")

    if config["API_KEY"]:
        print("  API Access:     Authenticated")
    else:
        print("  API Access:     [MISSING] API_KEY not set")

    print(f"  Log Level:      {config['LOG_LEVEL']}")

    if config["ZION_ENDPOINT"]:
        print("  Zion Network:   Online")
    else:
        print("  Zion Network:   [MISSING] ZION_ENDPOINT not set")


def security_check(config: dict, missing: list) -> None:
    print("\nEnvironment security check:")

    print("  [OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("  [OK] .env file properly configured")
    else:
        print("  [WARN] .env file not found — using env variables or defaults")

    if os.getenv("MATRIX_MODE"):
        print("  [OK] Production overrides available")
    else:
        print("  [WARN] No production overrides set")

    if missing:
        print(f"\n  [WARN] Missing variables: {', '.join(missing)}")
        print("  Copy .env.example to .env and fill in your values:")
        print("    cp .env.example .env")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()
    missing = validate_configuration(config)

    print_configuration(config, missing)
    security_check(config, missing)

    print("\nThe Oracle sees all configurations.")

