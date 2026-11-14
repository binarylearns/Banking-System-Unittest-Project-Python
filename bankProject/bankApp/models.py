
from django.db import models
from decimal import Decimal


class BankAccount(models.Model):

    account_holder = models.CharField(max_length=255)

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive value.")

        self.balance += amount
        self.save(update_fields=["balance"])

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive value.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        self.save(update_fields=["balance"])

    def __str__(self):
        return self.account_holder
