import datetime
import pytz
from prettytable import PrettyTable
import uuid

def func():
    x = PrettyTable()
    x.field_names = ["Country", "Capital", "is_russia", "uid", "datetime"]
    x.add_rows([["Russia", "Moscow", True, uuid.uuid4(), datetime.datetime.now(pytz.timezone("Europe/Moscow"))],\
                ["Argentina", "Buenos Aires", False, uuid.uuid4(), datetime.datetime.now(pytz.timezone("America/Argentina/Buenos_Aires"))],\
                ["Jamaica", "Kingston", False, uuid.uuid4(), datetime.datetime.now(pytz.timezone("America/Jamaica"))]])
    print(x)