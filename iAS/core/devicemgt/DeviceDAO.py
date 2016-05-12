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
from Device import Device


class DeviceDAO:
    def __init__(self):
        pass

    def createDevice(self, device):
        try:
            DatabaseCollections.deviceCollectionName.insert_one(
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
            DatabaseCollections.deviceCollectionName.update_one(
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
            DatabaseCollections.deviceCollectionName.remove({"deviceId": deviceId})
            return "Device Deleted Successfully"
        except IOError:
            return "Device Deletion Failed"

    def getDevice(self, deviceId):
        device = DatabaseCollections.deviceCollectionName.find({"deviceId": deviceId})
        if device is None:
            return None
        else:
            return device

    def getDevices(self, userId):
        deviceList = []
        try:
            devices = DatabaseCollections.deviceCollectionName.find({"deviceOwner": userId})
            for device in devices:
                dev = Device(device["deviceId"], device["deviceName"], device["deviceOwner"], device["deviceType"])
                deviceList.append(dev)
            return deviceList
        except IOError:
            return "Finding devices failed."
