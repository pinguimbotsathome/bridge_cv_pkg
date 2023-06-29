# Launcher bridge_cv_pkg
Pacote para pegar a Imagem do kinect, passar um filtro e publicar em outro nodo.

### Image_filter.py

Recebe a imagem do kinect ("camera/rgb/image_raw") e passa um filtro do open cv (cv2.Canny) e publica um topico ("bridge/image_filtered").

### Code_bridge_msg.py 

Recebe o topico do image_filter ("bridge/image_filtered") e plota na tela.

### Launch:

Iniciar kinect:
```
$ roslaunch openni_launch openni.launch
```

Passar a imagem:
```
$ rosrun bridge_cv_pkg image_filter.py 
```

Plotar na tela:
```
$ rosrun bridge_cv_pkg code_bridge_msg.py
```
