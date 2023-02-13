from Langues.Constantes import Constantes
from PeriodeDeLaJournee import PeriodeDeLaJournee

class LangueAnglaise:

    def dire_bonjour(self, periode_journee):
        if periode_journee == PeriodeDeLaJournee.MATIN:
            return Constantes.Anglais.GOOD_MORNING
        elif periode_journee == PeriodeDeLaJournee.APRES_MIDI:
            return Constantes.Anglais.GOOD_AFTERNOON
        elif periode_journee == PeriodeDeLaJournee.SOIR:
            return Constantes.Anglais.GOOD_EVENING
        elif periode_journee == PeriodeDeLaJournee.NUIT:
            return Constantes.Anglais.GOOD_NIGHT

        return Constantes.Anglais.HELLO

    def bien_dit(self):
        return Constantes.Anglais.WELL_DONE
