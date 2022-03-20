import requests
import GithubServices.GithubConfig as cfg  

class GithubRepoService(object):

    def __init__(self, api_domain=cfg.api_domain):
        self.api_domain = api_domain

    def get_repo_data(self, user, repo, type):
        # Generate the URL
        req_url = f"{self.api_domain}/repos/{user}/{repo}/{type}"

        # Run the request
        req = requests.request('GET', req_url)
        if not req or req.status_code == 404:
            print(f"Failed the retrieves stargazers from  /{user}/{repo}")
            print(f"reason: {req.reason}")
            return None
                
        return req.json()

    # Get all data about a repository
    def get_stargazers_data(self, user, repo):
        return self.get_repo_data(user, repo, "stargazers")

    def get_stargarzers_login(self, user, repo):
        stargazers = self.get_stargazers_data(user, repo)
        if not stargazers:
            return None
        return [stargazer["login"] for stargazer in stargazers]