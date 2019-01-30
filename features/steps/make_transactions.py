import os
import time

import requests
from behave import given, when, then

URL = os.getenv('URL', 'http://localhost')


@given('there is a customer "{name}"')
def create_customer(context, name):
    (first_name, surname) = name.split(' ', 2)
    create_customer_request = dict(firstName=first_name, surname=surname)

    response = requests.post(f'{URL}/customers/', json=create_customer_request)

    assert response.status_code == 201, response.status_code
    body = response.json()
    context.customer_id = body['customerId']


@given('"{name}" has a new account')
def create_account(context, name):
    create_account_request = dict(customerId=context.customer_id)

    response = requests.post(f'{URL}/accounts/',
                             json=create_account_request)

    assert response.status_code == 201, f'{response.status_code} {response.text}'
    body = response.json()
    context.account_number = body['accountNumber']


@when('I deposit {amount:d} the account')
def deposit(context, amount):
    deposit_request = dict(accountNumber=context.account_number,
                           amount=amount,
                           operation='credit')

    response = requests.post(f'{URL}/cashier/create', json=deposit_request)

    assert response.status_code == 202, f'{response.status_code} {response.text}'


@when("I withdraw {amount:d} the account")
def withdraw(context, amount):
    deposit_request = dict(accountNumber=context.account_number,
                           amount=amount,
                           operation='debit')

    response = requests.post(f'{URL}/cashier/create', json=deposit_request)

    assert response.status_code == 202, f'{response.status_code} {response.text}'


@when('"{name}" changes his name')
def create_customer(context, name):
    (first_name, surname) = name.split(' ', 2)
    create_customer_request = dict(firstName=first_name, surname=surname)

    response = requests.post(f'{URL}/customers/', json=create_customer_request)

    assert response.status_code == 201, response.status_code
    body = response.json()
    context.customer_id = body['customerId']


@then('then "{name}" will be created in a new account')
def create_account(context, name):
    create_account_request = dict(customerId=context.customer_id)

    response = requests.post(f'{URL}/accounts/',
                             json=create_account_request)

    assert response.status_code == 201, f'{response.status_code} {response.text}'
    body = response.json()
    context.account_number = body['accountNumber']



