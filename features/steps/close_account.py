import os
import time

import requests
from behave import given, when, then

URL = os.getenv('URL', 'http://localhost')


@when('"{name}" account is deleted')
def close_acc(context, name):
    close_request = dict(customerId=context.customer_id,
                         accountStatus='inactive')

    response = requests.post(f'{URL}/accounts/', json=close_request)

    assert response.status_code == 201, f'{response.status_code} {response.text}'


@then('then "{name}" account will be closed from accounts')
def check_close_account(name, context):
    get_account_request = dict(customerId=context.customer_id)

    response = requests.get(f'{URL}/accounts/',
                             json=get_account_request)

    assert response.status_code == 201, f'{response.status_code} {response.text}'
    # body = response.json()
    # context.accountStatus = body['accountStatus']
