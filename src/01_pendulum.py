from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams["text.usetex"] = True


def odes(x, t):
    # constants
    g = 9.81
    l = 1.0

    # assign each ode to a vector element
    phi = x[0]
    omega = x[1]

    dphi_dt = omega
    domega_dt = -g / l * np.sin(phi)

    return [dphi_dt, domega_dt]


# Initial conditions
phi0 = np.pi / 4
omega0 = 0.0
x0 = [phi0, omega0]

# declare a time vector (time window)
t = np.linspace(0, 10, 1000)
x = odeint(odes, x0, t)

phi = x[:, 0]
omega = x[:, 1]

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_title(r"Pendulum motion: Angle $\varphi(t)$ and Angular velocity $\omega(t)$")
ax.set_xlabel(r"Zeit $t$ in s")
ax.set_ylabel(r"$\varphi(t)$ in rad, $\omega(t)$ in rad/s")
ax.plot(t, phi, label=r"$\varphi(t)$")
ax.plot(t, omega, label=r"$\omega(t)$")
ax.legend()
plt.show()
