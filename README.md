pombEye : A protein localisation classifier for Schizosaccharomyces pombe microscopy images

pombEye is an image classifier that can be used to predict subcellular localisation (eg. fluorescent tagged proteins) within fission yeast (S.pombe, S.japonicus, S.octosporus and S.cryophilus ) species. pombEye runs on an image classifier built using Keras for Python with Tensorflow as the backend (V166 base fine tuned with pombe microscopy images). For training and validation, S.pombe fluorescent microscope images from the Orfeome project was used (1).

Prerequisites and installation instruction:

pombEye can be accessed using the python source code (.py extension) through Mac/ Linux Terminal

1) Numpy

pip install numpy

2) OpenCV

pip install opencv-python

3)Tensorflow

pip install tensorflow 

(For machines with compatible GPU, visit the Tensorlfow webpage)

4) Keras

pip install Keras

Instructions:

1) Open terminal and run the python source code using the following command

python path_to_the_file/pombEye_V1.py

2) The program loads Tensorflow and compiles the weights file (.h5).

3)The program asks for the filepath to the input image. The prompt accepts keyboard input. On macOS, drag the input file icon to the terminal and the filepath is pasted.

It is strongly recommended to input .jpg format input images instead of .tiff . The program can handle color and grayscale images (Images are converted to 8-bit images prior to feeding into the model).

The top hit for the prediction is listed on top along with a confidence score ranging between 0 and 100.

To exit the program, type 'exit' when the program asks for input filepath.

Planned features:

Ability to classify S.cerevisiae (budding yeast) microscopy images.



I welcome feedback, suggestions, contributions and input. Please contact me at wilson.3273@osu.edu.



References:
1) Matsuyama, A., Arai, R., Yashiroda, Y., Shirai, A., Kamata, A., Sekido, S., … Yoshida, M. (2006). ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe. Nature Biotechnology, 24(7), 841–847. https://doi.org/10.1038/nbt1222
