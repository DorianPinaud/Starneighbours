# Starneighours
*Updated 03/20/2022*

## Project description

Starneighours is an web application use to collect each github repository which are sharing the same stargazers.

In input, the user must specified an github account and a repository account. In output, the web service retrieves the data with the following format:

```json
[
 {
   "repo": <repoA>,
    "stargazers": [<stargazers in common>, ...],
 },
 {
   "repo": <repo>,
    "stargazers": [<stargazers in common>, ...],
 },
 ...
]
```

More detail about the project [here](https://mergify.notion.site/Stargazer-4cf5427e34a542f0aee4e829bb6d9035).

## Usage

For run the web service use the following command:
```batch
python WebApp.py
```

The web service expose an http entry point:
```
GET /repos/<user>/<repo>/starneighbours
```

Use an http client to trigger the functionality.

For now, only one account is available, and you cannot register a new one:
> login: user
> password: pass

## Installation

To install the **starneighbours** project please use the following command line from the root of the repository:

```batch
pip install -r requirements.txt
```

All necessary package are described [here](./requirements.txt).

## Configure projets

Two files configure the project:
- The *RunAppConfig.py*: Use to configure the web application parameters such as the ip or the port.
- The *GithubSercices/Config.py*: Use to configure the github api services. For now the only parameter is the *domain name* of the github api.

## Project structure

The structure is composed of two parts:
- The first is the web service **WebApp** and the **StarneighboursService** which describe the business logic of the application, handles the main algorithm to build the output data and manage the authentification system.
- The second part is composed of helper services for **github api usage**. These services handle network communication with externals api and refine the data.

## Test

No tests are available now, comming soon...


