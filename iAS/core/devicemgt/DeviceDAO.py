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


class DeviceDAO:

    def __init__(self):
        pass

    def createDevice(self, device):
        try:
            databaseCollections.deviceCollectionName.insert_one(
                {
                    "deviceId": device.deviceID,
                    "deviceName": device.deviceName,
                    "deviceOwner": device.deviceOwner,
                    "deviceType": device.deviceType,
                }
            )
            return "Success"
        except IOError:
            return "Insertion Failed"



    def updateDevice(self, deviceId, device):
        try:
            databaseCollections.deviceCollectionName.update_one(
                {"deviceId": deviceId},
                {
                    "deviceId": device.deviceID,
                    "deviceName": device.deviceName,
                    "deviceOwner": device.deviceOwner,
                    "deviceType": device.deviceType,
                })
            return "Update Device Successful"
        except IOError:
            return "Update Device Failed"

    def deleteDevice(self, deviceId):
        try:
            databaseCollections.deviceCollectionName.remove({"deviceId": deviceId})
            return "Device Deleted Successfully"
        except IOError:
            return "Device Deletion Failed"

    def getDevice(self, deviceId):
        device = databaseCollections.deviceCollectionName.find({"deviceId": deviceId})
        if device is None:
            return None
        else:
            return device

