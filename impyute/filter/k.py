import numpy as np

# 1) Predicted State
timestep = 1
X_k0 = np.transpose([[25, 20, 6, 6]])
w_k = 0
n = 2

A = np.identity(n*2)
for i in range(n):
    A[i][n+i] = timestep
B = np.identity(n)*((1/2)*timestep**2)
B = np.append(B, np.identity(n)*timestep)
B = np.reshape(B, (n*2, n))
u_k1 = np.ones((n, 1))

X_k_p = np.matmul(A, X_k0) + np.matmul(B, u_k1) + w_k

# 2) Initialize Process Covariance Matrix
errors = [[5, 5, 0.2, 0.2]]

P_k0 = np.matmul(np.transpose(errors), errors) * np.identity(n*2)

# 3) Predict Process Covariance Matrix
Q_k1 = np.zeros((n*2, n*2))

P_k_p = np.matmul(np.matmul(A, P_k0), A.T) + Q_k1

# 4) Kalman Gain
H = np.identity((n*2))
R = np.ones((n*2, n*2))

K = np.matmul(P_k_p, H.T)/(np.matmul(np.matmul(H, P_k_p), H.T) + R)

# 5) New Observation
C = np.identity(n*2)
Z_k = np.zeros((n*2, 1))

Y_km = np.transpose([[20, 18, 7, 7]])

Y_k = np.matmul(C, Y_km) + Z_k

# 6) Calculating the Current State
X_k1 = X_k_p + np.matmul(K, (Y_k - np.matmul(H, X_k_p)))

# 7) Update the Process Covariance Matrix
P_k1 = np.matmul(np.matmul(np.identity(n*2), np.matmul(K, H)), P_k_p)

# 8) Setup for next cycle
X_k0 = X_k1
P_k0 = P_k1
