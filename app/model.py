from mongoengine import *

#class User(Document):
#    username = StringField(required=True)
#    password = StringField(required=True)


class Note(Document):
    subject = StringField()
    body = StringField()
    creation_time = DateTimeField(required=True)
    modification_time = DateTimeField(required=True)

    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.order_by('-modification_time')