class StarneighboursService(object):

    route_url = "/repos/<string:user>/<string:repo>/starneighbours"

    def __init__(self, user_service, repo_service):
        self.user_service = user_service
        self.repo_service = repo_service

    def get_starneighbours_repo(self, user, repo):
        # Retrieve the data
        logins = self.repo_service.get_stargarzers_login(user, repo)

        if not logins:
            return None

        starred_repos_data = self.user_service.get_starred_repo_from_users(logins)

        if not starred_repos_data:
            return None

        # extract the data
        neighbours_repos = {}
        for user_login, starred_repos  in starred_repos_data:
            if starred_repos is None:
                return None
            for starred_repo in starred_repos:
                if not "full_name" in starred_repo:
                    return None
                repo = starred_repo["full_name"]
                if repo not in neighbours_repos:
                    neighbours_repos[repo] = [ user_login ]
                else:
                    neighbours_repos[repo].append(user_login)

        return neighbours_repos