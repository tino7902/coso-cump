import pyttsx3
from playsound import playsound
import tkinter as tk
import datetime


def musiquita(nom):
    engine = pyttsx3.init()
    engine.save_to_file(nom, "./audio/nom.wav")
    engine.runAndWait()

    venga_saltando_por = "C:\\Users\\santi\\Documents\\proyectos\\coso-cump\\audio\\venga saltando por.wav"
    nom = "C:\\Users\\santi\\Documents\\proyectos\\coso-cump\\audio\\nom.wav"
    en_su_cumple = "C:\\Users\\santi\\Documents\\proyectos\\coso-cump\\audio\\en su cumpleee.wav"

    playsound(venga_saltando_por)
    playsound(nom)
    playsound(en_su_cumple)

def tiempoQueFalta(nom):
    # tiempo actual
    now = datetime.datetime.now()

    # calcular tiempo hasta media noche
    midnight = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
    time_until_midnight = midnight - now

    # guarda las horas, minutos y segundos
    hours, seconds = divmod(time_until_midnight.seconds, 3600)
    minutes = seconds // 60
    seconds_formateado = seconds % 60

    # formatea el mensaje
    remaining_time_message = f"Faltan {hours}:{minutes}:{seconds_formateado:02} para el cumpleaños de {nom}"

    # pone musiquita cuando llegue la hora
    if seconds == 0:
        musiquita(nom)
    return remaining_time_message

# class para la gui
class temporizador:
    def __init__(self, root):
        self.root = root
        self.root.title("temporizador")

        # inicializa las variables de la class
        self.nom = " "      # nombre del cumpleañero/a 
        self.empezo = False # para saber si ya empezo la cuenta atras

        # label que despues va a mostrar cuanto tiempo falta
        self.tiempo_label = tk.Label(root, text="Ingresa tu nombre: ", font=("Helvetica", 38))
        self.tiempo_label.pack(pady=20, side=tk.TOP)

        # entry para poner el nombre
        self.entry = tk.Entry(root, font=("Helvetica", 38))
        self.entry.pack(pady=20, padx=10, side=tk.TOP)

        # boton de inicio
        self.start_button = tk.Button(root, text="Listo", command=self.inicio)
        self.start_button.pack(side=tk.LEFT, padx=10)

        # actualiza el tiempo
        self.update_timer()

    def inicio(self):
        if not self.empezo:
            self.empezo = True
            self.entry.config(state="disabled")
            self.update_timer()

    def update_timer(self):
        if self.empezo:
            self.tiempo_label.config(text=tiempoQueFalta(nom=self.entry.get()))
            self.root.after(1000, self.update_timer)  # actualiza cada segundo


if __name__ == "__main__":
    root = tk.Tk()
    app = temporizador(root)
    root.mainloop()