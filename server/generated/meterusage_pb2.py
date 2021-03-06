# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meterusage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="meterusage.proto",
    package="project",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x10meterusage.proto\x12\x07project\x1a\x1fgoogle/protobuf/timestamp.proto"Z\n\x0eMeterUsageItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nmeterusage\x18\x02 \x01(\x02\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp"<\n\x12MeterUsageResponse\x12&\n\x05items\x18\x01 \x03(\x0b\x32\x17.project.MeterUsageItem"4\n\x11MeterUsageRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x32_\n\x11MeterUsageService\x12J\n\rGetMeterUsage\x12\x1a.project.MeterUsageRequest\x1a\x1b.project.MeterUsageResponse"\x00\x62\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)


_METERUSAGEITEM = _descriptor.Descriptor(
    name="MeterUsageItem",
    full_name="project.MeterUsageItem",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="project.MeterUsageItem.id",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="meterusage",
            full_name="project.MeterUsageItem.meterusage",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time",
            full_name="project.MeterUsageItem.time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=62,
    serialized_end=152,
)


_METERUSAGERESPONSE = _descriptor.Descriptor(
    name="MeterUsageResponse",
    full_name="project.MeterUsageResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="items",
            full_name="project.MeterUsageResponse.items",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=154,
    serialized_end=214,
)


_METERUSAGEREQUEST = _descriptor.Descriptor(
    name="MeterUsageRequest",
    full_name="project.MeterUsageRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="page",
            full_name="project.MeterUsageRequest.page",
            index=0,
            number=1,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="project.MeterUsageRequest.page_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=216,
    serialized_end=268,
)

_METERUSAGEITEM.fields_by_name[
    "time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METERUSAGERESPONSE.fields_by_name["items"].message_type = _METERUSAGEITEM
DESCRIPTOR.message_types_by_name["MeterUsageItem"] = _METERUSAGEITEM
DESCRIPTOR.message_types_by_name["MeterUsageResponse"] = _METERUSAGERESPONSE
DESCRIPTOR.message_types_by_name["MeterUsageRequest"] = _METERUSAGEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MeterUsageItem = _reflection.GeneratedProtocolMessageType(
    "MeterUsageItem",
    (_message.Message,),
    {
        "DESCRIPTOR": _METERUSAGEITEM,
        "__module__": "meterusage_pb2"
        # @@protoc_insertion_point(class_scope:project.MeterUsageItem)
    },
)
_sym_db.RegisterMessage(MeterUsageItem)

MeterUsageResponse = _reflection.GeneratedProtocolMessageType(
    "MeterUsageResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _METERUSAGERESPONSE,
        "__module__": "meterusage_pb2"
        # @@protoc_insertion_point(class_scope:project.MeterUsageResponse)
    },
)
_sym_db.RegisterMessage(MeterUsageResponse)

MeterUsageRequest = _reflection.GeneratedProtocolMessageType(
    "MeterUsageRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _METERUSAGEREQUEST,
        "__module__": "meterusage_pb2"
        # @@protoc_insertion_point(class_scope:project.MeterUsageRequest)
    },
)
_sym_db.RegisterMessage(MeterUsageRequest)


_METERUSAGESERVICE = _descriptor.ServiceDescriptor(
    name="MeterUsageService",
    full_name="project.MeterUsageService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=270,
    serialized_end=365,
    methods=[
        _descriptor.MethodDescriptor(
            name="GetMeterUsage",
            full_name="project.MeterUsageService.GetMeterUsage",
            index=0,
            containing_service=None,
            input_type=_METERUSAGEREQUEST,
            output_type=_METERUSAGERESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_METERUSAGESERVICE)

DESCRIPTOR.services_by_name["MeterUsageService"] = _METERUSAGESERVICE

# @@protoc_insertion_point(module_scope)
