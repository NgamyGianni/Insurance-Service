import unittest
import requests


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = 'http://127.16.4.19:5000/'

    def test_01_insurance(self):

        #given
        data = {
            "code_insurance" : "L12fd5",
            "name_insurance" : "NATIXIS",
        }

        #when
        r = requests.post(self.BASE_URL + "api/v1/insurances", json=data)
        print("testCreateInsurance" + r.text)

        #then
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_02_GetInsurance(self):
        r = requests.get(self.BASE_URL + "api/v1/insurances")
        print("testGetInsurances" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_03_GetInsuranceId(self):
        r = requests.get(self.BASE_URL + "/api/v1/insurances/IC1")
        print("testGetInsuranceId :" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_04_GetInsurancesByIdDeal(self):
        r = requests.get(self.BASE_URL + "api/v1/deals/D1/insurance-contracts")
        print("GetInsurancesByIdDeal :" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)


if __name__ == '__main__':
    unittest.main()
