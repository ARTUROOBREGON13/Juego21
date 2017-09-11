from random import *

def gen_mazo():
    return sample([(x,y) for x in['A','J','Q','K']+range(2,11) for y in ['C','D','P','T']],52)

def valor_carta(carta):
    if str(carta[0]) in "JQK":
        return 10
    if str(carta[0]) == 'A':
        return 11
    return int(carta[0])

def valor_mano(mano):
    if mano==[]:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_mano2(mano):
    if mano==[]:
        return 0
    elif mano[0][0] == 'A':
        return 1 + valor_mano2(mano[1:])
    else:
        return valor_carta(mano[0]) + valor_mano2(mano[1:])

def mostrar_mano(mano):
    if mano == []:
        return ""
    return str(mano[0][0]) + " " + str(mano[0][1]) + "  " + mostrar_mano(mano[1:]) 

def juego_nuevo():
    if str(raw_input("Desea jugar otra ronda? (Y/N)\n")) == "Y":
        print("\n")*10
        return jugar([],[],[],False)
    else :
        return 0

def jugar(mano_casa, mano_jug, mazo, mostrar):
    if mazo == []:
        return jugar([],[],gen_mazo(), mostrar)
    if mano_casa == [] and mano_jug == []:
        return jugar([mazo[0],mazo[1]],[mazo[2],mazo[3]],mazo[4:],mostrar)
    if valor_mano(mano_casa)<22 and valor_mano(mano_jug)<22:
        if mostrar:
            print("Casa: " + mostrar_mano(mano_casa) + "\n")
        else:
            print("Casa: " + str(mano_casa[0][0]) + " " + str(mano_casa[0][1]) + "  -- --\n")
        print("Jugador: " + mostrar_mano(mano_jug) + "\n")
        if not mostrar:
            if str(raw_input("Desea otra carta? (Y/N)\n")) == "Y":
                return jugar(mano_casa,mano_jug + [mazo[0]], mazo[1:], mostrar)
            else:
                return jugar(mano_casa,mano_jug , mazo, True)

        if valor_mano(mano_casa) < valor_mano(mano_jug):
            return jugar(mano_casa + [mazo[0]], mano_jug, mazo[1:], mostrar)           
        else:
            print("Gana la casa\n")
            return juego_nuevo()
    if valor_mano(mano_jug)>21:
        if valor_mano2(mano_jug)>21:
            print("Casa: " + mostrar_mano(mano_casa) + "\n")
            print("Jugador: " + mostrar_mano(mano_jug) + "\n")
            print("Gana la casa\n")
            return juego_nuevo()
        else:
            if valor_mano(mano_casa)<22 and valor_mano2(mano_jug)<22:
                if mostrar:
                    print("Casa: " + mostrar_mano(mano_casa) + "\n")
                else:
                    print("Casa: " + str(mano_casa[0][0]) + " " + str(mano_casa[0][1]) + "  -- --\n")
                print("Jugador: " + mostrar_mano(mano_jug) + "\n")
                if not mostrar:
                    if str(raw_input("Desea otra carta? (Y/N)\n")) == "Y":
                        return jugar(mano_casa,mano_jug + [mazo[0]], mazo[1:], mostrar)
                    else:
                        return jugar(mano_casa,mano_jug , mazo, True)

                if valor_mano(mano_casa) < valor_mano2(mano_jug):
                    return jugar(mano_casa + [mazo[0]], mano_jug, mazo[1:], mostrar)
                else:   
                    print("Gana la casa\n")
                    return juego_nuevo()
    if valor_mano(mano_casa)>21:
        if valor_mano2(mano_casa)>21:            
            print("Casa: " + mostrar_mano(mano_casa) + "\n")
            print("Jugador: " + mostrar_mano(mano_jug) + "\n")
            print("Gana el jugador\n")
            return juego_nuevo()
        if valor_mano2(mano_casa) < valor_mano(mano_jug) or valor_mano2(mano_casa) < valor_mano2(mano_jug):
            return jugar(mano_casa + [mazo[0]], mano_jug, mazo[1:], mostrar)
        else: 
            print("Gana la casa\n")
            return juego_nuevo()
        
jugar([],[],[],False)
