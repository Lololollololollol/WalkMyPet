import sqlalchemy
import sqlalchemy.orm
from my_web_app.data.modelbase import SqlAlchemyBase


class Interest(SqlAlchemyBase):
    __tablename__ = 'Interest'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    activity_type = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    # hiking = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # swimming = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # cycling = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # scuba_diving = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # free_diving = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # skiing = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # skateboarding = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # cave_exploring = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # climbing = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # sailing = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # surfing = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # kite_surfing = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # mapping = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    # tennis = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    skill_set = sqlalchemy.Column(sqlalchemy.String)

    #     freediving_instructor = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    #     cave_rescuer = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Account.id'))
    account = sqlalchemy.orm.relationship('Account', back_populates='interests')
