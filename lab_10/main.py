
import typer
from lab7 import sum_nested_recursive, sum_nested_non_recursive
from lab8 import get_dog_fact_api
from lab9 import line_generator

app = typer.Typer()

@app.command()
def sum_nested(nested_list: str, recursive: bool = True):
    """Суммирует вложенные списки."""
    nested_list = eval(nested_list)  # Преобразуем строку в список
    if recursive:
        result = sum_nested_recursive(nested_list)
    else:
        result = sum_nested_non_recursive(nested_list)
    typer.echo(f"Сумма: {result}")

@app.command()
def fetch_dog_fact():
    """Получает факт о собаках из API."""
    dog_fact = get_dog_fact_api()
    if dog_fact:
        typer.echo(dog_fact)

@app.command()
def read_lines(file_path: str, max_length: int):
    """Читает строки из файла с ограничением по длине."""
    for short_line in line_generator(file_path, max_length):
        typer.echo(short_line)

if __name__ == "__main__":
    app()
