# coding=utf-8
from __future__ import unicode_literals
from pod_base import APIException, PodException
from examples.config import *
from pod_subscription import PodSubscription, \
    SubscriptionPlanPeriodType, \
    SubscriptionPlanSettlementPeriodType, \
    SubscriptionPlanPaymentType

try:
    pod_subscription = PodSubscription(api_token=API_TOKEN, server_type=SERVER_MODE)

    print(pod_subscription.pay_subscription_debt(subscription_id=2543, access_token=ACCESS_TOKEN))

    # OUTPUT
    # {
    #   "id": 2543,
    #   "fromDate": 1580710172725,
    #   "toDate": 1581142172725,
    #   "creationDate": 1580710172725,
    #   "plan": {
    #     "id": 5914,
    #     "typeCode": "SUBSCRIPTION_PLAN_TYPE_POST_PAID",
    #     "price": 0,
    #     "name": "ویرایش طرح"
    #   },
    #   "usageCount": 2,
    #   "usedAmount": 0,
    #   "notSettledUsedAmount": 0,
    #   "status": "SUBSCRIPTION_CONFIRM"
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
