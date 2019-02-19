import unittest
from app.models import Source



class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,'Al Jazeera','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

if __name__ == '__main__':
    unittest.main()
