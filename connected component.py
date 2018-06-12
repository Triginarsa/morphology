import cv2
import numpy as np
from matplotlib import pyplot as plt

#prosedur 8-connectivity
def delapanlabel(gambar):
    #membuat 8-connectivity pada gambar
    ret, labels = cv2.connectedComponents(gambar, connectivity=8)

    # memberi nilai hue pada gambar yang telah di labelkan
    label_hue = np.uint8(179 * labels / np.max(labels))
    #mengalikan warna hue dengan nilai 255 untuk mendapatkan nilai maksimal
    nilai_maks = 255 * np.ones_like(label_hue)
    #menggabungkan warna hue awal dengan warna maksimal agar memiliki 3 nilai untuk di rubah ke bentuk RGB
    label_rgb = cv2.merge([label_hue, nilai_maks, nilai_maks])

    # mengubah gambar hue menjadi RGB
    label_rgb = cv2.cvtColor(label_rgb, cv2.COLOR_HSV2RGB)

    # mengatur agar background tetap hitam
    label_rgb[label_hue == 0] = 0
    return label_rgb

def empatlabel(gambar):
    #membuat 8-connectivity pada gambar
    ret, labels = cv2.connectedComponents(gambar, connectivity=4)

    # memberi nilai hue pada gambar yang telah di labelkan
    label_hue = np.uint8(179 * labels / np.max(labels))
    #mengalikan warna hue dengan nilai 255 untuk mendapatkan nilai maksimal
    nilai_maks = 255 * np.ones_like(label_hue)
    #menggabungkan warna hue awal dengan warna maksimal agar memiliki 3 nilai untuk di rubah ke bentuk RGB
    label_rgb = cv2.merge([label_hue, nilai_maks, nilai_maks])

    # mengubah gambar hue menjadi RGB
    label_rgb = cv2.cvtColor(label_rgb, cv2.COLOR_HSV2RGB)

    # mengatur agar background tetap hitam
    label_rgb[label_hue == 0] = 0
    return label_rgb

#main program
#proses membaca gambar
gambar = cv2.imread('tes12.jpg', 0)
#menyalin gambar menjadi gambar_asli
gambar_asli = gambar
#mengubah gambar menjadi biner dengan threshold diatas 127 menjadi nilai 1
gambar = cv2.threshold(gambar, 127, 255, cv2.THRESH_BINARY)[1]
#memanggil prosedur empatlabel
hasil1 = empatlabel(gambar)
#memanggil prosedur delapanlabel
hasil2 = delapanlabel(gambar)

#membuat tampilan citra awal
plt.subplot(131),plt.imshow(gambar_asli, cmap='gray')
plt.title('Citra Awal'), plt.xticks([]), plt.yticks([])

#membuat tampilan citra hasil 4-connectivity
plt.subplot(132),plt.imshow(hasil1)
plt.title('Hasil 4-Connectivity'), plt.xticks([]), plt.yticks([])

#membuat tampilan citra hasil 8-connectivity
plt.subplot(133),plt.imshow(hasil2)
plt.title('Hasil 8-Connectivity'), plt.xticks([]), plt.yticks([])
#menampilkan gambar
plt.show()