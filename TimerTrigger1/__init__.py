import datetime
import logging

import azure.functions as func

import os
import json
import time
import requests
from bs4 import BeautifulSoup
from . import timerCrawler



def main(mytimer: func.TimerRequest, tablePath: func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

  
    list = timerCrawler.corona();

    data = {
            "seoul": list[0],
            "seoulNew": list[1],
            "ulsan": list[1],
            "ulsanNew": list[0],
            "daegu": list[2],
            "daeguNew": list[0],
            "gwangju": list[3],
            "gwangjuNew": list[0],
            "busan": list[4],
            "busanNew": list[0],
            "daejeon": list[5],
            "daejeonNew": list[0],
            "incheon": list[6],
            "incheonNew": list[0],
            "PartitionKey": "corona_index",
            "RowKey": int(time.time()-99999999999)
    }

    tablePath.set(json.dumps(data))

