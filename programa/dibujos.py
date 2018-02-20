import numpy as np
import matplotlib.pyplot as plt
from nilearn import plotting
from nilearn import image
import os

#ruta de la carpeta
direccion=os.getcwd()
#Dibujando imagen estructural
rutaT1='/alejandra-parra/restilb-alejandra-parra/T1/T1.nii.gz'#ruta imagen T1
T1=direccion+rutaT1
plotting.plot_img(T1)#graficar imagen T1
plt.title("Imagen estructural")
plt.show()#mostrar imagen

#suavizar imagen filtro gaussiano
smoth=image.smooth_img(T1,fwhm=3)
plotting.plot_img(smoth)
plt.title("Imagen estructural suavizada")
plotting.show()

#Dibujando imagen funcional
rutafunc='/alejandra-parra/restilb-alejandra-parra/func/func.nii.gz'
funcional=direccion+rutafunc#img funcional
#tamaño img funcional, la ultima es el tiempo
print(image.load_img(funcional).shape)
#Tomamos un tiempo especifico para graficar
tiempo=80
primerfunc=image.index_img(funcional,tiempo)
#bg img: imagen de fondo, aca puse la T1, threshold: cota inferior, dim: constraste img +oscuro -claro
plotting.plot_stat_map(primerfunc,bg_img=T1,threshold=1500,title="img funcional "+str(tiempo)+"/150",dim=1)
plt.show()

plotting.plot_glass_brain(primerfunc,black_bg=T1,threshold=1500)
plotting.show()

#componentes resultado del restlib
rutacomponentes='/alejandra-parra/restilb-alejandra-parra/ica/components/icaAna_sub01_component_ica_s1_.nii'
componentes=direccion+rutacomponentes
rutamascara='/alejandra-parra/restilb-alejandra-parra/ica/components/icaAnaMask.img'
mascara=direccion+rutamascara
#escogemos un componente entre los 30
compt=image.index_img(componentes,20)
plotting.plot_stat_map(compt,bg_img=mascara,threshold=0)
plt.show()