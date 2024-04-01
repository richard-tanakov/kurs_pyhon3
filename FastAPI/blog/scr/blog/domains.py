from dataclasses import dataclass


@dataclass
class User:
    """ Обычный пользователь."""
    id: str


@dataclass
class Admin:

    username: str
    password: str


@dataclass
class Articles:
    """ Сущность статьи """
    id: str
    title: str
    content: str
