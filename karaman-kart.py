age = int(input("Lütfen Yaşınızı Giriniz: "))
liste = ["Engelli", "Personel"]
sartli = str(input("Şartınızı Giriniz: "))

print(sartli in liste)

if age > 0 and age< 6:
    print(f"Merhaba, Yaşınız {age}. Dolmuş Ücretsizdir.")

elif age >= 6 and age< 18:
    print(f"Merhaba, Yaşınız {age}. Karaman Kart Öğrenciliği Alabilirsiniz.")

elif age >= 18 and age< 25:
    print(f"Merhaba, Yaşınız {age}. Karaman Kart Yetişkin Alabilirsiniz.")

elif age >= 65:
    print(f"Merhaba, Yaşınız {age}. karaman Kart 65 yaş Alabilirsiniz.")

# Age değişkeni oluşturdum ve integer ile kullanıcıdan veri almak istedim.
# liste değişkeniyle liste oluşturdum ve "Engelli", "Personel" ataması yaptım.
# sartli değişkeni ile string yani karakter ifadeleriyle engelli mi yoksa personel mi olduğunu sordum.
#print (sartli in liste) ile kullanıcıdan aldığımız veriyi sorgulattım eğer liste içerisinde varsa true yoksa false döndürecek.
# if ile ilk 0 and age yani kullanıcıdan alınacak veriyi sorgulattım 0-6 yaş aralığında ise printi döndürecek.
# elif ile 6,18 yaş aralığında olduğunu sorgulattım ve 6-18 yaş arasındaysa öğrenci alabileceğini söylettim.
# diğer elifler ise aynı mantıktan ilerledi.