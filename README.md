# Kanji-GAN
A GAN that produces Kanji similar characters (images).  
Almost following the tutorial on [pytorch website](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html).

# Results
Linear interpolation between outputs from several normal samples.  

https://user-images.githubusercontent.com/49623314/116908286-601d7500-ac4b-11eb-9730-7da246a6a19d.mp4


# Usage and Data
As direct as opening the Jupyer notebook.  
Check releases if you want trained networks for -currently- about 70 or 80 epochs.

### Extracting data
First, install `Fontforge`. Then In the repository folder run the command  
`Fontforge -lang=py -script script.py`  
A new folder which contains the images will be created.

### Notes
* Apparently the training is very sensitive to hyperparameters, stick to the values suggested in the tutorial.
