def heron(a, n = 5, report = False):
    """
    Ermittelt die Quadratwurzel nach dem Näherung von Heron von Alexandria
    """

    an = a
    bn = 1
    if report: print( an , bn )
    for i in range(n):
        an = ( an + bn ) / 2
        bn = a / an
        if report: print( an , bn )

    return an

if __name__ == "__main__":
#    help(heron) # Kommentare ausgeben zu kommentierter Funktion
    a = 5
    n = 5 # Durchäufe
    print("Annähern an die Wurzel von " + str(a) + " Nach Heron von Alexandria in " + str(n) + " Durchläufen")
    h = heron( a , n , False )
    print("Näherung ist " + str(h))
    print("  genau wäre " + str( a** (0.5)))
    