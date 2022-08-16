from datetime import datetime, date, time,timedelta
from io import open 

def consolaVB2008():
    global time1, time2, time3, time4, time5, time6
    horaInicio= timedelta(hours= 6, minutes= 45)
    horaFinal= timedelta(hours = 14)
    print(f"La hora de inicio del turno es: {horaInicio}")
    print(f"La hora de finalizacion del turno es: {horaFinal}")
    
    programaDeInicio= int(input("Cuantos minutos demoro el inicio del programa: "))
    time1 = horaInicio + timedelta(minutes= programaDeInicio)
    print(time1)
    
    AjustesIniciales= int(input("Cuanto tiempo demoraron los ajuestes inciales: "))
    time2 = time1 + timedelta(minutes= AjustesIniciales)
    print(time2)

    inicioDeProduccion= int(input("Cuantos minutos demoro el incio de la deproduccion: " ))
    time3 = time2 + timedelta(minutes=inicioDeProduccion)
    print(time3)

    reponerMarteriaPrima= int(input("Cuantos minutos demoro reponer la mateira prima: " ))
    time4 = time3 + timedelta(minutes=reponerMarteriaPrima)
    print(time4)

    DistribucionDeProductos= int(input("Cuantos minutos demoro la distribucion de productos: " ))
    time5 = time4 + timedelta(minutes=DistribucionDeProductos)
    print(time5)

    Almacenamientos= int(input("Cuantos minutos demoro el almacenamiento: " ))
    time6 = time5 + timedelta(minutes=Almacenamientos)
    print(time6)
    
    MaxTiempoPorActividad= datetime(time1-time2-time3-time4-time5-time6)
    
    if time6 != horaFinal:
        diferencia= time6 - horaFinal

    with open("resultados.txt","w") as file:
        file.write(f"Programa de inicio     :  {str(time1)} \n")
        file.write(f"Ajustes iniciales      :  {str(time2)} \n")
        file.write(f"Inicio de produccion       :  {str(time3)} \n")
        file.write(f"Reponer materia prima      :  {str(time4)} \n")
        file.write(f"Distribucion de productos      :  {str(time5)} \n")
        file.write(f"Almacenamiento     :  {str(time6)} \n")
        file.write(f"Hora final de actividad con mayor tiempo       :  {str(MaxTiempoPorActividad)} \n")
        file.write(f"Programa de inicio     :  {str(diferencia)} \n")
consolaVB2008()
