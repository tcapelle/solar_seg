import matplotlib.pyplot as plt
from PIL import Image


def show_image(img:Image, ax:plt.Axes=None, figsize:tuple=(3,3), hide_axis:bool=True, cmap:str='binary',alpha:float=None)->plt.Axes:
    if ax is None: fig,ax = plt.subplots(figsize=figsize)
    ax.imshow(img, cmap=cmap, alpha=alpha)
    if hide_axis: ax.axis('off')
    return ax