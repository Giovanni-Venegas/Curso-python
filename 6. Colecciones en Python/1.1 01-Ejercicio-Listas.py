#Declarar una lista
#Indices:
#0-Juan
#1-Karla
#2-Ricardo
#3-María
nombres = ["Juan", "Karla", "Ricardo", "María"]
#imprimir la lista
print(nombres)
#Acceder a los elementos de una lista
print(nombres[0]) #imprime el primer elemento
print(nombres[1]) #imprime el segundo elemento
#Navegacion inversa
print(nombres[-1]) #imprime el último elemento)
#Imprime un rango 
print(nombres[0:2])#sin incluir el indice 2
#ir del inicio al indice indicado
print(nombres[:3])#sin incluir el indice 3
#ir del índice indicado al final
print(nombres[1:]) 
#cambiar un valor de la lista
nombres[3] = "Ivone"
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
#revisar si existe un elemento en la lista
if "Carla" in nombres:
    print("Karla si existe en la lista de nombres")   
else:
    print("No existe en la lista de nombres")     
#preguntar el largo de una lista
print(len(nombres))    
#agregar un elemento
nombres.append("Lorenzo")
print(nombres)
#insertar un elemento en el índice indicada
nombres.insert(1, "Octavio")
print(nombres)
#remover el elemento proporcionado
nombres.remove("Octavio")
print(nombres)
#remover el último elemento agregado
nombres.pop()
print(nombres)
#remueve el indice indicado
del nombres[0]
print(nombres)
#limpiar la lista
nombres.clear()
print(nombres)
#borrar la lista por completo
del nombres
print(nombres){"threads":[{"position":0,"start":0,"end":708,"connection":"open"},{"position":1415,"start":709,"end":1415,"connection":"closed"}],"url":"https://att-a.udemycdn.com/2020-03-27_02-30-12-ce1e4ff7803e41a638bfbd74b2d976f8/original.py?eTtVrXxT2W_wVb3JQ_dsXIYF-WsZ5fE0rmoSrngMMO1uixqow53Q0RUY1YOjPRkCsjA7lIoN5bmpwTlY2MR-DusNc2RIOBV8_kdd3JI18MS7_nOEZLsk0_3k7JkRTIyKG53hUQX-VaI5VyknwXEx9e3XofgOHriK2GzHpE6MqA","method":"GET","port":443,"downloadSize":1415,"headers":{"accept-ranges":"bytes","access-control-allow-origin":"*","age":"361229","content-disposition":"attachment","content-type":"text/plain","date":"Fri, 24 Apr 2020 05:36:07 GMT","etag":"\"c43cf4d8de7c322fa07b6f70ab725781\"","last-modified":"Fri, 27 Mar 2020 02:30:13 GMT","server":"ECAcc (dcb/7F1A)","x-amz-id-2":"/shKoo+3HsCunjEW5t5Jl/MsgTGG8MNKPILreC0oLxWccjfeQjRccRBBBOvHyU3bb6X7ANNYgUg=","x-amz-meta-qqfilename":"01-Ejercicio-Listas.py","x-amz-request-id":"BCECA71D79B05200","x-amz-version-id":"DpTar9xz7iKFZR2C6Eh93HVt.qTx.qiY","x-cache":"HIT","content-length":"1415","connection":"close"}}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     