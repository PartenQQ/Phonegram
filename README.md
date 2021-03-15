# Osinteagle

Агрегатор OSINT Telegram ботов.

## Установка

1. `git clone https://github.com/Lpshkn/Osinteagle osinteagle`
2. `cd osinteagle`
3. `python3 -m venv venv && . ./venv/bin/activate`
4. `python3 -m pip install -r requirements.txt`

## Подготовка

Для использования необходимо получить API_ID и API_HASH с помощью аккаунта телеграма:

1. Переходим по [ссылке](https://my.telegram.org/) и входим в аккаунт телеграм
2. Далее в появившемся меню выбираем **API tools**
3. Создаем новое приложение: вводим только полное название и сокращенное (остальное не требуется)
4. Получаем API_ID и API_HASH

Если API_ID и API_HASH уже имеются или получены на предыдущем шаге, записываем их в файл `config/session.cfg` в директории проекта.

## Использование

Существует 2 режима работы программы: **режим настройки** и **режим запроса**:
* Режим настройки: `python main.py setting -c <конфиг файл>` - запускает в интерактивном режиме программу, чтобы 
авторизоваться в аккаунтах и получить от них session_string, необходимый для работы в режиме запроса
* Режим запроса: `python main.py request <номер телефона> -c <конфиг файл> -b <настройки ботов> -o <выходной файл>` - 
запускает запрос к перечисленным в файле, переданном с опцией `-b`, ботам и записывает агрегированный результат в 
  файл `-o` (по-умолчанию, stdout)
  
**Примечание**: параметры `-c` и `-b` не являются обязательными, и по-умолчанию принимают значения `config/bots.json`
для опции `-b` и `config/session.cfg` для опции `-c`.