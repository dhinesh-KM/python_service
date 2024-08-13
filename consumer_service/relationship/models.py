from mongoengine import *

class SpecialRelationship(Document):
    requestor_type = StringField()
    requestor_uid = StringField()
    requestor = GenericLazyReferenceField()
    acceptor_type = StringField()
    acceptor_uid = StringField()
    acceptor = GenericLazyReferenceField()
    created = DateTimeField() 
    accepted_date = DateTimeField()
    isaccepted = BooleanField()
    description = StringField()
    status = StringField()
    reject_reason = StringField()
    requestor_group_acls = ListField()
    acceptor_group_acls = ListField()
    tcfilename = StringField()
    requestor_tags = ListField(default=[])
    acceptor_tags = ListField(default=[])