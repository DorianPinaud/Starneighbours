import grequests
import GithubServices.GithubConfig as cfg

class GithubUserService(object):
    
    def __init__(self, api_domain=cfg.api_domain):
        self.api_domain = api_domain

    def _generate_user_req_url(self, login, type):
        return f"{self.api_domain}/users/{ login }/{type}"

    def get_starred_repo_from_users(self, users_login):

        # Check the entry data validity
        if users_login == None or len(users_login) == 0:
            return None

        # Retrieve the starred repo data
        urls = [ self._generate_user_req_url(user, "starred") for user in users_login]
        starred_repo_reqs = (grequests.get(u) for u in urls)
        starred_repos = grequests.map(starred_repo_reqs)
        return [(login, repos_data.json()) for (repos_data, login) in zip(starred_repos, users_login) ]
            


        
    