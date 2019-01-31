import os
import time

import requests
from behave import given, when, then

URL = os.getenv('URL', 'http://localhost')

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
    create_account_request = dict(customerId=context.customer_id, accountStatus='active')

    response = requests.post(f'{URL}/accounts/',
                             json=create_account_request)

    assert response.status_code == 201, f'{response.status_code} {response.text}'
    body = response.json()
    context.account_number = body['accountNumber']
