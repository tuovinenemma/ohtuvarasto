from varasto import Varasto 
import unittest

  

  

class TestVarasto(unittest.TestCase): 

    def setUp(self): 

        self.varasto = Varasto(10) 

        self.varasto_2 = Varasto(-2, -1) 

        self.varasto_3 = Varasto(5, 6) 

  

    def test_konstruktori_luo_tyhjan_varaston(self): 

        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual 

        self.assertAlmostEqual(self.varasto.saldo, 0) 

  

    def test_uudella_varastolla_oikea_tilavuus(self): 

        self.assertAlmostEqual(self.varasto.tilavuus, 10) 

  

    def test_lisays_lisaa_saldoa(self): 

        self.varasto.lisaa_varastoon(8) 

  

        self.assertAlmostEqual(self.varasto.saldo, 8) 

  

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self): 

        self.varasto.lisaa_varastoon(8) 

  

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2 

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2) 

  

    def test_ottaminen_palauttaa_oikean_maaran(self): 

        self.varasto.lisaa_varastoon(8) 

  

        saatu_maara = self.varasto.ota_varastosta(2) 

  

        self.assertAlmostEqual(saatu_maara, 2) 

  

    def test_ottaminen_lisaa_tilaa(self): 

        self.varasto.lisaa_varastoon(8) 

  

        self.varasto.ota_varastosta(2) 

  

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4) 

     

    def test_ota_huonosti_varastosta(self): 

        self.assertEqual(self.varasto.ota_varastosta(-2), 0.0) 

     

    def test_ota_liikaa_varastosta(self): 

        self.varasto.lisaa_varastoon(8) 

  

        self.assertEqual(self.varasto.ota_varastosta(10), 8) 

     

    def test_laita_liikaa_tavaraa(self): 

        self.varasto.lisaa_varastoon(11) 

  

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0) 

  

    def test_ylimaara_hukkaan(self): 

        self.assertEqual(self.varasto_3.saldo, 5) 


    def test_lisaa_miinusta(self): 

        self.varasto.lisaa_varastoon(-1) 

        self.assertEqual(self.varasto.saldo, 0) 


    def test_virheellinen_varaston_tilavuus(self): 

        self.assertEqual(self.varasto_2.tilavuus, 0.0) 

     

    def test_virheellinen_saldo(self): 

        self.assertEqual(self.varasto_2.saldo, 0.0) 

  

    def test_oikea_alkusaldo(self): 

        self.assertEqual(self.varasto.saldo, 0) 

  


     


     

    def test_teksti(self): 

        self.assertEqual(self.varasto.__str__(), 'saldo = 0, vielä tilaa 10') 