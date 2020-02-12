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
        # "id": 5914,      # شناسه طرح اشتراک
        # "periodTypeCode": SubscriptionPlanPeriodType.DAILY,  # نوع بازه زمانی
        # "periodTypeCountFrom": 0,  # مقدار بازه زمانی از
        # "periodTypeCountTo": 20,  # مقدار بازه زمانی تا
        # "fromPrice": 0,  # قیمت از
        # "toPrice": 1590,  # قیمت تا
        # "typeCode": SubscriptionPlanPaymentType.BLOCK,  # نوع پرداخت - یکی از موارد زیر
        # # SubscriptionPlanPaymentType.POST_PAID or
        # # SubscriptionPlanPaymentType.CASH or
        # # SubscriptionPlanPaymentType.BLOCK
        # "enable": True,  # وضعیت طرح
        # "permittedGuildCode": [GUILD_CODE],       # لیست کد صنف های مجاز جهت استفاده
        # "permittedBusinessId": [123, 456],        # شناسه کسب و کارهای مجاز جهت استفاده
        # "permittedProductId": [123,456],          # لیست شناسه محصولات مجاز جهت استفاده
        # "currencyCode": "IRR",  # کد ارز
        "page": 1,  # شماره صفحه
        "size": 50  # تعداد رکورد در خروجی
    }
    print(pod_subscription.subscription_plan_list(**params))
    print("Total :", pod_subscription.total_items())
    # OUTPUT
    # [
    #   {
    #     "id": 5914,
    #     "periodTypeCode": "SUBSCRIPTION_PLAN_PERIOD_TYPE_DAILY",
    #     "periodCount": 5,
    #     "creationDate": 1580625753498,
    #     "name": "طرح تستی",
    #     "price": 0,
    #     "enable": true,
    #     "permittedGuildList": [],
    #     "permittedBusinessList": [],
    #     "permittedProductList": [],
    #     "allGuildsPermitted": true,
    #     "allBusinessesPermitted": true,
    #     "allProductsPermitted": true,
    #     "currency": {
    #       "name": "ریال",
    #       "code": "IRR"
    #     },
    #     "typeCode": "SUBSCRIPTION_PLAN_TYPE_POST_PAID",
    #     "product": {
    #       "id": 0,
    #       "version": 2,
    #       "timelineId": 0,
    #       "entityId": 40717,
    #       "numOfLikes": 0,
    #       "numOfDisLikes": 0,
    #       "numOfFavorites": 0,
    #       "numOfComments": 0,
    #       "timestamp": 0,
    #       "enable": false,
    #       "hide": false,
    #       "business": {
    #         "id": 7867,
    #         "name": "شرکت رضا",
    #         "numOfProducts": 395,
    #         "rate": {
    #           "rate": 8,
    #           "rateCount": 1
    #         },
    #         "sheba": "640170000000000000000000"
    #       },
    #       "latitude": 0,
    #       "longitude": 0,
    #       "name": "سرویس کال به صورت تسهیمی",
    #       "description": "سرویس تستی",
    #       "categoryList": [],
    #       "unlimited": true,
    #       "availableCount": 0,
    #       "price": 100,
    #       "discount": 0,
    #       "attributeValues": [
    #         {
    #           "code": "provider",
    #           "name": "تامین کننده",
    #           "value": "کارتینگ، تمیزی با طعم آنلاین"
    #         },
    #         {
    #           "code": "guildcode",
    #           "name": "صنف",
    #           "value": "API_GUILD"
    #         },
    #         {
    #           "code": "methodtype",
    #           "name": "نوع متد",
    #           "value": "rest"
    #         }
    #       ],
    #       "guild": {
    #         "id": 561,
    #         "name": "سرویس دهندگان",
    #         "code": "API_GUILD"
    #       },
    #       "allowUserInvoice": false,
    #       "allowUserPrice": false,
    #       "templateCode": "service_call",
    #       "currency": {
    #         "name": "ریال",
    #         "code": "IRR"
    #       },
    #       "preferredTaxRate": 0
    #     }
    #   },
    #   ...
    # ]
    # Total : 2


except APIException as e:
    print("API Exception\nError {}\nError Code : {}\nReference Number : {}".format(e.message, e.error_code,
                                                                                   e.reference_number))
except PodException as e:
    print("Pod Exception: ", e.message)
