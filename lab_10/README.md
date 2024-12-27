# Отчёт

## lab7

```python
def sum_nested_recursive(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):
            total += sum_nested_recursive(element)
        else:
            total += element
    return total


result = sum_nested_recursive([1, [2, [3, 4, [5]]]])
print(result)

def sum_nested_non_recursive(nested_list):
    total = 0
    stack = [nested_list]

    while stack:
        current_list = stack.pop()
        for element in current_list:
            if isinstance(element, list):
                stack.append(element)
            else:
                total += element

    return total

result = sum_nested_non_recursive([1, [2, [3, 4, [5]]]])
print(result)
```

## lab8

```python
import requests

def api_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Произошла ошибка при запросе: {e}")
            return None
    return wrapper

def get_dog_fact_api():
    @api_decorator
    def fetch_dog_fact():
        url = "https://dogapi.dog/api/v2/facts"
        return requests.get(url)

    return fetch_dog_fact()

if __name__ == "__main__":
    dog_fact = get_dog_fact_api()
    if dog_fact:
        print(dog_fact)
```

## lab9

```python
def line_generator(file_path, max_length):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('n')
            if len(line) > max_length:
                yield line[:max_length]
            else:
                yield line

if __name__ == "__main__":
    file_path = 'example.txt'
    max_length = 10

    for short_line in line_generator(file_path, max_length):
        print(short_line)
```

## main.py

```python
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
```

## Запуск

 - python main.py sum-nested "[1, [2, [3, 4, [5]]]]" --recursive
 - python main.py fetch-dog-fact
 - python main.py read-lines "example.txt" --max-length 10

### Запуск осуществляется через командную строку
