# GET / account/register
import pyramid_handlers
import logging

from my_web_app.controllers.base_controller import BaseController
from my_web_app.services.account_service import AccountService
from my_web_app.viewmodels.profile_viewmodel import ProfileViewModel
from my_web_app.viewmodels.signin_viewmodel import SigninViewModel
from my_web_app.viewmodels.register_viewmodel import RegisterViewModel
from pyramid.httpexceptions import HTTPFound
import my_web_app.infrastructure.cookie_auth as cookie_auth
from my_web_app.services.profile_service import ProfilesService
log = logging.getLogger(__name__)


class AccountController(BaseController):
    @pyramid_handlers.action(renderer='templates/account/index.pt')
    def index(self):
        if not self.logged_in_user_id:
            print("Cannot view account page, must login")
            return HTTPFound(
                '/account/signin'
            )

        return {}

    @pyramid_handlers.action(renderer='templates/account/signin.pt', request_method='GET', name='signin')
    def signin_get(self):
        return SigninViewModel().to_dict()

    @pyramid_handlers.action(renderer='templates/account/signin.pt', request_method='POST', name='signin')
    def signin_post(self):
        vm = SigninViewModel()
        vm.from_dict(self.data_dict)

        # validation
        account = AccountService.get_authenticated_account(vm.email, vm.pw)
        if not account:
            vm.error = "Email address or password are incorrect."
            return vm.to_dict()
        # cookie-auth
        cookie_auth.set_auth(self.request, account.id)
        return HTTPFound(location='/account')
        # return self.redirect('/account')

    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='GET',
                             name='register')
    def register_get(self):
        # log.debug("Calling register via GET...")
        # study-guide: Introduce a view model
        vm = RegisterViewModel()
        return vm.to_dict()
        # study-guide: All the dictionary items should be stipulated from the beginning
        # return {
        #     'email': None,
        #     'password': None,
        #     'confirm_password': None,
        #     'error': None
        # }

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/account/register.pt',
                             request_method='POST',
                             name='register')
    def register_post(self):
        print("Calling register via POST...")
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)
        # study-guide: there's a POST-dictionary(multi-dict) on the request object
        # email = self.request.POST.get('email')
        # pw = self.request.POST.get('pw')
        # pw_confirmation = self.request.POST.get('pw_confirmation')

        # print("Calling register via POST: {}, {}, {}".format(email, pw, pw_confirmation))

        # Validation (whether it exists, password)
        vm.validate()
        if vm.error:
            return vm.to_dict()

        # Duplicate email error
        account = AccountService.find_account_by_email(vm.email)
        if account:
            vm.error = "An account with this email already exists. " \
                       "Please log-in instead."
            return vm.to_dict()
        # Create an account in DB

        accountdb = AccountService.create_account(vm.email, vm.pw)
        # print("Registered new user: " + accountdb.email)
        # <--Moved to RegisterVM-->
        # if pw != pw_confirmation:
        #     return {
        #         'email': email,
        #         'password': pw,
        #         'confirm_password': pw_confirmation,
        #         'error': "The password and confirmation don't match."
        #     }

        # Redirect
        print("Redirecting to account index page...")
        return HTTPFound(location='/account')

        # old version:
        # self.redirect('/account')

        # Send Welcome Email
        # print("Registered new user: " + accountdb.email)


    @pyramid_handlers.action(renderer='templates/account/profile/add_profile.pt',
                             request_method='GET',
                             name='add_profile')
    def add_profile_get(self):
        vm = ProfileViewModel()
        return vm.to_dict()


    @pyramid_handlers.action(renderer='templates/account/profile/add_profile.pt',
                             request_method='POST',
                             name='add_profile')
    def add_profile_post(self):
        vm = ProfileViewModel()
        vm.from_dict(self.request.POST)

        profiledb = ProfilesService.update_profile(vm.nickname, vm.interests, vm.comments)

        print("Redirecting to account index page...")
        return HTTPFound(location='/account')

    @pyramid_handlers.action(renderer='my_web_app:templates/account/profile/partials/show_add_form.pt',
                             request_method='GET',
                             name='cancel_add')
    def cancel_add_get(self):
        print("Cancel adding profile")
        vm = ProfileViewModel()
        return vm.to_dict()







    @pyramid_handlers.action()
    def logout(self):
        cookie_auth.logout(self.request)
        # self.redirect('/')
        return HTTPFound(location='/')


