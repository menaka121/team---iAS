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
from bson.objectid import ObjectId
from app import *


def putAppData(App):
    DatabaseCollections.appCollectionName.insert_one(
        {
            "name": App.name,
            "type": App.type,
            "description": App.description,
            "image": App.image
        }
    )
    logging.info("Inserted App data")


# def putAppDumyData():
#     DatabaseCollections.appCollectionName.insert_one(
#         {
#             "name": "Fire Alarm System",
#             "type": "FireAlarm",
#             "description": "A fire alarm system is number of devices working together to detect and warn people",
#             "image": "/static/images/devices/fireAlarmSystem/fireAlarmSystem.jpg"
#         }
#     )
#     logging.info("Inserted App data")

def rowCount(dbCollection):
    return dbCollection.count()


def NumberOfApps():
    return rowCount(DatabaseCollections.appCollectionName)


def getAppDetailsById(Id):
    document = DatabaseCollections.appCollectionName.find_one({'_id': ObjectId(Id)})
    obj = App(appid=document["_id"],
              name=document["name"],
              type=document["type"],
              description=document["description"],
              image=document["image"])

    return obj


def getAppsIDList():
    return DatabaseCollections.appCollectionName.distinct('_id')


def getAppList():
    len = NumberOfApps()
    list = []
    appIDList = getAppsIDList()
    for i in range(0, len):
        list.append(getAppDetailsById(appIDList[i]))
    return list
