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

    print(pod_subscription.add_subscription_plan(product_id=PRODUCT_ID, name="طرح تستی", price=100,
                                                 period_type=SubscriptionPlanPeriodType.DAILY,
                                                 period_type_count=5,
                                                 subscription_payment_type=SubscriptionPlanPaymentType.BLOCK,
                                                 guild_code=GUILD_CODE))

    # OUTPUT
    # {
    #   "id": 5912,
    #   "periodTypeCode": "SUBSCRIPTION_PLAN_PERIOD_TYPE_DAILY",
    #   "periodCount": 5,
    #   "creationDate": 1580567697348,
    #   "name": "طرح تستی",
    #   "price": 100,
    #   "enable": true,
    #   "usageAmountLimit": 100,
    #   "permittedGuildList": [],
    #   "permittedBusinessList": [],
    #   "permittedProductList": [],
    #   "allGuildsPermitted": true,
    #   "allBusinessesPermitted": true,
    #   "allProductsPermitted": true,
    #   "currency": {
    #     "name": "ریال",
    #     "code": "IRR"
    #   },
    #   "typeCode": "SUBSCRIPTION_PLAN_TYPE_BLOCK",
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
    #     "enable": false,
    #     "hide": false,
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
    #     "unlimited": true,
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
    #     "allowUserInvoice": false,
    #     "allowUserPrice": false,
    #     "templateCode": "service_call",
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "preferredTaxRate": 0
    #   }
    # }

    print(pod_subscription.add_subscription_plan(product_id=PRODUCT_ID, name="طرح تستی", price=0,
                                                 period_type=SubscriptionPlanPeriodType.DAILY,
                                                 period_type_count=5,
                                                 subscription_payment_type=SubscriptionPlanPaymentType.POST_PAID,
                                                 guild_code=GUILD_CODE,
                                                 settlementPeriodTypeCode=SubscriptionPlanSettlementPeriodType.DAILY,
                                                 maxDebtorAmount=10000))


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
