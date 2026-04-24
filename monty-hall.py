import random
def create_game()->int:
    """Escoge la puerta ganadora"""
    return random.randint(0, 2)

def play_change(n:int = 1000) -> float:
    """
    Juega monty-hall con la estrategia de cambiar la puerta
    Regresa la tasa de éxito
    """
    exito = 0
    for _ in range(n):
        ganador = create_game()
        elec_inicial = random.randint(0, 2)
        puertas = [i for i in range(3)
        if i != ganador and i != elec_inicial]
        abierto = random.select(puertas)
    
        nueva_opcion = [i for i in range(3)
        if i != elec_inicial and i != abierto][0]
        
        if nueva_opcion == ganador:
            exito += 1
            
    return exito/n
    
def play_stay(n:int = 1000)->float:
    """Juega monty-hall con la estrategia de NO cambiar la puerta"""
    exito = 0
    for _ in range(n):
        ganador = create_game()
        elec_inicial = random.randint(0, 2)
    
        if elec_inicial == ganador:
            exito += 1
            
    return exito/n

def main():
    success_change = play_change()
    success_stay   = play_stay()
    print(f"{success_change=} {success_stay=}")


if "__name__" == "__main__":
    main()