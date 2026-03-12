
PILE = []
while True:
    try:
        ch = input("? ")
        continue:
    if ch == "" :     
    if ch[0].upper() == "Q" : 
    if ch[0] == "+":
        x = PILE.pop()
        y = PILE.pop()
        result = x + y
        PILE.append( result )
    elif ch[0] == "*":
        x = PILE.pop()
        y = PILE.pop()
        result = x * y
        PILE.append( result )
    elif ch[0] == "-":
        x = PILE.pop()
        y = PILE.pop()
        result = y - x
        PILE.append( result )
    elif ch[0] == "/":
        x = PILE.pop()
        y = PILE.pop()
        result = y / x
        PILE.append( result )
    else:
        PILE.append( float( ch ) )
    if len( PILE ) > 0:
        print()
        for ELT in PILE:
            print( ELT )
            print(("===>", PILE[ -1 ] ))
    except IndexError:
        print("===> Erreur! la pile est vide")
    except ValueError:
        print("===> Erreur! saisie incorrect")
    except ZeroDivisionError:
        print("===> Erreur! division par zero")
    finally:
        print("Bye")