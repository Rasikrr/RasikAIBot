from bardapi import Bard, SESSION_HEADERS
import os
from dotenv import load_dotenv
import requests


class BardAI:
    def __init__(self, token):
        self.session = requests.Session()
        self.token = token
        self.session.cookies.set("__Secure-1PSID", self.token)
        self.session.cookies.set("__Secure-1PSIDCC", self.token)
        self.session.cookies.set("__Secure-1PSIDTS", self.token)
        self.session.headers = SESSION_HEADERS
        self.bard = Bard(token=self.token, session=self.session)

    def answer(self, question):
        return self.bard.get_answer(question)["content"]


