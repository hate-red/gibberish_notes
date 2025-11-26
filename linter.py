import re
from pathlib import Path


# Путь до директории, в которй лежит линтер
root_dir = Path(__file__).parent

git_ingore = Path(root_dir / '.gitignore').read_text()

# Собираем все папки, кроме тех, что в .gitignore
folders = [
    path.name for path in root_dir.iterdir()
    if path.is_dir() and path.name not in git_ingore
]

# Ищем строки вида ==*какой-то текст*==
# "==" с двух сторон для выделения цветом, "*" для курсива
highlighting_pattern = r'==\*.+?\*=='


def format_file(file_path: Path, pattern: str) -> None:
    # Early quit
    if not path.is_file():
        return

    file_contents = Path(path).read_text()
    matches = re.findall(highlighting_pattern, file_contents)
    
    for match in matches:
        # Удаляем только выделение, курсив сохраняем
        file_contents = file_contents.replace(match, match[2:-2])
    
    Path(path).write_text(file_contents)


if __name__ == '__main__':
    for folder in folders:
        for path in Path(folder).iterdir():
            format_file(path, highlighting_pattern)
