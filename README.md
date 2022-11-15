    Менеджер учёта расходов"
API in project:

    -api_auth/user_list/ # list of users
    -api_auth/register/ # user registgration
    -api_auth/token/ # get access token
    -api_auth/token/refresh/ # refresh access token

    -api_journal/category/ # category of notes
    -api_journal/category/<int> # for one category detail
    
    -api_journal/income/ # income of notes
    -api_journal/income/<int> # for one income detail

    -api_journal/expense/ # expense of notes
    -api_journal/expense/<int> # for one expense detail
    
    -api_journal/user_profile/ # user page
    


Для настройки базы данных необходимо войти в контейнер "manager_db" командой:

$ docker exec -it [id image] bash

После входа в консоль контейнера команда для входа в консоль постгрес:

$ psql -U postgres -d postgres

Создать базу данных:

$ CREATE DATABASE manager_db;

Создать пользователя:

$ CREATE USER manager_web WITH LOGIN PASSWORD '1111';

Добавить права доступа пользователя к бд:

$ GRANT ALL PRIVILEGES ON DATABASE manager_db TO manager_web;

$ alter user manager_web superuser createdb;
