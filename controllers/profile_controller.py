import pyramid_handlers
import logging

from my_web_app.controllers.base_controller import BaseController
from my_web_app.services.profile_service import ProfilesService
from my_web_app.viewmodels.profile_viewmodel import ProfileViewModel

log = logging.getLogger(__name__)


class ProfileController(BaseController):
    @pyramid_handlers.action(renderer='my_web_app:templates/profile/index.pt')
    def index(self):
        # data / service access
        all_profiles = ProfilesService.get_profiles()
        user = self.logged_in_user

        log.debug('in ProfileController.index')

        # return the model (return the dictionary)
        return {'profiles': all_profiles}


    @pyramid_handlers.action(renderer='my_web_app:templates/profile/partials/add_profile.pt', name='update_profile')
    def update_profile_get(self):
        pass
        #todo: query the profile status by the sign-in account

    @pyramid_handlers.action(renderer='my_web_app:templates/profile/partials/add_profile.pt', name='update_profile')
    def update_profile_post(self):
        pass


