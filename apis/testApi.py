import unittest
import requests


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.BASE_URL = 'http://127.0.0.1:8093/'

    def test_01_insurance(self):

        #given
        data = {
            "code_insurance" : "L12fd5",
            "name_insurance" : "NATIXIS",
        }

        #when
        r = requests.post(self.BASE_URL + "insurances", json=data)
        print("testCreateInsurance" + r.text)

        #then
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_02_getInsurance(self):
        r = requests.get(self.BASE_URL + "insurances")
        print("testGetContract" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_03_GetInsuranceId(self):
        r = requests.get(self.BASE_URL + "insurances/" + str(1))
        print("testGetInsuranceId :" + r.text)
        self.assertEqual(r.status_code, requests.codes.ok)


if __name__ == '__main__':
    unittest.main()
