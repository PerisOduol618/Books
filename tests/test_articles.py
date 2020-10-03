import unittest
from app.models import Article
class TestArticle(unittest.TestCase):
    def setUp(self):
        '''
        SetUp method that will run before every Test
        '''
        return Article()
    def test_instance(self):
        self.assertTrue(isinstance(self.setUp(), Article))
if __name__ == '__main__':
    unittest.main()
