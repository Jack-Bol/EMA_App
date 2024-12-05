import time
import hmac
import hashlib
import base64
import uuid
import requests


AppId = "decafe00000000000000000000000000"  # fill in your AppId and AppSecret
AppSecret = "1337deadbeef"


class emaApp:
    def __init__(self, appId, appSecret):
        self.AppId = appId
        self.AppSecret = appSecret
        self.XCASignatureMethod = "HmacSHA256"
        self.url = "https://i.dont.know.yet"

    def _generateSignature(self, stringToSign):
        appSecretBytes = self.AppSecret.encode('utf-8')
        hmacSha256 = hmac.new(appSecretBytes, digestmod=hashlib.sha256)
        hmacSha256.update(stringToSign.encode('utf-8'))
        hashResult = hmacSha256.digest()
        return base64.b64encode(hashResult).decode('utf-8')

    def _generateStringToSign(self, requestPath, httpMethod, XCATimestamp, XCANonce):
        stringToSign = list()
        stringToSign.append(XCATimestamp)
        stringToSign.append(XCANonce)
        stringToSign.append(self.AppId)
        stringToSign.append(requestPath)
        stringToSign.append(httpMethod)
        return "/".join(stringToSign)

    def _generateHeader(self, requestPath, httpMethod):
        XCATimestamp = str(int(time.time()))
        XCANonce = str(uuid.uuid1())
        headers = dict()
        headers["X-CA-Appld"] = self.AppId
        headers["X-CA-Timestamp"] = XCATimestamp                      # The timestamp you request the API.
        headers["X-CA-Nonce"] = XCANonce                              # UUID, a 32-bit string
        headers["X-CA-Signature-Method"] = self.XCASignatureMethod
        headers["X-CA-Signature"] = self._generateSignature(self._generateStringToSign(requestPath, httpMethod, XCATimestamp, XCANonce))
        return headers

    def getSystems(self):
        path = "/installer/api/v2/systems"
        method = "POST"
        print(self.url + path)
        resp = requests.post(self.url + path, headers=self._generateHeader(path, method))
        print(resp.json())


emaTest = emaApp(AppId, AppSecret)
emaTest.getSystems()


'''
3.1 System Details API
3.1.1 Get Systems
/installer/api/v2/systems
POST

3.1.2 Get Details for a Particular System
/installer/api/v2/systems/details/{sid}
GET

3.1.3 Get Inverters for a Particular System
/installer/api/v2/systems/inverters/{sid}
GET

3.1.4 Get Meters for a Particular System
/installer/api/v2/systems/meters/{sid}
GET

3.1.5 Get Storages for a Particular System
/installer/api/v2/systems/storages/{sid}
GET

3.2 System-level Data API
3.2.1 Get Summary Energy for a Particular System
/installer/api/v2/systems/summary/{sid}
GET

3.2.2 Get Energy in Period for a Particular System
/installer/api/v2/systems/energy/{sid}
GET

3.3 ECU-level Data API
3.3.1 Get Summary Energy for a Particular ECU
/installer/api/v2/systems/{sid}/devices/ecu/summary/{eid}
GET

3.3.2 Get Energy in Period for a Particular ECU
/installer/api/v2/systems/{sid}/devices/ecu/energy/{eid}
GET

3.4 Meter-level Data API
3.4.1 Get Summary Energy for a Particular Meter
/installer/api/v2/systems/{sid}/devices/meter/summary/{eid}
GET

3.4.2 Get Energy in Period for a Particular Meter
/installer/api/v2/systems/{sid}/devices/meter/period/{eid}
GET

3.5 Inverter-level Data API
3.5.1 Get Summary Energy for a Particular Inverter
/installer/api/v2/systems/{sid}/devices/inverter/summary/{uid}
GET

3.5.2 Get Energy in Period for a Particular Inverter
/installer/api/v2/systems/{sid)/devices/inverter/energy/{uid}
GET

3.5.3 Get Energy in a Day for all inverters below a Particular ECU
/installer/api/v2/systems/{sid}/devices/inverter/batch/energy/{eid}
'''
