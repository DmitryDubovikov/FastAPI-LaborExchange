from starlette.config import Config

config = Config(".env")

# DATABASE_URL = config("LE_DATABASE_URL", cast=str, default="")
# DATABASE_URL = config("postgresql://root:root@localhost:32700/labor_exchange", cast=str, default="")

DATABASE_URL = "postgresql://root:root@localhost:32700/labor_exchange"

