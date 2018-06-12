import cv2
import numpy as np
from matplotlib import pyplot as plt

#membaca gambar
img = cv2.imread('contoh.png',0)
#konversi biner dengan threshold apabila minValue 127 dan MaxValue 255 pada sebuah pixel maka nilainya 1
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#membuat sebuah kernel 3x3 tipe 8bit
kernel = np.ones((3,3),np.uint8)
#proses dilasi dengan menggunakan thresh sebagai background dan kernel sebagai foreground dengan sekali iterasi 1
dilasi = cv2.dilate(thresh,kernel,iterations = 1)

#membuat tampilan citra awal
plt.subplot(131),plt.imshow(img,cmap = 'gray')
plt.title('Citra Awal'), plt.xticks([]), plt.yticks([])

#membuat tampilan citra biner saat di threshold
plt.subplot(132),plt.imshow(thresh,cmap = 'gray')
plt.title('Citra Biner'), plt.xticks([]), plt.yticks([])

#membuat tampilan citra hasil dilasi
plt.subplot(133),plt.imshow(dilasi,cmap = 'gray')
plt.title('Hasil Dilasi'), plt.xticks([]), plt.yticks([])
#menampilkan gambar
plt.show()