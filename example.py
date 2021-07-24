from github_api import GithubHTTPApi


gh = GithubHTTPApi()


#all functions
print(gh.get_raw_file_content("thaaoblues/github_api","README.md"))

print(gh.get_user_infos("thaaoblues"))

print(gh.get_user_repos("thaaoblues"))

print(gh.get_release_download_count("copypastaofficial/copypasta",release_number=0))

print(gh.get_release_infos("copypastaofficial/copypasta",release_number=0))

print(gh.get_release_asset_download_link("copypastaofficial/copypasta","copypasta_installer.exe",release_number=2))

print(gh.download_release_asset("copypastaofficial/copypasta","copypasta_installer.exe",release_number=0,output_path=""))


#========================
# more precise examples
#========================


# example : if you wanna print my bio content :
print(gh.get_user_infos("thaaoblues")['bio'])

# or even the email address of mark zuckerberg :
print(gh.get_user_infos("im_a_reptilian")['email'])

# and the get an url to download my lastest project:
print(gh.get_release_asset_download_link("copypastaofficial/copypasta","copypasta_installer.exe"))

# but you are a bit of a OSINT person so you want to check if this app is a success before trying it
# release_number is working in reverse, 0 is the lastest (by default it's 0)
print(gh.get_release_download_count("copypastaofficial/copypasta",release_number=0))

# but you are lazy so you want it directly
gh.download_release_asset("copypastaofficial/copypasta","copypasta_installer.exe")

# and now you want to know a bit more about who follows me
print(gh.get_user_infos("thaaoblues")['followers'])

# if you want more, just put you mouse over the function name on your IDE and 
# it should display the docstring
# if it don't, no problem. Just check the readme file.