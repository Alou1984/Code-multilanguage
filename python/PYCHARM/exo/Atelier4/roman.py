import roman
def arabe_to_roman(nombre):
    """
    arabe_to_roman( nombre: int ) -> str
    - nombre: un nombre en chiffre arabe
    - valeur de retour: une chaine faite de chiffres romains
    """
    nb_qui_retreci = nombre
    nb_romain = ""
    while nb_qui_retreci > 0:
        # trouver la valeur la plus grande inferieur au nombre
        vmax = 0
        for x in sorted(ARABE_EQUIV_ROMAN.keys()):
            if x > nb_qui_retreci:
                break
            else:
                vmax = x
        nb_romain += ARABE_EQUIV_ROMAN[vmax]
        nb_qui_retreci -= vmax
    return nb_romain
    if __name__ == "__main__":
        print(">>>1863: ", arabe_to_roman(1863))
