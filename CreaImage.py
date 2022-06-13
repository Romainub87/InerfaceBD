from matplotlib import pyplot as plt
import pandas as pd

#
data_Nouvelle_Aquitaine = [ (16, 'Charente', 352015, 5956.0),
(17, 'Charente-Maritime', 651358, 6863.8),
(19, 'Corrèze', 240073, 5856.8),
(23, 'Creuse', 116617, 5565.4),
(24, 'Dordogne', 413223, 9060.0),
(33, 'Gironde', 1623749, 9975.6),
(40, 'Landes', 413690, 9242.6),
(47, 'Lot-et-Garonne', 331271, 5360.9),
(64, 'Pyrénées-Atlantiques', 682621, 7644.8),
(79, 'Deux-Sèvres', 374878, 5999.4),
(86, 'Vienne', 438435, 6990.4),
(87, 'Haute-Vienne', 372359, 5520.1)]

data = data_Nouvelle_Aquitaine
colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'pink', 'turquoise',
'purple', 'orange', 'gray', 'brown']
plt.title('Pourcentages populations départements Nouvelle-Aquitaine')
plt.pie([d[2] for d in data],
labels=[d[1] + ' (' + str(d[0]) + ')' for d in data],
colors=colors,
autopct='%1.1f %%',
shadow=False,
startangle=90)
plt.axis('equal')
plt.savefig("Image/figure.png")
