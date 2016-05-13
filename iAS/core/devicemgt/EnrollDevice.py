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
from io import BytesIO
from unittest import result

from flask import send_file, session

from Device import Device
from DeviceDAO import DeviceDAO
import time
import os
import zipfile
import config


def generateId():
    return int(round(time.time()))


def enrollDevice(deviceOwner = "", deviceType = "", deviceName = ""):
    deviceId = generateId()
    device = Device()
    device.deviceID = deviceId
    device.deviceType = deviceType
    device.deviceName = deviceName
    device.deviceOwner = deviceOwner

    deviceDao = DeviceDAO()
    return deviceDao.createDevice(device)

def createZipFile(src, fileName):
    zf = zipfile.ZipFile("%s.zip" % fileName, "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()

def downloadAgent(userId, deviceName, deviceId):
    enrollDevice(userId, "FireAlarm", deviceName)
    base_dir = config.app.root_path
    dir1 = os.path.join(base_dir, "devices", "fireAlarm")
    print(dir1)
    createZipFile(dir1, "agent")
    return os.path.abspath("agent.zip")
