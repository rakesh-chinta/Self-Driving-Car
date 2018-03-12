import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('selfdrivingcarproject.jpg')
print('This image is', type(image), 'with dimensions', image.shape)

ysize =image.shape[0]
xsize =image.shape[1]
region_select = np.copy(image)

left_buttom = [0, 539]
right_buttom = [900, 300]
apex = [400,0]

fit_left = np.ployfit((left_buttom[0], apex[0]),(left_buttom[1], apex[1]),1)
fit_right = np.ployfit((right_buttom[0], apex[0]),(right_buttom[1], apex[1]),1)
fit_bottom = np.polyfit((left_buttom[0],right_buttom[0]),(left_buttom[1],right_buttom[1]),1)

XX, YY = np.meshgrid(np.arange(0,xsize),np.arange(0,ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1]) &
                     YY > (XX * fit_right[0] + fit_right[1]) &
                    YY < (XX*fit_bottom[0] + fit_bottom[1]))

region_select[region_thresholds] = [255,0,0]

plt.imshow(region_select)
