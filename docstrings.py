""" Organizing data from trending Youtube videos """

class Account:
    """ Users will be able to register and create an account. If they already
    have an account saved then they can just login.
    Attributes:
        create_user(str, int): users when creating accounts will create a username.
        create_password(str, int): users when creating accounts will create a password.
    """
    
    def __init__(self, create_user, create_password):
        """Intializes the Account object"""
        
    def register(self, create_user, create_password, create_email,
                 create_phonenum, login):
        """ Users will register for an account and if they already have an 
        account, they can skip this part and login.
        Args:
            create_user(str, int): users will create a username for registering
            for an account.
            create_password(str, int): users will create a password for
            registering for an account.
            create_email(str, int): users will insert their email account for 
            registering for an account.
            create_phonenum(int): users will insert their phone number for
            registering for an account. 
            login(str): if user already has an account, they can type "login"
            to just only write their username and password.
        Returns:
            str: Account information will be saved onto their account. At the 
            end, users will have something to login. 
        Raises:
            TypeError: no spaces for writing phone numbers and login. Also phone
            numbers need to be an integer. 
        """
    
    def login(self, username_login, password_login, create_password,
              create_username):
        """ Users will login to their already made accounts
        Args:
            username_login(str, int): users will insert their username for an
            already register account.
            password_login(str, int): users will insert their password for an 
            already register account.
            create_username(str, int): users will insert username that they have
            previously created. 
            create_password(str, int): users will insert password that they have 
            previously created.
        Returns:
            str: users will be able to access their saved accounts based on if
            they correctly login. 
        Raises:
            NotImplementError: created username and password need to match with
            each other. 
        """
        
    def save_accountinfo(self, access_accountinfo, edit): 
        """ Users will be able to access their account information
        Args:
            access_accountinfo(str): users will either type yes or no to view
            their account information.
            edit(str): users will be able to redo the account information they
            provided previously if they select yes to edit.
        Returns:
            list: users will see their account information if they selected yes 
            and if they selected no they will move forward with the program. 
        Raises:
            ValueError: value needs to equal yes or no to the question.
        """
        
    def edit_accountinfo(self, edit_yes, edit_no):
        """ Users will be able to edit and save changes on their account 
        information
        Args:
            edit_yes(str): users will be able to redo the account information
            they provided previously if user types yes.
            edit_no(str): if user types no, they will continue on to the next
            thing
        Returns:
            list: user will be able to go back to their account information to
            redo their account information. If the user says no, they will move
            onto picking the five programs of their choice. 
        Raises: 
            TypeError: no spaces for writing phone numbers and login. Also phone
            numbers need to be an integer. 
        """
    
    def intro_program(self, selection, one, two, three, four, five):
        """  Users will have the option to explore fives areas of the program
        when they are done making or loging into their accounts. 
        The five areas options are account information, list of all trending
        youtube videos, youtube channel recommendation system, statistics on
        trending youtube videos to help new or existing creators grow their
        channel, and their bucketlist of channels or videos they would want to
        save into their accounts.
        Args:
            selection(int): user will pick a number to select which area of the
            program they would want to explore.
            one(int): will direct users to their account information.
            two(int): will direct users to the youtube recommendation system.
            three(int): will direct users to the list of trending youtube
            videos.
            four(int): will direct users to the statistics on trending youtube.
            videos that will help new or existing creators grow their channel.
            five(int): will direct users to their bucketlist of videos or
            channels users want to save for future reference. 
        Returns:
            list: program will take them to a list of other selections that they
            can choose from.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list
            will be accepted into the search engine. 
        """
        
class RecommendationSystem:
    """ Recommendation for selecting a specific category the user can view to
    find youtube channels to explore. They can select from a list of youtuber's 
    channel based on their specific category and view that channel top five
    trending videos on Youtube. """
    
    def __init__(self):
        """Initializes the RecommendationSystem Object"""
        
    def mainMenu(self, selection):
        """users will enter a number to select a specific category to view 
        a list of youtube channels based on the category picked by the user.
        
        Args:
            selection(int): user will pick a number to select their choice of
            category.
        Returns:
            list: users will view a list of Youtube channels that they are able 
            to choose based on the number they pick.  
        Raises:
            ValueError: Must select numbers, no strings, floats, or list will be 
            accepted into the search engine. 
        """
    
    def sports(self, sports_tags, extract_videos, sorted_extract, selection):
        """sort list of channel names based on tags matching one or more sport
        tags.
        Args:
            sports_tags(list): list of tags on a youtube video associated with 
            sports.
            extract_videos(list): pick youtube channels based on if the one or 
            more tags matches the sports tag.
            sorted_extract(list): only show users the channel name in 
            alphabetical order.
            selection(int): users will pick a number to select their choice of 
            Youtube channel
        Returns:
            list: Gives a list of the Youtube channels that the users can
            select from to view their top trending videos.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list will be 
            accepted into the search engine. 

        """
    
    def beauty(self, beauty_tags, extract_videos, sorted_extract, selection):
        """
        sort list of channel names based on tags matching one more beauty tags.
        Args:
            beauty_tags(list): list of tags on a youtube video associated with 
            beauty.
            extract_videos(list): pick youtube channels based on if the one or 
            more tags matches the beauty tag.
            sorted_extract(list): only show users the channel name in 
            alphabetical order.
            selection(int): users will pick a number to select their choice of 
            Youtube channel
        Returns:
            list: Gives a list of the Youtube channels that the users can
            select from to view their top trending videos.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list will be 
            accepted into the search engine. 
        """
        
    def comedy(self, comedy_tags, extract_videos, sorted_extract, selection):
        """
        sort list of channel names based on tags matching one more comedy/funny
        video tags.
        Args:
            comedy_tags(list): list of tags on a youtube video associated
            with comedy or anything funny.
            extract_videos(list): pick youtube channels based on if the one
            or more tags matches the comedy tag.
            sorted_extract(list): only show users the channel name in 
            alphabetical order.
            selection(int): users will pick a number to select their choice
            of Youtube channel. 
        Returns:
            list: Gives a list of the Youtube channels that the users can
            select from to view their top trending videos.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list
            will be accepted into the search engine.     
        """
    
    def games(self, games_tags, extract_videos, sorted_extract, selection):
        """
        sort list of channel names based on tags matching one more gaming tags.
        Args:
            games_tags(list): list of tags on a youtube video associated with 
            games.
            extract_videos(list): pick youtube channels based on if the one
            or more tags matches the games tag.
            sorted_extract(list): only show users the channel name in 
            alphabetical order.
            selection(int): users will pick a number to select their choice
            of Youtube channel. 
        Returns:
            list: Gives a list of the Youtube channels that the users can
            select from to view their top trending videos.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list
            will be accepted into the search engine. 
        """
    
    def music(self, music_tags, extract_videos, sorted_extract, selection):
        """
        sort list of channel names based on tags matching one more music tags.
        Args:
            music_tags(list): list of tags on a youtube video associated with 
            music.
            extract_videos(list): pick youtube channels based on if the one
            or more tags matches the music tag.
            sorted_extract(list): only show users the channel name in 
            alphabetical order.
            selection(int): users will pick a number to select their choice
            of Youtube channel. 
        Returns:
            list: Gives a list of the Youtube channels that the users can
            select from to view their top trending videos.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list
            will be accepted into the search engine. 
        """
    
    def random(self, extract_videos, sorted_extract, selection):
        """
        list of channel names that don't associate themselves with any of 
        the category tags listed above.
        Args:
            extract_videos(list): extract youtube channels that have no
            association with any of the particular category. 
            sorted_extract(list): only show users the channel name in 
            alphabetical order.
            selection(int): users will pick a number to select their choice
            of Youtube channel. 
        Returns:
            list: Gives a list of the Youtube channels that the users can
            select from to view their top trending videos.
        Raises:
            ValueError: Must select numbers, no strings, floats, or list
            will be accepted into the search engine. 
        """
    
    def topTrendingVideos(self, extract_videos, videos_sorted, sorted_extract,
                          exit):
        """Users selection of youtube channel will determine the list of
        five trending videos from that channel in order from highest to lowest
        amount of likes.
        Args:
            extract_videos(list): extract the videos based on the channel 
            name the user selected
            videos_sorted(list): sort video in ascending orders based on
            highest to lowest amount of likes
            sorted_extract(list): only show users the title of the video,
            description, amount of views, amount of likes and dislikes on each
            of the video. 
            exit: prompt users to inputed anything so that they can return to 
            the main menu and start from the beginning. 
        Returns: 
            list: Give users based on their input a list of the most 
            trending youtube video from that Youtube channel
        Raises:
            ValueError: Must select numbers, no strings, floats, or list
            will be accepted into the search engine. 
        """     

class Popularvideos:
    """ Users will be able to view top 100 videos on youtube. """
    
    def __init__(self):
        """Initialize the Popularvideos object"""
        
    def prompt_channel_search(self, extract_videos, videos_sorted,
                              sorted_extract, add):
        """
        Args:
            extract_videos(list): extract the videos based on the channel name
            the user inputted.
            videos_sorted(list): sort video in ascending orders based on highest
            to lowest amount of likes.
            sorted_extract(list): only show users the title of the video, 
            channel names, amount of views, amount of likes and dislikes on a
            video.
            add(str, list): write exit to skip this step or write yes to go to
            your bucketlist.
        Returns:
            list: list of channels you can explore. 
        """
        
class Bucketlist:
        """area where you can write down youtube channels you
        would want to delete or save"""
    
    def __init__(self):
        """ Intialize the Bucketlist object"""
        
    def add_list(self, selection, add_channel, add_video, exit):
        """ Ask users if they would like to add any of the channels or videos
        into the list. 
        Args:
            selection(str): user will type yes or no to be able to add to the
            bucket list.
            add_channel(str): user will type in youtube channel what they would
            want save onto their accounts.
            add_video(str): user will type in youtube video they would want
            saved. 
            exit(str): users will type exit to start from the intro_program
            function.  
        Returns: 
            list: users will see a list of youtube videos and channels they
            would want save onto their accounts for future reference. 
        """
        
    def delete_item(self, selection, yes, no):
        """
        Ask users if they would like to delete any of the channels or videos
        into the list.
        Args:
            selection(str): user will be asked yes or no question on if they 
            would want to make any changes to their bucketlist.
            yes(str): user will be asked a yes or no question on whether they
            would want to delete something from their channel or videos on their
            bucketlist.
            no(str): user will type exit to go back to the beginning 
        Returns:
            list: items on the list will be deleted if users wants them to be
            deleted
        """