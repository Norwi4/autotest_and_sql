# Финальный проект — Инженер по тестированию плюс

Абаев Евгений, 43-я когорта.

## Описание

Проект содержит SQL-запросы для проверки данных в базе и автотест API сервиса аренды самокатов.

## Структура

```
tests/
├── script.sql   — SQL-запросы к базе данных
├── tests.py     — автотест API
├── .gitignore
└── README.MD
```

## Работа с базой данных

Подключение:

```bash
psql -U morty -d scooter_rent
```

Пароль: `smith`

Файл `script.sql` содержит два запроса:

**Запрос 1** — логины курьеров и количество их заказов в статусе «В доставке»:

```sql
select c.login, count(o.id) as orders_count
from "Couriers" c
join "Orders" o on c.id = o."courierId"
where o."inDelivery" = true
group by c.login;
```

**Запрос 2** — трекеры заказов и их статусы (`2` — завершён, `-1` — отменён, `1` — в доставке, `0` — остальные):

```sql
select track, case
    when finished = true then 2
    when cancelled = true then -1
    when "inDelivery" = true then 1
    else 0
end as status
from "Orders";
```

## Автотест API

### Требования

```bash
pip install requests
```

### Запуск

```bash
python tests.py
```

При запуске скрипт запросит `BASE_URL` — базовый адрес сервера (например, `http://localhost:8080`).

### Что проверяет тест

1. Отправляет POST-запрос на создание заказа.
2. Сохраняет номер трека из ответа.
3. Отправляет GET-запрос на получение заказа по треку.
4. Проверяет, что код ответа равен `200`.

### Логи

Логи бэкенда: `/var/www/backend/logs/error.log`
