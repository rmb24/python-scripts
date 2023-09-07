import matplotlib.pyplot as plt
import pandas as pd
m = "M.xlsx"
base_base_datosM = pd.read_excel(m)


print(base_base_datosM)

valores_m = base_base_datosM[["X", "Y "]]
print(valores_m)

ax_m = valores_m.plot(x="X", y="Y ")
plt.xlabel("X")
plt.ylabel("Y")
plt.show(ax_m)


base_base_datosM["X"] = base_base_datosM["X"] * 1.5
base_base_datosM["Time"] = base_base_datosM["Time"] - \
    base_base_datosM["Time"].iloc[0] / 1000


tx_m = base_base_datosM.plot(x="Time", y="X")
plt.xlabel("Time")
plt.ylabel("X")
plt.show(tx_m)
