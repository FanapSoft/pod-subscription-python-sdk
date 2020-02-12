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
        "name": "ویرایش طرح",
        "price": 0,
        # "usageCountLimit": 1,
        # "periodTypeCount": 1,
        "periodTypeCode": SubscriptionPlanPeriodType.DAILY,
        "enable": True,
        # "permittedGuildCode": [],
        # "permittedBusinessId": [],
        # "permittedProductId": [],
        "maxDebtorAmount": 1000,
        "settlementPeriodTypeCode": SubscriptionPlanSettlementPeriodType.DAILY,
        # "oneTimeUse": False
    }
    print(pod_subscription.update_subscription_plan(subscription_plan_id=5914, **params))

    # OUTPUT
    # {
    #   "id": 5914,
    #   "periodTypeCode": "SUBSCRIPTION_PLAN_PERIOD_TYPE_DAILY",
    #   "periodCount": 5,
    #   "creationDate": 1580625753498,
    #   "name": "ویرایش طرح",
    #   "price": 0,
    #   "enable": True,
    #   "permittedGuildList": [],
    #   "permittedBusinessList": [],
    #   "permittedProductList": [],
    #   "allGuildsPermitted": True,
    #   "allBusinessesPermitted": True,
    #   "allProductsPermitted": True,
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "typeCode": "SUBSCRIPTION_PLAN_TYPE_POST_PAID",
    #   "product": {
    #     "id": 0,
    #     "version": 2,
    #     "timelineId": 0,
    #     "entityId": 40717,
    #     "numOfLikes": 0,
    #     "numOfDisLikes": 0,
    #     "numOfFavorites": 0,
    #     "numOfComments": 0,
    #     "timestamp": 0,
    #     "enable": False,
    #     "hide": False,
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
    #     "latitude": 0,
    #     "longitude": 0,
    #     "name": "سرویس کال به صورت تسهیمی",
    #     "description": "سرویس تستی",
    #     "categoryList": [],
    #     "unlimited": True,
    #     "availableCount": 0,
    #     "price": 100,
    #     "discount": 0,
    #     "attributeValues": [
    #       {
    #         "code": "provider",
    #         "name": "تامین کننده",
    #         "value": "کارتینگ، تمیزی با طعم آنلاین"
    #       },
    #       {
    #         "code": "guildcode",
    #         "name": "صنف",
    #         "value": "API_GUILD"
    #       },
    #       {
    #         "code": "methodtype",
    #         "name": "نوع متد",
    #         "value": "rest"
    #       }
    #     ],
    #     "guild": {
    #       "id": 561,
    #       "name": "سرویس دهندگان",
    #       "code": "API_GUILD"
    #     },
    #     "allowUserInvoice": False,
    #     "allowUserPrice": False,
    #     "templateCode": "service_call",
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "preferredTaxRate": 0
    #   }
    # }


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
