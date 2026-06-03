# Абаев Евгений, 43-я когорта — Финальный проект. Инженер по тестированию плюс

# Базовый URL API — вводится пользователем при запуске
BASE_URL = input("Введите BASE_URL: ").rstrip("/") + "/api/v1"

# Тестовые данные для создания заказа
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
