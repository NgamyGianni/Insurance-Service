import unittest
from FacilityProvider import *
class TestFacilityProvider(unittest.TestCase):

    def test_ShouldReturn(self):
        #given
        {'id':'F123456789','montant':'100K','currency':'Euro'}
        facilityProv  = FacilityProvider()
        #when
        facilityInfo = facilityProv.getFacility()
        #then
        self.assertTrue(facilityInfo)

if __name__ == '__main__':
    unittest.main()


    