from my_web_app.viewmodels.viewmodelbase import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self):
        # returning a dictionary with email as a key
        self.email = None
        self.pw = None
        self.pw_confirmation = None
        self.error = None

        # Profile
        # self.profile_image = None
        # self.nickname = None
        # self.interests = None
        # self.comments = None
        # self.is_active = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.pw = data_dict.get('pw')
        self.pw_confirmation = data_dict.get('pw_confirmation')
        # Profile
        # self.profile_image = data_dict.get('profile_image')
        # self.nickname = data_dict.get('nickname')
        # self.interests = data_dict.get('interests')
        # self.comments = data_dict.get('comments')
        # self.is_active = data_dict.get('is_active')

    def validate(self):
        self.error = None
        if self.pw != self.pw_confirmation:
            self.error = "The password and confirmation don't match."
            return
        if not self.pw:
            self.error = "You must specify a password"
            return
        if not self.email:
            self.error = "You must specify an email address"
            return
