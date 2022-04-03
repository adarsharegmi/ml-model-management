from __future__ import annotations
import uuid
from enum import Enum
import datetime
from typing import Any, Dict, Optional
from numpy import source
from pydantic import BaseModel as Model


class File(Model):
    id_: uuid.UUID
    name: str
    source: str
    parameters: str
    placement_name: str
    effective_from: str
    effective_to: str
    active: str

    class Config:
        extra = "forbid"
        allow_mutation = True
        title = "file_upload"
        arbitrary_types_allowed = True

    def add_file_id(self, file_id: uuid.UUID):
        self.file_id = file_id

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def __hash__(self):
        return hash(self.name)


def file_factory(
    name: str,
    source: str,
    parameters: str,
    placement_name: str,
    effective_from: str,
    effective_to: str,
    active: str,
) -> File:
    return File(
        id_=uuid.uuid4(),
        name=name,
        source=source,
        parameters=parameters,
        placement_name=placement_name,
        effective_from=effective_from,
        effective_to=effective_to,
        active=active,
    )


class Streaming(Model):
    id_: uuid.UUID
    name: str
    ip_address: str
    nic: str
    username: str
    password: str
    parameters: str
    placement_name: str
    effective_from: datetime.date
    effective_to: datetime.date
    active: bool

    class Config:
        extra = "forbid"
        allow_mutation = True
        title = "streaming"
        arbitrary_types_allowed = True

    def add_streaming_id(self, streaming_id: uuid.UUID):
        self.streaming_id = streaming_id

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def __hash__(self):
        return hash(self.name)


def streaming_factory(
    name: str,
    ip_address: str,
    nic: str,
    username: str,
    password: str,
    parameters: bool,
    placement_name: str,
    effective_from: datetime.date,
    effective_to: datetime.date,
    active: bool,
) -> Streaming:
    return Streaming(
        id_=uuid.uuid4(),
        name=name,
        ip_address=ip_address,
        nic=nic,
        username=username,
        password=password,
        source=source,
        parameters=parameters,
        placement_name=placement_name,
        effective_from=effective_from,
        effective_to=effective_to,
        active=active,
    )


class DBPull(Model):
    id_: uuid.UUID
    name: str
    source: str
    port: str
    parameters: str
    placement_name: str
    effective_from: datetime.date
    effective_to: datetime.date
    active: bool

    class Config:
        extra = "forbid"
        allow_mutation = True
        title = "dbpull"
        arbitrary_types_allowed = True

    def add_dbpull_id(self, streaming_id: uuid.UUID):
        self.streaming_id = streaming_id

    def update(self, mapping: Dict[str, Any]):
        return self.copy(update=mapping)

    def __hash__(self):
        return hash(self.name)


def dbpull_factory(
    name: str,
    source: str,
    port: str,
    pararmeters: str,
    placement_name: str,
    effective_from: datetime.date,
    effective_to: datetime.date,
    active: bool,
) -> Streaming:
    return Streaming(
        id_=uuid.uuid4(),
        name=name,
        source=source,
        port=port,
        pararmeters=pararmeters,
        placement_name=placement_name,
        effective_from=effective_from,
        effective_to=effective_to,
        active=active,
    )
