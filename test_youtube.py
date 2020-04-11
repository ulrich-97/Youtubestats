import unittest 
from docstrings import Account
from docstrings import RecommendationSystem
from docstrings import Popularvideos
from docstrings import Bucketlist
from pathlib import Path

class TestAccount(unittest.TestCase):
    def test_register(self, create_user, create_password, create_email,
                 create_phonenum, login):
        self.assertIsNotNone(create_user, 'username invalid')
        self.assertIsNotNone(create_password, 'password invalid')
        self.assertIsNotNone(create_email, 'email invalid')
        self.assertEqual(login, ["login"])
        with self.assertRaises(TypeError):
            create_phonenum.split(1)
            login.split(1)
    
    def test_login(self, username_login, password_login, create_password,
                   create_username):
        self.assertEqual(username_login, create_username,'incorrect username')
        self.assertEqual(password_login, create_password,'incorrect password')
        self.assertIn(create_username, create_password,
                      'username and/or password does not match')

    def save_accountinfo(self, access_accountinfo, edit): 
        self.assertEqual(access_accountinfo, ['yes'], ['no'])
        self.assertEqual(edit, ['yes'], ['no'])
        self.assertIsNotNone(access_accountinfo, 'answer invalid')
      
    def edit_accountinfo(self, edit_yes, edit_no):
        self.assertEqual(access_accountinfo, ['yes'], ['no'])
        self.assertEqual(edit_no, ['no'])
        @patch('Account.test_register')
        self.assertEqual(edit, ['yes'])
        self.assertIsNotNone(edit_yes, 'answer invalid')  
        self.assertIsNotNone(edit_no, 'answer invalid')     
        

    def intro_program(self, selection, one, two, three, four, five):
        @patch('Account.save_accountinfo')
        self.assertEqual(selection, ['1'])
        
        @patch('RecommendationSystem.mainMenu')
        self.assertEqual(selection, ['2'])
        
        @patch('Popularvideos.prompt_channel_search')
        self.assertEqual(selection, ['3'])
        
        @patch('Bucketlist.add_list')
        self.assertEqual(selection, ['4'])

        self.assertIsNotNone(selection, 'answer invalid')
        
class RecommendationSystem(unittest.Testcase):
    def mainMenu(self, selection):
        @patch('RecommendationSystem.sports')
        self.assertEqual(selection, ['1'])
        
        @patch('RecommendationSystem.beauty')
        self.assertEqual(selection, ['2'])
        
        @patch('RecommendationSystem.comedy')
        self.assertEqual(selection, ['3'])
        
        @patch('RecommendationSystem.games')
        self.assertEqual(selection, ['4'])
        
        @patch('RecommendationSystem.music')
        self.assertEqual(selection, ['5'])
        
        @patch('RecommendationSystem.random')
        self.assertEqual(selection, ['6'])
        
        self.assertIsNotNone(selection, 'answer invalid')
    
    def sports(self, sports_tags, extract_videos, sorted_extract, selection):
        self.assertIsNotNone(selection, 'answer invalid')
        
    def beauty(self, beauty_tags, extract_videos, sorted_extract, selection):
        self.assertIsNotNone(selection, 'answer invalid')
        
    def comedy(self, comedy_tags, extract_videos, sorted_extract, selection):
        self.assertIsNotNone(selection, 'answer invalid')
        
    def games(self, games_tags, extract_videos, sorted_extract, selection):
        self.assertIsNotNone(selection, 'answer invalid')
        
    def music(self, music_tags, extract_videos, sorted_extract, selection):
        self.assertIsNotNone(selection, 'answer invalid')  
        
    def random(self, random_tags, extract_videos, sorted_extract, selection):
        self.assertIsNotNone(selection, 'answer invalid')
        
    def topTrendingVideos(self, extract_videos, videos_sorted, sorted_extract,
                          exit):
        @patch('Popularvideos')
        self.assertEqual('exit')

class Popularvideos(unittest.Testcase):
    def prompt_channel_search(self, extract_videos, videos_sorted,
                              sorted_extract, add):
        @patch('Bucketlist.add_list')
        self.assertEqual('yes')
        self.assertEqual('exit')
        
class Bucketlist(unittest.Testcase):
    def add_list(self, selection, add_channel, add_video, exit):
        self.assertEqual(yes, 'yes')
        self.assertEqual(no, 'no')
    def delete_item(self, selection, add_channel, add_video, exit):
        self.assertEqual(yes, 'yes')
        self.assertEqual(no, 'no')
if __name__ == '__main__':
    unittest.main()