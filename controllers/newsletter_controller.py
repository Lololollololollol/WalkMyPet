import pyramid_handlers
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response

from my_web_app.controllers.base_controller import BaseController
from my_web_app.services.mailinglist_service import MailingListService


class NewsletterController(BaseController):
    # POST /newsletter/add_subscriber
    @pyramid_handlers.action(request_method='POST')
    def add_subscriber(self):
        email = self.data_dict.get('email')

        if not email:
            return HTTPFound(location='/newsletter/failed')
            # old version:
            # self.redirect('/newsletter/failed')

        if MailingListService.add_subscriber(email):
            # Possibly version update
            return HTTPFound(location='/newsletter/subscribed')
            # old version:
            # self.redirect('/newsletter/subscribed')

        return HTTPFound(location='/newsletter/failed')
        # old version:
        # self.redirect('/newsletter/failed')

    @pyramid_handlers.action(renderer='templates/newsletter/subscribed.pt')
    def subscribed(self):
        return {}

    @pyramid_handlers.action(renderer='templates/newsletter/failed.pt')
    def failed(self):
        return {}
