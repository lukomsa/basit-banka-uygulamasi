# BankaHesabı sınıfı
class BankaHesabı:
    # Kurucu fonksiyon
    def __init__(self, bakiye=500):
        self.bakiye = bakiye # Başlangıç bakiyesi
        self.para_birimi = "euro" # Varsayılan para birimi
        self.kur = {"dolar": 1.12, "euro": 1, "sterlin": 0.86} # Para birimleri arası kur
    
    # Para birimi seçme fonksiyonu
    def para_birimi_sec(self, secim):
        if secim == 1:
            self.para_birimi = "dolar"
        elif secim == 2:
            self.para_birimi = "euro"
        elif secim == 3:
            self.para_birimi = "sterlin"
        else:
            print("Geçersiz seçim. Euro olarak devam edilecek.")
        print(f"Para biriminiz {self.para_birimi} olarak ayarlandı.")
    
    # Para yatırma fonksiyonu
    def para_yatir(self, miktar):
        self.bakiye += miktar / self.kur[self.para_birimi] # Bakiyeyi euro cinsinden güncelle
        print(f"{miktar} {self.para_birimi} yatırdınız. Güncel bakiyeniz: {self.bakiye * self.kur[self.para_birimi]:.2f} {self.para_birimi}")
    
    # Para çekme fonksiyonu
    def para_cek(self, miktar):
        if miktar <= self.bakiye * self.kur[self.para_birimi]: # Bakiye yeterli mi kontrol et
            self.bakiye -= miktar / self.kur[self.para_birimi] # Bakiyeyi euro cinsinden güncelle
            print(f"{miktar} {self.para_birimi} çektiniz. Güncel bakiyeniz: {self.bakiye * self.kur[self.para_birimi]:.2f} {self.para_birimi}")
        else:
            print("Yetersiz bakiye. İşlem gerçekleştirilemedi.")
    
    # Bakiye gösterme fonksiyonu
    def bakiye_goster(self):
        print(f"Güncel bakiyeniz: {self.bakiye * self.kur[self.para_birimi]:.2f} {self.para_birimi}")

# Tkinter kütüphanesini içe aktar
import tkinter as tk

# BankaHesabı nesnesi oluştur
hesap = BankaHesabı()

# Tkinter penceresi oluştur ve başlığını ayarla
window = tk.Tk()
window.title('Banka Uygulaması')

# Pencereye arayüz elemanları ekle
# Bir metin etiketi
label = tk.Label(window, text='Hoşgeldiniz')
label.pack()

# Bir metin kutusu
entry = tk.Entry(window)
entry.pack()

# Bir çerçeve
frame2 = tk.Frame(window)
frame2.pack()
# Çerçevenin başlığı
label2 = tk.Label(frame2, text='Lütfen para birimi seçiniz:')
label2.pack()
# Çerçevenin içine seçim listesi
listbox = tk.Listbox(frame2)
listbox.insert(1, 'Dolar')
listbox.insert(2, 'Euro')
listbox.insert(3, 'Sterlin')
listbox.pack()

# Bir buton grubu
frame = tk.Frame(window)
frame.pack()
button1 = tk.Button(frame, text='Para yatır', command=lambda: hesap.para_yatir(float(entry.get())))
button1.pack(side=tk.LEFT)
button2 = tk.Button(frame, text='Para çek', command=lambda: hesap.para_cek(float(entry.get())))
button2.pack(side=tk.LEFT)
button3 = tk.Button(frame, text='Bakiye göster', command=hesap.bakiye_goster)
button3.pack(side=tk.LEFT)
button4 = tk.Button(frame, text='Çıkış', command=window.destroy)
button4.pack(side=tk.LEFT)

# Bir durum çubuğu
status = tk.Label(window, text='Lütfen para birimi seçiniz', bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

# Bir metin etiketi daha
bakiye_label = tk.Label(window, text=f'Güncel bakiyeniz: {hesap.bakiye * hesap.kur[hesap.para_birimi]:.2f} {hesap.para_birimi}')
bakiye_label.pack()

# Seçim listesinin seçim değiştiğinde çalışacak fonksiyonu
def onselect(event):
    secim = listbox.curselection()[0] + 1 # Seçilen indeksi al
    hesap.para_birimi_sec(secim) # Para birimini seç
    status.config(text=f'Para biriminiz {hesap.para_birimi} olarak ayarlandı') # Durum çubuğunu güncelle
    bakiye_label.config(text=f'Güncel bakiyeniz: {hesap.bakiye * hesap.kur[hesap.para_birimi]:.2f} {hesap.para_birimi}') # Bakiye etiketini güncelle

# Seçim listesine olay bağla
listbox.bind('<<ListboxSelect>>', onselect)

# Pencereyi göster
window.mainloop()
