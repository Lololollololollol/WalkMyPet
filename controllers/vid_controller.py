import pyramid_handlers
from pyramid.httpexceptions import HTTPFound
import logging

log = logging.getLogger(__name__)

from my_web_app.controllers.base_controller import BaseController
from my_web_app.data.dbsession import DbSessionFactory
from my_web_app.data.videos import Video
from my_web_app.services.videos_service import VideoService
from my_web_app.viewmodels.videos_viewmodel import VideosViewModel
from my_web_app.viewmodels.search_viewmodel import SearchViewModel


class VideosController(BaseController):

    @pyramid_handlers.action(renderer='my_web_app:templates/videos/index.pt',
                             request_method='GET')
    def index(self):
        # data / service access
        all_videos = VideoService.get_videos()

        # return the model (return the dictionary)
        return {'videos': all_videos,
                'mytitle': "Group One"}

    @pyramid_handlers.action(renderer='my_web_app:templates/videos/partials/add_video_form.pt',
                             request_method='GET',
                             name='add_video')
    def add_video_get(self):
        vm = VideosViewModel()
        print("GET videos")
        return vm.to_dict()

    @pyramid_handlers.action(renderer='my_web_app:templates/videos/partials/show_add_form.pt',
                             request_method='GET',
                             name='cancel_add')
    def cancel_add_get(self):
        print("Cancel adding videos")
        vm = VideosViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer='my_web_app:templates/videos/partials/add_video_form.pt',
                             request_method='POST',
                             name='add_video')
    def add_video_post(self):
        vm = VideosViewModel()
        vm.from_dict(self.request.POST)

        # insert videos to db
        new_video = VideoService.add_post(vm)

        # log new videos
        print("Added {} to Videos".format(new_video))

        print("Redirecting to videos index page...")
        return HTTPFound(location='/videos/index')

    # Search Videos by Active Search
    @pyramid_handlers.action(renderer='my_web_app:templates/videos/search.pt',
                             request_method='GET',
                             name='search')
    def search_get(self):
        vm = SearchViewModel()

        return vm.to_dict()

    @pyramid_handlers.action(renderer='my_web_app:templates/videos/partials/search_results.pt',
                             request_method='POST',
                             name='search')
    def search_post(self):
        # <complicated ver1>
        vm = SearchViewModel()
        vm.from_dict(self.request.POST)
        results = VideoService.get_search_results(vm.search_text)

        # <simple vers2>
        # log.debug('in videosController.index')
        # results = VideoService.get_search_results(self.data_dict['search_text'])

        return {'search_results': results}


