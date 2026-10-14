# Port Scanner en Python

Escáner de puertos básico hecho con la librería `socket` de Python. Recorre los puertos 1 a 1024 de una dirección IP y muestra cuáles están abiertos y qué servicio suelen usar. Proyecto educativo de ciberseguridad.

## Advertencia legal

Escanear puertos sin autorización es ilegal en muchos países. Usa este programa únicamente en redes y equipos propios o con permiso expreso del dueño.

## Cómo funciona

1. Pide una dirección IP.
2. Intenta conectarse a cada puerto del 1 al 1024 con un tiempo de espera de 0,5 segundos.
3. Si la conexión es exitosa, imprime el puerto y el nombre del servicio (por ejemplo `http`, `ssh`).

## Requisitos

- Python 3.x
- No necesita librerías externas.

## Uso

```bash
git clone https://github.com/pagarcia22/post-scanner.git
cd post-scanner
python Scanner.py
```

Ejemplo (en tu propio equipo):

```
IP a escanear: 127.0.0.1
Escaneando 127.0.0.1...
Puerto 80 abierto (http)
```

## Limitaciones y mejoras pendientes

- Escanea los puertos de uno en uno; usar hilos o `concurrent.futures` lo haría mucho más rápido.
- El rango de puertos está fijo (1-1024); pasarlo como parámetro.
- Falta manejo de errores para IPs inválidas.
