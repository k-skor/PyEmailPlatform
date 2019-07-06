from enum import IntEnum
from marshmallow import Schema, fields

from .contact import ContactSchema

class ContactGroupType(IntEnum):
    EARLY_ADOPTERS = 1
    BETA_TESTERS = 2
    TOP_CUSTOMERS = 3

class ContactGroup():
    def __init__(self, group_pk, group_name):
        self.group_pk = group_pk
        self.name = group_name
        self.contacts_list = []

class ContactGroupSchema(Schema):
    group_pk = fields.Integer()
    name = fields.String(32)
    contacts_list = fields.Nested(ContactSchema, many=True)

class ContactGroupList:
    groups = {
            ContactGroupType.EARLY_ADOPTERS: ContactGroup(0, "Early adopters"),
            ContactGroupType.BETA_TESTERS: ContactGroup(1, "Beta testers"),
            ContactGroupType.TOP_CUSTOMERS: ContactGroup(2, "Top customers"),
            }

    def get_group(self, group_pk):
        for g in self.groups.values():
            if g.group_pk == group_pk:
                return g
        return None

    def get_groups(self):
        return self.groups.values()

