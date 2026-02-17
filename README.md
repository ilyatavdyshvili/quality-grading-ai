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
