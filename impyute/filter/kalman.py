"""impyute.filter.kalman.py"""
import numpy as np


class Kalman:
    """ n-Dimensional Kalman Filter """
    def __init__(self, n, ts, X_k0, P_k0):
        """ Initialize a Kalman Filter with given parameters

        PARAMETERS
        ----------
        n: int
            Number of variables
        ts: int
            Timestep or change in time
        X_k0: numpy.array
            Initial state matrix
        P_k0: numpy.array
            Initial Covariance matrix
        """
        self.n = n
        self.ts = ts
        self.X_k0 = X_k0
        self.P_k0 = P_k0
        self.u_k1 = np.ones((n, 1))  # PARAMETER

        # Transition Matrices
        self.A = np.identity(n*2)
        for i in range(n):
            self.A[i][n+i] = ts
        B = np.identity(n)*((1/2)*ts**2)
        B = np.append(B, np.identity(n)*ts)
        B = np.reshape(B, (n*2, n))
        self.B = B
        self.H = np.identity((n*2))
        self.C = np.identity(n*2)

        # Kalman Gain
        self.R = np.ones((n*2, n*2))  # A bit added so we don't divide by 0

        # Noise Matrices
        self.w_k1 = np.zeros(n*2)
        self.Q_k1 = np.zeros((self.n*2, self.n*2))
        self.Z_k1 = np.zeros((n*2, 1))

    def filter(self, Y_km):
        """ Filter incoming measurement

        PARAMETERS
        ----------
        Y_km: numpy.array (n*2, 1)
        """

        # 1) Predict State
        X_k_p = np.matmul(self.A, self.X_k0) + np.matmul(self.B,
                                                         self.u_k1) + self.w_k1
        # 2) Predict Process Covariance
        P_k_p = np.matmul(np.matmul(self.A, self.P_k0), self.A.T) + self.Q_k1

        # 3) Calculate Kalman Gain
        K = np.matmul(P_k_p, self.H.T)/(np.matmul(np.matmul(self.H, P_k_p),
                                                  self.H.T) + self.R)
        # 4) New Observation
        Y_k = np.matmul(self.C, Y_km) + self.Z_k1
        # 5) Calculate Current State
        X_k1 = X_k_p + np.matmul(K, (Y_k - np.matmul(self.H, X_k_p)))
        # 6) Update the Process Covariance Matrix
        P_k1 = np.matmul((np.identity(self.n*2)-np.matmul(K, self.H)), P_k_p)
        # 7) Setup for next cycle
        self.X_k0 = X_k1
        self.P_k0 = P_k1

    def predict_next(self):
        return self.X_k0
