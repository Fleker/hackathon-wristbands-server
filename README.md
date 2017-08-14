# Hackathon Wristband Server
Originally used in ProfHacks 2016, is now used as a reference for other hackathons
and organizations.

## Original Setup
The original website was hosted on Heroku using Django. This includes the 2
add-ons:
* Heroku Postgres
* SendGrid

## Environment Variables
1. auth_token
    * Used for communication with the Android app sensor
    * (CURRENTLY SET STATICALLY IN SERVER)
2. DATABASE_NAME
    * The name of the database used by Herkou (commonly Herkou Postgres)
    * Generated by Heroku
3. DATABASE_PASSWORD
    * Password for database used by Heroku
    * Generated by Heroku
4. DATABASE_PORT
    * Port used by database for communication
    * *Default for PostgreSQL: 5432*
5. DATABASE_USER
    * Username for access to Heroku database with DATABASE_PASSWORD.
    * Generated by Heroku
6. DATABASE_URL
    * URL for Database
7. DATABASE_URL *Alternative*
    * A filled Database URL can replace all other Database Environment Variables
    * Example: postgres://*username*:*pass*@ec1-11-111-111-111.compute-1.amazonaws.com:5432/*database_name*
