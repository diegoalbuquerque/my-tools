import site
import sys
import os
from pathlib import Path

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

if sys.platform == "win32":
    os.system('color')

def scan_pth_files():
    # Pega todos os caminhos onde o Python busca por pacotes (site-packages)
    # Isso inclui o global e o do usuário (se houver)
    paths_to_check = site.getsitepackages()
    if site.ENABLE_USER_SITE:
        paths_to_check.append(site.getusersitepackages())

    print(f"{GREEN}{BOLD}PATHS TO CHECK:{RESET} {paths_to_check}\n")
    
    found_any = False

    for folder in paths_to_check:
        folder_path = Path(folder)
        if not folder_path.exists():
            continue

        pth_files = list(folder_path.glob("*.pth"))
        
        if pth_files:
            found_any = True
            print(f"{GREEN}{BOLD}[+] PATH:{RESET} {folder}")
            for pth in pth_files:
                print(f"\n{CYAN}{BOLD}[+] FILE:{RESET} {pth.name}")
                try:
                    content = pth.read_text().strip()
                    lines = content.splitlines()
                    for line in lines:
                        if line.startswith("import ") or line.startswith("import\t"):
                            print(f"{RED}{BOLD}[ALERT] CODE FOUND:{RESET} {line}")
                        else:
                            print(f"    - {line}")
                except Exception as e:
                    print(f"{RED}{BOLD}[!] FILE READ ERROR:{RESET} {e}")
               

    if not found_any:
        print("{GREEN}{BOLD}[!] .pth not found{RESET}")

if __name__ == "__main__":
    scan_pth_files()
