import sqlalchemy
import sqlalchemy.orm
from my_web_app.data.modelbase import SqlAlchemyBase


class Track(SqlAlchemyBase):
    __tablename__ = 'Track'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    length = sqlalchemy.Column(sqlalchemy.Integer)
    audio_url = sqlalchemy.Column(sqlalchemy.String)
    video_url = sqlalchemy.Column(sqlalchemy.String)
    display_order = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    # Relationship
    # Pass the table Name and field
    album_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Album.id'))
    # Lazy loading mapping by sqlalchemy
    album = sqlalchemy.orm.relationship('Album', back_populates='tracks')
