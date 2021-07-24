from requests import get
from typing import List


class GithubHTTPApi():


    def __init__(self):
        self.ac_username = ""
        self.ac_password = ""

        #best api endpoints 
        self.base_repos_url = "https://api.github.com/repos/"
        self.base_user_url = "https://api.github.com/users/"
        self.base_raw_url = "https://raw.githubusercontent.com/"

    def login():
        pass

    #private methods :




    def __is_json_key(self,json:dict,key:str) -> bool:
        try:
            json[key]
            return True
        except:
            return False



    #public methods :
    def user_exists(self,username:str)->bool:

        #check if user exists
        if self.__is_json_key(get(self.base_user_url+username).json(),"message"):
            return False
        else:
            return True
        


    def get_user_repos(self,username:str)-> list:

        """
        list the publics repositories of the specified user

        :raises: UserNotFoundException if user is not found

        :returns: A list of dict containing repository 'repo_name' and 'repo_url' of user public repositories 
        
        """
        
        if not self.user_exists(username):
            raise UserNotFoundException


        json = get(f"{self.base_user_url}{username}/repos").json()
        repos_names = [repo['full_name'] for repo in json]
        repos_urls = [repo['html_url'] for repo in json]
        

        ret = []
        for i in range(len(repos_names)):
            ret.append({'repo_name':repos_names[i],'repo_url':repos_urls[i],})
        
        
        return ret


    def repo_exists(self,repository_full_name:str) -> bool:
        """
        
        :return: True if the repo exists False if not

        """

        if self.__is_json_key(get(f"{self.base_repos_url}{repository_full_name}/releases").json(),'message'):
            return False

        else:
            return True





    def get_release_download_count(self,repository_full_name:str,release_number:int=0) -> List[tuple]:
        """
        
        :param repository_full_name: the repository full name like thaaoblues/github_api

        :param release_number: (default is 0), the more you increase it, the more the release 
        will be an old one.


        :returns: the release download count by assets (list of tuples ('asset_name',downloads_count) (from the lastest release by default) 

        :raises InvalidRepoNameException:

        :raises InvalidReleaseIndexException:

        :raises NoReleaseException:
        
        """

        #get http response content
        json = get(f"{self.base_repos_url}{repository_full_name}/releases").json()


        #takes care of exceptions
        if json == []:
            raise NoReleaseException

        elif not self.repo_exists(repository_full_name):
            raise InvalidRepoNameException

        elif release_number > len(json):
            raise InvalidReleaseIndexException

        
        release_json = json[release_number]
        assets = release_json['assets']

        return [(asset['name'],asset['download_count']) for asset in assets]

    


    def get_release_infos(self,repository_full_name:str,release_number:int=0) -> List[dict]:

        """

        :param repository_full_name: the repository full name like thaaoblues/github_api

        :param release_number: (default is 0), the more you increase it, the more the release 
        will be an old one.

        :returns: a dict of all the release stats that may be boring but quite usefull sometimes
            
            - creation_date : when the release has been created (str)

            - release_date : when the release has been..released :) (str)

            - released_by : author of the release (github login) (str)

            - version : tag name of the release (ofter the version) (str)

            - title : title of the release (str)

            - desc : description of the release (str)

            - assets : assets files names (list of str)

        :raises InvalidRepoNameException:

        :raises InvalidReleaseIndexException:

        :raises NoReleaseException:

        """

        #get http response content
        json = get(f"{self.base_repos_url}{repository_full_name}/releases").json()

        #takes care of exceptions
        if json == []:
            raise NoReleaseException
        elif not self.repo_exists(repository_full_name):
            raise InvalidRepoNameException
        elif release_number > len(json):
            raise InvalidReleaseIndexException

        #now that we are sure no errors are coming, get the right release
        json = json[release_number]

        return {'title':json['name'],'version':json['tag_name'],'desc':json['body'],"creation_date":json['created_at'],"release_date":json['published_at'],"released_by":json['author']['login'],"assets":[asset[0] for asset in self.get_release_download_count(repository_full_name,release_number=release_number)]}

        
    

    def get_raw_file_content(self,repository_full_name:str,file_name:str) -> str:
        """
        :param repository_full_name: the repository full name like thaaoblues/github_api
        
        :param file_name: the file which you wanna get the raw content

        :raises InvalidRepoNameException:

        :raises UnknownFileException:

        :returns: a string containing the raw file content
        """



        if not self.repo_exists(repository_full_name):
            raise InvalidRepoNameException


        content = get(f"{self.base_raw_url}{repository_full_name}/master/{file_name}").text
        
        if content == "404: Not Found":
            raise UnknownFileException

        return content
        

    def get_release_asset_download_link(self,repository_full_name:str,asset_name:str,release_number:int=0) -> str:
        """

        :param repository_full_name: the repository full name like thaaoblues/github_api

        :param asset_name: the release asset file name 

        :param release_number:  (default is 0), the more you increase it, the more the release 
        will be an old one.

        :returns: a string containing the release asset's download url

        :raises InvalidRepoNameException:

        :raises InvalidReleaseIndexException:

        :raises NoReleaseException:

        :raises UnknownAssetException:
        """

        #get http response content
        json = get(f"{self.base_repos_url}{repository_full_name}/releases").json()


        #takes care of exceptions
        if json == []:
            raise NoReleaseException

        elif not self.repo_exists(repository_full_name):
            raise InvalidRepoNameException

        elif release_number > len(json):
            raise InvalidReleaseIndexException

        json = json[release_number]

        for asset in json['assets']:
            if asset['name'] == asset_name:
                return asset['browser_download_url']

        raise UnknownAssetException

    def download_release_asset(self,repository_full_name:str,asset_name:str,release_number:int=0,output_path:str=""):
        """

        :param repository_full_name: the repository full name like thaaoblues/github_api

        :param asset_name: the release asset file name

        :param release_number:  (default is 0), the more you increase it, the more the release 
        will be an old one.

        :param output_path: (default is cwd), the path where the asset will be stored after download. 

        :returns: nothing

        :raises InvalidRepoNameException:

        :raises InvalidReleaseIndexException:

        :raises NoReleaseException:

        :raises UnknownAssetException:
        """
        

        url = self.get_release_asset_download_link(repository_full_name,asset_name,release_number=release_number)

        with open(f"{output_path}/{asset_name}" if output_path != "" else asset_name,"wb") as f:
            f.write(get(url).content)
            f.close()
        


    def get_user_infos(self,username:str) -> dict:

        """
        get additionnal informations on a user like

        - id (str)
        
        - bio (str)
        
        - name (str)
        
        - twitter_account (null if not) (str)
        
        - followers (list of usernames)
        
        - following (list of usernames)
        
        - starred_repos (list of urls)
        
        - blog_url (null if not) (str)
        
        - is_hireable (null if not specified) (bool)
        
        - email (null if not specified) (str)
        
        - user_location (null if not specified) (str)
        
        - user_type (str)
        
        - avatar_url (str)
        
        - company (str)
        
        - creation_date (str)

        :raises UserNotFoundException if user is not found:

        :returns: A dict with the upper specified keys

        """

        if not self.user_exists(username):
            raise UserNotFoundException

        #getting basic infos
        json = get(self.base_user_url+username).json()

        #getting infos from special urls
        followers = get(json['followers_url']).json()
        following = get(str(json['following_url']).replace("{/other_user}","",1)).json()
        starred_repos = [repo['html_url'] for repo in get(json['starred_url'].replace("{/owner}{/repo}","",1)).json()]

        return {"id": json['id'],"bio":json['bio'],"name":json['name'],"twitter_account":json['twitter_username'],"followers" : [f['login'] for f in followers], "following":[f['login'] for f in following],"starred_repos": starred_repos,"blog_url":json['blog'],"is_hireable":json['hireable'],"email":json['email'],"user_location":json['location'],"user_type":json['type'],"avatar_url":json['avatar_url'],"company":json['company'],"creation_date":json['created_at']}





class UserNotFoundException(Exception):
    """
    Exception raised if an username don't exists.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message="Username not found on github."):
        self.message = message
        super().__init__(self.message)


class InvalidRepoNameException(Exception):
    """
    Exception raised if a repository name does not exists or is malformed

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message="Invalid repository name. It must look like : thaaoblues/github_api"):
        self.message = message
        super().__init__(self.message)

class InvalidReleaseIndexException(Exception):
    """
    Exception raised if you decided to pass a certain release index to get stats not on the lastest but this index does not exists.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message="Invalid release index. The user must not have released that amount of versions"):
        self.message = message
        super().__init__(self.message)


class NoReleaseException(Exception):
    """
    Exception raised if you wanted to get stats from a release but the repo does not have any.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message="No release found. The user must not have released anything."):
        self.message = message
        super().__init__(self.message)



class UnknownAssetException(Exception):
    """
    Exception raised if you wanted to get download url for a specific release's asset but no assets has this name.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message="No release's assets found with this name."):
        self.message = message
        super().__init__(self.message)



class UnknownFileException(Exception):
    """
    Exception raised if you wanted to get raw content for a specific file but the file does not exists.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message="No file found with this name."):
        self.message = message
        super().__init__(self.message)