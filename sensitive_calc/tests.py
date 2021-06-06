from django.test import TestCase
from .score import sensitivity

class SensitiveScoreTestCase(TestCase):
    def test_document_1(self):
        blurb = """
            this file has 5 charecters
            secret
            dathena
        """
        self.assertEquals(sensitivity(blurb),17)
    
    def test_document_2(self):
        blurb = """
            this file has 5 charecters
            and another 26 characters - 56
            secret public
        """
        self.assertEquals(sensitivity(blurb),11)
    
    def test_document_3(self):
        blurb = """
            This is a top secret file.
            All these information are not meant to be external purposes.
            Regards,
            Joker.
            Dathena
        """
        self.assertEquals(sensitivity(blurb),20)