import requests
from data import BASE_URL


def create_order(order_body):
    """Отправляет POST-запрос для создания заказа. Возвращает объект ответа."""
    response = requests.post(
        f"{BASE_URL}/orders",
        json=order_body
    )
    return response


def get_order_by_track(track):
    """Отправляет GET-запрос для получения заказа по номеру трека. Возвращает объект ответа."""
    response = requests.get(
        f"{BASE_URL}/orders/track",
        params={"t": track}
    )
    return response
