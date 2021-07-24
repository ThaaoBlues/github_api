from github_api import GithubHTTPApi


gh = GithubHTTPApi()

print(gh.get_raw_file_content("thaaoblues/github_api","README.md"))
print(gh.get_user_infos("thaaoblues"))
print(gh.get_user_repos("thaaoblues"))
print(gh.get_release_download_count("copypastaofficial/copypasta"))
print(gh.get_release_infos("copypastaofficial/copypasta",release_number=0))
print(gh.get_release_asset_download_link("copypastaofficial/copypasta","copypasta_installer.exe",release_number=2))
print(gh.download_release_asset("copypastaofficial/copypasta","copypasta_installer.exe",output_path=""))