import sqlalchemy
import sqlalchemy.orm


from my_web_app.data.modelbase import SqlAlchemyBase


class Video(SqlAlchemyBase):
    __tablename__ = 'Video'

    video_id = sqlalchemy.Column(sqlalchemy.String, primary_key=True, unique=True)
    video_title = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    img_url = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=False)
    view_count = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    video_author = sqlalchemy.Column(sqlalchemy.String, index=True)