"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

# import os
#
# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
#
# Base = None
# Session = None
import asyncio
import os
from datetime import datetime, timedelta
from typing import List, Optional
from pprint import pprint

from sqlalchemy import (
    Column,
    Text,
    Integer,
    String,
    DateTime,
    func,
    or_,
    ForeignKey,
)
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    name = Column(String(32), primary_key=True)
    username = Column(String(32), unique=True)
    email = Column(String(32), nullable=False, default='example_test@email.com')
    post_user_id = Column(Integer, ForeignKey('posts.user_id'))
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    post = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"(name={self.name}, "
            f"username={self.username!r}, email={self.email}, post_user_id={self.post_user_id}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    user_id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    user = relationship("User", back_populates="post")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(user_id={self.user_id}, "
            f"title={self.title!r}, body={self.body}, "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)


async def create_user_admin():
    session = Session()

    name = "Adam Sandler"
    username = "admin"
    # email = "adam_sandler@gmail.com"
    admin = User(name=name, username=username)
    print("new admin:", admin)

    session.add(admin)

    try:
        await session.commit()
    except IntegrityError as e:
        print("oops could not save user", admin, e)
        await session.rollback()
    else:
        print("created admin:", admin)

    await session.close()


# def create_and_edit_user():
#     session = Session()
#
#     username = "jonh"
#     user = User(username=username)
#     print("new user:", user)
#
#     session.add(user)
#     session.commit()
#
#     print("created user:", user)
#     print("oops! update username!")
#     user.username = "john"
#     session.commit()
#     print("updated user:", user)
#
#     session.close()
#
#
# def get_users():
#     session = Session()
#
#     users: List[User] = session.query(User).all()
#     print("users:")
#     pprint(users)
#
#     session.close()
#
#
# def get_admin():
#     session = Session()
#
#     user: User = session.query(User).filter_by(username="admin").one()
#     # user: Optional[User] = session.query(User).filter_by(username="admin").one_or_none()
#     print(user)
#
#     session.close()
#
#
# def get_user():
#     session = Session()
#
#     # user: User = session.query(User).filter_by(username="admin").one()
#     user: Optional[User] = session.query(User).filter_by(username="sam").one_or_none()
#     # if user is None
#     if not user:
#         print("could not find user!")
#     print(user)
#
#     session.close()
#
#
# def get_users_filtered():
#     session = Session()
#
#     users: List[User] = (
#         session
#             .query(User)
#             .filter(User.id > 2)
#             .all()
#     )
#     pprint(users)
#
#     session.close()
#
#
# def get_recent_users():
#     session = Session()
#
#     now = datetime.utcnow()
#
#     recent_time = now - timedelta(minutes=15)
#     print("recent_time")
#     print(recent_time)
#     users: List[User] = (
#         session
#             .query(User)
#             .filter_by(is_staff=False)
#             .filter(
#             User.created_at > recent_time,
#         )
#             .all()
#     )
#     print("recent users")
#     pprint(users)
#
#     session.close()
#
#
# def get_some_recent_users():
#     session = Session()
#
#     now = datetime.utcnow()
#
#     recent_time = now - timedelta(minutes=20)
#     print("recent_time")
#     print(recent_time)
#     users: List[User] = (
#         session
#             .query(User)
#             # .filter_by(is_staff=False)
#             .filter(
#             or_(
#                 User.created_at > recent_time,
#                 # User.is_staff == True,
#                 User.is_staff.is_(True),
#             ),
#
#         )
#             .all()
#     )
#     print("some recent users")
#     pprint(users)
#
#     session.close()
#
#
# def get_user_by_pk():
#     session = Session()
#
#     u1 = session.query(User).get(1)
#     print("u1", u1)
#
#     session.close()




async def async_main():
    await create_user_admin()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
