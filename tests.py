import requests
# Абаев Евгений, 43-я когорта — Финальный проект. Инженер по тестированию плюс
BASE_URL = input("Введите BASE_URL: ").rstrip("/") + "/api/v1"


order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-05-31",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}


def test_get_order_by_track():
    print("\n===== СТАРТ ТЕСТА =====")

    print("\n[ШАГ 1] Создание заказа...")
    print("POST:", f"{BASE_URL}/orders")
    print("Тело запроса:", order_body)

    create_response = requests.post(
        f"{BASE_URL}/orders",
        json=order_body
    )

    print("Статус-код ответа:", create_response.status_code)
    print("Ответ сервера:", create_response.json())

    assert create_response.status_code == 201, (
        f"Ошибка создания заказа. "
        f"Ожидался код 201, получен {create_response.status_code}"
    )

    track = create_response.json()["track"]

    print("\n[ШАГ 2] Сохранение track заказа...")
    print("TRACK:", track)

    print("\n[ШАГ 3] Получение заказа по track...")
    print("GET:", f"{BASE_URL}/orders/track?t={track}")

    get_order_response = requests.get(
        f"{BASE_URL}/orders/track",
        params={"t": track}
    )

    print("Статус-код ответа:", get_order_response.status_code)
    print("Ответ сервера:", get_order_response.json())

    print("\n[ШАГ 4] Проверка статус-кода...")

    assert get_order_response.status_code == 200, (
        f"Ошибка получения заказа. "
        f"Ожидался код 200, получен {get_order_response.status_code}"
    )

    print("\n===== ТЕСТ УСПЕШНО ПРОЙДЕН =====")


if __name__ == "__main__":
    test_get_order_by_track()