import unittest
from utilities import *
from parameterized import *


class SalutationTest(unittest.TestCase):
    @parameterized.expand(
        [
            [LangueAnglaise(), Periodes.DEFAULT, Constantes.Anglais.HELLO],
            [LangueAnglaise(), Periodes.MATIN, Constantes.Anglais.GOOD_MORNING],
            [LangueAnglaise(), Periodes.APRES_MIDI, Constantes.Anglais.GOOD_AFTERNOON],
            [LangueAnglaise(), Periodes.SOIR, Constantes.Anglais.GOOD_EVENING],
            [LangueAnglaise(), Periodes.NUIT, Constantes.Anglais.GOOD_NIGHT],
            [LangueFrancaise(), Periodes.DEFAULT, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), Periodes.MATIN, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), Periodes.APRES_MIDI, Constantes.Francais.BONJOUR],
            [LangueFrancaise(), Periodes.SOIR, Constantes.Francais.BONSOIR],
            [LangueFrancaise(), Periodes.NUIT, Constantes.Francais.BONSOIR],
        ])
    def test_bonjour(self, langue, periode, attendu):
        ohce = OhceBuilder().ayant_pour_langue(langue).ayant_pour_periode(periode).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), Periodes.DEFAULT, Constantes.Anglais.GOOD_BYE],
            [LangueFrancaise(), Periodes.DEFAULT, Constantes.Francais.AU_REVOIR],
        ])
    def test_au_revoir(self, langue, periode, salutation):
        ohce = OhceBuilder().ayant_pour_langue(langue).ayant_pour_periode(periode).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(salutation, resultat[-len(salutation):])