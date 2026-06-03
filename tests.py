from data import order_body
from helpers import create_order, get_order_by_track


def test_get_order_by_track():
    # Шаг 1: создаём заказ и проверяем, что сервер вернул статус 201
    create_response = create_order(order_body)

    assert create_response.status_code == 201, (
        f"Ошибка создания заказа. "
        f"Ожидался код 201, получен {create_response.status_code}"
    )

    # Шаг 2: извлекаем номер трека из ответа на создание заказа
    track = create_response.json()["track"]

    # Шаг 3: получаем заказ по треку и проверяем, что сервер вернул статус 200
    get_order_response = get_order_by_track(track)

    assert get_order_response.status_code == 200, (
        f"Ошибка получения заказа. "
        f"Ожидался код 200, получен {get_order_response.status_code}"
    )


if __name__ == "__main__":
    test_get_order_by_track()
