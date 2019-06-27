from enum import Enum


class ContactGroup(Enum):
    UNASSOCIATED = -1
    EARLY_ADOPTERS = 0
    BETA_TESTERS = 1
    TOP_CUSTOMERS = 2

    def __init__(self, group_pk):
        self.group_pk = group_pk
        self.users_id_list = []


class ContactGroupList:
    groups = [
            ContactGroup(ContactGroup.EARLY_ADOPTERS),
            ContactGroup(ContactGroup.BETA_TESTERS),
            ContactGroup(ContactGroup.TOP_CUSTOMERS)
    ]

    def get_group(group_pk):
        for g in self.groups:
            if g.group_pk == group_pk:
                return g
        return None
