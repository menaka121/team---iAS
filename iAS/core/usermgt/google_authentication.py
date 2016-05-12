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
from urllib2 import Request, urlopen, URLError

from iAS.core.usermgt.userDAO import *
from iAS.core.usermgt.user import *


def get_user_data(access_token):
    headers = {'Authorization': 'OAuth ' + access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()

    return res.read()


UserObj = User()


def getUserInfo(access_token):
    response = json.loads(get_user_data(access_token))
    global UserObj
    UserObj = User(userId=response.get("id", ""),
                   userName=response.get("name", ""),
                   gender=response.get("gender", ""),
                   email=response.get("email", ""),
                   profilePicture=response.get("picture", ""))

    if getUserAvailability(response.get("email", "")):
        putUserData(userId=UserObj.userId,
                    userName=UserObj.userName,
                    gender=UserObj.gender,
                    email=UserObj.email,
                    profilePicture=UserObj.profilePicture)


def getUser():
    return UserObj


def getUserJson():
    return json.dumps(UserObj, default=lambda o: o.__dict__)
