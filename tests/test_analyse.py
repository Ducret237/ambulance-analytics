
import unittest

from analyse import calculer_statistiques, compter_par_region, compter_regions


class TestAnalyse(unittest.TestCase):

    def test_calcul_statistiques(self):
        interventions = [
            {"region": "Outaouais", "delai_minutes": "8"},
            {"region": "Montréal", "delai_minutes": "12"},
            {"region": "Outaouais", "delai_minutes": "20"}
        ]

        resultat = calculer_statistiques(interventions)

        self.assertEqual(resultat["nombre"], 3)
        self.assertAlmostEqual(resultat["moyenne"], 40 / 3)
        self.assertEqual(resultat["maximum"], 20)

    def test_compter_par_region(self):
        interventions = [
            {"region": "Outaouais"},
            {"region": "Montréal"},
            {"region": "Outaouais"}
        ]

        resultat = compter_par_region(interventions)

        self.assertEqual(resultat["Outaouais"], 2)
        self.assertEqual(resultat["Montréal"], 1)

    def test_liste_vide(self):
        resultat = calculer_statistiques([])

        self.assertEqual(resultat["nombre"], 0)
        self.assertIsNone(resultat["moyenne"])
        self.assertIsNone(resultat["maximum"])

    def test_compter_regions(self):
        interventions = [
            {"region": "Outaouais"},
            {"region": "Montréal"},
            {"region": "Outaouais"}
        ]

        resultat = compter_regions(interventions)

        self.assertEqual(resultat, 2)


if __name__ == "__main__":
    unittest.main()
