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

from __init__ import *
from iAS.core.transportmgt.ideamart.sendMessage import *


class messageHandler(Resource):
    def get(self):
        obj = messageBody(message="Waring Temparature is too high!", password="password",
                          url="http://localhost:7000/sms/send",
                          destAddress="tel:94771122336", applicationID="APP_000001")

        sendMessage(obj)
        return jsonify({'messageFromServer': "message Sent to device"})