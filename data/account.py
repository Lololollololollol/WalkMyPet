import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy_imageattach.entity import Image, image_attachment
import sqlalchemy.orm
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy import Column, String, Boolean, Date

from my_web_app.data.modelbase import SqlAlchemyBase


class Account(SqlAlchemyBase):
    __tablename__ = 'Account'

    id = Column(String, primary_key=True,
                default=lambda: str(uuid.uuid4()).replace('-', ''))
    email = Column(String, index=True, unique=True, nullable=False)
    # Do Not Put the Plain Password in your database
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    created = Column(Date, default=datetime.datetime.now)
    email_confirmed = Column(Boolean, nullable=False, default=False)
    is_super_user = Column(Boolean, nullable=False, default=False)

    #Profile(optional)
    # profile_image = image_attachment(ProfilePicture)
    nickname = Column(String, index=True, unique=True)
    comments = Column(String, index=True)
    is_active = Column(Boolean, index=True)

    #Relationship (Account & Interests)
    interests = sqlalchemy.orm.relationship('Interest', back_populates='account', cascade='all')


    #Todo: create the relationship with Account(tb)
# class ProfilePicture(SqlAlchemyBase, Image):
#     __tablename__ = 'Profile_Picture'
#     account_id = Column(String, Foreignkey=('account.id'), primary_key=True)
#     accunt = sqlalchemy.relationship('Account')