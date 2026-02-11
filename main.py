import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


CPSI = 750
k_factor = 5.5
O2_PER_G_CEO2 = 0.11

washcoat_nom = 160        # g/L
ceo2_nom = 0.275          # weight fraction
eta_nom = 0.70

#range of each parameter in osc calculation
volume = np.linspace(0.86, 1.0, 60)
washcoat = np.linspace(120, 200, 60)
ceo2_frac = np.linspace(0.20, 0.35, 60)
eta = np.linspace(0.65, 0.75, 60)

#osc calculation
def compute_osc(volume, washcoat, ceo2_frac, eta):
    washcoat_mass = volume * washcoat
    ceo2_mass = washcoat_mass * ceo2_frac
    stored_o2 = ceo2_mass * O2_PER_G_CEO2 * eta
    osc_geom = CPSI * k_factor * volume
    return osc_geom * stored_o2

# graph plot 1 (Volume vs Washcoat Loading)
V1, W = np.meshgrid(volume, washcoat)
OSC_vw = compute_osc(V1, W, ceo2_nom, eta_nom)

plt.figure()
c1 = plt.contour(V1, W, OSC_vw)
plt.clabel(c1)
plt.xlabel("Catalyst Volume (L)")
plt.ylabel("Washcoat Loading (g/L)")
plt.title("OSC Contour: Volume vs Washcoat Loading")
plt.show()

#Volume vs Cirica weight rfaction
V2, C = np.meshgrid(volume, ceo2_frac)
OSC_vc = compute_osc(V2, washcoat_nom, C, eta_nom)

plt.figure()
c2 = plt.contour(V2, C, OSC_vc)
plt.clabel(c2)
plt.xlabel("Catalyst Volume (L)")
plt.ylabel("CeO₂ Weight Fraction")
plt.title("OSC Contour: Volume vs CeO₂ Fraction")
plt.show()

#Volume vs/ Utilisation efficiency
V3, E = np.meshgrid(volume, eta)
OSC_ve = compute_osc(V3, washcoat_nom, ceo2_nom, E)

plt.figure()
c3 = plt.contour(V3, E, OSC_ve)
plt.clabel(c3)
plt.xlabel("Catalyst Volume (L)")
plt.ylabel("Utilisation Efficiency (η)")
plt.title("OSC Contour: Volume vs Utilisation Efficiency")
plt.show()

#contour plot
plt.figure()
plt.contourf(V1, W, OSC_vw)
plt.colorbar(label="OSC")
plt.xlabel("Catalyst Volume (L)")
plt.ylabel("Washcoat Loading (g/L)")
plt.title("Filled OSC Contour: Volume vs Washcoat")
plt.show()

#3d Volume vs washcoat loading vs osc
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(V1, W, OSC_vw)
ax.set_xlabel("Catalyst Volume (L)")
ax.set_ylabel("Washcoat Loading (g/L)")
ax.set_zlabel("OSC")
ax.set_title("3D Surface Plot: OSC")
plt.show()

#lookup table
volume_lut = np.linspace(0.86, 1.0, 10)
washcoat_lut = np.linspace(120, 200, 10)
ceo2_lut = np.linspace(0.20, 0.35, 10)
eta_lut = np.linspace(0.65, 0.75, 10)

osc_lut = compute_osc(volume_lut, washcoat_lut, ceo2_lut, eta_lut)

lut = pd.DataFrame({
    "Volume_L": volume_lut,
    "Washcoat_g_per_L": washcoat_lut,
    "CeO2_fraction": ceo2_lut,
    "Efficiency_eta": eta_lut,
    "OSC": osc_lut
})

print("\n=== OSC LOOKUP TABLE ===\n")
print(lut)

lut.to_csv("osc_lookup_table.csv", index=False)