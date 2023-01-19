class kilpailija:

    pisteet = 0
    vari = ""

    def lisaa_pisteet(self, lisays=1):
        self.pisteet = + lisays

    def lisaa_vari(self, valinta):
        self.vari = valinta

    def tulostus(self):
        print("Kilpailijalla",self.vari,"on",self.pisteet,"pistettä!")


def main():
    eka = kilpailija()
    eka.lisaa_vari("Sininen")
    eka.lisaa_pisteet(10)
    eka.tulostus()


if __name__ == "__main__":
    main()
