from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from extensions import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
