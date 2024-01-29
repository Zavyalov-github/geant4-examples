import matplotlib.pyplot as plt
import numpy as np
import csv

from scipy import stats

file = 'proton_230MeV'

x_data = []
y_data = []

fig, ax = plt.subplots(figsize=(15,10))

with open(f"{file}.csv", encoding='utf-8') as r_file:
    data = csv.reader(r_file, delimiter = ",")
    for row in data:
        x_data.append(float(row[2]))
        y_data.append(float(row[0]))

#ax.scatter(x_data, y_data, label=file)

new_x_data, new_y_data = zip(*[(b, a) for b, a in sorted(zip(x_data, y_data))])
bin_means, bin_edges, binnumber = stats.binned_statistic(new_x_data, new_y_data, statistic='mean', bins=100)
bin_width = (bin_edges[1] - bin_edges[0])
bin_centers = bin_edges[1:] - bin_width/2

ax.scatter(bin_centers, bin_means, label=file)

ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
ax.set_ylabel('mean energy loss per travel length dE/dx, MeV/cm', fontsize=14)
ax.set_xlabel('momentum p, MeV/c', fontsize=14)
ax.set_title('Ionization losses of electron, pion, kaon, proton, deuteron and He3', fontsize=14)
ax.minorticks_on()
ax.set_axisbelow(True)
ax.grid(which='major')
ax.grid(which='minor',linestyle=':')
ax.legend()

plt.show()

