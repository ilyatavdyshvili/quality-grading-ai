# Quality Grading AI

## Структура проекта

- **src/domain**: Сущности и интерфейсы (ядро системы)
- **src/application**: Бизнес-логика (Use Cases)
- **src/infrastructure**: Реализация интерфейсов (Mock-модели)
- **src/presentation**: Точка входа (FastAPI эндпоинты)

## Запуск

```bash
# Установка зависимостей
poetry install

# Запуск API
poetry run uvicorn src.presentation.api:app --reload

# Запуск тестов
poetry run pytest

## Standard-проверка:

curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 5.0, "density": 0.95, "alcohol_content": 10.0}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 4.5, "density": 0.9, "alcohol_content": 10.5}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 4.8, "density": 0.97, "alcohol_content": 11.0}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 5.2, "density": 0.94, "alcohol_content": 10.8}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 6.0, "density": 0.92, "alcohol_content": 10.5}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 4.9, "density": 0.95, "alcohol_content": 10.2}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 5.0, "density": 0.98, "alcohol_content": 11.0}'

## Premium-проверка:

curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 8.0, "density": 1.05, "alcohol_content": 15.0}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 7.5, "density": 1.02, "alcohol_content": 14.0}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 9.0, "density": 1.08, "alcohol_content": 16.0}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 8.5, "density": 1.0, "alcohol_content": 15.5}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 7.8, "density": 1.03, "alcohol_content": 14.5}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 8.2, "density": 1.06, "alcohol_content": 15.2}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 9.1, "density": 1.1, "alcohol_content": 16.5}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 7.9, "density": 1.04, "alcohol_content": 14.8}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 8.3, "density": 1.05, "alcohol_content": 15.0}'
curl -X POST http://127.0.0.1:8000/evaluate -H "Content-Type: application/json" -d '{"acidity": 8.7, "density": 1.07, "alcohol_content": 15.8}'
