# Building Blocks Part 2: Diameter AVPs

The *bromelia* library has implemented all standard [Diameter AVPs](https://tools.ietf.org/html/rfc6733#page-40) from RFC 6733 and much more. It is straighforward to create such AVPs by just including the desired value when instantiating the object from the chose AVP class. Furthermore, with *bromelia* it has never been easier to create custom AVPs.

This document covers the DiameterAVP class and a few of its subclasses which represent the standard AVPs.

This page contains the following sections:

- [DiameterAVP](#diameteravp)
- [Basic Usage](#basic-usage)
- [Flavors of AVPs](#flavors-of-avps)
- [Dunder Methods](#dunder-methods)
- [Complete reference (unittest files)](#complete-reference-unittest-files)
- [Bread and Butter: DiameterAVP instance methods](#bread-and-butter-diameteravp-instance-methods)
- [Powerful feature: The load staticmethod](#powerful-feature-the-load-staticmethod)
- [Extensibility: Create Your Own Diameter AVP Extension](#extensibility-create-your-own-diameter-avp-extension)
- [Complete List of DiameterAVP subclasses](#complete-list-of-diameteravp-subclasses)

## DiameterAVP

For AVP handling, the `bromelia.avps` package is used. It contains several classes, that create DiameterAVP objects, parse byte string and may be extended by another implementations.

The DiameterAVP class is defined in `bromelia.base` module as one of the *bromelia*'s core classes. All classes defined in `bromelia.avps` package are DiameterAVP subclasses. You may find a specific AVP by searching the folder, which holds the organization name, and the Python module, which holds the spec number. For instance, the Origin-Host AVP is found in [`bromelia.avps.ietf.rfc6733`](../bromelia/avps/ietf/rfc6733.py#L303).

The DiameterAVP class implements several methods, the `.load()` staticmethod and other instance methods such as `.dump()`, `.convert()` and `.copy()`.

There are a few setters-like and verification methods methods for bit flags handling such as `.set_vendor_bit()`, `.is_vendor_bit()`, `.set_mandatory_bit()`, `.is_mandatory()`, `.set_protected_bit()` and `.is_protected()`.

There are also getters-like methods such as `.get_code()`, `.get_flags()`, `.get_length()`, `.get_vendor_id()` and `.get_padding_length()`.

All these methods will be inherited if a developer extends the DiameterAVP class to create custom AVPs in case of not instantiating objects and manipulating it on the fly.

## Basic Usage

To create a DiameterAVP object, just import the class and instantiate it.

```python
>>> from bromelia.base import DiameterAVP
>>> avp = DiameterAVP()
>>> avp
<Diameter AVP: 0 [Unknown]>
```

Look at each attribute value.

```python
>>> avp.code
b'\x00\x00\x00\x00'
>>> avp.get_code()
0
>>> avp.flags
b'\x00'
>>> avp.get_flags()
0
>>> avp.length
b'\x00\x00\x08'
>>> avp.get_length()
8
>>> avp.vendor_id
>>> avp.get_vendor_id()
>>> avp.data
```

All DiameterAVP and DiameterAVP subclasses objects store its attributes as byte since Diameter protocol is a binary protocol.

Sometimes is better see some data in another format such as Integer or String. That's why we call the getters-like methods such as `.get_code()`, `.get_flags()`, `.get_length()`, `.get_vendor_id()` and `.get_padding_length()`.

As just presented, the previous DiameterAVP object does not contain data at all. In order to create meaningful DiameterAVP objects, you can either create a raw Diameter object and populate its attributes on the fly, or create a raw DiameterAVP objects by passing constructor input arguments.

### On the fly

```python
>>> from bromelia.base import DiameterAVP
>>> avp = DiameterAVP()
>>> avp.code = 1
>>> avp.flags = 40
>>> avp.vendor_id = 10415
>>> avp.data = "NewGenerationOfMobileNetwork"
>>> avp
<Diameter AVP: 1 [User-Name] PROTECTED>
```

### Constructor

```python
>>> from bromelia.base import DiameterAVP
>>> avp = DiameterAVP(1, 40, 10415, "Mobile-Network")
>>> avp
<Diameter AVP: 1 [User-Name] PROTECTED>
```

It is possible change values for each attribute that represents AVPs fields. However there is another approach specifically for `flags` attribute. Just use one of the setters-like methods such as `.set_vendor_id_bit()`, `.set_mandatory_bit()` and `set_protected_bit()`. See the example below.

```python
>>> from bromelia.base import DiameterAVP
>>> avp = DiameterAVP(1, 40, 10415, "Mobile-Network")
>>> avp
<Diameter AVP: 1 [User-Name] PROTECTED>
>>> avp.set_vendor_id_bit(True)
>>> avp
<Diameter AVP: 1 [User-Name] VENDOR, PROTECTED>
>>> avp.set_mandatory_bit(True)
>>> avp
<Diameter AVP: 1 [User-Name] VENDOR, MANDATORY, PROTECTED>
>>> avp.set_protected_bit(False)
>>> avp
<Diameter AVP: 1 [User-Name] VENDOR, MANDATORY>
```

It is pretty clear the `__repr__()` dunder method tracks the `flags` attribute to give the developer the DiameterAVP object state.

You can also perform a verification if a given flag field bit is set.

```python
>>> avp
<Diameter AVP: 1 [User-Name] VENDOR, MANDATORY>
>>> avp.is_protected()
False
>>> avp.is_vendor_id()
True
>>> avp.is_mandatory()
True
```

## Flavors of AVPs

*bromelia* is powered with several built-in AVPs from both RFC and 3GPP TS specs. It all take advantages of the powerful DiameterAVP superclass.

However it is up to the developer the AVP design in its applications. *bromelia* does not enforce DiameterAVP class inheritance approach, however do strongly recommend to use it.

For reference, see below two ways to create an object representing the Diameter's [Origin-Host AVP](https://tools.ietf.org/html/rfc6733#section-6.3).

### Built-in

```python
>>> from bromelia.avps import OriginHostAVP
>>> avp = OriginHostAVP("myhost.mynetwork.com")
>>> avp
<Diameter AVP: 264 [Origin-Host] MANDATORY>
>>> type(avp)
<class 'bromelia.avps.ietf.rfc6733.OriginHostAVP'>
```

### Handcrafted

```python
>>> from bromelia.base import DiameterAVP
>>> avp = DiameterAVP(264, None, 40, "myhost.mynetwork.com")
>>> avp
<Diameter AVP: 264 [Origin-Host] MANDATORY>
>>> type(avp)
<class 'bromelia.base.DiameterAVP'>
```

In both cases they hold the exact same data. However they are not the same object. Give it a try with other DiameterAVP subclasses which implements AVPs such as [User-Name](https://tools.ietf.org/html/rfc6733#section-8.14) (`UserNameAVP`), [Host-IP-Address](https://tools.ietf.org/html/rfc6733#section-5.3.5) (`HostIpAddressAVP`), [Result-Code](https://tools.ietf.org/html/rfc6733#section-7.1) (`ResultCodeAVP`) or even others available. See [Complete List of DiameterAVP subclasses](#complete-list-of-diameteravp-subclasses) section.

```python
>>> avp.code
b'\x00\x00\x01\x08'
>>> avp.get_code()
264
>>> avp.flags
b'('
>>> avp.get_flags()
40
>>> avp.length
b'\x00\x00\x1c'
>>> avp.get_length()
28
>>> avp.data
b'myhost.mynetwork.com'
```

Last but not least, you may serialize your object to send it down to the wire by calling the `.dump()` instance method. Regardless if the object is a DiameterAVP instance or DiameterAVP subclass instance, the result will always be the same.

```python
>>> avp.dump()
b'\x00\x00\x01\x08(\x00\x00\x1cmyhost.mynetwork.com'
>>> avp.dump().hex()
000001082800001c6d79686f73742e6d796e6574776f726b2e636f6d
```

## Dunder Methods

The DiameterAVP class makes use of the Python dunder methods in order to give a custom experience during development of any application which uses Diameter stack.

### Sum up two or more objects

The `__add__()` is overwritten to make possible sum up two or more DiameterAVP objects to create byte streams.

```python
>>> from bromelia.constants import DIAMETER_SUCCESS
>>> from bromelia.avps import ResultCodeAVP
>>> from bromelia.avps import OriginStateIdAVP
>>> rc = ResultCodeAVP(DIAMETER_SUCCESS)
>>> osi = OriginStateIdAVP(1524733202)
>>> dump = rc + osi
>>> dump
b'\x00\x00\x01\x0c@\x00\x00\x0c\x00\x00\x07\xd1\x00\x00\x01\x15@\x00\x00\x0c\x00\x00\x00\x00'
```

### Check the length

There are two ways to verify the length of a given AVP represented as a DiameterAVP object. First one, just get the value of the AVP length field as already seen.

```python
>>> from bromelia.avps import RouteRecordAVP
>>> rr = RouteRecordAVP("myhost.epc.mncMNC.mccMCC.3gppnetwork.org")
>>> rr
<Diameter AVP: 282 [Route-Record] MANDATORY>
>>> rr.length
b'\x00\x000'
>>> rr.get_length()
48
```

Second one, just use the `len()` Python built-in function.

```python
>>> from bromelia.avps import DestinationRealmAVP
>>> dr = DestinationRealmAVP("myhost.epc.mncMNC.mccMCC.3gppnetwork.org")
>>> dr
<Diameter AVP: 283 [Destination-Realm] MANDATORY>
>>> len(dr)
48
```

### Boolean verification

That has been implemented to compare two DiameterAVP objects, a DiameterAVP and a DiameterAVP subclass object or two DiameterAVP subclass objects.

Sometimes it may be usefull to compare objects before performing an action.

```python
>>> from bromelia.base import DiameterAVP
>>> from bromelia.avps import ReAuthRequestTypeAVP
>>> from bromelia.constants import RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY
>>> rar1 = ReAuthRequestTypeAVP(RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
>>> rar1
<Diameter AVP: 285 [Re-Auth-Request-Type] MANDATORY>
>>> rar2 = DiameterAVP(code=285, flags=DiameterAVP.flag_mandatory_bit, data=RE_AUTH_REQUEST_TYPE_AUTHORIZE_ONLY)
>>> rar2
<Diameter AVP: 285 [Re-Auth-Request-Type] MANDATORY>
>>> rar1 == rar2
True
```

If just a bit of thing be replaced or changed, the comparison will be return False.

```python
>>> from bromelia.base import DiameterAVP
>>> from bromelia.avps import TerminationCauseAVP
>>> from bromelia.constants import DIAMETER_LOGOUT
>>> tc1 = TerminationCauseAVP(DIAMETER_LOGOUT)
>>> tc1
<Diameter AVP: 295 [Termination-Cause] MANDATORY>
>>> tc2 = DiameterAVP(code=295, flags=DiameterAVP.flag_mandatory_bit,data=DIAMETER_LOGOUT)
>>> tc2
<Diameter AVP: 295 [Termination-Cause] MANDATORY>
>>> tc1 == tc2
True
>>> tc2.set_protected_bit(True)
>>> tc2
<Diameter AVP: 295 [Termination-Cause] MANDATORY, PROTECTED>
>>> tc1 == tc2
False
```

## Complete reference (unittest files)

Always good to remember, but *bromelia* library has been written from developer to developers with testing approach in mind.

There are a massive number of unit tests all over the place. That means you may, and should, take a look at those tests to have a good ideia on how each Diameter subclass and method work. Strongly recommended go through the code with an unittests tab side-by-side.

- [AVP unit tests](../tests/avps), `tests.avps`

Each class in `tests.avps` unittest package represents a set of unit tests for a particular `avps` package class. For instance, the first one is the TestDiameterAVP, a unittest.TestCase subclass. Each method implements a test regarding a specific DiameterAVP class feature.

Would be pointless to rewrite each test here in this tutorial as a written english example when they are written in clear Python programming language.

Find in the section below a few examples on how to use the unittest file for a given case.

## Bread and butter: DiameterAVP instance methods

### First hint

It's possible to set the [protected bit](https://tools.ietf.org/html/rfc6733#section-3) of a DiameterAVP instance, or even of any DiameterAVP subclass instance, by calling the `.set_protected_bit()` method. However, the `test_diameter_avp__protected_bit__set_when_is_set()` unittest says if you try to set the protected bit to a DiameterAVP instance with the protected bit already set, an exception will be thrown with the meaningul message "P-bit was already set".

### Second hint

DiameterAVP has a few class attributes which may be used to change, for instance, the flag bit to whatever expected value. That can be found on
`test_diameter_avp__custom_object__flags_by_set_flags_methods()` unittest.

### Third hint

Besides the bunch of unittests for DiameterAVP class, there are several others for each DiameterAVP subclass. As an example, let's see the TestResultCodeAVP unittests.

The first one, `test_result_code_avp__no_value` informs that it needs an input argument in its constructors. Otherwise it will be instantiated. The second one, `test_result_code_avp__repr_dunder` is a common unittest which shows how dunder method `__repr__()` will represent that object. The third one, `test_result_code_avp__diameter_avp_convert_classmethod` shows how to convert between a DiameterAVP subclass instance and a DiameterAVP instance. Something it may be helpful if you prefer to deal with pure DiameterAVP objects.

```python
>>> from bromelia.base import DiameterAVP
>>> avp1 = OriginHostAVP("myhost.mynetwork.com")
>>> avp1
<Diameter AVP: 264 [Origin-Host] MANDATORY>
>>> type(avp1)
<class 'bromelia.avps.ietf.rfc6733.OriginHostAVP'>
>>> avp2 = DiameterAVP.convert(avp1)
>>> avp2
<Diameter AVP: 264 [Origin-Host] MANDATORY>
>>> type(avp2)
<class 'bromelia.base.DiameterAVP'>
```

The following unittests in [tests/avps/ietf/test_rfc6733.py](../tests/avps/ietf/test_rfc6733.py#test_result_code_avp__diameter_success) file present how to instantiate the ResultCodeAVP class for a different set of expected values, such as [success](https://tools.ietf.org/html/rfc6733#section-7.1.2) (e.g. or [errors](https://tools.ietf.org/html/rfc6733#section-7.1.3) (e.g. `DIAMETER_SUCCESS`, `DIAMETER_UNABLE_TO_COMPLY`,`DIAMETER_UNABLE_TO_DELIVER` codes, etc).

### Fourth hint

For some reason you may need to manipulate an object and do not impact the original one due to [Python bindings](https://docs.python.org/3/library/copy.html). To achieve this, just use the `.copy()` method. Now any changes in `avp2` will not affect `avp1` object.

```python
>>> from bromelia.base import DiameterAVP
>>> avp1 = DiameterAVP(264, 0, 64, "myhost.mynetwork.com")
>>> avp1
<Diameter AVP: 264 [Origin-Host] MANDATORY>
>>> avp2 = avp1.copy()
>>> avp1 == avp2
True
>>> id(avp1) == id(avp2)
False
```

## Powerful feature: The load staticmethod

When it comes to Diameter AVPs, one of the most excited features in *bromelia* is the possibility to create DiameterAVP objects through a byte stream.

What does that mean? Well, you may use byte streams as input argument in the `.load()` staticmethod to create DiameterAVP objects which represent that AVP. Under the hood the staticmethod will parse that byte stream in order to create a more friendly data.

It is also possible to pass a concatenated byte stream of different Diameter AVPs. The `.load()` staticmethod will return a list of DiameterAVP or DiameterAVP subclasses instances. Take a look.

```python
>>> from bromelia.constants import DIAMETER_SUCCESS
>>> from bromelia.constants import STATE_MAINTAINED
>>> from bromelia.avps import AuthSessionStateAVP
>>> from bromelia.base import DiameterAVP
>>> from bromelia.avps import ResultCodeAVP
>>> result_code_avp = ResultCodeAVP(DIAMETER_SUCCESS)
>>> auth_session_state_avp = AuthSessionStateAVP(STATE_MAINTAINED)
>>> dump = result_code_avp + auth_session_state_avp
>>> avps = DiameterAVP.load(dump)
>>> avps
[<Diameter AVP: 268 [Result-Code] MANDATORY>, <Diameter AVP: 277 [Auth-Session-State] MANDATORY>]
```

Let's consider you have a different byte stream which you got from a pcap file or even from the network.

```python
>>> from bromelia.base import DiameterAVP
>>> stream = bytes.fromhex("0000010a4000000c000000000000010b0000000c00000001")
>>> avps = DiameterAVP.load(stream)
>>> avps
[<Diameter AVP: 266 [Vendor-Id] MANDATORY>, <Diameter AVP: 267 [Firmware-Revision]>]
```

There is no limit to the byte stream. The `.load()` staticmethod will return a list with as much as DiameterAVP found as AVPs in the bytestream. Needless to say that if the byte stream does not contain a valid Diameter AVP, it will throw an exception.

```python
>>> from bromelia.base import DiameterAVP
>>> stream = bytes.fromhex("00000000")
>>> avps = DiameterAVP.load(stream)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "F:\bromelia\base.py", line 349, in load
    raise AVPParsingError("invalid bytes stream")
bromelia.exceptions.AVPParsingError: invalid bytes stream
```

You can find more information in the `tests.avps` unittest package. There are examples for both valid and invalid ways of using the `.load()` staticmethod. Go over unittests that begins with `test_diameter_avp__load_staticmethod__parsing_` to have a better ideia.

## Extensibility: Create Your Own Diameter AVP Extension

It has never been too easy to create your own Diameter AVP extension. The *bromelia* has been created with extensibility as a design principle.

In [Flavors of AVPs](#flavors-of-avps) section, two common ways to create custom DiameterAVP objects have been discussed. While one of them creates instance objects, the other is inheritance oriented. That's the best way to package your new Diameter AVPs and ship to other developers.

The *bromelia* is powered with assets which bring several Diameter AVPs and Diameter Messages regarding different Diameter applications. Just take a look the [bromelia.lib](../bromelia/lib) package. You will notice that *bromelia* has assets to bring up Mobile Core Network applications such as ePDG ([`etsi_3gpp_swm`](../bromelia/lib/etsi_3gpp_swm)), AAA ([`etsi_3gpp_swx`](../bromelia/lib/etsi_3gpp_swx)), HSS ([`etsi_3gpp_s6a`](../bromelia/lib/etsi_3gpp_s6a)) and much more!

While there is no enforcement, strongly recommended to follow the pattern below when creating new DiameterAVP subclasses representing AVPs for known or custom Diameter application.

Let's see an example found for Proxy-State AVP in `bromelia.avps` package.

```python
class ProxyStateAVP(DiameterAVP, OctetStringType):
    """Implementation of Proxy-State AVP in Section 6.7.4 of IETF RFC 6733.

    The Proxy-State AVP (AVP Code 33) is of type OctetString.
    """
    code = PROXY_STATE_AVP_CODE
    vendor_id = None

    def __init__(self, data):
        DiameterAVP.__init__(self, ProxyStateAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)    
        OctetStringType.__init__(self, data=data)
```

The class needs to follow the pattern name as `<Diameter AVP Name>AVP`. It also needs to inherint first DiameterAVP class and secondly a BaseDataType subclass found in `bromelia/types.py` module. For [Proxy-State AVP](https://tools.ietf.org/html/rfc6733#section-6.7.4), it has been defined in the spec as OctectString type, that is because ProxyStateAVP inherints from OctectStringType.

Always provide documentation about the spec this subclass is defined, if so, or provide info on the reason behind a custom Diameter AVP was intended for.

All DiameterAVP subclass should have `code` and `vendor_id` class attributes as a 4 byte values (`vendor_id` may be `None` if DiameterAVP subclass is not vendor defined) and a constructor which calls for both DiameterAVP and the BaseDataType subclass constructors (always pass the `data` input argument).

Once Proxy-State AVP must have the M-bit set, it was included the `.set_mandatory_bit()` method with the `True` value input.

Now let's create a custom AVP called `My-Diameter-Attribute` with M-bit, V-bit and P-bit set.

```python
from bromelia.constants import convert_to_4_bytes

VENDOR_ID_CUSTOM = convert_4_bytes(37723)

class MyDiameterAttributeValuePairAVP(DiameterAVP, Unsigned32Type):
  """Implementation of My-Diameter-Attribute-Value-Pair AVP for a given goal.

  The My-Diameter-Attribute-Value-Pair AVP (AVP Code 1) is of type Unsigned32.
  """
  code = convert_to_4_bytes(1)
  vendor_id = VENDOR_ID_CUSTOM

  def __init__(self, data):
    DiameterAVP.__init__(self, MyDiameterAttributeValuePairAVP.code)

    DiameterAVP.set_mandatory_bit(self, True)
    DiameterAVP.set_protected_bit(self, True)
    DiameterAVP.set_vendor_id_bit(self, True)

    Unsigned32Type.__init__(self, data=data, vendor_id=MyDiameterAttributeValuePairAVP.vendor_id)
```

Differently from `ProxyStateAVP` subclass, the custom `MyDiameterAttributeValuePairAVP` subclass has the V-bit set, which means the `Unsigned32Type` constructor needs to be called with the input argument `vendor_id` passing the Vendor ID value. For our example, a constant `VENDOR_ID_CUSTOM` has been defined owning an [invalid IANA](https://www.iana.org/assignments/enterprise-numbers/enterprise-numbers) value (`37723`).

While creation of custom DiameterAVP subclasses is as pretty straighforwarded as above for the OctectString (`OctetStringType`), Integer32 (`Integer32Type`), Unsigned32 (`Unsigned32Type`), Unsigned64 (`Unsigned64Type`),  Address (`AddressType`), DiameterIdentity (`DiameterIdentityType`), DiameterURI (`DiameterURIType`) and UTF8String (`UTF8StringType`) types, there is a slightly difference when creating custom DiameterAVP subclasses for two others Diameter types.

Let's see next how create custom DiameterAVP subclasses for remaining Enumerated (`EnumeratedType`) and Grouped (`GroupedType`) types.

### EnumeratedType

Not really different. Aside all we have just discussed, once Enumerated type needs to have a set of expected values, the developer must include a class attribute called `values` as a Python list of such values. See the snippet implementation in *bromelia* for Disconnect-Cause AVP.

Remember: this AVP is not vendor specific, therefore there is no need to include the `vendor_id` input argument in the `EnumeratedType` constructor call within the `DisconnectCausaAVP` constructor. However, you need to include `vendor_id` class attribute for library internals purpose.

```python
class DisconnectCauseAVP(DiameterAVP, EnumeratedType):
    """Implementation of Disconnect-Cause AVP in Section 5.4.3 of 
    IETF RFC 6733.

    The Disconnect-Cause AVP (AVP Code 273) is of type Enumerated.
    """
    code = DISCONNECT_CAUSE_AVP_CODE
    vendor_id = None
    
    values = [
                DISCONNECT_CAUSE_REBOOTING,
                DISCONNECT_CAUSE_BUSY,
                DISCONNECT_CAUSE_DO_NOT_WANT_TO_TALK_TO_YOU
    ]

    def __init__(self, data=DISCONNECT_CAUSE_REBOOTING):
        DiameterAVP.__init__(self, DisconnectCauseAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        EnumeratedType.__init__(self, data=data)
```

### GroupedType

It has never been more easy to create well known or custom DiameterAVP subclasses basead on GroupedType subclass. Under the hood, GroupedType allows easy ways to go through its structure by accessing different deep levels of DiameterAVPs.

See below that GroupedType subclasses need to defined two new class attributes: `mandatory` and `optionals`. They are dictionaries which represent the DiameterAVP subclasses defined as mandatory or optional in the specs. It is important to include for internal checking purpose.

```python
class VendorSpecificApplicationIdAVP(DiameterAVP, GroupedType):
    """Implementation of Vendor-Specific-Application-Id AVP in Section 6.11 of
    IETF RFC 6733.

    The Vendor-Specific-Application-Id AVP (AVP Code 260) is of type Grouped.
    """
    code = VENDOR_SPECIFIC_APPLICATION_ID_AVP_CODE
    vendor_id = None

    mandatory = {
                    "vendor_id": VendorIdAVP,
    }
    optionals = {
                    "auth_application_id": AuthApplicationIdAVP,
                    "acct_application_id": AcctApplicationIdAVP,
    }

    def __init__(self, data):
        DiameterAVP.__init__(self, VendorSpecificApplicationIdAVP.code)
        DiameterAVP.set_mandatory_bit(self, True)
        GroupedType.__init__(self, data=data)
```

## Complete List of DiameterAVP subclasses

Please refer to link below for a complete list of DiameterAVP subclasses available.

[Complete List of DiameterAVP subclasses](./list-of-avps.md)
