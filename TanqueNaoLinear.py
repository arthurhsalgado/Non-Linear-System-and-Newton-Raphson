import numpy as np
import matplotlib.pyplot as plt

ca_in = 2000
V = 1
tau = 50
k0 = 10**8
DH = 2*10**5
rho = 10**3
cp = 4.18 * 10**3
UA = 1.5 * 10**3
E = 7* 10**4
Te = 330
Tc = 280
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

X_cal = np.linspace(100, 2000, 100)
Y_cal = np.linspace(300, 500, 100)

sol_X = np.zeros((len(X_cal), len(Y_cal)))
sol_Y = np.zeros((len(X_cal), len(Y_cal)))
sol_Y[:] = np.nan
for i, ca0 in enumerate(X_cal):
    for j, t0 in enumerate(Y_cal):

        X = np.array([[X_cal[i]], [Y_cal[j]]])
        Ea = 1
        tol = 0.001
        del_X = np.array([[0.0], [0.0]])
        try:
            while Ea > tol:

                F = f(X[0, 0], X[1, 0])
                J = jacobiano(X[0, 0], X[1, 0])

                # checa determinante antes de resolver
                if abs(np.linalg.det(J)) < 1e-12:
                    raise np.linalg.LinAlgError("Jacobiano singular")

                # ---------- Resolução manual do sistema 2x2 ----------
                a, b = J[0, 0], J[0, 1]
                c, d = J[1, 0], J[1, 1]
                rhs0, rhs1 = -F[0, 0], -F[1, 0]

                det = a * d - b * c
                if abs(det) < 1e-12:
                    raise np.linalg.LinAlgError("Jacobiano singular")

                x0 = (rhs0 * d - b * rhs1) / det
                x1 = (a * rhs1 - rhs0 * c) / det
                del_X = np.array([[x0], [x1]])
                # -----------------------------------------------------

                X = X + del_X
                Ea = np.linalg.norm(del_X)

            sol_X[j, i] = X[0, 0]
            sol_Y[j, i] = X[1, 0]

        except np.linalg.LinAlgError:
            continue

# Plot do mapa de calor
plt.figure(figsize=(7,6))
im = plt.imshow(
    sol_X,
    origin='lower',
    extent=[X_cal.min(), X_cal.max(), Y_cal.min(), Y_cal.max()],
    aspect='auto',
    cmap='viridis'
)
plt.colorbar(im, label='Y')
plt.xlabel('X inicial')
plt.ylabel('Y inicial')
plt.title('Valor de Ca para cada CI')
plt.show()

plt.figure(figsize=(7,6))
im = plt.imshow(
    sol_Y,
    origin='lower',
    extent=[X_cal.min(), X_cal.max(), Y_cal.min(), Y_cal.max()],
    aspect='auto',
    cmap='viridis'
)
plt.colorbar(im, label='Y')
plt.xlabel('X inicial')
plt.ylabel('Y inicial')
plt.title('Valor de T para cada CI')
plt.show()

