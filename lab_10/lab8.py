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
