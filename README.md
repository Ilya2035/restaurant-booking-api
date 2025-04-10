# 🚀 RESTAURANT BOOKING API

Небольшое приложение для работы с созданием столов и их резервации, в проекте продумана логика взаимодействия между столиками и временем резервации чтобы упростить работу в ресторане

---

## 🛠 Стек технологий

- **FastAPI** — асинхронный веб-фреймворк
- **SQLAlchemy** — ORM для работы с базой данных  
- **PostgreSQL (asyncpg)** — асинхронная БД  
- **Pydantic** — валидация и сериализация данных
- **Alembic** — создание миграций (авоматическое обновление после изменений моделкй)

---

## 📦 Установка и запуск

```bash
# Клонировать репозиторий
git clone https://github.com/Ilya2035/restaurant-booking-api.git
cd restaurant-booking-api

# Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate        # для Linux/macOS
venv\Scripts\activate           # для Windows

# Установить зависимости
pip install -r requirements.txt

# Создать .env и указать параметры для запуска бд
echo "DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/restaurant_db"" > .env
# Задайте свои параметры

# Запустить сборку контейнеров
docker-compose up --build

```
После проделанных действий у вас будут запущены контейнеры, с которыми вы сможете взаимодействовать

---

## 📡 Примеры API-запросов

Для наглядности перейдите по http://localhost:8000/docs

### ▶️ POST `/tables/`
Создаёт новый столик в ресторане.

**Request body:**
```commandline
{
  "name": "Table 1",
  "seats": 4,
  "location": "у окна"
}
```
**Responses:**

201	Successful Response
```commandline

{
  "name": "Table 1",
  "seats": 4,
  "location": "у окна",
  "id": 5
}

```


---

## 📁 Структура проекта

```
├── main.py # приложение и подключения роутеров
├── api/
│   ├── reservation.py # endpoints резервации
│   ├── table.py # endpoints столов
│   └── __init__.py
├── core/
│   ├── config.py # настройки проекта
│   └── __init__.py
├── crud/
│   ├── transactions.py # транзакции в бд
│   └── __init__.py
├── db/ # файлы создания бд и сессий к ней
│   ├── dependency.py
│   ├── engine.py
│   ├── init.py
│   ├── session.py
│   └── __init__.py
├── models/ 
│   ├── orm_models.py # ORM модели SQLAlchemy
│   └── __init__.py
├── schemas/
│   ├── pydantic_models.py # pydantic модели для работы с типизацией 
│   └── __init__.py
├── utils/
│   ├── http_exceptions.py # универсальное логирование для endpoints
│   └── __init__.py
└── __pycache__/
```

---

## ✅ Возможности

- Создание и удаление столиков
- Создание, получение и удаление броней
- Валидация занятости столика (нет пересечений по времени)


---

## 📬 Обратная связь

Если возникнут вопросы или предложения — fyrno2049@gmail.com
