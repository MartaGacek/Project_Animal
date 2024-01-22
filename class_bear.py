import numpy as np
import matplotlib.pyplot as plt

class Bear:
    def __init__(self, params):
        self.params = params
        self.matrices = {}
        self.matrix = np.zeros((111, 101))

    def build_partial_matrices(self):
        for key in self.params["indexes"].keys():
            if key not in self.matrices.keys():
                min_row = min([tup[0] for tup in self.params["indexes"][key]])
                max_row = max([tup[0] for tup in self.params["indexes"][key]])
                min_col = min([tup[1] for tup in self.params["indexes"][key]])
                max_col = max([tup[1] for tup in self.params["indexes"][key]])
                self.matrices[key] = np.zeros((max_row - min_row, max_col - min_col))
                self.matrices[key] = self.params["masks"][key]
            else:
                self.matrices[key] = self.matrix[min_row: max_row, min_col: max_col]
        return self

    def build_result_matrix(self):
        for key in self.params["indexes"].keys():
            min_row = min([tup[0] for tup in self.params["indexes"][key]])
            max_row = max([tup[0] for tup in self.params["indexes"][key]])
            min_col = min([tup[1] for tup in self.params["indexes"][key]])
            max_col = max([tup[1] for tup in self.params["indexes"][key]])
            self.matrix[min_row: max_row, min_col: max_col] = self.matrices[key]
        return self


    def solve_area(self, D_v, D_u, T, h_t, h_x, u_0, f, g):
        for t in T:
            for key in self.matrices.keys():
                # środek
                self.matrices[key][1:-1, 1:-1] = self.matrices[key][1:-1, 1:-1] + ( ) * ( )  + self.params['force_term'](self.matrices[key][1:-1, 1:-1])
                # ściany
        # for key in self.matrices.keys():
        #     for t in T:
        #         if t = 0:
        #             u[:,:,0]= u_0()
        #             v[:,:,0]= u_0()
        #         else:
        #             u[1:-1,1:-1, k] = h_t * (D_u/(h_x**2) * (u[2:, 1:-1, k-1] + + u[:-2, 1:-1, k-1] + u[1:-1, :-2, k-1] + u[1:-1, 2:, k-1] - 4 * u[1:-1, 1:-1, k-1]) - C_1*u[1:-1, 1:-1, k-1] + (C_2*u[1:-1, 1:-1, k-1]**2)/v[1:-1, 1:-1, k-1 + C_3) + u[1:-1, 1:-1, k-1]
        #             u[0,:,k] = u[1,:,k] + h_x*g(T[k])
        #             u[-1,:,k] = u[-2,:,k] + h_x*g(T[k])
        #             u[:,0,k] = u[:,1,k] + h_x*g(T[k])
        #             u[:,-1,k] = u[:,-2,k] + h_x*g(T[k])
        #             v[1:-1,1:-1, k] = h_t * (D_v/(h_x**2) * (v[2:, 1:-1, k-1] + + v[:-2, 1:-1, k-1] + v[1:-1, :-2, k-1] + v[1:-1, 2:, k-1] - 4 * v[1:-1, 1:-1, k-1]) + C_4*u[1:-1, 1:-1, k-1]**2 - C_5*v[1:-1, 1:-1, k-1]) + v[1:-1, 1:-1, k-1]
        #             v[0,:,k] = v[1,:,k] + h_x*g(T[k])
        #             v[-1,:,k] = v[-2,:,k] + h_x*g(T[k])
        #             v[:,0,k] = v[:,1,k] + h_x*g(T[k])
        #             v[:,-1,k] = v[:,-2,k] + h_x*g(T[k])
        #             k += 1
                


params = {"indexes": {"i": [(0, 0), (0, 10), (110, 0), (110, 10)],
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
                    "x": 0, "xi": 1, "xii": 1, "xiii": 1, "xiv": 0, "xv": 0, "xvi": 1, "xvii": 0,
                    "xviii": 1}}

coralgol = Bear(params)
coralgol.build_partial_matrices()
coralgol.build_result_matrix()
plt.imshow(coralgol.matrix)
plt.show()
