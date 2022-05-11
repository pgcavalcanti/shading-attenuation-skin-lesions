# Reference:
CAVALCANTI, Pablo G.; SCHARCANSKI, Jacob; LOPES, Carlos BO. Shading attenuation in human skin color images. In: International Symposium on Visual Computing. Springer, Berlin, Heidelberg, 2010. p. 190-198.

I wrote this paper more than 10 years ago, but still receive emails about it from time to time.    
So, today (May 2022) I finally decided to convert my original Matlab code to Python.  

The code includes 3 functions, but "shad_atten" is the importat one.  
Just use it with your skin lesion image and a binary mask with reference pixels (usually the image corners).  
I also included an example in the "main" part.  

Running this function, you are supposed to attenuate shading in skin lesion images, i.e. from this
![alt text](skin_lesion.jpg?raw=true)

to this
![alt text](new_skin.lesion.png?raw=true)
