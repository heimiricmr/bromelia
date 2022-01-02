# Building Blocks Part 3: Diameter Messages

The *bromelia* library is powered with all standard Diameter Messages from RFC 6733 and much more. There are at least three ways to create both standard and custom Diameter Messages.

This document covers the DiameterMessage class's fundamentals and the creation of Diameter Message custom classes and objects.

This page contains the following sections:

- [Fundamentals](#fundamentals)
- [DiameterHeader](#diameterheader)
- [DiameterMessage](#diametermessage)
- [Standard Diameter Messages](#standard-diameter-messages)
- [Dunder Methods](#dunder-methods)
- [Another Complete reference (unittest files)](#another-complete-reference-unittest-files)
- [Powerful feature comes to play again: The load staticmethod](#powerful-feature-comes-to-play-again-the-load-staticmethod)
- [Extensibility: Create Your Own Diameter Message Extension](#extensibility-create-your-own-diameter-message-extension)

## Fundamentals

When it comes to Diameter Message handling, *bromelia* makes use of two available modules: `bromelia.base` and `bromelia.messages`.

### The `base` module

The `bromelia.base` module contains three classes for creation, handling and parsing of [Diameter Headers](https://tools.ietf.org/html/rfc6733#page-34) (`DiameterHeader`), Diameter Messages (`DiameterMessage`) and [Diameter AVPs](https://tools.ietf.org/html/rfc6733#page-40). Aside that, it has built-in also more two specific classes for Diameter Messages: Diameter Requests (`DiameterRequest`) and Diameter Answers (`DiameterAnswer`). For more details on Diameter AVP handling, see [here](avps.md).

The `DiameterHeader` class represents a Diameter Header including all its header fields (`version`, `length`, `flags`, `command code`, `application id`, `hop by hop` and `end to end`) as instance attributes. It has several methods to handle easily its attributes.

The `DiameterMessage` class represents a generic Diameter Message which depends on a DiameterHeader object and one or more DiameterAVP objects. It has methods to allow append, pop, update, verify AVPs and more.

Both `DiameterRequest` and `DiameterAnswer` are classes created to facilitate the creation of custom Diameter Message classes by other developers. They have two private methods used to set the `hop_by_hop` (`__set_hop_by_hop_identifier`) and the `end_to_end` (`__set_end_to_end_identifier`) attributes. Not going to jump into it, but it worths get it clear in mind.

### The `message` module

The `bromelia.messages` contains classes which represent all stardard Diameter Messages from RFC 6733. It depends on `DiameterRequest` and `DiameterAnswer` classes from the `bromelia.base` module. This design unlocks a powerful way to create custom Diameter Message classes that may be used in another Diameter applications. We are going to deep dive on how to create and ship it to another developers later.

## DiameterHeader

The DiameterHeader class implements several methods, the `.load()` classmethod and other instance methods such as `.dump()` and `.copy()`.

There are a few setters-like and verification methods methods for bit flags handling such as `.set_request_bit()`, `.is_request()`, `.set_proxiable_bit()`, `.is_proxiable()`, `.set_error_bit()`, `.is_error()`, `.set_retransmitted_bit()` and `.is_retransmitted()`.

There are also getters-like methods such as `.get_version()`, `.get_length()`, `.get_flags()`, `.get_command_code()`, `.get_application_id()`, `.get_hop_by_hop()`, `.get_end_to_end()` and `.get_flags_bit()`.

The best way to create Diameter Headers is by just instantiating an object of DiameterHeader class.

### Basic Usage for DiameterHeader

To create a DiameterHeader object, just import the class and instantiate it.

```python
>>> from bromelia.base import DiameterHeader
>>> header = DiameterHeader()
>>> header
<Diameter Header: Unknown [], 0 [Diameter common message]>
```

Look at each attribute value.

```python
>>> header.version
b'\x01'
>>> header.get_version()
1
>>> header.length
b'\x00\x00\x14'
>>> header.get_length()
20
>>> header.flags
b'\x00'
>>> header.get_flags()
0
>>> header.command_code
b'\x00\x00\x00'
>>> header.get_command_code()
0
>>> header.application_id
b'\x00\x00\x00\x00'
>>> header.get_application_id()
0
>>> header.hop_by_hop
b'\x00\x00\x00\x00'
>>> header.get_hop_by_hop()
0
>>> header.end_to_end
b'\x00\x00\x00\x00'
>>> header.get_end_to_end()
0
```

All DiameterHeader class objects store its attributes as byte. This design lies on the nature of Diameter protocol.

Sometimes it is better see some data in another format such as Integer or String. That's why we call the getters-like methods such as `.get_version()`, `.get_length()`, `.get_flags()`, `.get_command_code()`, `.get_application_id()`, `.get_hop_by_hop()` and `.get_end_to_end()`.

As we can see, the previous DiameterHeader object does not contain data at all. In order to create DiameterHeader objects which represents real Diameter Headers, you can either create a raw DiameterHeader object and populate its attributes on the fly, or create a raw DiameterHeader object by passing constructor input arguments.

#### On the fly for DiameterHeader

```python
>>> from bromelia.base import DiameterHeader
>>> header = DiameterHeader()
>>> header.version = 1
>>> header.flags = 40
>>> header.command_code = 280
>>> header.application_id = 0
>>> header.hop_by_hop = 11111
>>> header.end_to_end = 11111
>>> header
<Diameter Header: 280 [DWA] ERR, 0 [Diameter common message]>
```

#### Constructor for DiameterHeader

```python
>>> from bromelia.base import DiameterHeader
>>> header = DiameterHeader(1, 40, 280, 0, 11111, 11111)
>>> header
<Diameter Header: 280 [DWA] ERR, 0 [Diameter common message]>
```

It is possible changing values for each attribute that represents Diameter Header fields. However there is another approach specifically for `flags` attribute. Just use one of the setters-like methods such as `.set_request_bit()`, `.set_proxiable_bit()`, `.set_error_bit()` and `.set_retransmitted_bit()`. See below from the "constructor" example.

```python
>>> from bromelia.base import DiameterHeader
>>> header = DiameterHeader(1, 0, 280, 0, 11111, 11111)
>>> header
<Diameter Header: 280 [DWA], 0 [Diameter common message]>
>>> header.set_request_bit(True)
>>> header
<Diameter Header: 280 [DWR] REQ, 0 [Diameter common message]>
>>> header.get_flags()
128
>>> header.set_proxiable_bit(True)
>>> header
<Diameter Header: 280 [DWR] REQ|PXY, 0 [Diameter common message]>
>>> header.get_flags()
192
>>> header.set_error_bit(True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "F:\bromelia\base.py", line 361, in set_error_bit
    raise DiameterHeaderError("E-bit MUST NOT be set when R-bit "\
bromelia.exceptions.DiameterHeaderError: E-bit MUST NOT be set when R-bit is set
>>> header.set_request_bit(False)
<Diameter Header: 280 [DWA] PXY, 0 [Diameter common message]>
>>> header.get_flags()
64
>>> header.set_error_bit(True)
>>> header
<Diameter Header: 280 [DWA] PXY|ERR, 0 [Diameter common message]>
>>> header.get_flags()
96
```

It is pretty clear the `__repr__()` dunder method tracks the `flags` attribute to give the user the DiameterHeader object state.

You can also perform a verification if a given flag field bit is set.

```python
>>> header
<Diameter Header: 280 [DWA] PXY|ERR, 0 [Diameter common message]>
>>> header.is_request()
False
>>> header.is_proxiable()
True
>>> header.is_error()
True
>>> header.is_retransmitted()
False
```

## DiameterMessage

As per DiameterMessage's contructor, an object may be instantiated by passing a DiameterHeader object and a list of DiameterAVPs objects. Together they define the two main DiameterMessage attributes: `header` and `avps`. It is also possible to have alias attributes to its DiameterAVP objects found in the `avps` attribute.

The DiameterMessage class implements several methods, the `.load()` staticmethod, the `.convert()` classmethod and a few instance methods such as `.dump()` and `.copy()`.

The `.append()` method is used to add only one DiameterAVP object into the DiameterMessage object's `avp` attribute. The `.extend()` method is used to add multiple DiameterAVP objects into the DiameterMessage object's `avp` attribute. The `.pop()` method is used to remove a DiameterAVP object from the DiameterMessage object's `avp` attribute. The `.clenaup()` method is used to cleanup all DiameterAVP objects from a DiameterMessage object. The `.has_avp()` checks if DiameterMessage has a given DiameterAVP by its name. The `.update_key()` method allows to change the alias attribute for a given DiameterAVP object in `avps` attribute. The `.update_avps()` method allows to update smoothly the data attribute (or the field) of all DiameterAVP objects of a given DiameterMessage.

Aside DiameterAVP objects oriented methods, there are also a few DiameterHeader objects oriented methods which follows the setters and getters-like pattern.

Only one setter-like method has been implemented for bit flags handling based on the application id. The `.set_flag_by_app_id()` method will edit the DiameterHeader object in the `header` attribute.

The getters-like methods are pretty straighforwarded and have the same structure seen before: `.get_version()`, `.get_length()`, `.get_flags()`, `.get_command_code()`, `.get_application_id()`, `.get_hop_by_hop()` and `.get_end_to_end()`. These are alias to the DiameterHeader object attributes.

### Basic Usage for DiameterMessage

To create a DiameterMessage object, just import the class and instantiate it.

```python
>>> from bromelia.base import DiameterMessage
>>> message = DiameterMessage()
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>
```

Look at each attribute value.

```python
>>> message.header
<Diameter Header: Unknown [], 0 [Diameter common message]>
>>> message.avps
[]
>>> message.header.length
b'\x00\x00\x14'
>>> message.get_length()
20
>>> message.header.flags
b'\x00'
>>> message.get_flags()
0
>>> message.header.command_code
b'\x00\x00\x00'
>>> message.get_command_code()
0
>>> message.header.application_id
b'\x00\x00\x00\x00'
>>> message.get_application_id()
0
>>> message.header.hop_by_hop
b'\x00\x00\x00\x00'
>>> message.get_hop_by_hop()
0
>>> message.header.end_to_end
b'\x00\x00\x00\x00'
>>> message.get_end_to_end()
0
```

The DiameterMessage's getters-like methods are a way to access attributes value from the `header` attribute in a more suitable format such as Integer or String.

Below you may find two ways to create meaningful DiameterMessage objects.

#### On the fly for DiameterMessage

```python
>>> from bromelia.base import DiameterMessage
>>> message = DiameterMessage()
>>> message.header.version = 1
>>> message.header.flags = 40
>>> message.header.command_code = 280
>>> message.header.application_id = 0
>>> message.header.hop_by_hop = 11111
>>> message.header.end_to_end = 11111
>>> message
<Diameter Message: 280 [DWA] ERR, 0 [Diameter common message], 0 AVP(s)>
>>> from bromelia.base import DiameterAVP
>>> avp = DiameterAVP(1, 10415, 40, "Mobile-Network")
>>> message.append(avp)
>>> message
<Diameter Message: 280 [DWA] ERR, 0 [Diameter common message], 1 AVP(s)>
```

#### Constructor for DiameterMessage

```python
>>> from bromelia.base import DiameterAVP
>>> from bromelia.base import DiameterHeader
>>> from bromelia.base import DiameterMessage
>>> header = DiameterHeader(1, 40, 280, 0, 11111, 11111)
>>> avps = list()
>>> avps.append(DiameterAVP(1, 40, 10415, "Mobile-Network"))
>>> message = DiameterMessage(header, avps)
>>> message
<Diameter Message: 280 [DWA] ERR, 0 [Diameter common message], 1 AVP(s)>
```

#### DiameterAVP objects handling methods

It is pretty reasonable thinking there are three operations while dealing with Diameter Messages when it comes to AVPs. The add (`.append()` and `.extend()` methods), update (`.update_key()` method) and delete (`.pop()` and `.cleanup()` method) AVPs operations has been implemented in DiameterMessage class to allow create custom DiameterMessage objects.

First, let's define the set for our examples.

```python
>>> from bromelia.avps import ProxyStateAVP
>>> from bromelia.avps import SessionTimeoutAVP
>>> from bromelia.base import DiameterMessage
>>> message = DiameterMessage()
>>> avp1 = SessionTimeoutAVP(10799)
>>> avp2 = ProxyStateAVP("CLOSED")
```

##### Append & Extend

To include a DiameterAVP object we just need to call the `.append()`. This method will create a custom attribute to allow an easy access to the AVP in the DiameterMessage object.

See below how the DiameterMessage object looks like after appending one DiameterAVP object.

```python
>>> message.append(avp1)
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 1 AVP(s)>
>>> message.__dict__
{'header': <Diameter Header: Unknown [], 0 [Diameter common message]>, 'avps': [<Diameter AVP: 27 [Session-Timeout] MANDATORY>], '_loaded': False, 'session_timeout_avp': <Diameter AVP: 27 [Session-Timeout] MANDATORY>}
```

It gets easy to access the SessionTimeoutAVP object with the custom attribute. See that it is exactly the same `avp1` previously defined.

```python
>>> message.session_timeout_avp
<Diameter AVP: 27 [Session-Timeout] MANDATORY>
>>> message.session_timeout_avp.data
b'\x00\x00*/'
>>> message.session_timeout_avp == avp1
True
```

Now we are going to add a second DiameterAVP object into it.

```python
>>> message.append(avp2)
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>
>>> message.__dict__
{'header': <Diameter Header: Unknown [], 0 [Diameter common message]>, 'avps': [<Diameter AVP: 27 [Session-Timeout] MANDATORY>, <Diameter AVP: 33 [Proxy-State] MANDATORY>], '_loaded': False, 'session_timeout_avp': <Diameter AVP: 27 [Session-Timeout] MANDATORY>, 'proxy_state_avp': <Diameter AVP: 33 [Proxy-State] MANDATORY>}
```

The same happens here with the DiameterAVP object `avp2`.

```python
>>> message.proxy_state_avp
<Diameter AVP: 33 [Proxy-State] MANDATORY>
>>> message.proxy_state_avp.data
b'CLOSED'
>>> message.proxy_state_avp == avp2
True
```

Imagine how cumbersome would be to append DiameterAVP objects one at a time into a DiameterMessage object if we would want to put into it more than one, two or even six DiameterAVP objects, but a list of maybe dozens. To address this requirement, there is the `.extend()` method.

```python
>>> from bromelia import DIAMETER_APPLICATION_SWm
>>> from bromelia.avps import AuthApplicationIdAVP
>>> from bromelia.avps import HostIpAddressAVP
>>> from bromelia.base import DiameterMessage
>>> message = DiameterMessage()
>>> avp1 = AuthApplicationIdAVP(DIAMETER_APPLICATION_SWm)
>>> avp2 = HostIpAddressAVP("10.129.241.214")
>>> avps = [avp1, avp2]
>>> message.extend(avps)
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 2 AVP(s)>
```

And all custom attributes are available as well.

```python
>>> message.__dict__
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>, <Diameter AVP: 257 [Host-IP-Address] MANDATORY>], '_loaded': False, 'auth_application_id_avp': <Diameter AVP: 258 [Auth-Application-Id] MANDATORY>, 'host_ip_address_avp': <Diameter AVP: 257 [Host-IP-Address] MANDATORY>}
>>> message.host_ip_address_avp.data
b'\x00\x01\n\x81\xf1\xd6'
>>> message.host_ip_address_avp.get_ip_address()
'10.129.241.214'
>>> message.host_ip_address_avp.is_ipv4()
True
>>> message.host_ip_address_avp.is_ipv6()
False
>>> len(message.auth_application_id_avp)
12
>>> message.auth_application_id_avp.data
b'\x01\x00\x000'
```

##### Pop & Cleanup

Don't want that DiameterAVP object in your DiameterMessage's `avp` attribute? Well, just pop it out.

```python
>>> from bromelia.avps import ClassAVP
>>> from bromelia.avps import ProxyStateAVP
>>> from bromelia.avps import SessionTimeoutAVP
>>> from bromelia.avps import UserNameAVP
>>> from bromelia.base import DiameterMessage
>>> avp1 = ClassAVP("CLOSED")
>>> avp2 = ProxyStateAVP("OPENED")
>>> avp3 = SessionTimeoutAVP(10799)
>>> avp4 = UserNameAVP("myuser@mydomain.com")
>>> avps = [avp1,avp2,avp3,avp4]
>>> message = DiameterMessage(avps=avps)
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 4 AVP(s)>
>>> message.__dict__
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 25 [Class] MANDATORY>, <Diameter AVP: 33 [Proxy-State] MANDATORY>, <Diameter AVP: 27 [Session-Timeout] MANDATORY>, <Diameter AVP: 1 [User-Name] MANDATORY>], '_loaded': False, 'class_avp': <Diameter AVP: 25 [Class] MANDATORY>, 'proxy_state_avp': <Diameter AVP: 33 [Proxy-State] MANDATORY>, 'session_timeout_avp': <Diameter AVP: 27 [Session-Timeout] MANDATORY>, 'user_name_avp': <Diameter AVP: 1 [User-Name] MANDATORY>}
>>> message.pop("proxy_state_avp")
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>
>>> message.__dict__
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 25 [Class] MANDATORY>, <Diameter AVP: 27 [Session-Timeout] MANDATORY>, <Diameter AVP: 1 [User-Name] MANDATORY>], '_loaded': False, 'class_avp': <Diameter AVP: 25 [Class] MANDATORY>, 'session_timeout_avp': <Diameter AVP: 27 [Session-Timeout] MANDATORY>, 'user_name_avp': <Diameter AVP: 1 [User-Name] MANDATORY>}
```

Surely would be tedious if you would like to try another set of AVPs in your DiameterMessage, but you need first remove each DiameterAVP object at a time. Just go with `.cleanup()` to get the work done.

```python
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>
>>> message.cleanup()
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 0 AVP(s)>
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [], '_loaded': False}
```

##### Has Key

There is a built-in method to check it for you. Let's take a look.

```python
>>> from bromelia import DIAMETER_FIRST_REGISTRATION
>>> from bromelia import DIAMETER_LOGOUT
>>> from bromelia import INBAND_SECURITY_ID_NO_SECURITY
>>> from bromelia.avps import ExperimentalResultCodeAVP
>>> from bromelia.avps import InbandSecurityIdAVP
>>> from bromelia.avps import TerminationCauseAVP
>>> from bromelia.base import DiameterHeader
>>> from bromelia.base import DiameterMessage
>>> header = DiameterHeader(1, 80, 278, 1, 22222, 33333)
>>> avp1 = ExperimentalResultCodeAVP(DIAMETER_FIRST_REGISTRATION)
>>> avp2 = InbandSecurityIdAVP(INBAND_SECURITY_ID_NO_SECURITY)
>>> avp3 = TerminationCauseAVP(DIAMETER_LOGOUT)
>>> avps = [avp1,avp2,avp3]
>>> message = DiameterMessage(header)
>>> message.extend(avps)
>>> message
<Diameter Message: Unknown [] PXY, 1 [NASREQ], 3 AVP(s)>
>>> message.__dict__
{'_header': <Diameter Header: Unknown [] PXY, 1 [NASREQ]>, '_avps': [<Diameter AVP: 298 [Experimental-Result-Code] MANDATORY>, <Diameter AVP: 299 [Inband-Security-Id]>, <Diameter AVP: 295 [Termination-Cause] MANDATORY>], '_loaded': False, 'experimental_result_code_avp': <Diameter AVP: 298 [Experimental-Result-Code] MANDATORY>, 'inband_security_id_avp': <Diameter AVP: 299 [Inband-Security-Id]>, 'termination_cause_avp': <Diameter AVP: 295 [Termination-Cause] MANDATORY>}
>>> message.has_avp("experimental_result_code_avp")
True
>>> message.has_avp("termination_cause_avp")
True
>>> message.has_avp("inband_security_id_avp")
True
```

Note all built-in DiameterMessage attributes related to DiameterAVP objects has the `<diameter_avp_name>_avp` format (a suffix `_avp` attached). However, you may search a given DiameterAVP object in a DiameterMessage by putting the `diameter_avp_name` only. Consider using the snippet code above with this approach.

```python
>>> message.has_avp("experimental_result_code")
True
>>> message.has_avp("termination_cause")
True
>>> message.has_avp("inband_security_id")
True
```

##### Update DiameterAVP data

Now you may update the DiameterAVP data on the go by simply calling the `.update_avps()` method passing the dictionary with new values you want to load a given DiameterMessage object. It already computes the final DiameterMessage length and updates its value.

```python
>>> from bromelia.avps import OriginHostAVP, OriginRealmAVP, DestinationRealmAVP
>>> from bromelia.base import DiameterMessage
>>> message = DiameterMessage()
>>> message.extend([OriginHostAVP("computer.network"), OriginRealmAVP("network"), DestinationRealmAVP("network")])
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 3 AVP(s)>
>>> message.__dict__
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 264 [Origin-Host] MANDATORY>, <Diameter AVP: 296 [Origin-Realm] MANDATORY>, <Diameter AVP: 283 [Destination-Realm] MANDATORY>], '_loaded': False, 'origin_host_avp': <Diameter AVP: 264 [Origin-Host] MANDATORY>, 'origin_realm_avp': <Diameter AVP: 296 [Origin-Realm] MANDATORY>, 'destination_realm_avp': <Diameter AVP: 283 [Destination-Realm] MANDATORY>}
>>> len(message)
76
>>> for avp in message.avps:
...     print(avp, avp.data)
...
<Diameter AVP: 264 [Origin-Host] MANDATORY> b'computer.network'
<Diameter AVP: 296 [Origin-Realm] MANDATORY> b'network'
<Diameter AVP: 283 [Destination-Realm] MANDATORY> b'network'
>>> avps = {
  "origin_host": "hss.br.epc.3gppnetwork.org",
  "origin_realm": "br.epc.3gppnetwork.org",
  "destination_realm": "pt.epc.3gppnetwork.org",
}
>>> message.update_avps(avps)
>>> len(message)
120
>>> for avp in message.avps:
...     print(avp, avp.data)
...
<Diameter AVP: 264 [Origin-Host] MANDATORY> b'hss.br.epc.3gppnetwork.org'
<Diameter AVP: 296 [Origin-Realm] MANDATORY> b'br.epc.3gppnetwork.org'
<Diameter AVP: 283 [Destination-Realm] MANDATORY> b'pt.epc.3gppnetwork.org'
```

##### Update Key

Sometimes you may add a custom DiameterAVP object that is not defined anywhere. Once *bromelia* is not aware on this spec, it will create a custom attribute for DiameterMessage named as `unknown_avp`. As new unknown DiameterAVP objects are placed into DiameterMessage's `avps` attribute, it will named it as `unknown_avp__1`, `unknown_avp__2` and so on. That's why `.update_key()` comes into play, to change as per your taste.

```python
>>> from bromelia.base import DiameterAVP
>>> from bromelia.base import DiameterMessage
>>> message = DiameterMessage()
>>> avp = DiameterAVP()
>>> message.extend(4*[avp])
>>> message
<Diameter Message: Unknown [], 0 [Diameter common message], 4 AVP(s)>
>>> message.__dict__
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 0 [Unknown]>, <Diameter AVP: 0 [Unknown]>, <Diameter AVP: 0 [Unknown]>, <Diameter AVP: 0 [Unknown]>], '_loaded': False, 'unknown_avp': <Diameter AVP: 0 [Unknown]>, 'unknown_avp__1': <Diameter AVP: 0 [Unknown]>, 'unknown_avp__2': <Diameter AVP: 0 [Unknown]>, 'unknown_avp__3': <Diameter AVP: 0 [Unknown]>}
>>> message.update_key("unknown_avp", "my_custom_avp")
>>> message.update_key("unknown_avp__1", "my_amazing_custom_avp")
>>> message
{'_header': <Diameter Header: Unknown [], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 0 [Unknown]>, <Diameter AVP: 0 [Unknown]>, <Diameter AVP: 0 [Unknown]>, <Diameter AVP: 0 [Unknown]>], '_loaded': False, 'unknown_avp__2': <Diameter AVP: 0 [Unknown]>, 'unknown_avp__3': <Diameter AVP: 0 [Unknown]>, 'my_custom_avp': <Diameter AVP: 0 [Unknown]>, 'my_amazing_custom_avp': <Diameter AVP: 0 [Unknown]>}
```

However, don't try to change an existing key, otherwise an expcetion will be thrown!

```python
>>> message.update_key("unknown_avp__2", "my_amazing_custom_avp")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "F:\bromelia\base.py", line 640, in update_key
    raise DiameterMessageError(f"`{old_avp_key}` key not defined")
bromelia.exceptions.DiameterMessageError: `my_amazing_custom_avp` key already defined
```

Needless to mention, but an exception will also be thrown if you try to change a nonexistent one!

```python
>>> message.update_key("not_known_avp", "my_blasting_custom_avp")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "F:\bromelia\base.py", line 640, in update_key
    raise DiameterMessageError(f"`{old_avp_key}` key not defined")
bromelia.exceptions.DiameterMessageError: `not_known_avp` key not defined
```

## Standard Diameter Messages

Every network protocol defines base messages to allow communication. In the Diameter standard, it is not different and we already know a message is composed of a header and one or more AVPs.

Aside that there are a set of core messages each one used for a given purpose.

For example, two Diameter Peers cannot talk to each other directly until there is a connection established between them. To achieve this, both peers need to be aware on the other one previously. A handshake will take place only if that requirement is fulfilled.

That is the moment capabilities need to be exchange through the CER/CEA pair messages. Browsing the RFC 6733 we found the Section [5.3.1. Capabilities-Exchange-Request](https://tools.ietf.org/html/rfc6733#section-5.3.1) which defines the Message Format for CER as per Command Code Format (CFF) specification.

```text
<CER> ::= < Diameter Header: 257, REQ >
                   { Origin-Host }
                   { Origin-Realm }
                1* { Host-IP-Address }
                   { Vendor-Id }
                   { Product-Name }
                   [ Origin-State-Id ]
                 * [ Supported-Vendor-Id ]
                 * [ Auth-Application-Id ]
                 * [ Inband-Security-Id ]
                 * [ Acct-Application-Id ]
                 * [ Vendor-Specific-Application-Id ]
                   [ Firmware-Revision ]
                 * [ AVP ]
```

The square brackets refers to optional AVPs, which means there is no need to include it into the CER message. The remaining AVPs wrapped in curly brackets are mandatory and there is no way to not include it.

We already have seen so far everything we need to make it happen through the library. Let's hands on!

### Handcrafted

```python
>>> from bromelia.avps import HostIpAddressAVP
>>> from bromelia.avps import OriginHostAVP
>>> from bromelia.avps import OriginRealmAVP
>>> from bromelia.avps import ProductNameAVP
>>> from bromelia.avps import VendorIdAVP
>>> from bromelia.base import DiameterHeader
>>> from bromelia.base import DiameterMessage
>>> avp1 = HostIpAddressAVP("10.129.241.214")
>>> avp2 = OriginHostAVP("myhost.mynetwork.com")
>>> avp3 = OriginRealmAVP("mynetwork.com")
>>> avp4 = ProductNameAVP("MyDiameterApplicationServer")
>>> avp5 = VendorIdAVP()
>>> avps = [avp1,avp2,avp3,avp4,avp5]
>>> header = DiameterHeader(1, 128, 257, 0, 12345, 54321)
>>> message = DiameterMessage(header,avps)
>>> message
<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 5 AVP(s)>
```

And we can see its internal attributes.

```python
>>> message.__dict__
{'header': <Diameter Header: 257 [CER] REQ, 0 [Diameter common message]>, 'avps': [<Diameter AVP: 264 [Origin-Host] MANDATORY>, <Diameter AVP: 296 [Origin-Realm] MANDATORY>, <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, <Diameter AVP: 266 [Vendor-Id] MANDATORY>, <Diameter AVP: 269 [Product-Name]>], '_loaded': False, 'origin_host_avp': <Diameter AVP: 264 [Origin-Host] MANDATORY>, 'origin_realm_avp': <Diameter AVP: 296 [Origin-Realm] MANDATORY>, 'host_ip_address_avp': <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, 'vendor_id_avp': <Diameter AVP: 266 [Vendor-Id] MANDATORY>, 'product_name_avp': <Diameter AVP: 269 [Product-Name]>}
```

Finally we have got our message ready. But it took a while to set it up. What if we had a way to do it quickly? That's why the standard DiameterMessage subclasses comes into play.

### Ready-to-Go

```python
>>> from bromelia.messages import CER # CapabilitiesExchangeRequest
>>> cer = CER()
>>> cer
<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>
```

Yeah, that's right! By calling only one line of code we can create a CER message. You may asking why in our first example there are 5 AVPs and now there are 6 AVPs. Well, the CapabilitiesExchangeRequest class has been implemented to include all 5 mandatory AVPs plus the Firmware-Revision AVP once a lot of Diameter networks in Telecom industry has such AVP.

By the way, the CapabilitiesExchangeRequest class deals with the hostname and domain resolution as well as the IP address of your host. That's the reason you don't need to provide it manually.

See below its internal attributes.

```python
>>> cer.__dict__
{'header': <Diameter Header: 257 [CER] REQ, 0 [Diameter common message]>, 'avps': [<Diameter AVP: 264 [Origin-Host] MANDATORY>, <Diameter AVP: 296 [Origin-Realm] MANDATORY>, <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, <Diameter AVP: 266 [Vendor-Id] MANDATORY>, <Diameter AVP: 269 [Product-Name]>, <Diameter AVP: 267 [Firmware-Revision]>], '_loaded': False, 'origin_host_avp': <Diameter AVP: 264 [Origin-Host] MANDATORY>, 'origin_realm_avp': <Diameter AVP: 296 [Origin-Realm] MANDATORY>, 'host_ip_address_avp': <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, 'vendor_id_avp': <Diameter AVP: 266 [Vendor-Id] MANDATORY>, 'product_name_avp': <Diameter AVP: 269 [Product-Name]>, 'firmware_revision_avp': <Diameter AVP: 267 [Firmware-Revision]>}
```

There is also a way to check what are the mandatory and optional AVPs of a given standard DiameterMessage subclasses. As we are talking about CER, let's see it by checking its class attributes `mandatory` and `optionals`.

#### Mandatory (CER)

```python
>>> CER.mandatory
{'origin_host': <class 'bromelia.avps.ietf.rfc6733.OriginHostAVP'>, 'origin_realm': <class 'bromelia.avps.ietf.rfc6733.OriginRealmAVP'>, 'host_ip_address': <class 'bromelia.avps.ietf.rfc6733.HostIpAddressAVP'>, 'vendor_id': <class 'bromelia.avps.ietf.rfc6733.VendorIdAVP'>, 'product_name': <class 'bromelia.avps.ietf.rfc6733.ProductNameAVP'>}
```

#### Optionals (CER)

```python
>>> CER.optionals
{'origin_state_id': <class 'bromelia.avps.ietf.rfc6733.OriginStateIdAVP'>, 'supported_vendor_id': <class 'bromelia.avps.ietf.rfc6733.SupportedVendorIdAVP'>, 'auth_application_id': <class 'bromelia.avps.ietf.rfc6733.AuthApplicationIdAVP'>, 'inband_security_id': <class 'bromelia.avps.ietf.rfc6733.InbandSecurityIdAVP'>, 'acct_application_id': <class 'bromelia.avps.ietf.rfc6733.AcctApplicationIdAVP'>, 'vendor_specific_application_id': <class 'bromelia.avps.ietf.rfc6733.VendorSpecificApplicationIdAVP'>, 'firmware_revision': <class 'bromelia.avps.ietf.rfc6733.FirmwareRevisionAVP'>}
```

### Building a response

Maybe your Diameter application has received a CER message and it needs to reply with a CEA message. Browsing the RFC 6733 we found the Section [5.3.2. Capabilities-Exchange-Answer](https://tools.ietf.org/html/rfc6733#section-5.3.2) which defines the Message Format for CEA as per Command Code Format (CFF) specification.

```text
<CEA> ::= < Diameter Header: 257 >
                   { Result-Code }
                   { Origin-Host }
                   { Origin-Realm }
                1* { Host-IP-Address }
                   { Vendor-Id }
                   { Product-Name }
                   [ Origin-State-Id ]
                   [ Error-Message ]
                   [ Failed-AVP ]
                 * [ Supported-Vendor-Id ]
                 * [ Auth-Application-Id ]
                 * [ Inband-Security-Id ]
                 * [ Acct-Application-Id ]
                 * [ Vendor-Specific-Application-Id ]
                   [ Firmware-Revision ]
                 * [ AVP ]
```

We already know how to create it by hand, but we can simply instantiate a CapabilitiesExchangeAnswer object to do so.

```python
>>> from bromelia.messages import CEA # CapabilitiesExchangeAnswer
>>> cea = CEA()
>>> cea
<Diameter Message: 257 [CEA], 0 [Diameter common message], 7 AVP(s)>
```

It includes all mandatory AVPs and the optional Auth-Application-Id AVP.

However, if there is need to customize it with a different value in mandatory AVPs or include expected optional AVPs, the classes in `bromelia.messages` module provide a more flexible way to achieve this.

The CapabilitiesExchangeAnswer objects are instantiated with the ResultCodeAVP object attribute set as `DIAMETER_SUCCESS` by default, however your application may have specific constraints which needs a non-mandatory AVP in the CER message. Therefore your application could end the handshake connection and reply with another Result-Code AVP value and include a Failed-AVP AVP with the reason.

Below there are two examples on how to create a custom CEA message which applies to whatever other class in `bromelia.messages` module. Remember that each class this module has a `mandatory` and `optionals` class attribute.

#### Mandatory (CEA)

```python
>>> CEA.mandatory
{'result_code': <class 'bromelia.avps.ietf.rfc6733.ResultCodeAVP'>, 'origin_host': <class 'bromelia.avps.ietf.rfc6733.OriginHostAVP'>, 'origin_realm': <class 'bromelia.avps.ietf.rfc6733.OriginRealmAVP'>, 'host_ip_address': <class 'bromelia.avps.ietf.rfc6733.HostIpAddressAVP'>, 'vendor_id': <class 'bromelia.avps.ietf.rfc6733.VendorIdAVP'>, 'product_name': <class 'bromelia.avps.ietf.rfc6733.ProductNameAVP'>}
```

#### Optionals (CEA)

```python
>>> CEA.optionals
{'origin_state_id': <class 'bromelia.avps.ietf.rfc6733.OriginStateIdAVP'>, 'error_message': <class 'bromelia.avps.ietf.rfc6733.ErrorMessageAVP'>, 'failed_avp': <class 'bromelia.avps.ietf.rfc6733.FailedAvpAVP'>, 'supported_vendor_id': <class 'bromelia.avps.ietf.rfc6733.SupportedVendorIdAVP'>, 'auth_application_id': <class 'bromelia.avps.ietf.rfc6733.AuthApplicationIdAVP'>, 'inband_security_id': <class 'bromelia.avps.ietf.rfc6733.InbandSecurityIdAVP'>, 'acct_application_id': <class 'bromelia.avps.ietf.rfc6733.AcctApplicationIdAVP'>, 'vendor_specific_application_id': <class 'bromelia.avps.ietf.rfc6733.VendorSpecificApplicationIdAVP'>, 'firmware_revision': <class 'bromelia.avps.ietf.rfc6733.FirmwareRevisionAVP'>}
```

### Creating a dictionary with simple AVPs

In this example, we are going to create a dictionary `attrs` with one key from CEA's `mandatory` class attribute and one key from CEA's `optionals` class attribute. The value in each key will be the input argument with respective DiameterAVP subclass object. It applies to all DiameterAVP subclasses which inherint from all Diameter type classes except GroupedType.

```python
>>> from bromelia.messages import CEA # CapabilitiesExchangeAnswer
>>> from bromelia.constants import DIAMETER_MISSING_AVP
>>> attrs = {
...   "result_code": DIAMETER_MISSING_AVP,
...   "error_message": "Vendor-Specific-Application-Id AVP missing."
... }
>>> cea = CEA(**attrs)
>>> cea
<Diameter Message: 257 [CEA], 0 [Diameter common message], 8 AVP(s)>
```

Checking its internals.

```python
>>> cea.__dict__
{'_header': <Diameter Header: 257 [CEA], 0 [Diameter common message]>, '_avps': [<Diameter AVP: 268 [Result-Code] MANDATORY>, <Diameter AVP: 264 [Origin-Host] MANDATORY>, <Diameter AVP: 296 [Origin-Realm] MANDATORY>, <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, <Diameter AVP: 266 [Vendor-Id] MANDATORY>, <Diameter AVP: 269 [Product-Name]>, <Diameter AVP: 281 [Error-Message]>, <Diameter AVP: 258 [Auth-Application-Id] MANDATORY>], '_loaded': False, 'result_code_avp': <Diameter AVP: 268 [Result-Code] MANDATORY>, 'origin_host_avp': <Diameter AVP: 264 [Origin-Host] MANDATORY>, 'origin_realm_avp': <Diameter AVP: 296 [Origin-Realm] MANDATORY>, 'host_ip_address_avp': <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, 'vendor_id_avp': <Diameter AVP: 266 [Vendor-Id] MANDATORY>, 'product_name_avp': <Diameter AVP: 269 [Product-Name]>, 'error_message_avp': <Diameter AVP: 281 [Error-Message]>, 'auth_application_id_avp': <Diameter AVP: 258 [Auth-Application-Id] MANDATORY>}
```

Besides the expected CEA attributes (`result_code_avp`, `origin_host_avp`, `origin_realm_avp`, `host_ip_address_avp`, `vendor_id_avp`, `product_name_avp`, `auth_application_id_avp`), now we can see a new one (`error_message_avp`). By the way, the `result_code_avp` has a custom value (`DIAMETER_MISSING_AVP`) different from the default one (`DIAMETER_SUCCESS`).

```python
>>> cea.result_code_avp.data
b'\x00\x00\x13\x8d'
>>> cea.error_message_avp.data
b'Vendor-Specific-Application-Id AVP missing.'
```

### Creating a dictionary with one or more AVPs of Grouped type

This example applies if you need to custom a standard Diameter Message from `bromelia.messages` module which may have an DiameterAVP object which inherints from `GroupedType` class. The basic difference is that you need to provide a list of DiameterAVP objects which constitute that DiameterAVP object of GroupedType.

The `FailedAvpAVP` class in `bromelia.avps` module inherints from `GroupedType`. It may be composed of any DiameterAVP object inside of it. Then, we need to create a list of DiameterAVP objects and pass it to the `failed_avp` key to create a CEA message with this AVP.

Let's suppose we are going to inform the remote peer that its CER message has came with two AVPs with invalid length. First we are going to include the `DIAMETER_INVALID_AVP_LENGTH` result code and second the list of two DiameterAVP objects representing the intended AVPs.

By the way, we could also let the `error_message` key.

```python
>>> from bromelia.avps import DestinationHostAVP
>>> from bromelia.avps import DestinationationRealmAVP
>>> from bromelia.messages import CEA # CapabilitiesExchangeAnswer
>>> from bromelia.constants import DIAMETER_INVALID_AVP_LENGTH
>>> destination_host_error = DestinationHostAVP("your-remote-host.your-network.com")
>>> destination_realm_error = DestinationHostAVP("your-network.com")
>>> attrs = {
...   "result_code": DIAMETER_INVALID_AVP_LENGTH,
...   "failed_avp": [destination_host_error, destination_realm_error],
...   "error_message": "Invalid AVP length."
... }
>>> cea = CEA(**attrs)
>>> cea
<Diameter Message: 257 [CEA], 0 [Diameter common message], 9 AVP(s)>
```

Checking its internals.

```python
>>> cea.__dict__
{'header': <Diameter Header: 257 [CEA], 0 [Diameter common message]>, 'avps': [<Diameter AVP: 268 [Result-Code] MANDATORY>, <Diameter AVP: 264 [Origin-Host] MANDATORY>, <Diameter AVP: 296 [Origin-Realm] MANDATORY>, <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, <Diameter AVP: 266 [Vendor-Id] MANDATORY>, <Diameter AVP: 269 [Product-Name]>, <Diameter AVP: 281 [Error-Message]>, <Diameter AVP: 279 [Failed-AVP] MANDATORY>, <Diameter AVP: 258 [Auth-Application-Id] MANDATORY>], '_loaded': False, 'result_code_avp': <Diameter AVP: 268 [Result-Code] MANDATORY>, 'origin_host_avp': <Diameter AVP: 264 [Origin-Host] MANDATORY>, 'origin_realm_avp': <Diameter AVP: 296 [Origin-Realm] MANDATORY>, 'host_ip_address_avp': <Diameter AVP: 257 [Host-IP-Address] MANDATORY>, 'vendor_id_avp': <Diameter AVP: 266 [Vendor-Id] MANDATORY>, 'product_name_avp': <Diameter AVP: 269 [Product-Name]>, 'error_message_avp': <Diameter AVP: 281 [Error-Message]>, 'failed_avp_avp': <Diameter AVP: 279 [Failed-AVP] MANDATORY>, 'auth_application_id_avp': <Diameter AVP: 258 [Auth-Application-Id] MANDATORY>}
```

And the new DiameterAVP objects.

```python
>>> cea.result_code_avp.data
b'\x00\x00\x13\x95'
>>> cea.error_message_avp.data
b'Invalid AVP length.'
>>> cea.failed_avp_avp.data
b'\x00\x00\x01%@\x00\x00)your-remote-host.your-network.com\x00\x00\x00\x00\x00\x01%@\x00\x00\x18your-network.com'
```

The *bromelia* has implemented the standard Diameter Messages from RFC 6733. Take a look at `bromelia.messages` module and give a try the other classes. For sake of clarity, we encorage you to import those as per shown below. That way your code may be cleaner and readable.

```python
>>> from bromelia.messages import CER # CapabilitiesExchangeRequest
>>> from bromelia.messages import CEA # CapabilitiesExchangeAnswer
>>> from bromelia.messages import RAR # ReAuthRequest 
>>> from bromelia.messages import RAA # ReAuthAnswer
>>> from bromelia.messages import ASR # AbortSessionRequest
>>> from bromelia.messages import ASA # AbortSessionAnswer
>>> from bromelia.messages import STR # SessionTerminationRequest
>>> from bromelia.messages import STA # SessionTerminationAnswer
>>> from bromelia.messages import DWR # DeviceWatchdogRequest
>>> from bromelia.messages import DWA # DeviceWatchdogAnswer
>>> from bromelia.messages import DPR # DisconnectPeerRequest
>>> from bromelia.messages import DPA # DisconnectPeerAnswer
```

### Customization with Standard Messages

It's nothing new that Standard Messages classes we just have seen are inherinted from DiameterMessage class. That means we may leverage the use of its instance methods during the creation of DiameterMessage to an application.

```python
>>> from bromelia.messages import DWR # DeviceWatchdogRequest
>>> attrs = {
...   "origin_state_id": 1524733202
... }
>>> dwr = DWR(**attrs)
>>> dwr
<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 3 AVP(s)>
>>> dwr.__dict__
{'_header': <Diameter Header: 280 [DWR] REQ, 0 [Diameter common message]>, '_avps': [<Diameter AVP: 264 [Origin-Host] MANDATORY>, <Diameter AVP: 296 [Origin-Realm] MANDATORY>, <Diameter AVP: 278 [Origin-State-Id] MANDATORY>], '_loaded': False, 'origin_host_avp': <Diameter AVP: 264 [Origin-Host] MANDATORY>, 'origin_realm_avp': <Diameter AVP: 296 [Origin-Realm] MANDATORY>, 'origin_state_id_avp': <Diameter AVP: 278 [Origin-State-Id] MANDATORY>}
```

#### Adding AVPs

As per RFC 6733, that's all for Device-Watch-Request message. Are you going to test something unthinkable though? Maybe a DWR with custom AVPs? Just use either `.append()` or `.extend()` methods to include those new ones.

```python
>>> from bromelia.avps import ReAuthRequestTypeAVP
>>> from bromelia.avps import RedirectHostAVP
>>> from bromelia.avps import SubscriptionIdDataAVP
>>> avp1 = ReAuthRequestTypeAVP(RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
>>> dwr.append(avp1)
>>> dwr
>>> <Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 4 AVP(s)>
>>> avp2 = RedirectHostAVP("aaa://host.example.com;transport=tcp")
>>> avp3 = SubscriptionIdDataAVP("5521123456789")
>>> dwr.extend([avp2,avp3])
>>> dwr
>>> <Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 6 AVP(s)>
```

However surely your endpoint will reject it, especially if it is RFC compliance. Be prepare to see your Diameter connection tearing down! The Device-Watchdog-Request was made to have 3 AVPs maximum, 2 mandatories (`Origin-Host AVP` and `Origin-Realm AVP`) and 1 optional (`Origin-State-Id AVP`). This tutorial is only a way to introduce you the *bromelia* toolkits in order to show the flexibilities of the library.

#### Mandatory (DWR)

```python
>>> DWR.mandatory
{'origin_host': <class 'bromelia.avps.ietf.rfc6733.OriginHostAVP'>, 'origin_realm': <class 'bromelia.avps.ietf.rfc6733.OriginRealmAVP'>}
```

#### Optionals (DWR)

```python
>>> DWR.optionals
{'origin_state_id': <class 'bromelia.avps.ietf.rfc6733.OriginStateIdAVP'>}
```

#### Checking AVPs

Just to make sure, we can verify its internals.

```python
>>> dwr.has_avp("subscription_id_data_avp")
True
>>> dwr.has_avp("redirect_host_avp")
True
>>> dwr.has_avp("re_auth_request_type_avp")
True

```

#### Removing AVPs

Maybe after the rejection, you need to remove those DiameterAVP objects.

```python
>>> dwr.pop("subscription_id_data_avp")
>>> dwr.has_avp("subscription_id_data_avp")
False
>>> dwr.pop("redirect_host_avp")
>>> dwr.has_avp("redirect_host_avp")
False
>>> dwr.pop("re_auth_request_type_avp")
>>> dwr.has_avp("re_auth_request_type_avp")
False
>>> dwr
<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 3 AVP(s)>
```

#### Refactoring DiameterMessage object

For some reason you realised you want to make the DiameterMessage object again from the ground up by cleaning up all the DiameterAVP objects. We are going to make some changes, but already know if we send it to whatever RFC compliant enpoint, it will reject. Let's do it though!

```python
>>> dwr.cleanup()
>>> dwr
<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 0 AVP(s)>
>>> from bromelia.base import DiameterAVP
>>> dwr.append(DiameterAVP(1, 40, 10415, "Mobile-Network"))
>>> dwr
<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 1 AVP(s)>
>>> dwr.header.set_proxiable_bit(True)
>>> dwr.header.set_retransmitted_bit(True)
>>> dwr.__dict__
{'_header': <Diameter Header: 280 [DWR] REQ, 0 [Diameter common message]>, '_avps': [<Diameter AVP: 1 [User-Name] PROTECTED>], '_loaded': False, 'user_name_avp': <Diameter AVP: 1 [User-Name] PROTECTED>}
>>> dwr
<Diameter Message: 280 [DWR] REQ|PXY, 0 [Diameter common message], 1 AVP(s)>
>>> dwr.has_avp("user_name_avp")
True
>>> dwr.update_key("user_name_avp", "my_custom_avp")
>>> dwr.has_avp("user_name_avp")
False
>>> dwr.has_avp("my_custom_avp")
True
```

#### Inserting non-mandatory and non-optional AVP in constructor

We have discussed in previous [Creating a dictionary with simple AVPs](###creating-a-dictionary-with-simples-avps) Section about Standard DiameterMessage objects by using dictionaries as input arguments. Both `mandatory` and `optionals` DiameterAVPs were used in the example with CapabilitiesExchangeAnswer class instantiation. It worths note that you may also include any other DiameterAVP object following the pattern.

Below we are going to use the exact same dictionary except the two new keys included (`subscription_id_type` and ). That means we may include the DiameterAVP in the first call, not only pos-instantion with `.append()` and `.extend()` methods.

```python
>>> from bromelia.messages import CEA # CapabilitiesExchangeAnswer
>>> from bromelia.constants import DIAMETER_MISSING_AVP
>>> attrs = {
...   "result_code": DIAMETER_MISSING_AVP,
...   "error_message": "Vendor-Specific-Application-Id AVP missing.",
...   "subscription_id_type": END_USER_E164,
...   "redirect_host": "aaas://host.example.com:6666;transport=tcp"
... }
>>> cea = CEA(**attrs)
>>> cea

```

## Dunder Methods

Both `bromelia.base` and `diameter.messages` modules have classes which implements Python dunder methods in order to give a custom experience during development of any application which uses Diameter stack.

### Sum up two or more objects

The `__add__()` is overwritten to make possible sum up two or more DiameterMessage objects to create byte streams.

```python
from bromelia.messages import STR # SessionTerminationRequest
str1 = STR(username="Alice")
str2 = STR(username="Bob")
dump = str1 + str2
dump
>>> dump
b"\x01\x00\x00\xb8\x80\x00\x01\x13\x00\x00\x00\x00\x81\xd8,\xa2og!\xb8\x00\x00\x01\x07@\x00\x003my-host.my-network.com;403292;403292;403292\x00\x00\x00\x01\x08@\x00\x00\x1emy-host.my-network.com\x00\x00\x00\x00\x01(@\x00\x00\x16my-network.com\x00\x00\x00\x00\x01\x1b@\x00\x00\x1fremote-host.network.com\x00\x00\x00\x01\x02@\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x01'@\x00\x00\x0c\x00\x00\x00\x01\x01\x00\x00\xb8\x80\x00\x01\x13\x00\x00\x00\x00x?\xe4c\\\xc5\x083\x00\x00\x01\x07@\x00\x003my-host.my-network.com;403292;403292;403292\x00\x00\x00\x01\x08@\x00\x00\x1emy-host.my-network.com\x00\x00\x00\x00\x01(@\x00\x00\x16my-network.com\x00\x00\x00\x00\x01\x1b@\x00\x00\x1fremote-host.network.com\x00\x00\x00\x01\x02@\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x01'@\x00\x00\x0c\x00\x00\x00\x01"
```

### Check the length

There are two ways to verify the length of a given AVP represented as a DiameterMessage object. First one, just get the value of the AVP length field.

Surely in your computer or your server the length will be different since Origin-Host and Origin-Realm AVPs will have a different content.

```python
>>> from bromelia.messages import DPR # DisconnectPeerRequest
>>> dpr = DPR()
>>> dpr
<Diameter Message: 282 [DPR] REQ, 0 [Diameter common message], 3 AVP(s)>
>>> dpr.length
b'\x00\x00l'
>>> dpr.get_length()
64
```

Second one, just use the `len()` Python built-in function.

```python
>>> from bromelia.messages import DPA # DisconnectPeerAnswer
>>> dpa = DPA()
>>> dpa
<Diameter Message: 282 [DPA], 0 [Diameter common message], 3 AVP(s)>
>>> len(dpa)
64
```

### Boolean verification

That has been implemented to compare two DiameterMessage objects, a DiameterMessage and a DiameterMessage subclass objects or two DiameterMessage subclass objects.

Sometimes it may be usefull to compare objects in order to perform an action. Let's find out how to compare a standard Diameter Message created by hand and a Diameter Message created by using two classes from `bromelia.messages` module.

```python
>>> from bromelia.avps import SessionIdAVP
>>> from bromelia.avps import OriginHostAVP
>>> from bromelia.avps import OriginRealmAVP
>>> from bromelia.avps import DestinationRealmAVP
>>> from bromelia.avps import DestinationHostAVP
>>> from bromelia.avps import AuthApplicationIdAVP
>>> from bromelia.base import DiameterHeader
>>> from bromelia.base import DiameterMessage
>>> from bromelia import DIAMETER_APPLICATION_Rx
>>>
>>> avp1 = SessionIdAVP("my-host.my-network.com")
>>> avp2 = OriginHostAVP("my-host.my-network.com")
>>> avp3 = OriginRealmAVP("my-network.com")
>>> avp4 = DestinationRealmAVP("remote-host.network.com")
>>> avp5 = DestinationHostAVP("network.com")
>>> avp6 = AuthApplicationIdAVP(DIAMETER_APPLICATION_Rx)
>>>
>>> header = DiameterHeader(version=1, flags=DiameterHeader.flag_request_bit, command_code=convert_to_3_bytes(274), application_id=DIAMETER_APPLICATION_Rx, hop_by_hop=convert_to_4_bytes(11111), end_to_end=convert_to_4_bytes(11111))
>>> avps = [avp1, avp2, avp3, avp4, avp5, avp6]
>>>
>>> asr1 = DiameterMessage(header, avps)
>>> asr1.set_flag_by_app_id(DIAMETER_APPLICATION_Rx)
>>> asr1
<Diameter Message: 274 [ASR] REQ|PXY, 16777236 [3GPP Rx], 6 AVP(s)>
>>> type(asr1)
<class 'bromelia.base.DiameterMessage'>
>>> len(asr1)
192
```

What if you create it by using the `DiameterRequest` class in `bromelia.messages` module? We are going consider the objects above are already defined for the next declarations.

```python
>>> from bromelia.base import DiameterRequest
>>> asr2 = DiameterRequest(application_id=DIAMETER_APPLICATION_Rx, command_code=convert_to_3_bytes(274))
>>> asr2.extend(avps)
>>> asr2
<Diameter Message: 274 [ASR] REQ|PXY, 16777236 [3GPP Rx], 6 AVP(s)>
>>> type(asr2)
<class 'bromelia.base.DiameterRequest'>
>>> len(asr2)
192
```

We already know the best way to create a standard Diameter Message using *bromelia* is by calling one of the classes from `bromelia.messages` module.

```python
>>> from bromelia.messages import ASR # AbortSessionRequest
>>> from bromelia import DIAMETER_APPLICATION_Rx
>>> attrs = {
...   "session_id": "my-host.my-network.com",
...   "origin_host": "my-host.my-network.com",
...   "origin_realm": "my-network.com",
...   "destination_realm": "network.com",
...   "destination_host": "remote-host.network.com",
...   "auth_application_id": DIAMETER_APPLICATION_Rx
>>> }
>>> asr3 = ASR(**attrs)
>>> asr3
<Diameter Message: 274 [ASR] REQ|PXY, 16777236 [3GPP Rx], 6 AVP(s)>
>>> type(asr3)
<class 'bromelia.messages.AbortSessionRequest'>
>>> len(asr3)
192
```

If we compare each one of the three objects we have just created that will show us they are not equal. There is a good reason why that happens. First: Remember DiameterMessage objects have information regarding its Headers. The `hop_by_hop` and `end_to_end` attributes will be different, once each Diameter Message needs to have it different as per spec - with an exception, that we are not going into it. Second: maybe both two DiameterMessage or DiameterMessage subclass objects have the exact same DiameterAVP objects in its `avps` attributes with the exact same content, but maybe the list is ordered differently (the case of our example. Take a look at each avp content in `data` attribute).

```python
>>> asr1.avps == asr2.avps
True
>>> asr1.avps == asr3.avps
False
>>> asr2.avps == asr3.avps
False
```

### List-like behavior

It's great that *bromelia* is able to create custom attributes to allow an easy access to each DiameterAVP object inside the DiameterMessage object. However, once any Diameter Message is a stream of bytes defining sections for our data, we could think on DiameterMessage as a list of Diameter AVPs, besides the first header part. That's why *bromelia* has been implemented with another dunder methods, the `__setitem__()` and `__getitem__()`.

You may choose between two alternatives to interate through the DiameterMessage's `avps` attribute.

#### Over `avps` attribute

```python
>>> for avp in asr1.avps:
...     print(avp)
...
<Diameter AVP: 263 [Session-Id] MANDATORY>
<Diameter AVP: 264 [Origin-Host] MANDATORY>
<Diameter AVP: 296 [Origin-Realm] MANDATORY>
<Diameter AVP: 283 [Destination-Realm] MANDATORY>
<Diameter AVP: 293 [Destination-Host] MANDATORY>
<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>
```

#### Over list-like behavior

```python
>>> for avp in asr1:
...     print(avp)
...
<Diameter AVP: 263 [Session-Id] MANDATORY>
<Diameter AVP: 264 [Origin-Host] MANDATORY>
<Diameter AVP: 296 [Origin-Realm] MANDATORY>
<Diameter AVP: 283 [Destination-Realm] MANDATORY>
<Diameter AVP: 293 [Destination-Host] MANDATORY>
<Diameter AVP: 258 [Auth-Application-Id] MANDATORY>
```

## Another Complete reference (unittest files)

Nothing new here. If you has read the [Complete reference (unittest files)](avps.md#complete-reference-unittest-files) section in previous `docs/avps.md` documentation file in this tutorial series you already know *bromelia* library has been written by developer to developers with testing in mind.

Therefore for further information, just take a look at unittest files for Diameter Message classes to get the dynamics.

- [Base unittests](../tests/test_base.py), `tests.test_base`
- [Messages unittests](../tests/test_messages.py), `tests.test_messages`

## Powerful feature comes to play again: The load staticmethod

It comes again because! This feature has already showed up in the previous `docs/avps.md` documentation file in this tutorial series for DiameterAVP objects. It is still awesome to have it at hand when it comes to DiameterMessage objects.

Basically the same dynamics work here. You may use byte streams as inputs argument in the `.load()` staticmethod to create DiameterMessage objects which represents that Diameter Message. Under the hood the staticmethod will parse that byte stream in order to create a more friendly data.

```python
>>> from bromelia.messages import CER # CapabilitiesExchangeRequest
>>> from bromelia.messages import CEA # CapabilitiesExchangeAnswer
>>> cer = CER()
>>> cea = CEA()
>>> dump = cer + cea
>>> dump
b'\x01\x00\x00\x90\x80\x00\x01\x01\x00\x00\x00\x00\xdd\xb8\x1b\xb8>\xf6\xe5\xcb\x00\x00\x01\x08@\x00\x00\x1emy-host.my-network.com\x00\x00\x00\x00\x01(@\x00\x00\x16my-network.com\x00\x00\x00\x00\x01\x01@\x00\x00\x0e\x00\x01\n\x81\xf1\xd6\x00\x00\x00\x00\x01\n@\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x01\r\x00\x00\x00\x1aPython bromelia\x00\x00\x00\x00\x01\x0b\x00\x00\x00\x0c\x00\x00\x00\x01\x01\x00\x00\x9c\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c@\x00\x00\x0c\x00\x00\x07\xd1\x00\x00\x01\x08@\x00\x00\x1emy-host.my-network.com\x00\x00\x00\x00\x01(@\x00\x00\x16my-network.com\x00\x00\x00\x00\x01\x01@\x00\x00\x0e\x00\x01\n\x81\xf1\xd6\x00\x00\x00\x00\x01\n@\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x01\r\x00\x00\x00\x1aPython bromelia\x00\x00\x00\x00\x01\x02@\x00\x00\x0c\x00\x00\x00\x00'
```

Now we may use the `.load()` staticmethod to parse that byte stream to come up with a list of DiameterMessage objects.

```python
>>> from bromelia.base import DiameterMessage
>>> messages = DiameterMessage.load(dump)
>>> messages
[<Diameter Message: 257 [CER] REQ, 0 [Diameter common message], 6 AVP(s)>, <Diameter Message: 257 [CEA], 0 [Diameter common
message], 7 AVP(s)>]
```

Let's consider you have a different byte stream which you got from a file or even from the network. In the example below we are going to convert a hexadecimal string which represents a Diameter Messages to a byte stream. Next, we will pass it to the `.load()` staticmethod. Follow along.

```python
>>> from bromelia.base import DiameterMessage
>>> stream = bytes.fromhex("01000034800001180000000030fa20a508db4bcd000001084000001048656e7269717565000001284000001048656e726971756501000034800001180000000030fa20a508db4bcd000001084000001048656e7269717565000001284000001048656e726971756501000034800001180000000030fa20a508db4bcd000001084000001048656e7269717565000001284000001048656e7269717565")
>>> messages = DiameterMessage.load(stream)
>>> messages
[<Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>, <Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>, <Diameter Message: 280 [DWR] REQ, 0 [Diameter common message], 2 AVP(s)>]
```

There is no limit to the byte stream. The `.load()` staticmethod will return a list with as much as DiameterMessage objects found as Diameter Message in the byte stream. Needless to say that if the byte stream does not contain a valid Diameter Message, it will throw an exception.

You may use a Wireshark Python library to get a Diameter byte streams and use *bromelia* library to create DiameterMessage objects in order to do whatever you want as easily as possible. Like for example automation testing or traffic inspection. That's the beauty of *bromelia*.

You can find more information in the `tests/test_base.py` and `tests/test_messages.py` files.

## Extensibility: Create Your Own Diameter Message Extension

Along this tutorial we found a lot of *bromelia* internals when it comes to DiameterMessage subclasses and objects. Several examples have showed up how to handle standard Diameter Messages from RFC 6733 spec.

But that's not all! Remember *bromelia* has been created with extensibility as a principle design. It also applies to Diameter Message. It has built-in a few more Diameter Messages in order to allow Diameter Applications for 3GPP TS specs. It has been never been too easy to create your own Diameter Message extension.

The *bromelia* is powered with the `3gpp_s6a_s6d` asset which brings several Diameter AVPs and Diameter Messages to the 3GPP `S6a/S6d application`. It means there is a Diameter application stack available to be used for development of a few Mobile Core Network application servers such as MME, SGSN or HSS.

While there is no enforcement, we strongly recommend to follow the pattern below when creating new DiameterMessage subclasses representing Diameter Messages for known or custom Diameter application.

Consider the Section [8.3.1. Re-Auth-Request](https://tools.ietf.org/html/rfc6733#section-8.3.1) from RFC 6733 which defines the Message Format for RAR as per Command Code Format (CFF) specification.

```text
<RAR>  ::= < Diameter Header: 258, REQ, PXY >
                  < Session-Id >
                  { Origin-Host }
                  { Origin-Realm }
                  { Destination-Realm }
                  { Destination-Host }
                  { Auth-Application-Id }
                  { Re-Auth-Request-Type }
                  [ User-Name ]
                  [ Origin-State-Id ]
                * [ Proxy-Info ]
                * [ Route-Record ]
                * [ AVP ]
```

Let's see an example found for ReAuthRequest class in `bromelia/messages.py` code.

```python
class ReAuthRequest(DiameterRequest):
    """Implementation of Re-Auth-Request (RAR) in Section 8.3.1 of
    IETF RFC 6733.

    The Re-Auth-Request is indicated by the Command Code 258 and the
    Command Flags' 'R' bit set.

    Usage::

        >>> from bromelia.messages import ReAuthRequest as RAR
        >>> from bromelia import DIAMETER_APPLICATION_Gx
        >>> from bromelia import AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY
        >>> rar_avps = {
        ...     "auth_application_id": DIAMETER_APPLICATION_Gx,
        ...     "destination_realm": "example.com",
        ...     "destination_host": "host.example.com",
        ...     "re_auth_request_type": AUTH_REQUEST_TYPE_AUTHENTICATE_ONLY
        ... }
        >>> rar = RAR(**rar_avps)
        <Diameter Message: 258 [RAR] REQ, PXY 3GPP Gx, 7 AVP(s)>
    """

    mandatory = {
                    "session_id": SessionIdAVP,
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP,
                    "re_auth_request_type": ReAuthRequestTypeAVP
    }
    optionals = {
                    "user_name": UserNameAVP,
                    "origin_state_id": OriginStateIdAVP,
                    "proxy_info": ProxyInfoAVP,
                    "route_record": RouteRecordAVP
    }

    def __init__(self,
                 session_id=platform.node(),
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 destination_realm=socket.gethostbyname(platform.node()),
                 destination_host=None,
                 auth_application_id=None,
                 re_auth_request_type=None,
                 user_name=None,
                 origin_state_id=None,
                 proxy_info=None,
                 route_record=None,
                 **kwargs):

        if not auth_application_id:
            raise DiameterMessageError("invalid auth_application_id value. "\
                                       "It needs to include a valid Auth "\
                                       "Application Id")

        DiameterRequest.__init__(self, auth_application_id, RE_AUTH_MESSAGE)
        DiameterRequest._load(self, locals())
```

The class needs to follow the pattern name as `<Diameter Message Name>` in and CamelCase as per [Python's class name convention](https://www.python.org/dev/peps/pep-0008/). It also needs to inherint either DiameterRequest or DiameterAnswer class depending on the Diameter Message under development. For ReAuthRequest message, it has been inherinted the DiameterRequest class.

Always provide documentation about the spec this subclass is defined, if so, or provide info on the reason behind a custom Diameter Message was intended for.

All DiameterMessage subclass should have two class attributes: `mandatory` which implements a dictionary of mandatory AVPs and `optionals` which implements a dictionary of optional AVPs. Both should follow the pattern:

- `key` equals to AVP name in lower case where each word is separated by underscores.
- `value` equals to DiameterAVP object implemented with *bromelia* or any other DiameterAVP class extension (**do not call it!**)

```python
mandatory = {
                "session_id": SessionIdAVP,
                "origin_host": OriginHostAVP,
                "origin_realm": OriginRealmAVP,
                "destination_realm": DestinationRealmAVP,
                "destination_host": DestinationHostAVP,
                "auth_application_id": AuthApplicationIdAVP,
                "re_auth_request_type": ReAuthRequestTypeAVP
}
```

The constructor must have input arguments with the same name as presented in the `key` expressed above. The input arguments intended for mandatory AVPs must have default values. That ones intended for optional AVP may have default values or, if not, should be `None`. That's the convention in order to fulfill the internal requirements to allow smoothly custom Diameter Messages creation by inheritance.

You must include `**kwargs` at the end to allow arbitrary AVPs not related neither to mandatory nor optionals class attributes dictionaries. That way any development may include any DiameterAVP object different from those expected ones.

```python
def __init__(self,
             session_id=platform.node(),
             origin_host=platform.node(),
             origin_realm=socket.getfqdn(),
             destination_realm=socket.gethostbyname(platform.node()),
             destination_host=None,
             auth_application_id=None,
             re_auth_request_type=None,
             user_name=None,
             origin_state_id=None,
             proxy_info=None,
             route_record=None,
             **kwargs):
```

The example we are getting has a conditional-block which is not mandatory, but you may include it if your Diameter Message implementation has some special validation such as RAR message under analysis.

```python
if not auth_application_id:
    raise DiameterMessageError("invalid auth_application_id value. "\
                               "It needs to include a valid Auth "\
                               "Application Id")
```

In the end, it must always include the superclass constructor call (in our example, the `DiameterRequest`) and the `._load()` method. Your may also include another block of code if your implemenation needs so.

```python
DiameterRequest.__init__(self, auth_application_id, RE_AUTH_MESSAGE)
DiameterRequest._load(self, locals())
```

There is a warning here: if your Diameter Message class does not intend to be a Default one, which may be the case, you must implement the `auth_application_id` input argument in the class constructor and put such DiameterAVP in the `mandatory` classattribute. Otherwise, just put the `DIAMETER_APPLICATION_DEFAULT` constant into it. (Refer to `CapabilitiesExchangeRequest` in `bromelia.messages` module for more information). Finally, the second input argumnet of superclass constructor must be the constant which represents the Command Code of such Diameter Message (in this case, `RE_AUTH_MESSAGE` constant).

### Creating our own custom Diameter Message

Now let's create a custom Diameter Message where the message flag's 'R' bit set. Below you may find a reference written in the Command Code Format (CFF) specification.

```text
<MDR>  ::= < Diameter Header: 999, REQ, PXY >
                  { Origin-Host }
                  { Origin-Realm }
                  { Destination-Realm }
                  { Destination-Host }
                  [ User-Name ]
                * [ AVP ]
```

Therefore, its implementation according to discussed previously.

```python
class MyDiameterRequest(DiameterRequest):
    """Implementation of My-Diameter-Request (MDR).

    The My-Diameter-Request is indicated by the Command Code 999 and
    the Command Flags' 'R' bit and 'P' bit set.

    Usage::

        >>> from my_custom_bromelia.messages import MyDiameterRequest as MDR
        >>> from my_custom_bromelia import DIAMETER_CUSTOM_APPLICATION
        >>> mdr_avps = {
        ...     "username": "Henrique",
        ...     "auth_application_id": DIAMETER_CUSTOM_APPLICATION
        ... }
        >>> mdr = MDR(**mdr_avps)
        <Diameter Message: 999 [MDR] REQ, PXY, 5 AVP(s)>
    """

    mandatory = {
                    "origin_host": OriginHostAVP,
                    "origin_realm": OriginRealmAVP,
                    "destination_realm": DestinationRealmAVP,
                    "destination_host": DestinationHostAVP,
                    "auth_application_id": AuthApplicationIdAVP,
    }
    optionals = {
                    "user_name": UserNameAVP,
    }

    cmd_code = MY_DIAMETER_MESSAGE

    def __init__(self,
                 origin_host=platform.node(),
                 origin_realm=socket.getfqdn(),
                 destination_realm=socket.gethostbyname(platform.node()),
                 destination_host=None,
                 auth_application_id=None,
                 user_name=None,
                 **kwargs):

        if not auth_application_id:
            raise DiameterMessageError("invalid auth_application_id value. "\
                                       "It needs to include a valid Auth "\
                                       "Application Id")

        DiameterRequest.__init__(self, auth_application_id, MY_DIAMETER_MESSAGE)
        DiameterRequest._load(self, locals())
```
