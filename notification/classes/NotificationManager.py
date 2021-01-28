from notification.models import Realtime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class NotificationManager:
    cred = credentials.Certificate('./canaryserviceaccount.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    def notificationmanager(self, data):
        if data['payload']['type'] == 'realtime':
            self.notificationrealtime(data)
        elif data['payload']['type'] == 'email':
            self.notificationemail(data)
        elif data['payload']['type'] == 'push':
            self.notificationpush(data)

    def notificationrealtime(self, data):
        message = ''
        eventid = data['eventid']
        username = data['payload']['username']
        language = data['payload']['language']
        asset_symbol = data['payload']['asset_symbol']

        queryset = Realtime.objects.filter(event_id=eventid, language=language)
        for obj in queryset:
            message = obj.message

        eventid = eventid + '_' + asset_symbol
        self.firebase(message, eventid, username)

    def notificationemail(self, data):
        print("email" + data)

    def notificationpush(self, data):
        print("push" + data)

    def firebase(self, message, eventid, username):
        doc_ref = self.db.collection(u'users').document(username).collection(u'notification').document(eventid)
        doc_ref.set({
            u'message': message,
            u'read': u'false'
        })
