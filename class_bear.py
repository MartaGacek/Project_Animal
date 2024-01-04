import numpy as np

class Bear:

    def __init__(self):
        self.params = {"indexes": {"i": [(0,0), (0, 10), (110, 0), (110, 10)],
                              "ii": [(0, 10), (0, 30), (40, 10), (40, 30)],
                              "iii": [(0, 30), (0, 40), (10, 30), (10, 40)],
                              "iv": [(10, 30), (10, 40), (40, 30), (40, 40)],
                              "v": [(0, 40), (0, 70), (10, 40), (10, 70)],
                              "vi": [(10, 40), (10, 70), (40, 40), (40, 70)],
                              "vii": [(0, 70), (0, 80), (10, 70), (10, 80)],
                              "viii": [(10, 70), (10, 80), (40, 70), (40, 80)],
                              "ix": [(0, 80), (0, 100), (40, 80), (40, 100)],
                              "x": [(0, 100), (0, 110), (110, 100), (110, 110)],
                              "xi": [(40, 10), (40, 30), (60, 10), (60, 30)],
                              "xii": [(40, 30), (40, 80), (90, 30), (90, 80)],
                              "xiii": [(40, 80), (40, 100), (60, 80), (60, 100)],
                              "xiv": [(60, 10), (60, 30), (90, 10), (90, 30)],
                              "xv": [(60, 80), (60, 100), (90, 80), (90, 100)],
                              "xvi": [(90, 10), (90, 50), (110, 10), (110, 50)],
                              "xvii": [(90, 50), (90, 60), (110, 50), (110, 60)],
                              "xviii": [(90, 60), (90, 100), (110, 60), (110, 100)]},
                  "masks": {"i": 0, "ii": 0, "iii": 1, "iv": 0, "v": 0, "vi": 1, "vii": 1, "viii": 0, "ix": 0,
                            "x": 0, "xi": 1, "xii": 1, "xiii": 1, "xiv": 0, "xv": 0, "xvi": 1, "xvii": 0, "xviii": 1}}

        self.matrices = {}
        for key in params["indexes"].keys():
            min_row = min([tup[0] for tup in params["indexes"][key]])
            max_row = max([tup[0] for tup in params["indexes"][key]])
            min_col = min([tup[1] for tup in params["indexes"][key]])
            max_col = max([tup[1] for tup in params["indexes"][key]])
            self.matrices[key] = np.zeros((max_row - min_row, max_col - min_col))
            self.matrices[key] = params["masks"][key]
            
    return self




# if __name__ == "main":
# coralgol = Bear()
# print(coralgol.params)
