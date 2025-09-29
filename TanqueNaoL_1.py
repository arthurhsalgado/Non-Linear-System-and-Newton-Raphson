import numpy as np
import matplotlib.pyplot as plt

ca_in = 2000
V = 1
tau = 100
k0 = 10**6
DH = 4*10**4
rho = 10**3
cp = 4.18 * 10**3
UA = 2 * 10**4
E = 8* 10**4
Te = 330
Tc = 300
R = 8.314

C1 = (DH* V *k0)/(rho * cp * (V/tau) * Te + UA * Tc)
C2 = (rho*cp * (V/tau) + UA)/(rho*cp * (V/tau) * Te + UA *Tc)

def f(x, y):
    return np.array([[(x/ca_in) * (tau * k0 * np.exp(-E/(R*y)) + 1) - 1],
                     [C1 * x * np.exp(-E/(R*y)) - y * C2 + 1]])

def jacobiano(x, y):
  df1_dx = (k0*tau*np.exp(-E/(R*y)) + 1)/ca_in
  df1_dy = (E*k0*tau*x*np.exp(-E/(R*y)))/(R*ca_in*y**2)
  df2_dx = C1*np.exp(-E/(R*y))
  df2_dy = C1*E*x*np.exp((-E/(R*y)))/(R*y**2) - C2

  return np.array([[df1_dx, df1_dy],
                   [df2_dx, df2_dy]])

Ea = 1
tol = 0.001
X_cal = np.array([[600], [305]])
del_X = np.array([[0], [0]])

while Ea > tol:

  F = f(X_cal[0,0], X_cal[1,0])
  J = jacobiano(X_cal[0,0], X_cal[1,0])

  del_X = np.linalg.solve(J, -F)
  X_cal = X_cal + del_X

  Ea = np.linalg.norm(del_X)

print(X_cal)