from sqlalchemy.orm import joinedload
import logging

from my_web_app.data.account import Account
from my_web_app.data.dbsession import DbSessionFactory
from my_web_app.data.interest import Interest
from my_web_app.viewmodels.profile_viewmodel import ProfileViewModel


class ProfilesService:
    @staticmethod
    def get_profile():
        session = DbSessionFactory.create_session()

        #todo: get the profile from DB.
        #performance:joinedload(load 
        profiles = session.query(Account)\
            .options(joinedload('interests'))\
            .filter(Account.is_active)\
            .order_by(Account.interest.desc())\
            .all()

        return profiles
    #
    #
    # @classmethod
    # def update_profile(cls, profile_image=None, nickname, interests, comments, interest_set:[]):
    #
    #     session = DbSessionFactory.create_session()
    #
    #     account = Account(profile_image=profile_image, nickname=nickname, interests=interests, comments=comments, is_active=True)
    #     interest = Interest()
    #     session.add(account)
    #     logging.debug('in profile_service for adding interests')
    #
    #     for idx, activity in enumerate(interest_set):
    #         interest = Interest(activity_type=activity)
    #         account.interest.append(interest)
    #
    #     session.commit()
    #     return account
    #
    #




