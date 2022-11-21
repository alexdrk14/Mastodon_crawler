from mastodon import Mastodon
from streaming_listener import CallbackStreamListener
from handler import MongoHandler
import configfile as config
import time

def login():
    mastodon = Mastodon(client_id='pytooter_clientcred.secret')
    mastodon.log_in(config.ACCOUNT["mail"], config.ACCOUNT["passwd"], to_file = config.ACCOUNT["file"])
    return mastodon

while True:
    try:
        API = login()
        handler = MongoHandler()
        listener = CallbackStreamListener(update_handler=handler.handler_post,
                                      local_update_handler=handler.handler_post,
                                      delete_handler=handler.handler_deletion,
                                      notification_handler=None,
                                      conversation_handler=None,
                                      unknown_event_handler=None,
                                      status_update_handler=None)
        oo = API.stream_public(listener=listener)
    except Exception as e:
        print(f'Exception {e}')
        time.sleep(5*60)


