# Building Blocks Part 1: Data Types

This tutorial does not have any intention to explain the Diameter protocol itself. For that, the [IETF RFC 6733](https://tools.ietf.org/html/rfc6733) covers in detail all internals of the protocol.

It assumes developers have at least a very basic understanding of Diameter structures, such as [Data Formats](https://tools.ietf.org/html/rfc6733#section-4.2), [Diameter AVPs](https://tools.ietf.org/html/rfc6733#page-40), [Diameter Header](https://tools.ietf.org/html/rfc6733#page-34) and [Diameter Connections](https://tools.ietf.org/html/rfc6733#section-5). Even though the tutorial has several good insights on the protocol when its comes to explain the library itself.

This document covers the very basic of Diameter protocol that comes from its Data Formats.

This page contains the following sections:

- [Fundamentals](#fundamentals)
- [Data Types](#types)
- [Reference (unittest files)](#reference-unittest-files)

## Fundamentals

When sending or receiving information by using the Diameter protocol, it is usefull to know exactly which kind of information needs to be handled.

In the upcoming parts of the tutorial, it will be clearer how to handle Diameter AVPs and create Diameter Messages. However all such structures relies on Data Formats like any programming languages relies on Data types.

As the same way it is possible to create composite data types (or record) with almost any programming languages, such as `struct` keyword in `C` or `class` keyword in `Python` - considering their differences -, its possible to construct composite Data Formats in Diameter protocol. The concept used in Object Oriented Programming languages also comes here when a few Diameter Data Formats are derived from others, such as `Address` is derived from the `OctetString` Basic AVP Format. There is even a list-like structure represented by the `Grouped`, a sequence of concatenated AVPs.

## Types

The base class representing Data Formats in *bromelia* is the `BaseDataType` abstract base class. All other Data Formats are inherinted from it. Neither `BaseDataType` nor its subclasses can be instantiated as objects. They may be used only for inheritance of Diameter AVP classes. We are going into the details in the next tutorial.

Below you may find a list of Diameter Data Formats and the implemented classes in *bromelia*.

| Classes               | Diameter Data Format |
| --------------------- | -------------------- |
| BaseDataType          | `n/a`                |
| OctetStringType       | OctetString          |
| Integer32Type         | Integer32            |
| `n/a`                 | Integer64            |
| Unsigned32Type        | Unsigned32           |
| Unsigned64Type        | Unsigned64           |
| `n/a`                 | Float32              |
| `n/a`                 | Float64              |
| GroupedType           | Grouped              |
| AddressType           | Address              |
| TimeType              | Time                 |
| UTF8StringType        | UTF8String           |
| DiameterIdentityType  | DiameterIdentity     |
| DiameterURIType       | DiameterURI          |
| EnumeratedType        | Enumerated           |
| `n/a`                 | IPFilterRule         |

## Reference (unittest files)

The *bromelia* library has been written from developer to developers with testing approach in mind.

There are lots of unit testsa all over the place. That means you may, and should, take a look at those tests to have a good ideia on how each of the internals work. Strongly recommended go through the code with an unittests tab side-by-side.

- [Types unit tests](../tests/test_types.py), `tests.test_types`
