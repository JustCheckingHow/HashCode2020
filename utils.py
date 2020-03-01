import numpy as np


class Library:
    def __init__(self, books, signup_time, number_of_scans, id, **kwargs):
        self.id = id
        self.signup_time = int(signup_time)
        self.number_of_scans = int(number_of_scans)
        self.books = np.array(books).astype(int)
        self._mapped = None

        # internal efficiency params
        self.param_names = [
            '_number_of_scans_power', '_number_of_scan_weight',
            '_signup_time_weight', '_mapped_sum_weight'
        ]
        if set(kwargs.keys()).issubset(set(self.param_names)):
            self.set_params(kwargs)
        else:
            raise AttributeError(
                f"The passed kwargs do not contain all required params!")
        # self._number_of_scans_power = 1
        # self._number_of_scan_weight = 1

        # self._signup_time_weight = 1
        # self._mapped_sum_weight = 1

    def get_params(self, deep=False):
        """
        Get the parameters of the model 
        """
        param_dict = {}
        for param in self.param_names:
            param_dict[param] = getattr(self, param)
        return param_dict

    def set_params(self, **param):
        """
        Set the internal params of the model 
        """
        for p in param:
            setattr(self, p, param[p])

    @staticmethod
    def parse(line1, line2, id, **kwargs):
        signup_time = int(line1.split(" ")[1])
        books_per_day = int(line1.split(" ")[2])

        books = [int(x) for x in line2.split()]
        return Library(books, signup_time, books_per_day, id, **kwargs)

    def get_mapped(self, val_map):
        if self._mapped is None:
            self._mapped = [val_map[i] for i in self.books]
        return self._mapped

    def get_efficiency(self, val_map, day_no):
        mapped = self.get_mapped(val_map)

        return (self._mapped_sum_weight * np.sum(mapped) /
                (self._signup_time_weight * self.signup_time)) * (
                    self._number_of_scan_weight *
                    self.number_of_scans**self._number_of_scans_power)
