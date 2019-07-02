from email_platform.model import groups
#from contacts import get_contacts_for_group

group_list = groups.ContactGroupList()

#class GroupAggregation:
#    name = ""
#    contacts_list = []
#
#def get_aggregate_groups():
#    aggregate = {}
#    for (t, g) in group_list.groups:
#        ga = GroupAggregation()
#        ga.name = t.value
#        ga.contacts_list = get_contacts_for_group(g.group_pk)
#        aggregate[g.group_pk] = ga
#    return aggregate

def add_contact_to_group(contact):
    group = group_list.get_group(contact.group_id)
    group.contacts_list.append(contact)

def change_contact_group(contact, group_id):
    old_group = group_list.get_group(group_id)
    print("remove contact id: {}".format(contact.contact_pk))
    if old_group is not None:
        print("contacts list: {}".format(old_group.contacts_list))
        old_group.contacts_list.remove(contact)

    print("change contact group, old {0} -> new {1}".format(old_group, group_id))
    add_contact_to_group(contact)
