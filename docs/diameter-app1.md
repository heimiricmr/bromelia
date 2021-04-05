# How to build your Diameter application: The 1st way (Not that good)

This document covers how to build your Diameter application from the ground up by using the Diameter class only.

This page contains the following sections:

- [Getting building blocks glued](#getting-building-blocks-glued)
- [Starting the project](#starting-the-project)
- [Sending messages down to the Wire](#sending-messages-down-to-the-wire)

## Getting building blocks glued

There are a lot we have seen so far around *bromelia* library. We have discussed the foundations of [Data Types](docs/data-types.md), learned how to create and handle all kinds of [DiameterAVPs](docs/avps.md) and discovered ways to deal with [DiameterMessages](docs/messages.md) to whatever Diameter application. But one thing is missing.

How exactly to build a Diameter application with *bromelia* library?

The first step is having any issue, improvement or new feature for a given network which depends on Diameter protocol somehow. That's the right place to get started.

The second step is defining which Diameter application fits your needs and requirements. Remember the Diameter protocol is aimed to handle the concept of AAA in computer networks, which deals with network access for a given device. For example, there are a few [technical specs](https://en.wikipedia.org/wiki/Diameter_(protocol)#Applications) defining how Diameter applications should work. Besides that IETF RFC specs, there are lots of applications defined by 3GPP standard organization aimed to the Mobile Core Networks such as EPC (known for 4G cellular technology) and IMS network (known for VoLTE and Wi-Fi Calling services). Therefore if your application needs any kind of authentication, authorization or accounting, you should give it a try.

The third step is starting to code. Surely you need to have clear how the system should be designed. Once it has been defined, *bromelia* will help you to hit the ground running. How? Let's get through.

## Starting the project

The Diameter protocol is not only the AVP, Header and Messages formating. There are also both message processing and the state machine part. Before your application connects to a Diameter backend server, your application needs to handle the connection establishment, maintenance and release procedures.

That can be pretty unwieldy, bored and daunting. All you want to do is integrating quickly your Diameter application client to that Diameter server to get things ready. Or even your Diameter application server with a Diameter application client. That's how *bromelia* will help you.

Under the hood *bromelia* implements a few classes to handle the state machine to set the connection procedures up. As an user of this library, all you have to do is to instantiate an object of `Diameter` class, configure it and start to run. The layers beneath will handle the `PeerStateMachine`, `DiameterAssociation` and `TcpConnection` classes.

First things first. Let's instantiate the `app` Diameter object and configure it.

```python
>>> from bromelia import Diameter
>>> app = Diameter()
```

The `app` object has a dictionary `config` attribute which has info regarding to desire Diameter connection.

```python
>>> app.config
{'MODE': 'CLIENT', 'APPLICATIONS': [], 'LOCAL_NODE_HOSTNAME': 'my-host.my-network.com', 'LOCAL_NODE_REALM': 'my-network.com', 'LOCAL_NODE_IP_ADDRESS': '10.129.241.214', 'LOCAL_NODE_PORT': 3868, 'PEER_NODE_HOSTNAME': None, 'PEER_NODE_REALM': None, 'PEER_NODE_IP_ADDRESS': None, 'PEER_NODE_PORT': 3868, 'WATCHDOG_TIMEOUT': 60}
```

By being instantiated, `app` object will fetch automatically the hostname, domain (called by realm in Diameter jargon) and the IP address of the machine. Note that there is no remote peer node setup in the config attribute. That's the reason we need to provide the hostname (`PEER_NODE_HOSTNAME`), domain (`PEER_NODE_REALM`) and IP address (`PEER_NODE_IP_ADDRESS`) of the remote peer node.

For testing purpose, let's consider the remote peer node will be hosted in our own computer, but it could surely be in another computer or server. Now we are going to rename it.

```python
>>> app.config["PEER_NODE_HOSTNAME"] = "remote-host.network.com"
>>> app.config["PEER_NODE_REALM"] = "network.com"
>>> app.config["PEER_NODE_IP_ADDRESS"] = "10.129.241.214"
```

But that's not all. It also needs to define the type of connection of the local node. Will it be client or server? In other means, will your Diameter application start (send CER message and receive a CEA message) or reply to an connection establishment (receive CER message and send a CEA message)?

Once the Diameter connection is established, your Diameter application may send and receive Diameter Messages for a given Diameter application. For example, if you intend to create a MME server or at least emulate a few functions of one, you may go with the `S6a/S6d Application` which will be fine.

Let's consider this `app` will start the connection procedure, then it is also fine keep the `MODE` as `CLIENT`. We are going to change the `APPLICATIONS` key only.

```python
>>> from bromelia import DIAMETER_APPLICATION_S6a_S6d
>>> from bromelia import VENDOR_ID_3GPP
>>> app.config["APPLICATIONS"] = [
                                    {
                                        "vendor_id": VENDOR_ID_3GPP,
                                        "app_id": DIAMETER_APPLICATION_S6a_S6d
                                    }
    ]
```

If you need to setup a Diameter connection with a remote peer node which will use more than only one Diameter application, you just need to include more dictionary entries in this `app.config["APPLICATIONS"]` list. For now, the `S6/S6d Application` is enough.

Just a little note here. The `WATCHDOG_TIMEOUT` represents the timer that your application will use to keep track on connection status. This value is defined in seconds and tells that your Diameter application will send Diameter-Watchdog-Request message every minute to the remote peer node in order to make sure there is network layer connection between them.

The `LOCAL_NODE_PORT` is applied if the `MODE` is set as `SERVER` only. It represents the port your local peer node will use to listen to new incoming connections. The `PEER_NODE_PORT` is applied if the `MODE` is set as `CLIENT`. It represents the port your remote peer node will use to listen to your outgoing connections.

Finally, our `app` is configured and ready to start a Diameter connection.

```python
>>> app.config
{'MODE': 'CLIENT', 'APPLICATIONS': [{'vendor_id': b'\x00\x00(\xaf', 'app_id': b'\x01\x00\x00#'}], 'LOCAL_NODE_HOSTNAME': 'my-host.my-network.com', 'LOCAL_NODE_REALM': 'my-network.com', 'LOCAL_NODE_IP_ADDRESS': '10.129.241.214', 'LOCAL_NODE_PORT': 3868, 'PEER_NODE_HOSTNAME': "remote-host.network.com", 'PEER_NODE_REALM': "network.com", 'PEER_NODE_IP_ADDRESS': '10.129.241.214', 'PEER_NODE_PORT': 3868, 'WATCHDOG_TIMEOUT': 60}
```

However there is no remote peer node available. By the way, we can check the Diameter connection status for this `app` object by calling its `.get_current_state()` method.

```python
>>> app.get_current_state()
'Closed'
```

Nothing different than expected. As we already mentioned earlier, let's setup another peer node. At this time, we need to open up another Python interactive session through its Command-Line interface to keep moving. The difference here comes to the `config` attribute, which will be such below. Instead of naming the `Diameter` object as `app`, let's name it as `app2` and change its `config` attribute.

```python
>>> from bromelia import Diameter
>>> app2 = Diameter()
>>> app2.config = {'MODE': 'SERVER', 'APPLICATIONS': [{'vendor_id': b'\x00\x00(\xaf', 'app_id': b'\x01\x00\x00#'}], 'LOCAL_NODE_HOSTNAME': 'remote-host.network.com', 'LOCAL_NODE_REALM': 'network.com', 'LOCAL_NODE_IP_ADDRESS': '10.129.241.214', 'LOCAL_NODE_PORT': 3868, 'PEER_NODE_HOSTNAME': 'my-host.my-network.com', 'PEER_NODE_REALM': 'my-network.com', 'PEER_NODE_IP_ADDRESS': '10.129.241.214', 'PEER_NODE_PORT': 3868, 'WATCHDOG_TIMEOUT': 60}
```

Now we are ready to start our remote peer node which will be listening on port `3868` by calling its `.start()` method.

```python
>>> app2.start()
```

You will notice the Command-Line will be on hold waiting for upcoming CER message. By calling `.start()` method in the first `Diameter` object configured, both side will exchange its capabilities and bringup the connection moving its internal state from `CLOSED` to `OPEN`. It follows the expected state machine behavior as per RFC 6733.

### CEX Client-side (`app`)

```python
>>> app.get_current_state()
'I-Open'
```

### CEX Server-side (`app2`)

```python
>>> app2.get_current_state()
'R-Open'
```

Yaay! Now you have a Diameter connection setup right on your machine. But maybe you are wondering what does that mean. Remember we have discussed previously the need to [exchange CER/CEA messages between two Diameter nodes](docs/messages.md#standard-diameter-messages) in order to both be able to exchange Diameter Messages for whatever Diameter application setup in a connection. Well, it has been done by both `Diameter` objects. The client-side sent a CER message and the server-side replied it with a CEA message.

In its internals, `Diameter` object creates a representation for each of the most basic Diameter Messages which any Diameter node should implement. That means the request and answer for Capabilities-Exchange (CER/CEA), Diameter-Watchdog (DWR/DWA) and Disconnect-Peer messages (DPR/DPA).

There is another method which allows you to check the content of each one of those objects! Let's see the client-side `Diameter` object.

```python
>>> app.get_base_messages()
<bromelia.proxy.BaseMessages object at 0x0000005916C94A88>
```

It returns a `BaseMessages` object where its attributes represent each Diameter Base Protocol Message to establish (CER/CEA), maintain (DWR/DWA) and release (DPR/DPA) a connection.

```python
>>> base = app.get_base_messages()
>>> base.__dict__
{'cer': <Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 9 AVP(s)>, 'cea': <Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>, 'dwr': <Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>, 'dwa': <Diameter Message: 280 [DWA], 0 [Diameter common message], 3 AVP(s)>, 'dpr': <Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>, 'dpa': <Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>}
```

When instantiated, the `Diameter` object creates each Diameter Message specific object according to `config` attribute, fulfilling each mandatory DiameterAVP input argument. Let's go over each object and a few attributes.

### `cer` & `cea` attributes

```python
>>> base.cer.host_ip_address_avp.data
b'\x00\x01\n\x81\xf1\xd6'
>>> base.cer.host_ip_address_avp.get_ip_address()
'10.129.241.214'
>>> base.cea.result_code_avp.data
b'\x00\x00\x07\xd1'
```

### `dwr` & `dwa` attributes

```python
>>> base.dwr.origin_realm_avp.data
b'my-network.com'
>>> base.dwa.origin_host_avp.data
b'my-host.my-network.com'
```

### `dpr` & `dpa` attributes

```python
>>> base.dpr.disconnect_cause_avp.data
b'\x00\x00\x00\x00'
>>> base.dpa.result_code_avp.data
b'\x00\x00\x07\xd1'
```

## Sending messages down to the Wire

We have covered a lot until up now. The time has come to send and to receive Diameter messages to & from the Wire. The `.send_message()` method built-in in `Diameter` class allows developers sending any kind of Diameter Messages, except those ones representing the most basic Diameter Requests, such as Capabilities-Exchange-Request (CER), Diameter-Watchdog-Request (DWR) and Disconnect-Peer-Request messages (DPR). It returns either Diameter Answer object representing the request's answer if sent a Diameter Request or `None` if sent a Diameter Answer. This method is intended to be used by Diameter application client side.

The `.get_message()` method built-in in `Diameter` class allows developers receiving any kind of Diameter Messages, except those ones representing the most basic Diameter Answers, such as Capabilities-Exchange-Answer (CEA), Diameter-Watchdog-Answer (DWA) and Disconnect-Peer-Answer messages (DPA). It returns either Diameter Request object or Diameter Answer object, depending on the Application Id defined in such Diameter Connection. This method is intended to be used by Diameter application server side.

Since *bromelia* library follows the standard protocol basis and lets other developers to focus on Diameter application server implementations, there is no such way to send or to handle the base protocol messages like CER/CEA, DWR/DWA and DPR/DPA. Those messages are handled by the `DiameterAssociation` class underneath in order to keep the Diameter connection up.

It is up to develeper implementing a loop to check constantly if there are messages to be processed by its Diameter application server.

Now let's go through a Real Diameter Application example and see how to setup a real project in both Diameter Client and Diameter Server side.

### Real Diameter Application

The *bromelia* has been implemented with Mobile Core Networks in mind. Therefore, there is no such thing better than taking an example from that domain.

The Evolved Packet Core (EPC) is the core system which handles the ingress of 4G subscribers. That means whenever your device has the 4G button toggled ON (for the sake of clarity, let's consider 4G data session only and forget a bit about the Voice over LTE service), a few servers will take control of upcoming signaling messages from device side. The entrypoint is the Mobility Management Equipment (MME) network function, which receives requests from devices containing several information.

Any either real or virtual world services need to authenticate its customers. When it comes to Mobile Core Networks, there is no difference except the "customer" word renamed to "subscriber". Surely there are a lots of technical details under the hood around maths and cryptography which won't be in discussion.

The MME needs to intermediate the authentication procedure by interacting with a backend network function called by Home Subscriber Server (HSS), which owns the subscriber profile indicating the services allowed (eg. Roaming, APNs, VoLTE, DL/UL rate, etc.). In other words, it works like a database, but you won't send neither SQL statements nor HTTP-based Web APIs to change the data inside of it. Instead, you will use the Diameter Protocol. For such MME/HSS communication, there are already have predefined APIs, called by Diameter Application Id or Interface. For this communication specifically, it is known as `S6a interface`. You may find more information about such Application Id in the [ETSI TS 29.272 spec](https://www.etsi.org/deliver/etsi_ts/129200_129299/129272/16.03.00_60/ts_129272v160300p.pdf).

If you go through the specs, you will find in Section 7.2. a few Commands, which are the Diameter Messages (or even the APIs, if you prefer) that can be used between the MME and HSS network functions. Take a look at all Diameter Messages defined for `S6 interface`.

| Command-Name                      | Abbreviation | Code | Clause |
| --------------------------------- | ------------ | ---- | ------ |
| Update-Location-Request           | ULR          | 316  | 7.2.3  |
| Update-Location-Answer            | ULA          | 316  | 7.2.4  |
| Cancel-Location-Request           | CLR          | 317  | 7.2.7  |
| Cancel-Location-Answer            | CLA          | 317  | 7.2.8  |
| Authentication-InformationRequest | AIR          | 318  | 7.2.5  |
| Authentication-InformationAnswer  | AIA          | 318  | 7.2.6  |
| Insert-Subscriber-Data-Request    | IDR          | 319  | 7.2.9  |
| Insert-Subscriber-Data-Answer     | IDA          | 319  | 7.2.10 |
| Delete-Subscriber-Data-Request    | DSR          | 320  | 7.2.11 |
| Delete-Subscriber-Data-Answer     | DSA          | 320  | 7.2.12 |
| Purge-UE-Request                  | PUR          | 321  | 7.2.13 |
| Purge-UE-Answer                   | PUA          | 321  | 7.2.14 |
| Reset-Request                     | RSR          | 322  | 7.2.15 |
| Reset-Answer                      | RSA          | 322  | 7.2.16 |
| Notify-Request                    | NOR          | 323  | 7.2.17 |
| Notify-Answer                     | NOA          | 323  | 7.2.18 |

Each Command (or API) has a direction. It means that MME cannot send a few requests or answers to HSS. The opposite is also true.

On the one hand, the Update-Location-Request (ULR) must be sent from MME to HSS only, whereas the Update-Location-Answer (ULA) must be replied by HSS to MME only. On the other hand, the Cancel-Location-Request (CLR) must be sent from HSS to MME only, whereas the Cancel-Location-Answer must be replied by MME to HSS only.

If you choose to emulate a MME network function with *bromelia*, keep in mind your Update-Location-Request-like object may be sent to your HSS endpoint, but never send Update-Location-Answer-like objects, unless you want to test if your HSS backend follows the spec.

Let's go through two scripts which are going to emulate both MME and HSS network functions by sending a ULR from the first Diameter node (MME) to the second Diameter node (HSS) and receiving its ULA. However before going into implementation, we need to get the ULR and ULA formats. From Sections 7.2.3 and 7.2.4, we can have it.

#### Update-Location-Request

```text
< Update-Location-Request> ::= < Diameter Header: 316, REQ, PXY, 16777251 >
                   < Session-Id >
                   [ DRMP ]
                   [ Vendor-Specific-Application-Id ]
                   { Auth-Session-State }
                   { Origin-Host }
                   { Origin-Realm }
                   [ Destination-Host ]
                   { Destination-Realm }
                   { User-Name }
                   [ OC-Supported-Features ]
                   *[ Supported-Features ]
                   [ Terminal-Information ]
                   { RAT-Type }
                   { ULR-Flags }
                   [UE-SRVCC-Capability ]
                   { Visited-PLMN-Id }
                   [ SGSN-Number ]
                   [ Homogeneous-Support-of-IMS-Voice-Over-PS-Sessions ]
                   [ GMLC-Address ]
                   *[ Active-APN ]
                   [ Equivalent-PLMN-List ]
                   [ MME-Number-for-MT-SMS ]
                   [ SMS-Register-Request ]
                   [ SGs-MME-Identity ]
                   [ Coupled-Node-Diameter-ID ]
                   [ Adjacent-PLMNs ]
                   [ Supported-Services ]
                   *[ AVP ]
                    *[ Proxy-Info ]
                   *[ Route-Record ]
```

#### Update-Location-Answer

```text
< Update-Location-Answer> ::= < Diameter Header: 316, PXY, 16777251 >
                   < Session-Id >
                   [ DRMP ]
                   [ Vendor-Specific-Application-Id ]
                   [ Result-Code ]
                   [ Experimental-Result ]
                   [ Error-Diagnostic ]
                   { Auth-Session-State }
                   { Origin-Host }
                   { Origin-Realm }
                   [ OC-Supported-Features ]
                   [ OC-OLR ]
                   *[ Load ]
                   *[ Supported-Features ]
                   [ ULA-Flags ]
                   [ Subscription-Data ]
                   *[ Reset-ID ]
                   *[ AVP ]
                   [ Failed-AVP ]
                    *[ Proxy-Info ]
                   *[ Route-Record ]
```

#### Creating the scripts

As we already did for CER/CEA Diameter Messages, we are going to implement only the mandatory AVPs with already known DiameterAVP subclasses objects and push it into a custom DiameterRequest (for ULR on MME side) and DiameterAnswer (for ULA on HSS side) objects.

Even though we know ULR message is sent by MME and ULA is replied by HSS, we are going to create a MME script to act as a server to connection establishment, so it will be waiting to CER message coming from HSS side and under its receipt, it will reply with CEA message and connection will bringup. That being said, we need to change the `Diameter` object's config attribute for each script.

##### MME side (Diameter Client side)

First let's talk about the MME side. Below you can find the script in `examples/mme.py` to emulate just a tiny little procedure of this network function as a Diameter application client.

`examples/mme.py`

```python
from bromelia import Diameter
from bromelia import DIAMETER_APPLICATION_S6a_S6d
from bromelia import NO_STATE_MAINTAINED
from bromelia import RAT_TYPE_EUTRAN
from bromelia import VENDOR_ID_3GPP
from bromelia.avps import AuthSessionStateAVP
from bromelia.avps import DestinationRealmAVP
from bromelia.avps import OriginHostAVP
from bromelia.avps import OriginRealmAVP
from bromelia.avps import SessionIdAVP
from bromelia.avps import UserNameAVP
from bromelia.base import DiameterRequest
from bromelia.etsi_3gpp_s6a_s6d.avps import UlrFlagsAVP
from bromelia.etsi_3gpp_swm.avps import RatTypeAVP

LOCAL_HOST_NAME = 'my-mme.epc.mynetwork.com'
LOCAL_DOMAIN = 'epc.mynetwork.com'
LOCAL_IP_ADDRESS = '10.129.241.214'

REMOTE_HOST_NAME = 'my-hss.epc.mynetwork.com'
REMOTE_DOMAIN = 'epc.mynetwork.com'
REMOTE_IP_ADDRESS = '10.129.241.214'

#: Basic DiameterAVPs for ULR message
avp1 = SessionIdAVP(LOCAL_HOST_NAME)
avp2 = AuthSessionStateAVP(NO_STATE_MAINTAINED)
avp3 = OriginHostAVP(LOCAL_HOST_NAME)
avp4 = OriginRealmAVP(LOCAL_DOMAIN)
avp5 = DestinationRealmAVP(REMOTE_DOMAIN)
avp6 = UserNameAVP("123456789123456")
avp7 = RatTypeAVP(RAT_TYPE_EUTRAN)
avp8 = UlrFlagsAVP(3)   # it indicates S6a/S6d-Indicator bit and Single-Registration-Indication bit are set.

avps = [avp1, avp2, avp3, avp4, avp5, avp6, avp7, avp8]

#: ULR message creation
ulr = DiameterRequest(command_code=316, application_id=16777251)
ulr.extend(avps)

#: Setting up Diameter connection
app = Diameter()
app.config = {'MODE': 'SERVER', 'APPLICATIONS': [{'vendor_id': VENDOR_ID_3GPP, 'app_id': DIAMETER_APPLICATION_S6a_S6d}], 'LOCAL_NODE_HOST_NAME': LOCAL_HOST_NAME, 'LOCAL_NODE_REALM': LOCAL_DOMAIN, 'LOCAL_NODE_IP_ADDRESS': LOCAL_IP_ADDRESS, 'LOCAL_NODE_PORT': 3868, 'PEER_NODE_HOSTNAME': REMOTE_HOST_NAME, 'PEER_NODE_REALM': REMOTE_DOMAIN, 'PEER_NODE_IP_ADDRESS': REMOTE_IP_ADDRESS, 'PEER_NODE_PORT': 3868, 'WATCHDOG_TIMEOUT': 60}

with app.context():
    while app.is_open():
        for i in range(5):
            ula = app.send_message(ulr)
        break
```

Let's walk through each line and see what's happening.

All needed imports are done right at the begining. Next the constants we are going to use to the connection are created defining both local and remote peer node, each Diameter application server and client.

```python
from bromelia import Diameter
from bromelia import DIAMETER_APPLICATION_S6a_S6d
from bromelia import NO_STATE_MAINTAINED
from bromelia import RAT_TYPE_EUTRAN
from bromelia import VENDOR_ID_3GPP
from bromelia.avps import AuthSessionStateAVP
from bromelia.avps import DestinationRealmAVP
from bromelia.avps import OriginHostAVP
from bromelia.avps import OriginRealmAVP
from bromelia.avps import SessionIdAVP
from bromelia.avps import UserNameAVP
from bromelia.base import DiameterRequest
from bromelia.etsi_3gpp_s6a_s6d.avps import UlrFlagsAVP
from bromelia.etsi_3gpp_swm.avps import RatTypeAVP

LOCAL_HOST_NAME = 'my-mme.epc.mynetwork.com'
LOCAL_DOMAIN = 'epc.mynetwork.com'
LOCAL_IP_ADDRESS = '10.129.241.214'

REMOTE_HOST_NAME = 'my-hss.epc.mynetwork.com'
REMOTE_DOMAIN = 'epc.mynetwork.com'
REMOTE_IP_ADDRESS = '10.129.241.214'
```

Once those definitions are fine, we can start to create our Diameter Message. Remember a Diameter Message is composed of AVPs, so that's why we have instantiated a few DiameterAVP objects and put them together in a Python list. Those DiameterAVPs follow the ULR definition in spec just discussed previously.

```python
#: Basic DiameterAVPs for ULR message
avp1 = SessionIdAVP(LOCAL_HOST_NAME)
avp2 = AuthSessionStateAVP(NO_STATE_MAINTAINED)
avp3 = OriginHostAVP(LOCAL_HOST_NAME)
avp4 = OriginRealmAVP(LOCAL_DOMAIN)
avp5 = DestinationRealmAVP(REMOTE_DOMAIN)
avp6 = UserNameAVP("123456789123456")
avp7 = RatTypeAVP(RAT_TYPE_EUTRAN)
avp8 = UlrFlagsAVP(3)   # it indicates S6a/S6d-Indicator bit and Single-Registration-Indication bit are set.

avps = [avp1, avp2, avp3, avp4, avp5, avp6, avp7, avp8]

#: ULR message creation
ulr = DiameterRequest(command_code=316, application_id=16777251)
ulr.extend(avps)
```

Just as easy as we see it. The `.extend()` allows push the Python list of DiameterAVPs all at once in the newest ULR message, which we have created by using the `DiameterRequest` class. Surely would be possible to do so by using `DiameterMessage` class though. By the way, you could also provide the input argument values by using constants from `bromelia.constants` module if available or define ones by yourself.

```python
#: Setting up Diameter connection
app = Diameter()
app.config = {'MODE': 'SERVER', 'APPLICATIONS': [{'vendor_id': VENDOR_ID_3GPP, 'app_id': DIAMETER_APPLICATION_S6a_S6d}], 'LOCAL_NODE_HOST_NAME': LOCAL_HOST_NAME, 'LOCAL_NODE_REALM': LOCAL_DOMAIN, 'LOCAL_NODE_IP_ADDRESS': LOCAL_IP_ADDRESS, 'LOCAL_NODE_PORT': 3868, 'PEER_NODE_HOSTNAME': REMOTE_HOST_NAME, 'PEER_NODE_REALM': REMOTE_DOMAIN, 'PEER_NODE_IP_ADDRESS': REMOTE_IP_ADDRESS, 'PEER_NODE_PORT': 3868, 'WATCHDOG_TIMEOUT': 60}

with app.context():
    while app.is_open():
        for i in range(5):
            ula = app.send_message(ulr)
        break
```

That's the icing on the cake! See how easily we can setup a Diameter connection and interact according to our needs. The `.context()` method allows to define a context manager to bringup the connection regardless if this node is a client or server. Because of that we can use it with the `with` statement. Next the `while` loop to track the connection state. Now it's time to put everything about Diameter Messages. Once this script handles a MME network function's procedure, we have called the `.send_message()` method by passing the `ulr` object representing the Update-Location-Request message. Keep in mind this method will return the exact response (or answer, in Diameter jargon) to your request. It is up to you as a developer to make all needed verification to your Diameter application. In this example, the script will send 5 Update-Location-Request messages to the HSS and will receive the respective answers. Finally, the `while` loop will break and the context manager will handle the release of the connection between MME and HSS network functions.

##### HSS side (Diameter Server side)

Second let's talk about the HSS side. Below you can find the script in `examples/hss.py` to emulate just a tiny little procedure of this network function as well, but as a Diameter application server.

##### `examples/hss.py`

```python
from bromelia import Diameter
from bromelia import DIAMETER_APPLICATION_S6a_S6d
from bromelia import DIAMETER_SUCCESS
from bromelia import NO_STATE_MAINTAINED
from bromelia import VENDOR_ID_3GPP
from bromelia.avps import AuthApplicationIdAVP
from bromelia.avps import AuthSessionStateAVP
from bromelia.avps import DiameterAVP
from bromelia.avps import OriginHostAVP
from bromelia.avps import OriginRealmAVP
from bromelia.avps import ResultCodeAVP
from bromelia.avps import SessionIdAVP
from bromelia.avps import UserNameAVP
from bromelia.avps import VendorIdAVP
from bromelia.avps import VendorSpecificApplicationIdAVP
from bromelia.base import DiameterAnswer
from bromelia.etsi_3gpp_s6a_s6d.avps import FeatureListAVP
from bromelia.etsi_3gpp_s6a_s6d.avps import FeatureListIdAVP
from bromelia.etsi_3gpp_s6a_s6d.avps import SupportedFeaturesAVP
from bromelia.etsi_3gpp_swm.avps import RatTypeAVP

LOCAL_HOST_NAME = 'my-hss.epc.mynetwork.com'
LOCAL_DOMAIN = 'epc.mynetwork.com'
LOCAL_IP_ADDRESS = '10.129.241.214'

REMOTE_HOST_NAME = 'my-mme.epc.mynetwork.com'
REMOTE_DOMAIN = 'epc.mynetwork.com'
REMOTE_IP_ADDRESS = '10.129.241.214'

#: Basic DiameterAVPs for ULA message
avp1 = ResultCodeAVP(DIAMETER_SUCCESS)
avp2 = OriginHostAVP(LOCAL_HOST_NAME)
avp3 = OriginRealmAVP(LOCAL_DOMAIN)
avp4 = AuthSessionStateAVP(NO_STATE_MAINTAINED)

#: Vendor-Specific-Application-Id AVP
vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
auth_app_id_avp = AuthApplicationIdAVP(DIAMETER_APPLICATION_S6a_S6d)

avp5 = VendorSpecificApplicationIdAVP([vendor_id_avp, auth_app_id_avp])

#: Supported-Features AVP
vendor_id_avp = VendorIdAVP(VENDOR_ID_3GPP)
feature_list_id_avp = FeatureListIdAVP(1)
feature_list_avp = FeatureListAVP(402653191)

avp6 = SupportedFeaturesAVP([vendor_id_avp, feature_list_id_avp, feature_list_avp])

#: ULA-Flags AVP (which is not defined in the library)
avp7 = DiameterAVP(code=1406, flags=192, vendor_id=10415, data=1)

#: Setting up Diameter connection
app = Diameter()
app.config = {'MODE': 'CLIENT', 'APPLICATIONS': [{'vendor_id': VENDOR_ID_3GPP, 'app_id': DIAMETER_APPLICATION_S6a_S6d}], 'LOCAL_NODE_HOST_NAME': LOCAL_HOST_NAME, 'LOCAL_NODE_REALM': LOCAL_DOMAIN, 'LOCAL_NODE_IP_ADDRESS': LOCAL_IP_ADDRESS, 'LOCAL_NODE_PORT': 3868, 'PEER_NODE_HOSTNAME': REMOTE_HOST_NAME, 'PEER_NODE_REALM': REMOTE_DOMAIN, 'PEER_NODE_IP_ADDRESS': REMOTE_IP_ADDRESS, 'PEER_NODE_PORT': 3868, 'WATCHDOG_TIMEOUT': 60}

with app.context():
    while app.is_open():
        ulr = app.get_message()

        if ulr:
            #: Basic validation and ULA message creation
            if ulr.user_name_avp.data.decode("utf-8") == "123456789123456":
                avp0 = ulr.session_id_avp
                avps = [avp0, avp1, avp2, avp3, avp4, avp5, avp6, avp7]

                ula = DiameterAnswer(header=ulr.header, avps=avps)
                app.send_message(ula)
```

The exact same pattern happens here. Imports, constants definitions, DiameterAVPs instantiation and DiameterAnswer creation. However it worths note two differences here.

```python
#: ULA-Flags AVP
avp7 = DiameterAVP(code=1406, flags=192, vendor_id=10415, data=1)
```

Instead of instantiating the UlaFlagsAVP object, we have used the base DiameterAVP object to show that it may be used at the same way a especialized subclass. That's a design choice.

```python
with app.context():
    while app.is_open():
        ulr = app.get_message()

        if ulr:
            #: Basic validation and ULA message creation
            if ulr.user_name_avp.data.decode("utf-8") == "123456789123456":
                avp0 = ulr.session_id_avp
                avps = [avp0, avp1, avp2, avp3, avp4, avp5, avp6, avp7]

                ula = DiameterAnswer(header=ulr.header, avps=avps)
                app.send_message(ula)
```

The ULA message creation is within the `with` statement code block, because we need to perform specific procedures before replying a Diameter Request message. Instead of using `.send_message()`, we called `.get_message()` method to track any incoming Diameter Message. Naturally, we are expecting Update-Location-Request messages. Next we check if it is a valid object (not `None`), otherwise it would throw an exception.

Several Diameter Messages define sessions, and because of that, the Diameter Answer for a given Diameter Request needs to follow the exact same Session-Id AVP. That's why we have accessed the Update-Location-Request's Session-Id AVP data by using `ulr.session_id_avp`.

The Diameter Answer messages need to have the exact same Hop-by-Hop and End-to-End, the reason we need to pass it in `DiameterAnswer` object instantiation. See that we have used a different pattern to call `DiameterAnswer` when compared to `DiameterRequest`.

Finally, we are able to reply the ULR by sending the ULA object. Here we find another difference. In one hand, when sending a request, the `.send_message()` will return an DiameterAnswer object. In other hand, when sending a answer, the `.send_message()` will return `None`. That's why we didn't assign it to a variable.
