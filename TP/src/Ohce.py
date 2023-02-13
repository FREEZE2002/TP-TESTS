class Ohce:
    def init(self, langue, periode_journee):
        self.langue = langue
        self.periode_journee = periode_journee

    def bien_dit(self):
        return self.langue.bien_dit()

    def bonjour(self):
        return self.langue.dire_bonjour(self.periode_journee)

    def au_revoir(self):
        return "Au revoir"

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return self.bonjour() + miroir + (self.bien_dit() if miroir == palindrome else "") + self.au_revoir()