def count_code_lines(file_path):
    code_lines = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            # Ignorovat prázdné řádky a řádky začínající komentářem
            if stripped_line and not stripped_line.startswith("#"):
                code_lines += 1
    return code_lines

file_path = 'Main.py'
print(f'Počet řádků s kódem v souboru {file_path}: {count_code_lines(file_path)}')