import os

def build() -> None:
    # Ensure the public directory exists
    if os.path.exists("public"):
        print(f"[build] ✓ Public folder detected with {len(os.listdir('public'))} files.")
    else:
        os.makedirs("public", exist_ok=True)
        print("[build] ! Warning: Public folder was missing and has been created.")

if __name__ == "__main__":
    build()