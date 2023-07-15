import matplotlib
import matplotlib.pyplot as plt
import numpy as np

run1 = open("BIASED_COLVAR_1zih200lines_4ops.txt", "r").read()

x = run1.strip().splitlines()
y = run1.strip().splitlines()

x= [float(i.split()[7]) for i in x]
y= [float(i.split()[8]) for i in x]

colors = ["blue", "green", "red"]
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("name", colors)
norm = matplotlib.colors.Normalize(vmin=-3, vmax=3)
fig, (ax, ax2) = plt.subplots(nrows=2, figsize=(6,3), 
      gridspec_kw={"height_ratios":[1,3]}, sharex=True)
ax.axis("off")
ax.hist(x, bins=21, edgecolor="k")
sc = ax2.scatter(x,y,s=15, c=x, cmap=cmap, norm=norm)
fig.colorbar(sc, ax=ax2)
cax = fig.colorbar(sc, ax=ax)
cax.ax.set_visible(False)
plt.show()
