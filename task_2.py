def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        cats = [
            {"id": parts[0], "name": parts[1], "age": parts[2]}
            for line in lines
            if len(parts := line.strip().split(',')) == 3
        ]
        return cats

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
