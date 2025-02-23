import tkinter as tk
import time
import webbrowser
import os

def paivita_kello():
    aika = time.strftime("%H:%M:%S")
    kello.config(text=aika)
    kello.after(1000, paivita_kello)

def paivita_suomi_aika():
    suomi_aika = time.strftime("%H:%M:%S", time.gmtime(time.time() + 2*3600))  # Suomi aika
    suomi_kello.config(text=suomi_aika)
    suomi_kello.after(1000, paivita_suomi_aika)

def avaa_tyopoyta(event):
    tyopoyta = tk.Toplevel(ikkuna)
    tyopoyta.configure(bg="pink")
    tyopoyta.attributes('-fullscreen', True)

    kello.pack_forget()

    tehtavapalkki = tk.Frame(tyopoyta, bg="purple", height=50)
    tehtavapalkki.pack(side="bottom", fill="x")

    koti_painike = tk.Button(tehtavapalkki, text="Koti", bg="lightblue", width=10, height=5, command=avaa_uusi_ikkuna)
    koti_painike.pack(side="left")

    hakukentta = tk.Entry(tehtavapalkki, width=30, font=("Helvetica", 14), bg="#800080")
    hakukentta.pack(side="left", padx=10, pady=5)

    hakukentta.config(highlightthickness=2, highlightbackground="black")
    hakukentta.bind("<FocusIn>", lambda event: hakukentta.config(highlightbackground="blue"))
    hakukentta.bind("<FocusOut>", lambda event: hakukentta.config(highlightbackground="black"))

    hakukentta.bind("<Return>", lambda event: avaa_ohjelma(hakukentta.get()))

    hae_painike = tk.Button(tehtavapalkki, text="Hae", bg="lightgrey", width=10, command=lambda: avaa_ohjelma(hakukentta.get()))
    hae_painike.pack(side="left", padx=5)

    tiedostot_painike = tk.Button(tehtavapalkki, text="Tiedostot", bg="lightgrey", width=10, height=5, command=lambda: os.startfile("."))
    tiedostot_painike.pack(side="left", padx=50)

    spotify_painike_tehtavapalkki = tk.Button(tehtavapalkki, text="Spotify", bg="lightgrey", width=10, height=5, command=lambda: webbrowser.open("https://www.spotify.com"))
    spotify_painike_tehtavapalkki.pack(side="left", padx=5)

    global suomi_kello
    suomi_kello = tk.Label(tehtavapalkki, font=("Helvetica", 18), bg="purple", fg="white")
    suomi_kello.pack(side="right", padx=10)
    paivita_suomi_aika()

    chrome_painike = tk.Button(tyopoyta, text="Google Chrome", bg="lightgrey", font=("Helvetica", 16), command=lambda: webbrowser.open("https://www.google.com"))
    chrome_painike.place(x=10, y=10)

    spotify_painike = tk.Button(tyopoyta, text="Spotify", bg="lightgrey", font=("Helvetica", 16), command=lambda: webbrowser.open("https://www.spotify.com"))
    spotify_painike.place(x=180, y=10)

def avaa_uusi_ikkuna():
    uusi_ikkuna = tk.Toplevel(ikkuna)
    uusi_ikkuna.title("Uusi Ikkuna")
    uusi_ikkuna.configure(bg="purple")

    chrome_painike = tk.Button(uusi_ikkuna, text="Google Chrome", bg="lightgrey", font=("Helvetica", 16), command=lambda: webbrowser.open("https://www.google.com"))
    chrome_painike.pack(pady=10)

    spotify_painike = tk.Button(uusi_ikkuna, text="Spotify", bg="lightgrey", font=("Helvetica", 16), command=lambda: webbrowser.open("https://www.spotify.com"))
    spotify_painike.pack(pady=10)

    tiedostot_painike = tk.Button(uusi_ikkuna, text="Tiedostot", bg="lightgrey", font=("Helvetica", 16), command=lambda: os.startfile("."))
    tiedostot_painike.pack(pady=10)

    sammuta_painike = tk.Button(uusi_ikkuna, text="Sammuta", bg="red", font=("Helvetica", 16), command=lambda: os.system("shutdown /s /t 1"))  # Lisätään Sammuta-painike
    sammuta_painike.pack(pady=10)

    # Lisätään Lepotila-painike
    lepotila_painike = tk.Button(uusi_ikkuna, text="Lepotila", bg="yellow", font=("Helvetica", 16), command=lambda: os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0"))
    lepotila_painike.pack(pady=10)

    ikkuna_leveys = 400
    ikkuna_korkeus = 300
    ruutu_leveys = uusi_ikkuna.winfo_screenwidth()
    ruutu_korkeus = uusi_ikkuna.winfo_screenheight()

    x = (ruutu_leveys / 2) - (ikkuna_leveys / 2)
    y = (ruutu_korkeus / 2) - (ikkuna_korkeus / 2)
    uusi_ikkuna.geometry(f'{ikkuna_leveys}x{ikkuna_korkeus}+{int(x)}+{int(y)}')

def avaa_ohjelma(ohjelma):
    ohjelmat = [
        "Spotify",
        "Google Chrome",
        "Tiedostot"
    ]

    if ohjelma in ohjelmat:
        if ohjelma == "Spotify":
            webbrowser.open("https://www.spotify.com")
        elif ohjelma == "Google Chrome":
            webbrowser.open("https://www.google.com")
        elif ohjelma == "Tiedostot":
            os.startfile(".")
    else:
        print("Ohjelmaa ei löydy")

ikkuna = tk.Tk()
ikkuna.configure(bg="pink")

kello = tk.Label(ikkuna, font=("Helvetica", 48), bg="pink", fg="white")
kello.pack(pady=50)

paivita_kello()

ikkuna.bind("<Key>", avaa_tyopoyta)
ikkuna.bind("<Button-1>", avaa_tyopoyta)

ikkuna.mainloop()