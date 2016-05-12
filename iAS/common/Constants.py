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

from iAS.core.dbmgt.getConnection import *

class GoogleAuthentication:
    def __init__(self):
        pass

    GOOGLE_CLIENT_ID = '927082250462-ho1ode0ig0rrhicrhvfgvpbk50bou779.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'BbjUuhHLVIDyeQbASzeamSmf'
    REDIRECT_URI = '/callback'  # one of the Redirect URIs from Google APIs console


class DatabaseCollections:
    def __init__(self):
        pass

    userCollectionName = getDatabase().Users
    appCollectionName = getDatabase().Apps
