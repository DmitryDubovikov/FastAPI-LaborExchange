from repositories.users import UserRepository
from db.base import database


def get_user_repository() -> UserRepository:
    return UserRepository(database)

# async def get_current_user(
#     users: UserRepository = Depends(get_user_repository),
#     token: str = Depends(JWTBearer()),
# ) -> User:
#     return 1
