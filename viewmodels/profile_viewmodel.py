from my_web_app.viewmodels.viewmodelbase import ViewModelBase


class ProfileViewModel(ViewModelBase):
    def __init__(self):
        self.profile_image = None
        self.nickname = None
        self.interests = None
        self.comments = None
        self.error = None

    def from_dict(self, data_dict):
        self.profile_image = data_dict.get('image')
        self.nickname = data_dict.get('nickname')
        self.interests = data_dict.get('interests')
        self.comments = data_dict.get('comments')


    @property
    def interested_activities(self):
        return [
            i.strip()
            for i in self.interests.split('\n')
            if i and i.strip()
        ]

