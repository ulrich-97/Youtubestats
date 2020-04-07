""" Organizing data from trending Youtube videos """

Class SearchEngine:
    """ Search bar for finding a youtuber's channel trending videos (organized based from highest to lowest amount of likes)

    Attributes:
        prompt(str): user inputs a Youtube channel's name
        extract_videos(list): extract the videos based on the channel name the user inputted
        videos_sorted(list): sort video in ascending orders based on highest to lowest amount of likes
        sorted_extract(list): only show users the title of the video, amount of views, amount of likes and dislikes on a video
    Returns: 
        list: Give users based on their input a list of the most trending youtube video from that Youtube channel
    Raises:
        ValueError: Users are only able to search for channel names

"""
    def __init__ (self):
        #attrbutes 
    
    def prompt_channel_search(self, prompt, extract_videos, videos_sorted, sorted_extract):
        """prompt user to search for Youtube channel name and sort the list of trending videos based on highest to lowest amount of likes
                Args:
                    prompt(str): the value to use for the prompt attribute
                    extract_videos (list):
                    videos_sorted (list):
                    sorted_extract (list):
        """