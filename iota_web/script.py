import tdameritrade.auth as ameritrade
import environ
import os
import selenium.webdriver as webdriver

env = environ.Env()
environ.Env.read_env()  # reading .env file

if __name__ == '__main__':
    print(ameritrade.authentication(client_id=env('AMERITRADE_CLIENT_ID'), redirect_uri=env('AMERITRADE_REDIRECT_URI')))
