from Langues.Constantes import Constantes
from PeriodeDeLaJournee import PeriodeDeLaJournee


class LangueFrancaise:
    def __init__(self):
        self.BONJOUR = "Bonjour"
        self.BONSOIR = "Bonsoir"
        self.BIEN_DIT = "Bien dit"

    def dire_bonjour(self, periode_journee):
        if periode_journee in (PeriodeDeLaJournee.SOIR, PeriodeDeLaJournee.NUIT):
            return self.BONSOIR
        else:
            return self.BONJOUR

    def bien_dit(self):
        return self.BIEN_DIT
