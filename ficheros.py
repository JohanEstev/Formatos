
#f = open ("tarea.txt","w")
#f.write("torta")
#f.close


#f = open ("tarea.txt","r")
#mensaje=f.read()
#print(mensaje)
#f.close()



#f = open ("tarea.txt","a")
#f.write("\n"+"hola nuevo mundo")
#f.close()



invitados= open ("invitados.csv","w")
invitados.write("Lista de personas invitadas")
invitados.close

invitados = open ("invitados.csv","a")
persona_1=input("Ingrese nombre invitados :")
persona_2=input("Ingrese nombre invitados : ")
persona_3=input("Ingrese nombre invitados :")
persona_4=input("Ingrese nombre invitados : ")
persona_5=input("Ingrese nombre invitados :")
persona_1.write("\n"+"persona_1")
invitados.write("\n"+"persona_2")
invitados.write("\n"+"persona_3")
invitados.write("\n"+"persona_4")
invitados.write("\n"+"persona_5")
invitados.close()

invitados = open ("invitados.csv","r")
mensaje=invitados.read()
print(mensaje)
invitados.close()