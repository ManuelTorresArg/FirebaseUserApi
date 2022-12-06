import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("scanapp-11ac7-firebase-adminsdk-yp3iq-4854f27cfe.json")

default_app = firebase_admin.initialize_app(cred)

user = auth.get_user_by_email("patagon.dev@gmail.com")
print('Successfully fetched user data: {0}'.format(user.id))