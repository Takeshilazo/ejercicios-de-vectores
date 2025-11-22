#ejercicios con matrices es un grafico de dias de la semana 
import matplotlib.pyplot as plt
dias =['lunes','martes','miercoles','jueves','viernes']
temperatura =[25,26,21,28,22]
plt.plot(dias,temperatura,'ro-') #'ro-' significa puntos rojos
plt.title("templeratura semanal")
plt.show()