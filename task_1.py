def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salaries.append(int(parts[1]))

            if not salaries:
                return 0, 0

            total = sum(salaries)
            average = total // len(salaries)
            return total, average

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return 0, 0

if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
