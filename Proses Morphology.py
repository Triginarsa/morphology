import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkFileDialog

#prosedur update event saat di klik hotkey
def update(event):
    #variabel global img awal
    global img
    #variabel global img untuk proses morphology
    global img2
    #membuat sebuah kernel 3x3 tipe 8bit
    kernel = np.ones((3, 3), np.uint8)
    # konversi biner dengan threshold apabila minValue 127 dan MaxValue 255 pada sebuah pixel maka nilainya 1
    ret, thresh = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
    #jika menekan tombol "x"
    if event.key == 'x':
        #proses dilasi dengan menggunakan img hasil threshold biner dengan kernel 3x3 dan sekali iterasi
        dilasi = cv2.dilate(thresh, kernel, iterations=1)
        #mengubah value im untuk tampilan gambar
        im.set_data(dilasi)
        #mengubah value img2 dengan hasil dilasi
        img2 = dilasi
        #menampilkan gambar
        fig.canvas.draw()
    elif event.key == 'c':
        # proses erosi dengan menggunakan img hasil threshold biner dengan kernel 3x3 dan sekali iterasi
        erosi = cv2.erode(thresh, kernel, iterations=1)
        im.set_data(erosi)
        img2 = erosi
        fig.canvas.draw()
    elif event.key == 'v':
        # proses opening dengan melakukan erosi terlebih dahulu kemudian dilasi
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        im.set_data(opening)
        img2 = opening
        fig.canvas.draw()
    elif event.key == 'b':
        # proses closing dengan melakukan dilasi terlebih dahulu kemudian erosi
        closing = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE, kernel, iterations=1)
        im.set_data(closing)
        img2 = closing
        fig.canvas.draw()
    elif event.key == 'n':
        gradient = cv2.morphologyEx(thresh,cv2.MORPH_GRADIENT, kernel, iterations=1)
        im.set_data(gradient)
        img2 = gradient
        fig.canvas.draw()
    elif event.key == 'z':
        #mengubah value img2 menjadi img gambar awal
        img2 = img
        im.set_data(img2)
        fig.canvas.draw()
    elif event.key == 'o':
        #proses mengambil gambar dengan tipe file jpg,png dan bitmap
        fname = tkFileDialog.askopenfilename(filetypes=(("Template files", "*.JPG .PNG .BITMAP"), ("All files", "*")))
        #membaca path dari fname dengan imread agar dibaca sebagai gambar
        img = cv2.imread(fname, 0)
        img2 = img
        im.set_data(img2)
        fig.canvas.draw()
    elif event.key == 'i':
        #invert gambar
        img2 = cv2.bitwise_not(img2)
        im.set_data(img2)
        fig.canvas.draw()

#inisialisasi gambar awal
img = cv2.imread('buka.png', 0)
#menambahkan value img2 dengan img awal
img2 = img
#membuat figure dan 1 plot xy
fig, ax = plt.subplots()
#membuat judul figure
fig.suptitle('Morphology', fontsize=20, fontweight='bold')
#membuat label x
plt.xlabel("Keterangan = 'z':Reset  'x':Dilasi  'c':Erosi  'v':Opening  'b':Closing  'n':Gradient"), plt.xticks([]), plt.yticks([])
#menampilkan gambar
im = ax.imshow(img, cmap = 'gray')
#action untuk trigger saat menekan tombol
fig.canvas.mpl_connect('key_press_event', update)
plt.show()