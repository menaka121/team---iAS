# Copyright 2016 Team - iAS, University Of Peradeniya
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from flask import json

from messageBody import messageBody
import logging
import requests


def sendMessage(messageBody):
    res = {'message': messageBody.message,
           "destinationAddresses": messageBody.destAddress,
           "password": messageBody.password,
           "applicationId": messageBody.applicationID
           }

    logging.info(res)
    form_data = json.dumps(res)
    logging.info(form_data)
    result = requests.post(url=messageBody.url, data=form_data)

    logging.info(result.content)

    if result.status_code == 200:
        logging.info('*** Message delivered Successfully! ****')
    else:
        logging.info('*** Message was not delivered Successfully!! ERROR-CODE: ' + result.status_code + ' ****')



