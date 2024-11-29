from collections import deque
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
dizi = [] #park_area
satir=3
sutun=3
def location():
    park_station =[]
    for i in range(satir):
        satirelemanlari=[]
        for j in range(sutun):
          deger = int(input(f"{i+1}. satir, {j+1}. sütun değeri: "))
          satirelemanlari.append(deger)
        dizi.append(satirelemanlari)
location()       
print (dizi)

def location_analys():
    for i in range(satir):
        for j in range(sutun):
            sonuc=dizi[i][j]
            if sonuc==1:
                print(f"{i+1}.satir,{j+1}.sütuna park edilemez")
            else:
               print(f"{i+1}.satir,{j+1}.sütuna park edilebilir")
location_analys() 

baslangic_satir = int(input("Başlangic satirini girin: "))
baslangic_sutun = int(input("Başlangic sütununu girin: "))

def nearest_way(matris,baslangic_noktasi):
    satir =len(matris)
    sutun=len(matris[0])
    #4 yönlü hareket
    hareketler = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #BFS için kuyruk ve ziyaret edilenler seti
    kuyruk = deque([baslangic_noktasi])
    ziyaret_edilen = set([baslangic_noktasi])
    #Eğer başlangıç noktası boşsa, hemen mesafe olarak 0'ı döndür
    if matris[baslangic_noktasi[0]][baslangic_noktasi[1]] == 0:
        return baslangic_noktasi, 0
    #BFS başlıyor
    while kuyruk:
        for a in range(len(kuyruk)):
            x, y = kuyruk.popleft()
            # Eğer mevcut nokta boş alan (0) ise ve başlangıç noktasından farklıysa
            if matris[x][y] == 0 and (x, y) != baslangic_noktasi:
                #Manhattan mesafesi hesapla
                mesafe = abs(x - baslangic_noktasi[0]) + abs(y - baslangic_noktasi[1])
                return (x, y), mesafe  # En yakın boş alan ve mesafeyi döndür
            # 4 yönlü hareketi kontrol et
            for dx, dy in hareketler:
                yeni_x, yeni_y = x + dx, y + dy
                # Matris sınırları içinde mi?
                if 0<= yeni_x < satir and 0<= yeni_y < sutun:
                    if (yeni_x, yeni_y) not in ziyaret_edilen:
                        ziyaret_edilen.add((yeni_x, yeni_y))
                        kuyruk.append((yeni_x, yeni_y))
    return print("bos alan bulunamadı")
baslangic_noktasi = (baslangic_satir,baslangic_sutun)
nokta, mesafe = nearest_way(dizi,baslangic_noktasi)
if nokta:
    print(f"En yakin boş alan: {nokta}, Manhattan mesafesi: {mesafe}")

# Görselleştirme
def visualize_parking_area(matris, en_yakin_nokta):
    # Park alanını numpy array olarak dönüştür
    grid = np.array(matris)
    
    #özel renk haritası
    cmap = ListedColormap(['green', 'red'])    
    
    # Görselleştirme için renkler
    fig, ax = plt.subplots()
    ax.imshow(matris, cmap=cmap, interpolation='nearest')

    # En uygun park yerini mavi yap
    if en_yakin_nokta:
        ax.scatter(en_yakin_nokta[1], en_yakin_nokta[0], color='blue', s=100, label='En Uygun Park Yeri')

    # Başlangıç noktasını işaretle
    ax.scatter(baslangic_sutun, baslangic_satir, color='black', s=100, label='Başlangıç Noktası')
    
    # Başlık ve etiketler
    ax.set_title("Park Alanı Görselleştirmesi")
    ax.set_xticks(np.arange(sutun))
    ax.set_yticks(np.arange(satir))
    ax.set_xticklabels(np.arange(1, sutun + 1))
    ax.set_yticklabels(np.arange(1, satir + 1))
    
    # Grafik üzerine etiketler ekle
    for i in range(satir):
        for j in range(sutun):
            if matris[i][j] == 1:
                ax.text(j, i, 'dolu', ha="center", va="center",color="black",fontsize=15)
            elif matris[i][j] == 0:
                ax.text(j, i, 'bos', ha="center", va="center", color="white", fontsize=15)

    # Renkli dikdörtgen kutular ekle
    plt.legend(loc='upper left')
    
    plt.show()
visualize_parking_area(dizi, nokta)