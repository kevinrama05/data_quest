import sys
import importlib


def check_package(package_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def check_dependencies() -> bool:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "requests": "Network acccess ready"
    }

    all_ok = True

    print("Checking dependencies:")
    for package, description in packages.items():
        available, version = check_package(package)
        if available:
            print(f"  [OK] {package} ({version}) - {description}")
        else:
            print(f"  [MISSING] {package} - {description}")
            all_ok = False

    if all_ok is False:
        print("\nMissing packages. Install them using:")
        print("\n  With pip:")
        print("    pip install -r requirements.txt")
        print("\n  With Poetry:")
        print("    poetry install")
        sys.exit(1)

    return all_ok

def load_data() -> tuple:
    import numpy as np
    import pandas as pd

    print("\nAnalyzing Matrix data...")

    np.random.seed(42)
    n_points = 1000

    signal = np.random.randn(n_points)
    anomaly = (np.random.rand(n_points) < 0.08).astype(int)
    timestamp = np.arange(n_points)
    df = pd.DataFrame({
        "timestamp": timestamp,
        "signal": signal,
        "anomaly": anomaly,
    })
    print(f"Processing {n_points} data points...")
    
    return df, signal, anomaly, timestamp

def generate_visualization(
    df, signal, anomaly, timestamp
) -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    print("Generating visualization...\n")

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    fig.suptitle("Matrix Signal Analysis", fontsize=14)

    axes[0].plot(
        timestamp[::50],
        signal[::50],
        color="#378AAD",
        linewidth=1.5,
        label="signal"
    )
    anomaly_idx = np.where(anomaly == 1)[0]
    axes[0].scatter(
        anomaly_idx,
        signal[anomaly_idx],
        color="#E24B4A",
        s=20,
        zorder=5,
        label="anomaly"
    )
    axes[0].set_title("Signal over time")
    axes[0].set_xlabel("Timestamp")
    axes[0].set_ylabel("Signal")
    axes[0].legend(fontsize=8)

    axes[1].hist(
        signal,
        bins=20,
        color="#1D9E75",
        edgecolor="none"
    )
    axes[1].set_title("Signal distribution")
    axes[1].set_xlabel("Value")
    axes[1].set_ylabel("Frequency")
    
    normal_count = int(df["anomaly"].value_counts().get(0, 0))
    anomaly_count = int(df["anomaly"].value_counts().get(1, 0))
    axes[2].pie(
        [normal_count, anomaly_count],
        labels=["Normal", "Anomaly"],
        colors=["#378AAD", "#E24B4A"],
        autopct="%1.1f%%",
        startangle=90
    )
    axes[2].set_title("Anomaly ratio")

    plt.tight_layout()
    plt.savefig("matrix_analysis.png", dpi=150, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        sys.exit(1)

    df, signal, anomaly, timestamp = load_data()
    generate_visualization(df, signal, anomaly, timestamp)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
