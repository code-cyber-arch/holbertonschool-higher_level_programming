#!/usr/bin/python3
"""
Module for City class and Base instance.

Defines:
    - Base: SQLAlchemy declarative base
    - City: ORM class for 'cities' table
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city with id and name attributes.

    Attributes:
        __tablename__ (str): The table name
        id (Column): The city's id, primary key
        name (Column): The city's name
    """
    __tablename__ = 'cities'
    id = Column(Integer,
                unique=True,
                autoincrement=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
