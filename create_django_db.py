from decouple import config
import subprocess

DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASSWORD = config("DB_PASSWORD")
POSTGRES_USER = config("DB_POSTGRES_USER")


def psql(cmd, db=None):
    base = ["sudo", "-u", POSTGRES_USER, "psql"]
    if db:
        base += ["-d", db]
    base += ["-c", cmd]
    subprocess.run(base, check=True)


print("Создание базы данных...")

psql(f"CREATE DATABASE {DB_NAME} WITH ENCODING 'UTF8' TEMPLATE template0;")
psql(f"CREATE USER {DB_USER} WITH PASSWORD '{DB_PASSWORD}';")
psql(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};")

psql(f"GRANT ALL ON SCHEMA public TO {DB_USER};", DB_NAME)
psql(f"GRANT CREATE ON SCHEMA public TO {DB_USER};", DB_NAME)
psql(
    f"ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO {DB_USER};",
    DB_NAME,
)
psql(
    f"ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO {DB_USER};",
    DB_NAME,
)

psql("CREATE EXTENSION IF NOT EXISTS unaccent;", DB_NAME)

print("Готово!")
print(f"DATABASE_URL=postgresql://{DB_USER}:{DB_PASSWORD}@localhost:5432/{DB_NAME}")