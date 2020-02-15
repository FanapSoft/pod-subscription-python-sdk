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

    params = {
        "call_url": "http://yahoo.com",
        "redirect_url": "http://google.com",
        "gateway": "PEP",
    }

    print(pod_subscription.request_subscription(subscription_plan_id=5970, user_id=12043))

    # OUTPUT
    # {
    #   "id": 2612,
    #   "creationDate": 1581748700491,
    #   "plan": {
    #     "id": 5970,
    #     "typeCode": "SUBSCRIPTION_PLAN_TYPE_CASH",
    #     "price": 10,
    #     "name": "طرح تست پایتونی"
    #   },
    #   "usageCount": 0,
    #   "usedAmount": 0,
    #   "notSettledUsedAmount": 0,
    #   "status": "SUBSCRIPTION_NOT_VERIFY",
    #   "invoiceSrv": {
    #     "id": 65870,
    #     "payableAmount": 10,
    #     "uniqueNumber": "8cc1042e4dcb4b80",
    #     "description": "",
    #     "business": {
    #       "id": 7867,
    #       "name": "شرکت رضا",
    #       "numOfProducts": 462,
    #       "rate": {
    #         "rate": 8,
    #         "rateCount": 1
    #       },
    #       "sheba": "640170000000000000000000"
    #     },
    #     "userSrv": {
    #       "id": 12043,
    #       "name": "احسان شکاری",
    #       "ssoId": "6254762",
    #       "ssoIssuerCode": 1,
    #       "profileImage": "https://core.pod.ir:443/nzh/image/?imageId=..."
    #     }
    #   },
    #   "paymentLink": "https://sandbox.pod.ir:1033/v1/pbc/payInvoiceByUniqueNumber/?uniqueNumber=8cc1042e4dcb4b80&gateway=PEP&call_url=http://yahoo.com&redirect_url=http://google.com"
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
