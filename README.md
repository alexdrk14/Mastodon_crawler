# Streaming crawler of Mastodon social media
This github repository present the real time streaming Mastodon crawler, implemented in python language according to [Mastodon.py manual page](https://mastodonpy.readthedocs.io/en/stable/). Particular implementation stores collected events in local MongoDB. Stored data are separated into two collections: 
- Events (also known as user posts/re-posts)
- Deletion (delete event containing post/re-post id that is deleted)

## Requirements
This implementetation required following python packages that can be installed via following commands:
```
# Python 3
pip3 install -r requirements.txt
```
## Mastodon API user credentials

Mastodon API requires to create unique user cridentials for crawler authentication. This credentials should be created one time and stored for further usage. In order to create them we developed python script that creates them in case when the file is not exist, in other case credentials creation is ignored. In order to use this script execute:
```
python3 create_user_credentials.py 
```

## Streaming crawling execution

```
python3 mastodon_stream.py  
```

## Disclaimer
Currently our script do not remove the posts/re-posts that was pushed via deletion stream. In our case we only store the ids of elements that should be removed from MongoDB.

## Deployment

For real time data collection based on our implementation you should do the following:
- Create account at Mastodon socila media server
- Install defined requirements
- Generate Mastodon API user credentials
- Deploy local or remote MongoDB server
- Update configfile.py with your mongo and account information
- Initiate the streaming crawler 

## Contact Information
For any information and bug report please contact the author.

Author: Alexander Shevtsov@University of Crete, Computer Science Department
[E-mail](mailto:shevtsov@csd.uoc.gr)

