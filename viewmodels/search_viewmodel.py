from my_web_app.viewmodels.viewmodelbase import ViewModelBase


class SearchViewModel(ViewModelBase):
    def __init__(self):
        self.search_text = None
        self.search_results = None
        self.error = None

    def from_dict(self, data_dict):
        self.search_text = data_dict.get('search_text')
        self.search_results = data_dict.get('search_results')
