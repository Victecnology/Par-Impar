import tkinter as tk
from random import randint


class ParOImpar(tk.Frame):
  """
  Clase para representar el juego de Par o Impar.
  """

  def __init__(self, master):
    super().__init__(master)

    # Atributos de la ventana
    self.master.title("Par o Impar")
    self.master.resizable(False, False)

    # Elementos de la GUI
    self.label_titulo = tk.Label(self, text="Par o Impar")
    self.label_numero_jugador = tk.Label(self, text="Tu número:")
    self.entry_numero_jugador = tk.Entry(self)
    self.label_numero_amigo = tk.Label(self, text="Número de tu amigo:")
    self.entry_numero_amigo = tk.Entry(self)
    self.button_jugar = tk.Button(self, text="Jugar", command=self.jugar)
    self.label_resultado = tk.Label(self, text="")
    self.label_puntuacion_jugador = tk.Label(self, text="Puntuación: 0")
    self.label_puntuacion_amigo = tk.Label(self, text="Puntuación: 0")

    # Posición de los elementos
    self.label_titulo.pack(pady=10)
    self.label_numero_jugador.pack(pady=5)
    self.entry_numero_jugador.pack(pady=5)
    self.label_numero_amigo.pack(pady=5)
    self.entry_numero_amigo.pack(pady=5)
    self.button_jugar.pack(pady=10)
    self.label_resultado.pack(pady=5)
    self.label_puntuacion_jugador.pack(pady=5)
    self.label_puntuacion_amigo.pack(pady=5)

  def jugar(self):
    # Inicializa la variable puntuacion_jugador.
    puntuacion_jugador = 0
    puntuacion_amigo = 0

    # Genera un número aleatorio entre 1 y 100.
    numero = randint(1, 100)

    # Obtiene la entrada del jugador.
    numero_jugador = int(self.entry_numero_jugador.get())

    # Obtiene la entrada del amigo.
    numero_amigo = int(self.entry_numero_amigo.get())

    # Comprueba la respuesta del jugador y del amigo.
    if numero % 2 == 0 and numero_jugador % 2 == 0:
      resultado = "Empate"
    elif numero % 2 == 0 and numero_jugador % 2 != 0:
      resultado = "Perdiste"
      puntuacion_jugador -= 1
    elif numero % 2 != 0 and numero_jugador % 2 == 0:
      resultado = "Ganaste"
      puntuacion_amigo += 1
    else:
      if numero_jugador > numero_amigo:
        resultado = "Ganaste"
        puntuacion_jugador += 1
      elif numero_jugador < numero_amigo:
        resultado = "Ganaste"
        puntuacion_amigo += 1
      else:
        resultado = "Empate"

    # Actualiza el resultado en la GUI.
    self.label_resultado.config(text=resultado)

    # Actualiza la puntuación.
    self.label_puntuacion_jugador.config(text="Puntuación: {}".format(puntuacion_jugador))
    self.label_puntuacion_amigo.config(text="Puntuación: {}".format(puntuacion_amigo))

  # Atributos para controlar el número de rondas y la puntuación.
  rondas = 0
  puntuacion_jugador = 0
  puntuacion_amigo = 0


root = tk.Tk()
ParOImpar(root).pack()
root.mainloop()