import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_tree(path: Path, prefix: str = ""):
    try:
        entries = sorted(path.iterdir())
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Доступ заборонено]{Style.RESET_ALL}")
        return

    for i, item in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")

        if item.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}{Style.BRIGHT}{item.name}/{Style.RESET_ALL}")
            print_directory_tree(item, next_prefix)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Використання: python task_3.py <шлях_до_директорії>")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях не існує.{Style.RESET_ALL}")
        sys.exit(1)

    if not directory_path.is_dir():
        print(f"{Fore.RED}Помилка: Вказаний шлях не є директорією.{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.YELLOW}{Style.BRIGHT}{directory_path.resolve()}{Style.RESET_ALL}")
    print_directory_tree(directory_path)

if __name__ == "__main__":
    main()
