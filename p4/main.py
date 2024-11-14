import customtkinter as ctk
from play import play_musica

def main():
    janela = ctk.CTk()

    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")

    janela.geometry("500x500")

    botao_play = ctk.CTkButton(janela, text="Play", command=play_musica)
    botao_play.pack()
    botao_play.place(x=300, y=400)

    janela.mainloop()
main()