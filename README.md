## Librerias necesarias

**requests**

**BeautifulSoup**


## Uso

``` bash
Mail = TempMail(proxies = None)               # Creamos el hotmail. Si por algún motivo quieren realizar las poticiones con proxies, las deben poner al igual que en requests

Mail.get                               # Obtenemos el hotmail

Mail.Response_Brute()         # Obtenemos el buzón del correo en bruto

Mail.Response_Order()        # Recibimos el buzón del correo con un formato ordenado, el cual contiene una lista que adentro tiene más listas con todos los mensajes recibidos = [[nombre mail, mensaje, hace cuanto lo envio]]

Mail.WaitResponse(stop = 1, cooldown = 0)            # Se ejecuta el codigo hasta que se haya recibido la cantidad de mensajes dichos. tambien se le puede poner un cooldown en segundos de cuanto en cuanto se tienen que realizar peticiones

Mail.Time_Order()               # Te muestra cuanto tiempo lleva creado el hotmail, de no renovarlo se elimina a los 10 minutos. formato de respuesta = [minutos, segundos]

Mail.Time_Seconds()            # Como Time_Order pero la respuesta te la devuelve en segundos

Mail.Reset_Time()                # Si el correo se esta por eliminar por llegar a los 10 minutos puedes poner este comando para que se resetee el tiempo
```
