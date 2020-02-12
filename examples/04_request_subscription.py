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

    print(pod_subscription.request_subscription(subscription_plan_id=5969, user_id=USER_ID))

    # OUTPUT
    # {
    #   "id": 2551,
    #   "creationDate": 1580738028017,
    #   "plan": {
    #     "id": 5969,
    #     "typeCode": "SUBSCRIPTION_PLAN_TYPE_CASH",
    #     "price": 10,
    #     "name": "طرح تست پایتونی"
    #   },
    #   "usageCount": 0,
    #   "usedAmount": 0,
    #   "notSettledUsedAmount": 0,
    #   "status": "SUBSCRIPTION_NOT_VERIFY",
    #   "invoiceSrv": {
    #     "id": 64067,
    #     "payableAmount": 10,
    #     "uniqueNumber": "3b63e2a516f4c6c5",
    #     "description": "",
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 395,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000000"
    #     },
    #     "userSrv": {
    #       "id": 16849,
    #       "name": "رضا زارع",
    #       "ssoId": "11923337",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     }
    #   }
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
