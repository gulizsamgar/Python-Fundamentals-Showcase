###############################################
# PYTHON FUNDAMENTALS SHOWCASE:
# Algoritma & Veri Yapıları Pratikleri
###############################################

###############################################
# GÖREV 1: Veri Yapılarının Tiplerini İnceleme
###############################################

x= 8
print(type(x))

y= 3.2
print(type(y))

z = 8j + 18
print(type(z))

a = "Hello World"
print(type(a))

b = True
print(type(b))

c = 23 < 22
print(type(c))

l = [1, 2, 3, 4]
print(type(l))
# Sıralı, Kapsayıcı, Değiştirilebilir

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
print(type(d))
# Sırasız*, Kapsayıcı, Değiştirilebilir, Key değerleri farklı olacak

t = ("Machine Learning", "Data Science")
print(type(t))
# Sıralı, Kapsayıcı, Değiştirilemez*

s = {"Python", "Machine Learning", "Data Science"}
print(type(s))
# Sırasız, Eşsiz*, Kapsayıcı, Değiştirilebilir

###############################################
# GÖREV 2: String Manipülasyonu
# Aşağıda string bir ifade verilmiştir.
# — Bütün harfleri büyük harfe çevirin,
# — Virgül ve noktayı kaldırıp boşlukla değiştirin,
# — Kelimelere ayırın.
###############################################

text = "The goal is to turn data into information, and information into insight."
formatted_text= text.upper().replace(",","").replace("."," ").split()
print(formatted_text)

###############################################
# GÖREV 3: Liste İşlemleri
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.
len(lst)
print("Adım 1 - Eleman sayısı:", len(lst))

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırın.
print("Adım 2 - 0. indeks:", lst[0])
print("        10. indeks:", lst[10])

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturun.
data_list = lst[0:4]
print("Adım 3 - Yeni liste:", data_list)

# Adım 4: Sekizinci indeksteki elemanı silin.
removed_item = lst.pop(8)
print("Adım 4 - Silinen eleman:", removed_item)
print("         Güncel liste:", lst)

# Adım 5: Yeni bir eleman ekleyin.
lst.append(100)
print("Adım 5 - Yeni eleman eklendi:", lst)

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyin.
lst.insert(8, "N")
print("Adım 6 - Eleman tekrar eklendi:", lst)

###############################################
# GÖREV 4: Sözlük İşlemleri
###############################################

students = {
    "Christian": ["America", 18],
    "Daisy": ["England", 12],
    "Antonio": ["Spain", 22],
    "Dante": ["Italy", 25],
}

# Adım 1: Key değerlerine erişin.
keys = students.keys()
print("Adım 1 - Anahtarlar:", list(keys))

# Adım 2: Value'lara erişin.
values = students.values()
print("Adım 2 - Değerler:", list(values))

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyin.
students["Daisy"][1] = 13
print("Adım 3 - Güncel Daisy değeri:", students["Daisy"])

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyin.
students["Ahmet"] = ["Turkey", 24]
print("Adım 4 - Ahmet eklendi:", students)

# Adım 5: Antonio'yu dictionary'den siliniz.
students.pop("Antonio")
print("Adım 5 - Antonio silindi:", students)

###############################################
# GÖREV 5: Tek/Çift Sayı Ayırma Fonksiyonu
# Argüman olarak bir liste alan,
# listenin içerisindeki tek ve çift sayıları ayrı listelere atayan
# ve bu listeleri return eden fonksiyon tanımlayın.
###############################################

def tek_cift_ayir(list):
     """Girilen listenin tek ve çift elemanlarını ayırır."""
     ciftler=[]
     tekler=[]
     for index in list:
          if index %2 == 0:
               ciftler.append(index)
          else:
               tekler.append(index)
     return ciftler,tekler

sayi_listesi = [2,13,18,93,22]
cift, tek = tek_cift_ayir(sayi_listesi)
print("Çiftler:", cift)
print("Tekler:", tek)

###############################################
# GÖREV 6: Enumarate Kullanımı
# Aşağıda dereceye giren öğrecilerin listesi bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken
# son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırın.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]

for index, ogrenci in enumerate(ogrenciler):
     if index < 3:
          index += 1
          print("Mühendislik Fakültesi",index,". öğrenci: ",ogrenci)
     else:
          index -= 2
          print("Tıp Fakültesi", index, ". öğrenci: ",ogrenci)

###############################################
# GÖREV 7: Zip Kullanımı
# Aşağıda 3 adet liste verilmiştir.
# Ders kodları, krediler ve kontenjanlar listelerini
# zip ile birleştirip anlamlı bir çıktı oluşturun.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for kod, kredi, kont in zip(ders_kodu, kredi, kontenjan):
     print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjanı {kont} kişidir.")

###############################################
# GÖREV 8: Set İşlemleri
# Aşağıda 2 adet set verilmiştir.
# Eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını yazdıran
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlayın.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kume_islemi(set1,set2):
     """Kümeler arası kapsayıcılık kontrolü yapar."""
     if set1.issuperset(set2):
          print("Ortak elemanlar:", set1.intersection(set2))
     else:
          print("Farklı elemanlar:", set2.difference(set1))

kume_islemi(kume1,kume2)