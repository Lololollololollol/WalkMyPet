import pyramid_handlers
from my_web_app.infrastructure.supressor import suppress
from my_web_app.controllers.base_controller import BaseController
import logging

log = logging.getLogger(__name__)


class HomeController(BaseController):
    alternate_mode = False

    @pyramid_handlers.action(renderer='my_web_app:templates/home/index.pt')
    def index(self):
        log.info('In home view.')
        return {
            'value': 'HOME',
        }

    @pyramid_handlers.action(renderer='my_web_app:templates/home/about.pt')
    def about(self):
        return {
            'value': 'ABOUT',
        }

    @pyramid_handlers.action(renderer='my_web_app:templates/home/contact.pt')
    def contact(self):
        return {
            'value': 'CONTACT'
        }

    @pyramid_handlers.action(renderer='templates/home/inviteus.pt')
    def inviteus(self):
        return {
            'value': 'invite_us'
        }

    @pyramid_handlers.action(renderer='templates/home/image_credits.pt')
    def image_credits(self):
        return {}

    @suppress
    def dont_expose_as_web_action(self):
        print("Called dont_expose_web_action, what happened?")

    # toggle its mode from True to False, False to True
    def alternate_row_style(self):
        alt = self.alternate_mode
        self.alternate_mode = not self.alternate_mode
        if alt:
            return "alternate"
        else:
            return ""
