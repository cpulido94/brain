
import numpy as np
import matplotlib.pyplot as plt
from nilearn.datasets import MNI152_FILE_PATH
from nilearn import plotting

t = np.linspace(1, 10, 2000)


plt.plot(t, np.cos(t))
plt.show()
print('Path to MNI152 template: %r' % MNI152_FILE_PATH)
plotting.plot_img(MNI152_FILE_PATH)
plt.show()
plotting.plot_img('/home/cristian/PycharmProjects/pruebas/img1.nii')
plt.show()
plotting.plot_img('/home/cristian/PycharmProjects/pruebas/img2.nii')
plt.show()
