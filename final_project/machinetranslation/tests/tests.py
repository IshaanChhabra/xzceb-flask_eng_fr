import unittest
from deep_translator import MyMemoryTranslator
def englishToFrench(englishText):
    frenchText=MyMemoryTranslator(source="english",target="french").translate(englishText)
    return frenchText
def frenchToEnglish(frenchText):
    englishText=MyMemoryTranslator(source="french",target="english").translate(frenchText)
    return englishText

class TestEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("bonjour"), "hello")
        self.assertEqual(frenchToEnglish("moi"), "me")
        self.assertNotEqual(frenchToEnglish("moi"), "mouse")
        
class TestFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("hello"), "bonjour")
        self.assertNotEqual(englishToFrench("mouse"), "moi")

unittest.main()