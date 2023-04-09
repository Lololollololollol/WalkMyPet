from sqlalchemy.orm import joinedload

from my_web_app.data.dbsession import DbSessionFactory
from my_web_app.data.videos import Video
from my_web_app.viewmodels.videos_viewmodel import VideosViewModel
import sqlalchemy


class VideoService:
    @staticmethod
    def get_videos():
        session = DbSessionFactory.create_session()

        videos = session.query(Video) \
            .all()

        return videos

    @classmethod
    def add_post(cls, vm: VideosViewModel):
        session = DbSessionFactory.create_session()

        video = Video(video_title=vm.video_title, video_id=vm.video_id, video_author=vm.video_author,
                      img_url=vm.img_url, view_count=vm.view_count)

        session.add(video)

        # for idx, title in enumerate(track_titles):
        #     track = Track(name=title, length=60, display_order=idx+1)
        #     album.tracks.append(track)

        session.commit()
        return video

    @classmethod
    def get_search_results(cls, search_text):
        session = DbSessionFactory.create_session()

        # stmt = select(sometable). \
        #     where(sometable.c.column.ilike("%foobar%"))
        results = session.query(Video).filter(Video.video_title.ilike(f'%{search_text}%'))
        for video in results:
            print(video)
        return results

