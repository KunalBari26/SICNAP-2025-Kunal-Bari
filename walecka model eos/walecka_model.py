import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import pandas as pd


HBAR_C = 197.327  
PI = 3.14
DEG = 4.0        

# USE_TM1 = True
USE_TM1 = False

if USE_TM1:
    M_N      = 939.0      
    M_SIGMA  = 511.198    
    M_OMEGA  = 783.0      
    G_SIGMA  = 10.0289
    G_OMEGA  = 12.6139
    SAT_DENS = 0.145      
else:
    M_N      = 939.0
    M_SIGMA  = 550.0
    M_OMEGA  = 783.0
    G_SIGMA  = 10.0289
    G_OMEGA  = 12.6139
    SAT_DENS = 0.160


def fermi_momentum(mu_b, m_eff, omega):
    mu_eff = mu_b - G_OMEGA * omega
    if mu_eff <= m_eff:
        return 0.0
    return np.sqrt(mu_eff**2 - m_eff**2)

def baryon_density(kf):
    return DEG * kf**3 / (6.0 * PI**2)

def scalar_density(kf, m_eff):
    a = DEG * m_eff / (4.0 * PI**2)
    b = kf * np.sqrt(kf**2 + m_eff**2)
    c = m_eff**2 * np.log((kf + np.sqrt(kf**2 + m_eff**2)) / m_eff)
    return a * (b - c)

def field_equations(vars_, mu_b):
    sigma, omega = vars_
    m_eff = M_N - G_SIGMA * sigma
    kf    = fermi_momentum(mu_b, m_eff, omega)
    n_b   = baryon_density(kf)
    n_s   = scalar_density(kf, m_eff)
    eq1 = sigma - (G_SIGMA / M_SIGMA**2) * n_s
    eq2 = omega - (G_OMEGA / M_OMEGA**2) * n_b
    return [eq1, eq2]

def solve_fields(mu_b):
    # start_guess = [25.0, 25.0]
    # start_guess = [10.0, 12.0]
    # start_guess = [10.0, 8.0]
    start_guess = [25.0, 12.0]
    sigma, omega = fsolve(field_equations, start_guess, args=(mu_b,))
    m_eff = M_N - G_SIGMA * sigma
    kf    = fermi_momentum(mu_b, m_eff, omega)
    n_b   = baryon_density(kf)
    return sigma, omega, m_eff, n_b

mu_values = np.arange(922.0, 1601.0, 1.0)  

sigmas, omegas, masses, nb_list = [], [], [], []

for mu in mu_values:
    s, o, m_eff, n_b = solve_fields(mu)
    sigmas.append(s)
    omegas.append(o)
    masses.append(m_eff)
    nb_list.append(n_b / HBAR_C**3)  


plt.plot(nb_list, sigmas, label='sigma')
plt.plot(nb_list, omegas, label='omega')
plt.xlabel('n_B  [fm^-3]')
plt.ylabel('Mean fields  [MeV]')
plt.legend()
plt.show()

plt.plot(nb_list, masses)
plt.xlabel('n_B  [fm^-3]')
plt.ylabel('Effective mass  [MeV]')
plt.title('M* versus density')
plt.show()


def energy_density(kf, m_eff, sigma, omega):
    ef = np.sqrt(kf**2 + m_eff**2)
    k_term = (DEG / (16 * PI**2)) * (kf * ef * (2 * kf**2 + m_eff**2) + m_eff**4 * np.log((kf + ef) / m_eff))
    m_term = 0.5 * M_SIGMA**2 * sigma**2 + 0.5 * M_OMEGA**2 * omega**2
    return k_term + m_term

def pressure(kf, m_eff, sigma, omega):
    ef = np.sqrt(kf**2 + m_eff**2)
    k_term = (DEG / (24 * PI**2)) * (kf * ef * (kf**2 - 1.5 * m_eff**2) + 1.5 * m_eff**4 * np.log((kf + ef) / m_eff))
    m_term = -0.5 * M_SIGMA**2 * sigma**2 + 0.5 * M_OMEGA**2 * omega**2
    return k_term + m_term

eps_list, pres_list = [], []
for n_b, s, o, m_eff in zip(nb_list, sigmas, omegas, masses):
    kf_val = (3 * PI**2 * n_b * 2)**(1/3)   
    eps = energy_density(kf_val, m_eff, s, o) / HBAR_C**3
    pres = pressure(kf_val, m_eff, s, o) / HBAR_C**3
    eps_list.append(eps)
    pres_list.append(pres)

plt.plot(mu_values, eps_list)
plt.xlabel('mu_B  [MeV]')
plt.ylabel('Energy density  [MeV/fm^3]')
plt.show()

plt.plot(mu_values, pres_list)
plt.xlabel('mu_B  [MeV]')
plt.ylabel('Pressure  [MeV/fm^3]')
plt.show()

plt.plot(eps_list, pres_list)
plt.xlabel('Energy density  [MeV/fm^3]')
plt.ylabel('Pressure  [MeV/fm^3]')
plt.title('Equation of State')
plt.show()


df = pd.DataFrame({
    'mu_B': mu_values,
    'energy_density': eps_list,
    'pressure': pres_list
})
df.to_csv('walecka_model_output.csv', index=False)
