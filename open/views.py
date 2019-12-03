from random import random

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import models
from chapter import forms
import tdameritrade.auth as ameritrade
import environ
from tdameritrade import TDClient

env = environ.Env()
environ.Env.read_env()  # reading .env file

access_token = ''
refresh_token = ''


# Create your views here.
def index(request):
    is_authenticated = request.user.is_authenticated
    context = {'is_authenticated': is_authenticated}
    if is_authenticated:
        return render(request, 'chapter/index.html', context)
    return render(request, 'open/home.html', context)


def update_tokens():
    auth = ameritrade.authentication(client_id=env('AMERITRADE_CLIENT_ID'), redirect_uri=env('AMERITRADE_REDIRECT_URI'),
                                     tdauser=env('AMERITRADE_USER'), tdapass=env('AMERITRADE_PASSWORD'))
    global access_token
    access_token = auth.get('access_token')
    global refresh_token
    refresh_token = auth.get('refresh_token')


def icm(request):
    global access_token
    try:
        c = TDClient(access_token=access_token)
        accounts = c.accounts(positions=True)
    except Exception:
        update_tokens()
        c = TDClient(access_token=access_token)
        accounts = c.accounts(positions=True)
    account = accounts.get('496041278')
    cash_balance = account.get('securitiesAccount').get('initialBalances').get('cashAvailableForTrading')
    long_stock_val = account.get('securitiesAccount').get('initialBalances').get('longStockVal')
    positions = account.get('securitiesAccount').get('positions')
    symbols = []
    for dictionary in positions:
        symbols.append(dictionary.get('instruments'))

    print(dictionary)

    if cash_balance is None:
        cash_balance = '0.00'
    if long_stock_val is None:
        long_stock_val = '0.00'

    context = {'cash_balance': cash_balance,
               'long_stock_val': long_stock_val,
               'positions': positions,
               'content': accounts, }

    return render(request, 'open/pages/icm.html', context=context)


def basic_register(request):
    form = ''

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            login(request=request, user=user)

            return HttpResponseRedirect(reverse('custom_registration', args=['home']))
    else:
        form = forms.UserForm()

    context = {
        'form': form,
    }
    return render(request, 'open/register/user_register.html', context)


def rush(request):
    rush_post = models.Post.objects.filter(post_identifier='Rush Information')[0]
    return render(request, 'open/pages/rush.html', {'rush_content': rush_post.post_content})


var = {'496041278':
           {'securitiesAccount':
                {'type': 'CASH',
                 'accountId': '496041278',
                 'roundTrips': 0,
                 'isDayTrader': False,
                 'isClosingOnlyRestricted': False,
                 'initialBalances':
                     {'accruedInterest': 0.02,
                      'cashAvailableForTrading': 7000.05,
                      'cashAvailableForWithdrawal': 7000.05,
                      'cashBalance': 0.0, 'bondValue': 0.0,
                      'cashReceipts': 0.0, 'liquidationValue': 7000.05,
                      'longOptionMarketValue': 0.0, 'longStockValue': 0.0,
                      'moneyMarketFund': 7000.05, 'mutualFundValue': 0.0,
                      'shortOptionMarketValue': 0.0, 'shortStockValue': 0.0,
                      'isInCall': False, 'unsettledCash': 0.0, 'cashDebitCallValue': 0.0,
                      'pendingDeposits': 0.0, 'accountValue': 7000.05},
                 'currentBalances':
                     {'accruedInterest': 0.02, 'cashBalance': 0.0,
                      'cashReceipts': 0.0, 'longOptionMarketValue': 0.0,
                      'liquidationValue': 7000.05, 'longMarketValue': 0.0,
                      'moneyMarketFund': 7000.05, 'savings': 0.0,
                      'shortMarketValue': 0.0, 'pendingDeposits': 0.0,
                      'cashAvailableForTrading': 7000.05,
                      'cashAvailableForWithdrawal': 7000.05, 'cashCall': 0.0,
                      'longNonMarginableMarketValue': 7000.05, 'totalCash': 0.0,
                      'shortOptionMarketValue': 0.0, 'bondValue': 0.0,
                      'cashDebitCallValue': 0.0, 'unsettledCash': 0.0},
                 'projectedBalances':
                     {'cashAvailableForTrading': 7000.05,
                      'cashAvailableForWithdrawal': 7000.05}
                 }
            }
       }

