from enum import IntEnum
from marshmallow import Schema, fields

from .contact import ContactSchema

class ContactGroupType(IntEnum):
    EARLY_ADOPTERS = 1
    BETA_TESTERS = 2
    TOP_CUSTOMERS = 3

class ContactGroup():
    #UNASSOCIATED = -1
    #EARLY_ADOPTERS = 0
    #BETA_TESTERS = 1
    #TOP_CUSTOMERS = 2

    def __init__(self, group_pk, group_name):
        self.group_pk = group_pk
        self.name = group_name
        self.contacts_list = []

class ContactGroupSchema(Schema):
    group_pk = fields.Integer()
    name = fields.String(32)
    contacts_list = fields.Nested(ContactSchema, many=True)

    #@post_load
    #def make_contact_group(self, data, **kwargs):
    #    return ContactGroup(**data)

class ContactGroupList:
    #groups = [
    #        ContactGroup(ContactGroup.EARLY_ADOPTERS),
    #        ContactGroup(ContactGroup.BETA_TESTERS),
    #        ContactGroup(ContactGroup.TOP_CUSTOMERS)
    #]
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

    #def get_json_formatted_list(self):
    #    grs = []
    #    schema = ContactGroupSchema()

    #    for g in self.groups.values():
    #        gr_data = schema.dump(g).data
    #        grs.append(gr_data)
    #    return grs

