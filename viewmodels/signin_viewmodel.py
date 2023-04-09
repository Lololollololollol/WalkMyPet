from my_web_app.viewmodels.viewmodelbase import ViewModelBase


class SigninViewModel(ViewModelBase):
    def __init__(self):
        self.email = None
        self.pw = None
        self.error = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.pw = data_dict.get('pw')
