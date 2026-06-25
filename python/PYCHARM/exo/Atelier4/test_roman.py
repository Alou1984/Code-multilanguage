import unittest
import roman
import os

NB_SIMPLES = {
    1000:"M", 1333:"MCCCXXXIII", 1651:"MDCLI",
}
NB_COMPLEXES = {
    901:"CMI", 1944:"MCMXLIV", 3999:"MMMCMXCIX"
}

def test_serie( DICO ):
    for nb_arabe, nb_roman in DICO.items():
        assert roman.arabe_to_roman(nb_arabe) == nb_roman

class TestRoman( unittest.TestCase ):
    def tests_simples(self):
        test_serie( NB_SIMPLES )
    def tests_complexes(self):
        test_serie( NB_COMPLEXES )
        
if __name__ == "__main__":
    unittest.main()