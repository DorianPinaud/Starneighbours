import re
from gevent import monkey
monkey.patch_all()

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from GithubServices.GithubUserService import GithubUserService
from GithubServices.GithubRepoService import GithubRepoService
from StarneighboursService import StarneighboursService
import WebAppConfig as cfg

users = {
    "user": generate_password_hash("pass")
}

class WebApp(Flask):

    def __init__(self, name):
        super().__init__(name)

    def run(self):
        super().run(host=cfg.host, port=cfg.port, threaded = cfg.threaded)

# Create the web app
app = WebApp(__name__)
basicAuth = HTTPBasicAuth()

# Init the scheduler
repo_service = GithubRepoService()
user_service = GithubUserService()
starneighbours_service = StarneighboursService(user_service, repo_service)

@basicAuth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route(StarneighboursService.route_url)
@basicAuth.login_required
def route_starneighbours(user, repo):

    # Retrieve the starneighours data.
    neighbours_repos = starneighbours_service.get_starneighbours_repo(user, repo)
    if not neighbours_repos:
        return "Fail to retrieves neighbours data", 503

    # format ouput data.
    output = [{ "repos": k, "stargazers": str(v) } for 
        k, v in neighbours_repos.items() ]
    return f"{ output }", 200

app.run()