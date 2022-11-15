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
    


To configure the database, you need to log into the "manager_db" container with the command:

$ docker exec is [image id] bash

After logging in to the container console, the command to log in to the postgres console:

$ psql -U postgres -d postgres

Create a database:

$ CREATE DATABASE manager_db;

Create a user:

$ CREATE manager_web USER WITH LOGIN PASSWORD '1111';

Add user access rights to the database:

$ GRANT ALL PRIVILEGES FOR manager_db DATABASE TO manager_web;

$ ALTER USER eduplatform_web superuser createdb;