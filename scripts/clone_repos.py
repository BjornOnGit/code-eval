from github import Github
import os

g = Github("your_github_token")

def clone_repo(repo_url, destination):
    os.system(f"git clone {repo_url} {destination}")