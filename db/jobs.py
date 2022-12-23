import sqlalchemy
from .base import metadata


jobs = sqlalchemy.Table(
    'jobs',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True), 
    sqlalchemy.Column('title', sqlalchemy.String),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('is_active', sqlalchemy.Boolean),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False)
)


# from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# Base = declarative_base()

# class Job(Base):
#     __tablename__ = "job"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     is_active = Column(Boolean)
#     salary_from = Column(Integer)
#     salary_to = Column(Integer)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())
#     time_updated = Column(DateTime(timezone=True), onupdate=func.now())
#     user_id = Column(Integer, ForeignKey("user.id"))
