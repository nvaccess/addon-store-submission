import unittest
import os
import json
from _tools import validate
from . import SOURCE_DIR

TEMPLATE_FILE = os.path.join(SOURCE_DIR, "_tools", "21.02.json")
JSONSCHEMA = validate.JSONSCHEMA


def getTemplateData():
	with open(TEMPLATE_FILE) as f:
		data = json.load(f)
	return data

class TestValidate(unittest.TestCase):

	def test_validateJson(self):
		data = defTemplateData()
		with self.assertRaises(exceptions.ValidationError):
			validate.validateJson(data)
