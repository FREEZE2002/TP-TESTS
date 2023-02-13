import unittest
import parameterized.parameterized

from ..src.Langues.Constantes import Constantes
from ..src.Langues.LangueAnglaise import LangueAnglaise
from ..src.Langues.LangueFrancaise import LangueFrancaise
from utilities.LangueSpy import LangueSpy
from utilities.OhceBuilder import OhceBuilder


class TestPalindrome(unittest.TestCase):
    def test_return_mirror(self):
        string = "toto"

        ohce = OhceBuilder.default()
        result = ohce.palindrome(string)

        self.assertIn(string[::-1], result)

    @parameterized.parameterize(
        (LangueAnglaise(), Constantes.Anglais.WELL_DONE),
        (LangueFrancaise(), Constantes.Francais.BIEN_DIT),
    )
    def test_palindrome_language(self, language, bien_dit):
        palindrome = "radar"

        ohce = OhceBuilder().using_language(language).build()
        result = ohce.palindrome(palindrome)

        self.assertIn(palindrome, result)
        self.assertIn(bien_dit, result[len(palindrome):])

    def test_not_palindrome(self):
        spy_language = LangueSpy()
        ohce = OhceBuilder().using_language(spy_language).build()

        ohce.palindrome("toto")

        self.assertEqual(0, spy_language.well_done_calls)


if __name__ == '__main__':
    unittest.main()