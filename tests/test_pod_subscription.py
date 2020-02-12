# coding=utf-8
from __future__ import unicode_literals

import unittest

from pod_base import InvalidDataException

from pod_subscription import PodSubscription, SubscriptionStatus, SubscriptionPlanPeriodType, \
    SubscriptionPlanSettlementPeriodType, SubscriptionPlanPaymentType
from tests.config import *


class TestPodSubscription(unittest.TestCase):
    __slots__ = "__subscription"

    def setUp(self):
        self.__subscription = PodSubscription(api_token=API_TOKEN, server_type=SERVER_MODE)

    def test_01_add_subscription_plan(self):
        params = {
            "product_id": PRODUCT_ID,
            "name": "طرح تستی - unit test Python",
            "price": 10,
            "period_type": SubscriptionPlanPeriodType.DAILY,
            "period_type_count": 1,
            "subscription_payment_type": SubscriptionPlanPaymentType.BLOCK,
            "guild_code": GUILD_CODE
        }

        result = self.__subscription.add_subscription_plan(**params)
        self.assertIsInstance(result, dict, msg="add subscription plan : check instance")

    def test_01_add_subscription_plan_all_params(self):
        params = {
            "product_id": PRODUCT_ID,
            "name": "طرح تستی - unit test Python",
            "price": 10,
            "period_type": SubscriptionPlanPeriodType.DAILY,
            "period_type_count": 1,
            "subscription_payment_type": SubscriptionPlanPaymentType.BLOCK,
            "guild_code": GUILD_CODE,
            "usageCountLimit": 10,
            "usageAmountLimit": 10000,
            "permittedGuildCode": [GUILD_CODE],
            "permittedBusinessId": [],
            "permittedProductId": [],
            "currencyCode": "IRR",
            "maxDebtorAmount": 1000,
            "settlementPeriodTypeCode": SubscriptionPlanSettlementPeriodType.DAILY
        }

        result = self.__subscription.add_subscription_plan(**params)
        self.assertIsInstance(result, dict, msg="add subscription plan (all params): check instance")

    def test_01_add_subscription_plan_post_paid_with_price(self):
        params = {
            "product_id": PRODUCT_ID,
            "name": "طرح تستی - unit test Python",
            "price": 10,
            "period_type": SubscriptionPlanPeriodType.DAILY,
            "period_type_count": 1,
            "subscription_payment_type": SubscriptionPlanPaymentType.POST_PAID,
            "guild_code": GUILD_CODE,
            "maxDebtorAmount": 1000,
            "settlementPeriodTypeCode": SubscriptionPlanSettlementPeriodType.DAILY
        }

        with self.assertRaises(InvalidDataException, msg="add subscription plan : post paid with price"):
            self.__subscription.add_subscription_plan(**params)

    def test_01_add_subscription_plan_validation_error(self):
        params = {
            "product_id": str(PRODUCT_ID),
            "name": "طرح تستی - unit test Python",
            "price": "10",
            "period_type": SubscriptionPlanPeriodType.DAILY,
            "period_type_count": "1",
            "subscription_payment_type": SubscriptionPlanPaymentType.CASH,
            "guild_code": GUILD_CODE,
            "maxDebtorAmount": "1000",
            "settlementPeriodTypeCode": SubscriptionPlanSettlementPeriodType.DAILY
        }

        with self.assertRaises(InvalidDataException, msg="add subscription plan : validation error"):
            self.__subscription.add_subscription_plan(**params)

    def test_01_add_subscription_plan_required_params(self):
        with self.assertRaises(TypeError, msg="add subscription plan : required params"):
            self.__subscription.add_subscription_plan()

    def test_02_subscription_plan_list(self):
        result = self.__subscription.subscription_plan_list()
        self.assertIsInstance(result, list, msg="subscription plan list : check instance")

    def test_02_subscription_plan_list_all_params(self):
        params = {
            "id": 123,
            "periodTypeCode": SubscriptionPlanPeriodType.DAILY,  # نوع بازه زمانی
            "periodTypeCountFrom": 0,  # مقدار بازه زمانی از
            "periodTypeCountTo": 20,  # مقدار بازه زمانی تا
            "fromPrice": 0,  # قیمت از
            "toPrice": 1590,  # قیمت تا
            "typeCode": SubscriptionPlanPaymentType.BLOCK,  # نوع پرداخت - یکی از موارد زیر
            # SubscriptionPlanPaymentType.POST_PAID or
            # SubscriptionPlanPaymentType.CASH or
            # SubscriptionPlanPaymentType.BLOCK
            "enable": True,  # وضعیت طرح
            "permittedGuildCode": [GUILD_CODE],  # لیست کد صنف های مجاز جهت استفاده
            "permittedBusinessId": [123, 456],  # شناسه کسب و کارهای مجاز جهت استفاده
            "permittedProductId": [123, 456],  # لیست شناسه محصولات مجاز جهت استفاده
            "currencyCode": "IRR",  # کد ارز
            "page": 1,  # شماره صفحه
            "size": 50  # تعداد رکورد در خروجی
        }
        result = self.__subscription.subscription_plan_list(**params)
        self.assertIsInstance(result, list, msg="subscription plan list (all params): check instance")

    def test_02_subscription_plan_list_validation_error(self):
        params = {
            "id": "123",
            "periodTypeCode": SubscriptionPlanPeriodType.DAILY,  # نوع بازه زمانی
            "periodTypeCountFrom": "0",  # مقدار بازه زمانی از
            "periodTypeCountTo": "20",  # مقدار بازه زمانی تا
            "fromPrice": "0",  # قیمت از
            "toPrice": "1590",  # قیمت تا
            "typeCode": SubscriptionPlanPaymentType.BLOCK,  # نوع پرداخت - یکی از موارد زیر
            # SubscriptionPlanPaymentType.POST_PAID or
            # SubscriptionPlanPaymentType.CASH or
            # SubscriptionPlanPaymentType.BLOCK
            "enable": "True",  # وضعیت طرح
            "permittedGuildCode": [GUILD_CODE],  # لیست کد صنف های مجاز جهت استفاده
            "permittedBusinessId": ["123", "456"],  # شناسه کسب و کارهای مجاز جهت استفاده
            "permittedProductId": ["123", "456"],  # لیست شناسه محصولات مجاز جهت استفاده
            "currencyCode": "IRR",  # کد ارز
            "page": 1,  # شماره صفحه
            "size": 50  # تعداد رکورد در خروجی
        }

        with self.assertRaises(InvalidDataException, msg="subscription plan list : validation error"):
            self.__subscription.subscription_plan_list(**params)

    def __add_subscription_plan(self, **kwargs):
        return self.__subscription.add_subscription_plan(product_id=PRODUCT_ID,
                                                         name="طرح تست پایتونی",
                                                         price=10,
                                                         period_type=SubscriptionPlanPeriodType.DAILY,
                                                         period_type_count=1,
                                                         subscription_payment_type=SubscriptionPlanPaymentType.CASH,
                                                         guild_code=GUILD_CODE,
                                                         **kwargs)

    def test_03_update_subscription_plan(self):
        subscription = self.__add_subscription_plan()
        updated_name = "ویرایش طرح"
        updated_price = 123
        result = self.__subscription.update_subscription_plan(subscription_plan_id=subscription["id"],
                                                              name=updated_name, price=updated_price)

        self.assertIsInstance(result, dict, msg="update subscription plan : check instance")
        self.assertEqual(result["name"], updated_name, msg="update subscription plan : check name")
        self.assertEqual(result["price"], updated_price, msg="update subscription plan : check price")

    def test_03_update_subscription_plan_required_params(self):
        with self.assertRaises(TypeError, msg="update subscription plan : required params"):
            self.__subscription.update_subscription_plan()

    def test_03_update_subscription_plan_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="update subscription plan : validation error"):
            self.__subscription.update_subscription_plan(subscription_plan_id="123", price="120.5")

    def test_04_request_subscription(self):
        subscription = self.__add_subscription_plan()
        result = self.__subscription.request_subscription(subscription_plan_id=subscription["id"], user_id=USER_ID)
        self.assertIsInstance(result, dict, msg="request subscription : check instance")
        self.assertEqual(result["invoiceSrv"]["userSrv"]["id"], USER_ID, msg="request subscription : check user id")

    def test_04_request_subscription_required_params(self):
        with self.assertRaises(TypeError, msg="request subscription : required params"):
            self.__subscription.request_subscription()

    def test_04_request_subscription_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="request subscription : validation error"):
            self.__subscription.request_subscription(subscription_plan_id="1234", user_id=str(USER_ID))

    def test_05_confirm_subscription_required_params(self):
        with self.assertRaises(TypeError, msg="confirm subscription : required params"):
            self.__subscription.confirm_subscription()

    def test_05_confirm_subscription_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="confirm subscription : validation error"):
            self.__subscription.confirm_subscription(subscription_id="123", code=1234)

    def test_06_subscription_list(self):
        subscription = self.__add_subscription_plan()

        result = self.__subscription.subscription_list(subscription_plan_id=subscription["id"])
        self.assertIsInstance(result, list, msg="subscription list")

    def test_06_subscription_list_required_params(self):
        with self.assertRaises(TypeError, msg="subscription list : required params"):
            self.__subscription.subscription_list()

    def test_06_subscription_list_validation_error(self):
        params = {
            "subscription_plan_id": "123",
            "userId": str(USER_ID),      # شناسه کاربر
            "fromDate": "START DATE",         # از تاریخ به صورت شمسی و فرمت yyyy/mm/dd
            "toDate": "END DATE",         # تا تاریخ به صورت شمسی و فرمت yyyy/mm/dd
            "status": SubscriptionStatus.NOT_VERIFY,       # وضعیت اشتراک
            "subscriptionId": "2543",       # شناسه اشتراک
        }
        with self.assertRaises(InvalidDataException, msg="subscription list : validation error"):
            self.__subscription.subscription_list(**params)

    # def test_07_user_subscription_list(self):
    #     result = self.__subscription.user_subscription_list(access_token=ACCESS_TOKEN)
    #     self.assertIsInstance(result, list, msg="user subscription list")

    def test_07_user_subscription_list_required_params(self):
        with self.assertRaises(TypeError, msg="user subscription list : required params"):
            self.__subscription.user_subscription_list()

    def test_07_user_subscription_list_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="user subscription list : validation error"):
            self.__subscription.user_subscription_list(access_token=ACCESS_TOKEN, subscription_plan_id="123456")

    def test_09_consume_subscription_required_params(self):
        with self.assertRaises(TypeError, msg="consume subscription : required params"):
            self.__subscription.consume_subscription()

    def test_09_consume_subscription_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="consume subscription : validation error"):
            self.__subscription.consume_subscription(subscription_id="123", used_amount="456.5645")

    def test_10_pay_subscription_debt_required_params(self):
        with self.assertRaises(TypeError, msg="pay subscription debt : required params"):
            self.__subscription.pay_subscription_debt()

    def test_10_pay_subscription_debt_validation_error(self):
        with self.assertRaises(InvalidDataException, msg="pay subscription debt : validation error"):
            self.__subscription.pay_subscription_debt(subscription_id="123", access_token="123456")
