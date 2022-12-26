from starlette.config import Config

config = Config(".env")

# DATABASE_URL = config("LE_DATABASE_URL", cast=str, default="")
# DATABASE_URL = config("postgresql://root:root@localhost:32700/labor_exchange", cast=str, default="")

DATABASE_URL = "postgresql://root:root@localhost:32700/labor_exchange"

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
SECRET_KEY = config("LE_SECRET_KEY", cast=str, default="2b2d197649061838c0c381612cb117d5f562ff181f2ed68c7847471af22f83ce")
