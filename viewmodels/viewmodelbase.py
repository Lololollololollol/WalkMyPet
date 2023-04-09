# Study-guide
# :Consistent Data Exchange(specific classes bundles the data and convert the data. A single view dedicated to a single view
class ViewModelBase:
    # Take a class and turn it into a dictionary
    def to_dict(self):
        # __dict__ : where the fields/attr are stored
        return self.__dict__
