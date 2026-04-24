[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y59lTQr6)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23711527)

# Miaunty - Hall

# Integrantes
- Lazcano Flores Valeria 

# Introducción
Un gato hambriento enfrenta tres cajas: solo una guarda un pescado
fresco, las otras esconden pepinos. Después de que el gato selecciona una
de las cajas el humano abre una caja sin pescado y le ofrece la opción de
cambiar. ¿El gato debería seguir su instinto inicial o cambiar su
selección?

Nuestro código simula el famoso problema de Monty Hall, que es un juego de probabilidad con 3 puertas: detrás de una hay premio y detrás de las otras no. La idea es comparar dos estrategias:

1. Cambiar de puerta
2. Quedarse con la elección inicial

# Uso e Instalación
Instalamos los siguientes paquetes:
- `random`: genera números pseudoaleatorios

Posteriormente ejecutamos `monty-hall.py`

# Código Monty Hall
Definimos la función `create_game()`, la cual escoge aleatoriamente la puerta ganadora entre las puertas 1, 2 y 3.
En la funcion `play_change(n)` se simula cuando el gato cambia su selección posteriormente a que el humano haya elegido su puerta, con las condiciones de que el gato no elige la misma puerta que el humano y regresa el porcentaje de que probabilidad hay de que obtenga su pescado.
En la función `play_stay(n)` se simula cuando el gato no cambia su selección posteriormente a que el humano haya elegido su puerta, con las condiciones de que el gato no elige la misma puerta que el humano.
Al ejecutarlo vemos como hay mayor posibilidad de que el gato gane su pescado si cambia de elección. 