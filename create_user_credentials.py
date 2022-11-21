from mastodon import Mastodon
from os.path import exists
import configfile as cnf

if not exists(cnf.ACCOUNT["file"]):
    print("User credentials file is not exists. Let's create one.")
    Mastodon.create_app('pytooterapp', 
            api_base_url = 'https://mastodon.social',
            to_file = cnf.ACCOUNT["file"])
else:
    print("User credentials file already exists.")
