from notification import locale
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class NotificationManager:
    cred = credentials.Certificate('./canaryserviceaccount.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    def notificationmanager(self, data):
        if data['payload']['comp'] == 'realtime':
            self.notificationrealtime(data)
        elif data['payload']['comp'] == 'email':
            self.notificationemail(data)
        elif data['payload']['comp'] == 'push':
            self.notificationpush(data)

    def notificationrealtime(self, data):
        event_id = data['event_id']
        username = data['payload']['username']
        lang_id = data['payload']['language']
        comp = data['payload']['comp']
        asset_symbol = data['payload']['asset_symbol']

        message = locale.get_translation(lang_id, comp, event_id)
        message = message.replace("<<asset_symbol>>", asset_symbol)

        event_id = event_id + '_' + asset_symbol
        self.firebase(message, event_id, username)

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
