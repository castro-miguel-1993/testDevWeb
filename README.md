# Prueba de Desarrollo Web

Resolucion de 3 ejercicios, usando Django como backend y Vue.js como frontend.
## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


## Pre-requisitos 📋

- Tener instalado git en nuestra computadora, pueden descargar por este enlace, elegir su s.o. y siguiendo las instrucciones de instalacion: [Descarga git](https://git-scm.com/downloads "Descarga git")
- Instalar python (la version usada es la 3.7.7) que se puede obtener de este enlace: [python 3.7.7](https://www.python.org/downloads/release/python-377/ "python 3.7.7")
- Instalar Nodejs (la version usada es la 12.16.1) descargue el archivo de su preferencia a instalar: [nodejs v12.16.1](https://nodejs.org/download/release/v12.16.1/ "nodejs v12.16.1")

## Instalación 🔧

Ahora que tenemos git podemos proceder a la instalacion y configuracion de nuestro proyecto:
1. clonamos el repositorio del proyecto:

`> git clone https://github.com/castro-miguel-1993/testDevWeb.git`

### Configuraciones para el Backend
2. Abrimos la consola de comandos en la raiz del repositorio y escribimos lo siguiente:

`> $ pip install -r requirements.txt`

_-esto instalará las dependencias necesarias para correr el backend_

3. Al terminar la instalacion del requirements, escriba el siguiente comando:

`> python run server`


### Configuraciones para el Frontend
4. como estamos `/testDevWeb` por la consola ingresamos a la subcarpeta `/testDevWeb/frontend` y ahi ejecutamos el comando:

`> npm install`

_-esto instalará las dependencias necesarias para correr el frontend_

5. Al terminar esta instalacion ejecutamos el siguiente comando, para poner en marcha el frontend:

`> npm run dev`

## Ejecución de ejercicios

#### EJERCICIO #1 : Liga de Padel

**Ejemplo de Entrada**

```html
Junior
Buenisimos 3 Malisimos 0
Buenillos 2 Malillos 1
Buenillos 3 Malisimos 0
Buenisimos 3 Malillos 0
Buenisimos 2 Buenillos 1
Malisimos 0 Buenisimos 3
Malillos 1 Buenillos 2
Malisimos 0 Buenillos 3
Malillos 0 Buenisimos 3
Buenillos 1 Buenisimos 2
FIN
Senior
Abuelos 3 Abueletes 0
Abueletes 2 Abuelos 1
FIN
```
**Ejemplo de Salida**

```html
Buenisimos 12
EMPATE 0
```
## Construido con 🛠️
- [DJANGO](https://www.djangoproject.com/ "DJANGO") - Framework backend.
- [DjangoRESTframework](https://www.django-rest-framework.org/ "DjangoRESTframework") - Herramienta para construir APIs
- [VUE.JS](https://vuejs.org/") - Framework frontend.
- [AXIOS](https://github.com/axios/axios "AXIOS") - Librería para consumir APIs

------------

⌨️ con ❤️ por [Miguel Castro](https://github.com/castro-miguel-1993 "Miguel Castro") 😊
