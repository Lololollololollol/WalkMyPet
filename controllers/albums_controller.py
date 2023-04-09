import pyramid_handlers
import logging

from my_web_app.controllers.base_controller import BaseController
from my_web_app.services.albums_service import AlbumsService

log = logging.getLogger(__name__)


class AlbumsController(BaseController):
    @pyramid_handlers.action(renderer='my_web_app:templates/albums/index.pt')
    def index(self):
        # data / service access
        all_albums = AlbumsService.get_albums()
        user = self.logged_in_user

        log.debug('in AlbumsContoller.index')

        # return the model (return the dictionary)
        return {'albums': all_albums,
                'mytitle': "Dan's title"}

