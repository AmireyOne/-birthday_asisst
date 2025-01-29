from celery import shared_task
# from .models import Remind_member
# from datetime import date
# from main_page.models import Information
import http.client
import json
import logging

logger = logging.getLogger(__name__)



@shared_task
def send_reminder_sms():
   

    conn = http.client.HTTPSConnection("api.sms.ir")
    payload = json.dumps({
        "lineNumber": 30007487130754,
        "messageTexts": [
          "message",  
        ],
        "mobiles": [
          "09104057136",
        ],
        "senddatetime": None
      })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'X-API-KEY': 'YtEKfmrrr5Fxpyl8CQYX8nqWaKDYWMD24SSnsq0eXNSVRiNZ'
      }
    conn.request("POST", "/v1/send/likeToLike", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))

   
    # remind = Remind_member.objects.all()
    # today = date.today()
    # for item in remind:
    #     birth_date = item.Date_remind
    #     birthday = birth_date.replace(year=today.year)
    #     if today == birthday:
            
    #         obj = Information.objects.filter(user=item.user).first()
    #         phone_number = obj.Phone
    #         message=f"امروز تولد {item.Full_name} یادت نره بهش تبریک بگی💕"
    #         conn = http.client.HTTPSConnection("api.sms.ir")
    #         payload = json.dumps({
    #             "lineNumber": 30007487130754,
    #             "messageTexts": [
    #             message,  
    #             ],
    #             "mobiles": [
    #             "09104057136",
    #             ],
    #             "senddatetime": None
    #         })
    #         headers = {
    #             'Content-Type': 'application/json',
    #             'Accept': 'text/plain',
    #             'X-API-KEY': 'YtEKfmrrr5Fxpyl8CQYX8nqWaKDYWMD24SSnsq0eXNSVRiNZ'
    #         }
    #         conn.request("POST", "/v1/send/likeToLike", payload, headers)
    #         res = conn.getresponse()
    #         data = res.read()
    #         logger.info(f"Response status: {res.status}")
    #         logger.info(f"Response body: {data.decode('utf-8')}")
            
            
    #     else :
    #         conn = http.client.HTTPSConnection("api.sms.ir")
    #         payload = json.dumps({
    #             "lineNumber": 30007487130754,
    #             "messageTexts": [
    #             "نیست",  
    #             ],
    #             "mobiles": [
    #             "09104057136",
    #             ],
    #             "senddatetime": None
    #         })
    #         headers = {
    #             'Content-Type': 'application/json',
    #             'Accept': 'text/plain',
    #             'X-API-KEY': 'YtEKfmrrr5Fxpyl8CQYX8nqWaKDYWMD24SSnsq0eXNSVRiNZ'
    #         }
    #         conn.request("POST", "/v1/send/likeToLike", payload, headers)
    #         res = conn.getresponse()
    #         data = res.read()
    #         logger.info(f"Response status: {res.status}")
    #         logger.info(f"Response body: {data.decode('utf-8')}")




