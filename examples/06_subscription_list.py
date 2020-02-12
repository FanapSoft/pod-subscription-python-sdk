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
        # "userId": USER_ID,      # شناسه کاربر
        # "fromDate": "1398/11/14",         # از تاریخ به صورت شمسی و فرمت yyyy/mm/dd
        # "toDate": "1398/11/15",         # تا تاریخ به صورت شمسی و فرمت yyyy/mm/dd
        # "status": SubscriptionStatus.NOT_VERIFY,       # وضعیت اشتراک
        # "subscriptionId": 2543,       # شناسه اشتراک
    }

    print(pod_subscription.subscription_list(subscription_plan_id=5914, **params))
    print("Total :", pod_subscription.total_items())

    # OUTPUT
    # [
    #   {
    #     "id": 2543,
    #     "fromDate": 1580710172725,
    #     "toDate": 1581142172725,
    #     "creationDate": 1580710172725,
    #     "plan": {
    #       "id": 5914,
    #       "typeCode": "SUBSCRIPTION_PLAN_TYPE_POST_PAID",
    #       "price": 0,
    #       "name": "ویرایش طرح"
    #     },
    #     "usageCount": 0,
    #     "usedAmount": 0,
    #     "notSettledUsedAmount": 0,
    #     "status": "SUBSCRIPTION_CONFIRM",
    #     "subscriber": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     }
    #   },
    #   ...
    # ]
    # Total : 1


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
