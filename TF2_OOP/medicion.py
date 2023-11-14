import re


class Medicion:
    def __init__(self, muestra, especie, pplant, pconfig, pini, pfin):
        self.set_muestra(muestra)
        self.set_especie(especie)
        self.set_pplant(pplant)
        self.set_pconfig(pconfig)
        self.set_pini(pini)
        self.set_pfin(pfin)

    def set_muestra(self, muestra):
        # Validar que muestra contiene solo alfanuméricos
        if re.match("^[A-Za-z0-9]+$", muestra):
            self.muestra = muestra
        else:
            raise ValueError("La muestra debe contener solo alfanuméricos")

    def set_especie(self, especie):
        self.especie = especie

    def set_pplant(self, pplant):
        self.pplant = pplant

    def set_pconfig(self, pconfig):
        self.pconfig = pconfig

    def set_pini(self, pini):
        self.pini = pini

    def set_pfin(self, pfin):
        self.pfin = pfin
