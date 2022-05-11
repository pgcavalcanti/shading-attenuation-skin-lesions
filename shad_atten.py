import scipy
import numpy as np
from skimage import io, color
from matplotlib import pyplot as plt

def shad_atten(im, mask, viz=True):
    '''
    im = skin RGB image
    mask = binary mask indicating reference pixels as 1
    '''
    
    rows, cols, dep = im.shape
    
    hsv = color.rgb2hsv(im)
    V = hsv[:,:,2]
      
    Y, X = np.where(mask>0)
    Z = V[mask>0]
    
    c = [0, 0, 0, 0, 0, 0, 0.5]
    
    c1 = scipy.optimize.fmin(func=error_fun, x0=c, args=(X,Y,Z))

    y = np.arange(0, rows)
    x = np.arange(0, cols)    
    [X1, Y1] = np.meshgrid(x,y)
    new_z = model(c1, X1, Y1)
    
    new_V = V / new_z
    new_V[new_V>1] = 1
    new_V[new_V<0] = 0
    
    hsv[:,:,2] = new_V
    new_im = color.hsv2rgb(hsv)
    
    if viz:
        plt.figure()
        plt.subplot(221)
        plt.imshow(new_z)
        plt.subplot(222)
        plt.imshow(new_V)
        plt.subplot(223)
        plt.imshow(im)
        plt.subplot(224)
        plt.imshow(new_im)
        
    return new_im


def error_fun(c, X, Y, Z):
    "Sum of the squared error"
    e = Z - model(c, X, Y)
    ee = e**2
    s = ee.sum()
    return s

def model(c, X, Y):
    return c[0]*(X**2) + c[1]*(Y**2) + c[2]*X*Y + c[3]*X + c[4]*Y + c[5]


#main
im = io.imread('skin_lesion.jpg') #skin lesion example

#create a binary mask with 20x20 in all 4 corners of the image
#to be used as shading reference
mask = np.zeros(im.shape[:2])
mask[:20,:20] = 1
mask[:20,-20:] = 1
mask[-20:,:20] = 1
mask[-20:,-20:] = 1

new_im = shad_atten(im, mask)
io.imsave('new_skin_lesion.png', new_im)
    
    