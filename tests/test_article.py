import unittest
from app.models import Article


class ArticleTest(unittest.TestCase):
    '''Test class to test the beahviour of the Article class'''

    def setUp(self):
        '''method that will run before each test case'''
        self.new_article = Article('123','Title of the article','Scott Stein','description of the article','https://www.cnet.com/news/heres-why-we-need-an-iphone-se-2-right-now-wish-list/','https://cnet4.cbsistatic.com/img/ZBhDBbHH44bcXii1YC6Vkqf4p_U=/724x407/2018/12/11/e850b2b2-2ffc-4984-af8a-09a59cbffcb2/iphone-se-1.jpg','2019-02-18T10:47:00Z','content of the article')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()
