"""
Writes index.html into the ./public directory for Firebase Hosting.
"""
import os, datetime
HTML = f"<html><body style='font-family:sans-serif;text-align:center;margin-top:20vh;'><h1>Hello World... last build: </h1><p>{datetime.datetime.now():%Y-%m-%d %I:%M:%S %p}</p></body></html>"
def build() -> None:
    #Create the 'public' directory so Python doesn't crash
    os.makedirs("public", exist_ok=True)    
    #Save the file inside that directory
    out = os.path.join("public", "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"[build] ✓ Written → {os.path.abspath(out)}")
if __name__ == "__main__":
    build()
