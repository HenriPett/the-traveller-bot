import datetime
import logging
from urllib3 import PoolManager
from json import dumps

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

http = PoolManager()


def run(event, context):
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))

    data = {"content": "text that you want to display"}

    http.request("POST",
                 "Discord Webhook",
                 body=dumps(data),
                 headers={"Content-Type": "application/json"})
