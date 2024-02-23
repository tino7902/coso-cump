import pyttsx3
from playsound import playsound

def musiquita():
    engine = pyttsx3.init()
    nom = input("ingrese el nombre: ")
    engine.save_to_file(nom, "./audio/nom.wav")
    engine.runAndWait()

    venga_saltando_por = "C:\\Users\\santi\\Documents\\proyectos\\coso-cump\\audio\\venga saltando por.wav"
    nom = "C:\\Users\\santi\\Documents\\proyectos\\coso-cump\\audio\\nom.wav"
    en_su_cumple = "C:\\Users\\santi\\Documents\\proyectos\\coso-cump\\audio\\en su cumpleee.wav"

    playsound(venga_saltando_por)
    playsound(nom)
    playsound(en_su_cumple)


if __name__ == "__main__":
    pass