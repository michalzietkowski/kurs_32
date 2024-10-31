class PoprosZoneOWyjscieNaPiwo:
    def __enter__(self):
        print("Posprzataj dom")
        print("Wynies smieci")
        print("Odbierz dzieci")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Zona krzyczy, bo znowu sie nachlales")
        print("Kac morderca")


with PoprosZoneOWyjscieNaPiwo():
    print("Pijemy piwo")
    print("Pijemy piwo")
    print("Gramy w gry")