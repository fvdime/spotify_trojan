import spotipy                #spotify için modüller
import spotipy.util as util    
import time                    
import numpy as np
import matplotlib.pyplot as plt       #resimler için modüller
from PIL import Image
import tkinter.messagebox              #yazı için modüller
from tkinter import Button


# istediğimiz kullanıcının bilgilerini k_adi, k_id, k_secret yerleştiriyoruz
k_adi = 'kullanıcı adı'
k_id = 'cilent id'
k_secret = 'client secret'
redirect_uri = 'http://localhost:8888/callback'

#Spotify API erişmek için token yöntemi kullanıyoruz 
#kullanıcıyı token yöntemi ile yetkilendiriyoruz 
scope = 'user-read-playback-state,user-modify-playback-state'
token = util.prompt_for_user_token(k_adi, scope, k_id, k_secret, redirect_uri)
sp = spotipy.Spotify(auth=token) # spotify müşterişi, kullanıcısı, oluşturuyoruz.


# istediğimiz playlistin URI sını ekliyoruz
playlist_uri = 'spotify:playlist:5r9Tyfitz4nem72OygfLuH'

# playlistten şarkıları çekiyoruz
results = sp.playlist_tracks(playlist_uri)
tracks = results['items']
while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

# şarkıları döngüye sokuyoruz
while True:
    for track in tracks:
        #şarkının oynatıldığı kısım
        sp.start_playback(uris=[track['track']['uri']])

        #şarkının bitmesini bekler
        while True:
            playback = sp.current_playback()
            if playback is None:
                break
            time.sleep(1)


                        #RESİM OYNATMA
            #resmin adres yollarını ekliyoruz
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\ad.jpg'
            cizim = Image.open(adresYolu)
            cizim_Numpy = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\add.jpg'
            cizim = Image.open(adresYolu)
            cizim_Numpy1 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\1.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy2 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\2.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy3 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\3.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy4 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\4.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy5 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\5.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy6 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\6.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy7 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\7.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy8 = np.asarray(cizim)
            adresYolu = 'C:\\Users\\hp\\OneDrive\\Masaüstü\\spotify_trojan\\8.jpeg'
            cizim = Image.open(adresYolu)
            cizim_Numpy9 = np.asarray(cizim)
            while True:                #while döngüsüne alıyoruz ki 
                    plt.imshow(cizim_Numpy)
                    plt.draw()
                    plt.pause(1) #kaç saniye duracağı
                    plt.close()


                    plt.imshow(cizim_Numpy1)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy2)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy3)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy4)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy5)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy6)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy7)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy8)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    plt.imshow(cizim_Numpy9)
                    plt.draw()
                    plt.pause(1)
                    plt.close()


                    #YAZI
                    # tkinter modülünden pencere oluşturuyoruz
                    root = tkinter.Tk()

                    # pencerenin adını ve boyutunu ayarlıyoruz
                    root.title("çizimleri kapatmak için ÇIKIŞ butonuna basınız")
                    root.geometry('500x300')

                    # çıkışa basınca oluşan mesaj kutusunu oluşturuyoruz
                    def onClick():
                        tkinter.messagebox.showinfo("", "SIKEEEEE")

                    # buton oluşturuyoruz
                    button = Button(root, text="ÇIKIŞ", command=onClick, height=5, width=10)

                    # butonun penceredeki yerini ayarlıyoruz
                    button.pack(side='bottom')
                    root.mainloop()