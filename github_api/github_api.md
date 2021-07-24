Module github_api.github_api
============================

Classes
-------

`github_api()`
:   

    ### Methods

    `download_release_asset(self)`
    :   coming soon

    `get_raw_file_content(self)`
    :   coming soon

    `get_release_asset_download_link() ‑> str`
    :   coming soon

    `get_release_download_count(self, repository_full_name: str, release_number: int = 0) ‑> List[tuple]`
    :   :param: release_number (default is 0), the more you increase it, the more the release will be an old one.
        
        :returns: the release download count by assets (list of tuples ('asset_name',downloads_count) (from the lastest release by default) 
        
        :raises: InvalidRepoNameException
        
        :raises: InvalidReleaseIndexException
        
        :raises: NoReleaseException

    `get_release_infos(self, repository_full_name: str, release_number: int = 0) ‑> List[dict]`
    :   :param: release_number (default is 0), the more you increase it, the more the release 
        will be an old one.
        
        :returns: a dict of all the release stats that may be boring but quite usefull sometimes
            
            - creation_date : when the release has been created (str)
        
            - release_date : when the release has been..released :) (str)
        
            - released_by : author of the release (github login) (str)
        
            - version : tag name of the release (ofter the version) (str)
        
            - title : title of the release (str)
        
            - desc : description of the release (str)
        
            - assets : assets files names (list of str)
        
        :raises: InvalidRepoNameException
        
        :raises: InvalidReleaseIndexException
        
        :raises: NoReleaseException

    `get_user_infos(self, username: str) ‑> dict`
    :   get additionnal informations on a user like
        
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
        
        :raises: UserNotFoundException if user is not found
        
        :returns: A dict with the upper specified keys

    `get_user_repos(self, username: str) ‑> list`
    :   list the publics repositories of the specified user
        
        :raises: UserNotFoundException if user is not found
        
        :returns: A list of dict containing repository 'repo_name' and 'repo_url' of user public repositories

    `login()`
    :

    `repo_exists(self, repository_full_name: str) ‑> bool`
    :   :return: True if the repo exists False if not

    `user_exists(self, username: str) ‑> bool`
    :




Exceptions
-------

`InvalidReleaseIndexException(message='Invalid release index. The user must not have released that amount of versions')`
:   Exception raised if you decided to pass a certain release index to get stats not on the lastest but this index does not exists.
    
    Attributes:
        message -- explanation of the error

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

`InvalidRepoNameException(message='Invalid repository name. It must look like : thaaoblues/github_api')`
:   Exception raised if a repository name does not exists or is malformed
    
    Attributes:
        message -- explanation of the error

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

`NoReleaseException(message='No release found. The user must not have released anything.')`
:   Exception raised if you wanted to get stats from a release but the repo does not have any.
    
    Attributes:
        message -- explanation of the error

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

`UserNotFoundException(message='Username not found on github.')`
:   Exception raised if an username don't exists.
    
    Attributes:
        message -- explanation of the error

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException