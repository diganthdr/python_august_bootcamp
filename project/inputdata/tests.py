import unittest
from inputdata.parse_input import get_input_data

class TestInputData(unittest.TestCase):

    def test_api_connection_wrong_url(self):
        '''
        input: url
        output: None
        '''
        in_url = "https://api.covid1999india.org/state_district_wise.json2"
        ret_val = get_input_data(in_url)
        self.assertEqual(ret_val, None)

    def test_api_connection_right_url(self):
        '''
        input: url
        output: dictionary with some content 
        '''
        in_url = "https://api.covid19india.org/state_district_wise.json"
        ret_val = get_input_data(in_url)
        self.assertTrue(isinstance(ret_val, dict))

    def test_api_connection_right_url_non_json(self):
        '''
        input: url
        output: None
        '''
        in_url = "https://github.com/diganthdr/python_august_bootcamp/issues/1"
        ret_val = get_input_data(in_url)
        self.assertEqual(ret_val, None)


if __name__ == '__main__':
    unittest.main()

