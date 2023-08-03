# generated by datamodel-codegen:
#   filename:  nullable.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, NotRequired, Optional, TypedDict


class Cursors(TypedDict):
    prev: Optional[str]
    next: NotRequired[str]
    index: float
    tag: NotRequired[str]


class TopLevel(TypedDict):
    cursors: Cursors


class Info(TypedDict):
    name: str


class User(TypedDict):
    info: Info


class Api(TypedDict):
    apiKey: NotRequired[str]
    apiVersionNumber: NotRequired[str]
    apiUrl: NotRequired[str]
    apiDocumentationUrl: NotRequired[str]


Apis = Optional[List[Api]]


class EmailItem(TypedDict):
    author: str
    address: str
    description: NotRequired[str]
    tag: NotRequired[str]


Email = List[EmailItem]


Id = int


Description = Optional[str]


Name = Optional[str]


Tag = str


class Notes(TypedDict):
    comments: NotRequired[List[str]]
