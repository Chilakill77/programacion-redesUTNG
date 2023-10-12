#Kevin Cabrera Luna
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
hortot = hour + (mins + dura) // 60
minfi = (mins + dura) % 60
horf = hortot % 24
print("Tiempo final: {:02}:{:02}".format(horf, minfi))

