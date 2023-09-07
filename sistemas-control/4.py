import matplotlib.pyplot as plt
import pandas as pd

v = "V.xlsx"
base_base_datosV = pd.read_excel(v)

valores_v = base_base_datosV[["X", "Y "]]

ax_v = valores_v.plot(x="X", y="Y ")
plt.xlabel("X")
plt.ylabel("Y")
plt.show(ax_v)

base_base_datosV["X"] = base_base_datosV["X"] * 1.5
base_base_datosV["Time"] = base_base_datosV["Time"] - \
    base_base_datosV["Time"].iloc[0] / 1000

tx_v = base_base_datosV.plot(x="Time", y="X")
plt.xlabel("Time")
plt.ylabel("X")
plt.show(tx_v)
