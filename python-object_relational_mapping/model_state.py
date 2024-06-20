#!/usr/bin/python3
"""
Module for State class and Base instance.

Defines:
    - Base: SQLAlchemy declarative base
    - State: ORM class for 'states' table
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state with id and name attributes.

    Attributes:
        __tablename__ (str): The table name
        id (Column): The state's id, primary key
        name (Column): The state's name
    """
    __tablename__ = 'states'
    id = Column(Integer(11),
                unique=True,
                autoincrement=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
