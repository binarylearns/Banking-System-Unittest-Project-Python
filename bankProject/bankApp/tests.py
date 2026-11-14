
from django.test import TestCase
from decimal import Decimal
from .models import BankAccount


class BankAccountTest(TestCase):

    def setUp(self):
        self.account = BankAccount.objects.create(
        account_holder="Ishwor",
        balance=Decimal("1000.00")
    )
        

    def test_account_creation(self):
        self.assertIsNotNone(self.account.pk)

    def test_initial_balance(self):
        self.assertEqual(
            self.account.balance,
            Decimal("1000.00")
        )

    def test_deposit(self):
        self.account.deposit(Decimal("500.00"))
        self.account.refresh_from_db()

        self.assertEqual(
            self.account.balance,
            Decimal("1500.00")
        )
