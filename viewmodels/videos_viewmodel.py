from my_web_app.viewmodels.viewmodelbase import ViewModelBase


class VideosViewModel(ViewModelBase):
    def __init__(self):
        self.video_id = None
        self.video_title = None
        self.img_url = None
        self.view_count = None
        self.video_author = None
        self.error = None

    def from_dict(self, data_dict):
        self.video_id = data_dict.get('video_id')
        self.video_title = data_dict.get('video_title')
        self.img_url = data_dict.get('img_url')
        self.view_count = int(data_dict.get('view_count', 0))
        self.video_author = data_dict.get('video_author')

