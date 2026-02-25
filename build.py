import os

def build() -> None:
    # Check if public exists and has files
    if os.path.exists("public"):
        file_count = len([f for f in os.listdir('public') if os.path.isfile(os.path.join('public', f))])
        print(f"[build] ✓ Found {file_count} files in public folder.")
    else:
        os.makedirs("public", exist_ok=True)
        print("[build] ! Created missing public folder.")

if __name__ == "__main__":
    build()