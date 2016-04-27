# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remBook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='remBook.proto',
  package='tutorial',
  serialized_pb=_b('\n\rremBook.proto\x12\x08tutorial\"\xa2\x01\n\x04\x43\x61rd\x12\x0c\n\x04side\x18\x01 \x03(\t\x12\x14\n\x0ctrainingDate\x18\x02 \x03(\x03\x12)\n\x0etrainingResult\x18\x03 \x03(\x0e\x32\x11.tutorial.Quality\x12\'\n\x06\x61nswer\x18\x04 \x01(\x0e\x32\x10.tutorial.Answer:\x05WRITE\x12\"\n\x04type\x18\x05 \x01(\x0e\x32\x0e.tutorial.Type:\x04NONE\"2\n\x04\x42ook\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1c\n\x04\x63\x61rd\x18\x02 \x03(\x0b\x32\x0e.tutorial.Card*E\n\x07Quality\x12\r\n\tEXCELLENT\x10\x01\x12\x08\n\x04GOOD\x10\x02\x12\x08\n\x04\x46\x41IR\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\x0b\n\x07NO_CLUE\x10\x05* \n\x06\x41nswer\x12\t\n\x05WRITE\x10\x01\x12\x0b\n\x07IN_HEAD\x10\x02*;\n\x04Type\x12\x08\n\x04NONE\x10\x01\x12\t\n\x05\x43LOZE\x10\x02\x12\r\n\tTWO_SIDED\x10\x03\x12\x0f\n\x0bMULTI_SIDED\x10\x04')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_QUALITY = _descriptor.EnumDescriptor(
  name='Quality',
  full_name='tutorial.Quality',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXCELLENT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIR', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_CLUE', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=244,
  serialized_end=313,
)
_sym_db.RegisterEnumDescriptor(_QUALITY)

Quality = enum_type_wrapper.EnumTypeWrapper(_QUALITY)
_ANSWER = _descriptor.EnumDescriptor(
  name='Answer',
  full_name='tutorial.Answer',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IN_HEAD', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=315,
  serialized_end=347,
)
_sym_db.RegisterEnumDescriptor(_ANSWER)

Answer = enum_type_wrapper.EnumTypeWrapper(_ANSWER)
_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='tutorial.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOZE', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWO_SIDED', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTI_SIDED', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=349,
  serialized_end=408,
)
_sym_db.RegisterEnumDescriptor(_TYPE)

Type = enum_type_wrapper.EnumTypeWrapper(_TYPE)
EXCELLENT = 1
GOOD = 2
FAIR = 3
FAILED = 4
NO_CLUE = 5
WRITE = 1
IN_HEAD = 2
NONE = 1
CLOZE = 2
TWO_SIDED = 3
MULTI_SIDED = 4



_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='tutorial.Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='side', full_name='tutorial.Card.side', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainingDate', full_name='tutorial.Card.trainingDate', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainingResult', full_name='tutorial.Card.trainingResult', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='tutorial.Card.answer', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='tutorial.Card.type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=190,
)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='tutorial.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.Book.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='card', full_name='tutorial.Book.card', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=242,
)

_CARD.fields_by_name['trainingResult'].enum_type = _QUALITY
_CARD.fields_by_name['answer'].enum_type = _ANSWER
_CARD.fields_by_name['type'].enum_type = _TYPE
_BOOK.fields_by_name['card'].message_type = _CARD
DESCRIPTOR.message_types_by_name['Card'] = _CARD
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.enum_types_by_name['Quality'] = _QUALITY
DESCRIPTOR.enum_types_by_name['Answer'] = _ANSWER
DESCRIPTOR.enum_types_by_name['Type'] = _TYPE

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), dict(
  DESCRIPTOR = _CARD,
  __module__ = 'remBook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Card)
  ))
_sym_db.RegisterMessage(Card)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), dict(
  DESCRIPTOR = _BOOK,
  __module__ = 'remBook_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Book)
  ))
_sym_db.RegisterMessage(Book)


# @@protoc_insertion_point(module_scope)
