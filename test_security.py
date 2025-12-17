import unittest
# Aquesta línia fallarà a l'Evidència 4 perquè security.py encara no existeix
from security import validar_password

class TestSecurity(unittest.TestCase):
    
    def test_password_curt(self):
        # Ha de retornar False si té 8 caràcters o menys
        self.assertEqual(validar_password("12345"), False)

    def test_password_llarg(self):
        # Ha de retornar True si té més de 8 caràcters
        self.assertEqual(validar_password("contrasenyaSegura123"), True)

if __name__ == '__main__':
    unittest.main()
