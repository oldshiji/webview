import tornado.web
import requests
import config
from model import db

from tornado.web import RequestHandler

class SendmsgHandler(RequestHandler):
    def post(self, *args, **kwargs):

        import jpush

        # __jpush = jpush.JPush('ba5645ed9b17309f7abb116b', '02947521a9540e832c8d0a6d')
        __jpush = jpush.JPush('ba930456252a3ac98c746dc7', 'b5ae4b7a4ff60e5c9045b278')

        useridList = self.get_body_argument("userid")
        msg        = self.get_body_argument("msg")

        print(useridList)
        print(msg)
        '''
        
         push = __jpush.create_push()
        alias = ["57", "65"]

        alias1 = {"alias": alias}
        push.audience = jpush.audience(
            # jpush.tag("tag1", "tag2"),
            alias1
        )

        push.notification = jpush.notification(alert="由py推送的消息来自趣喝茶商城1")
        push.platform = jpush.all_

        try:
            response = push.send()
        except common.Unauthorized:
            raise common.Unauthorized("Unauthorized")
        except common.APIConnectionException:
            raise common.APIConnectionException("conn error")
        except common.JPushFailure:
            print("JPushFailure")
        except:
            print("Exception")
        '''

