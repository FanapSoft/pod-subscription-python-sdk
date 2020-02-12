# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_subscription import PodSubscription, SubscriptionStatus

try:
    pod_subscription = PodSubscription(api_token=API_TOKEN, server_type=SERVER_MODE)
    params = {
        "page": 1,
        "size": 50,
        # "subscription_plan_id": 1,      # شناسه اشتراک کاربر در یک طرح
        # "fromDate": "",         # از تاریخ به صورت شمسی و فرمت yyyy/mm/dd
        # "toDate": "",         # تا تاریخ به صورت شمسی و فرمت yyyy/mm/dd
    }

    print(pod_subscription.user_subscription_list(access_token=ACCESS_TOKEN, **params))
    print("Total :", pod_subscription.total_items())

except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
