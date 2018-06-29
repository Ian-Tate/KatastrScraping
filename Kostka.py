class Kostka:


    """
    Třída reprezentující hrací kostku
    """
    def __init__(self, pocet_sten=6):
        self.__pocet_sten = pocet_sten
        """
        Konstruktor kostky, ktery nastaví počet stran. Zároveň není veřejný, takže
        k jeho přístupu potřebujeme metody. Volá se při inicializaci.
        """

    def __str__(self):
        """
        Vrací textovou reprezentaci instance třídy Kostka.
        """
        return str("Kostka s {0} stenami".format(self.__pocet_sten))

    def vrat_pocet_sten(self):
        return self.__pocet_sten

    def hod_kostkou(self):
        import random as _random
        return _random.randint(1,self.__pocet_sten)