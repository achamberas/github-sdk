# Github SDK

## Overview

The following SDK packages bits of the Github API and allows the user access the following information in rich HTML format:

* list of thier organizations
* list of their repositories
* count of their organization
* count of their repositories

## Requirements

The user must provide their Github username and personal access token for this SDK.  Instructions for obtaining a personal access token can be found here:

<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>

Ensure the following libraries are installed on your computer:

```
pandas
requests
ipython
```

Use the `requirements.txt` file included to install these libraries with the command `pip install -r requirements.txt`

## Usage

To use the SDK, import the library and an iPython core to display results in HTML

```
from github import github_sdk
from IPython.core.display import HTML
```

Initialize the SDK by calling it with username and personal access token:

```
user = '<your username>'
token = '<your personal access token>'

g = github_sdk(user, token)
```

call the SDK functions wrapped in an HTML function to render results:

`HTML(g.list_repos())`

The available functionbs are

* `list_repos()`
* `list_orgs()`
* `count_repos()`
* `count_orgs()`

See the included Jupyter notebook for examples.