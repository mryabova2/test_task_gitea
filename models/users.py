import dataclasses


@dataclasses.dataclass
class User:
    name: str
    email: str
    password: str


test_user = User(
    name='SantaClause',
    email='sanatas@mail.com',
    password='Hohohoho'
)
