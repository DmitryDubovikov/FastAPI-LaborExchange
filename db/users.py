import sqlalchemy
from .base import metadata


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True), 
    sqlalchemy.Column('email', sqlalchemy.String, primary_key=True, unique=True),
    sqlalchemy.Column('name', sqlalchemy.String),
    sqlalchemy.Column('hashed_password', sqlalchemy.String),
    sqlalchemy.Column('is_company', sqlalchemy.Boolean)
)



# from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "user"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, primary_key=True, index=True)
#     name = Column(String)
#     hashed_password = Column(String)
#     is_company = Column(Boolean)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())
#     time_updated = Column(DateTime(timezone=True), onupdate=func.now())

