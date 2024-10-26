import random #random kütübahanesi projeye alınır
chars="+-/*!.,_&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #seçebileceği karakterler
password="" #en osnda verilicek olan şifrenin değişkeni tanımlanır
chars=list(chars) #charlar listye çevrilir
passlength=int(input("parolanun unuznluğunu girin ")) #şifrenin uzunluğu sorulur ve bunu integer olarak alınır
for i in range(0,passlength): #döngüyle şifrenin uzunluğu kadar çalışmasını sağlanır
    password+=random.choice(chars) #listeeden rastgale bir karakter seçilir
print(password) #şifre yazılır
