import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def dilasi(thresh,kernel):
    d = cv2.dilate(thresh, kernel, iterations=1)
    return d;

FILE_OUTPUT = 'Hasil Deteksi.png'

# mengecek apakah ada file hasil deteksi.png
# dengan fungsi dibawah output bisa di overwrite
if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

#membaca file gambar
gambar = cv2.imread('2.jpg',0)
#konversi biner dengan threshold apabila minValue 127 dan MaxValue 255 pada sebuah pixel maka nilainya 1
ret, thresh = cv2.threshold(gambar, 127, 255, cv2.THRESH_BINARY)
#membuat sebuah kernel 3x3 tipe 8bit
kernel = np.ones((3,3),np.uint8)

