run docker compose file to create database.
> docker-compose up -d --build

if u need to change current database schema create migration file
> alembic revision --autogenerate -m "some_text"

to apply migration files
> alembic upgrade head

to start scraping run bot scripts consequently 
> python scraper_full.py
