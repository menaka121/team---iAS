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

from iAS.common.Constants import *
import logging

def putUserData(userId,
                userName,
                gender,
                email,
                profilePicture):
    DatabaseCollections.userCollectionName.insert_one(
        {
            "userId": userId,
            "userName": userName,
            "gender": gender,
            "email": email,
            "profilePicture": profilePicture
        }
    )
    logging.info("Inserted User data")


def getUserAvailability(email):
    if DatabaseCollections.userCollectionName.find({'email': email}).count() > 0:
        return False
    else:
        return True
