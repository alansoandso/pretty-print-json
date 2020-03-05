# -*- coding: utf-8 -*-
import unittest
from ppjson.ppj import show_json


class TestPPJ(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_unicoded(self):
        raw_data = (
            "{u'RS_001460': [{u'765095806066017': u'SKY_MM2'}], u'RS_001461': [{u'320082899500852': u'SKY_MM1'}], u'RS_001462': [{u'215012105756500': u'SKY_MG'}], "
            "u'RS_001463': [{u'700351138133376': u'SKY_DISNEY'}],u'RS_001464': [{u'897950621578257': u'SKY_SP1'}], u'RS_001465': [{u'240034520929200': u'SKY_SP2'}], "
            "u'RS_001466': [{u'263285605830995': u'SKY_SP3'}], u'RS_001467': [{u'128499894876690': u'SKY_SP5'}], u'RS_001469': [{u'461250645709477': u'SKY_DTHMC'}]}"
        )
        expected = (
            '{"RS_001460": [{"765095806066017": "SKY_MM2"}],\n'
            ' "RS_001461": [{"320082899500852": "SKY_MM1"}],\n'
            ' "RS_001462": [{"215012105756500": "SKY_MG"}],\n'
            ' "RS_001463": [{"700351138133376": "SKY_DISNEY"}],\n'
            ' "RS_001464": [{"897950621578257": "SKY_SP1"}],\n'
            ' "RS_001465": [{"240034520929200": "SKY_SP2"}],\n'
            ' "RS_001466": [{"263285605830995": "SKY_SP3"}],\n'
            ' "RS_001467": [{"128499894876690": "SKY_SP5"}],\n'
            ' "RS_001469": [{"461250645709477": "SKY_DTHMC"}]}'
        )
        self.assertMultiLineEqual(show_json(raw_data), expected)

    def test_escaped_quotes(self):
        raw_data = '{\"charges\": [{\"rate\": \"11.25\", \"rateId\": \"138870001\", \"categoryId\": \"00002\"}, {\"rate\": \"17.50\", \"rateId\": \"138930001\", \"categoryId\": \"00001\"}]}'
        expected = (
            '{"charges": [{"categoryId": "00002", "rate": "11.25", "rateId": "138870001"},\n'
            '             {"categoryId": "00001", "rate": "17.50", "rateId": "138930001"}]}'
        )
        self.assertMultiLineEqual(show_json(raw_data), expected)

    def test_valid_json(self):
        raw_data = (
            '{"charges": [{"categoryId": "00002", "rate": "11.25", "rateId": "138870001"},\n'
            '             {"categoryId": "00001", "rate": "17.50", "rateId": "138930001"}]}'
        )
        expected = (
            '{"charges": [{"categoryId": "00002", "rate": "11.25", "rateId": "138870001"},\n'
            '             {"categoryId": "00001", "rate": "17.50", "rateId": "138930001"}]}'
        )
        self.assertMultiLineEqual(show_json(raw_data), expected)

    def test_not_valid_json(self):
        raw_data = '('
        self.assertRegex(show_json(raw_data), 'Not valid JSON')

    def test_not_valid_json_multiline(self):
        raw_data = 'one, two'
        expected = (
            'Not valid JSON\n'
            'one,\n'
            ' two'
        )
        self.assertMultiLineEqual(show_json(raw_data), expected)

    def test_over_escaped_quotes(self):
        raw_data = '{\"customer \\\\\\\"quote\\\\\\\"  \": {\"partyId\": \"11111111111111111112351\", "amount":"£99.99"}}'
        expected = '{"customer quote  ": {"amount": "£99.99", "partyId": "11111111111111111112351"}}'
        self.assertEqual(show_json(raw_data), expected)


