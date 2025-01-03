CRM Система

Описание проекта

Краткое описание

CRM-система предназначена для оптимизации и автоматизации бизнес-процессов, связанных с привлечением клиентов, обработкой обращений и управлением контрактами. Это веб-приложение позволяет эффективно управлять услугами, рекламными кампаниями и данными о клиентах. Система предусматривает ролевой доступ, что обеспечивает прозрачность работы и разделение обязанностей.

Цели

Автоматизация работы с лидами и перевод их в активных клиентов.

Анализ эффективности рекламных кампаний.

Повышение уровня взаимодействия команд за счёт ролевого функционала.

Упрощённое управление услугами, контрактами и клиентами.

Основные функции

Управление ролями пользователей:

Администратор: управление пользователями, назначение ролей и прав.

Оператор: создание и ведение записей о потенциальных клиентах.

Маркетолог: управление услугами и рекламными кампаниями.

Менеджер: перевод потенциальных клиентов в активные, работа с контрактами.

Управление кампаниями и услугами:

Создание, редактирование и просмотр услуг и рекламных кампаний.

Работа с клиентами:

Учёт потенциальных клиентов и их перевод в активные.

Аналитика:

Отчёты об эффективности рекламных кампаний: привлечение лидов, конверсии и ROI.

Технологический стек

Backend: Django 5.1.3

База данных: PostgreSQL

Язык программирования: Python 3.10+

Качество кода: Pylint, Ruff

Дополнительно: mypy (проверка типов), pytest (юнит-тесты)

Установка и запуск

Предварительные требования

Python 3.10+

PostgreSQL (установлен и запущен)

Среда виртуального окружения (venv или virtualenv)

Шаги установки

Клонирование репозитория:

git clone <https://github.com/IvanFr1/CRM-django-system.git>

Создание и активация виртуального окружения:

python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

Установка зависимостей:

pip install -r requirements.txt

Настройка базы данных:

Создайте базу данных PostgreSQL для проекта.

Обновите настройки DATABASES в settings.py с учётом данных вашей базы.

Применение миграций:

python manage.py makemigrations
python manage.py migrate

Создание суперпользователя:

python manage.py createsuperuser

Запуск сервера разработки:

python manage.py runserver

Откройте приложение по адресу: http://127.0.0.1:8000/.

Проверка качества кода (опционально):

Установите и запустите Pylint и Ruff:

pylint <project-directory>
ruff <project-directory>

Функциональные возможности

Управление услугами

Создание: добавление новых услуг с указанием названия, описания и стоимости.

Редактирование: изменение данных об услугах.

Просмотр: отображение списка услуг и их детальной информации.

Удаление: удаление устаревших услуг.

Управление рекламными кампаниями

Атрибуты: название, услуга, канал продвижения, бюджет.

CRUD: создание, чтение, обновление и удаление записей.

Работа с потенциальными клиентами

Данные: имя, контактная информация, кампания, из которой узнали об услуге.

Действия: управление записями и перевод в активные клиенты.

Управление контрактами

Атрибуты: название, услуга, документ, период действия, сумма.

CRUD: удобное управление контрактами.

Активные клиенты

Создание из списка потенциальных клиентов при оформлении контракта.

Отслеживание данных и истории взаимодействий.

Аналитика кампаний

Метрики:

Количество лидов.

Конверсии в активных клиентов.

Доходы и расходы на рекламу.