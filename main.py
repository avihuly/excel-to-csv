from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import io
from apiclient.http import MediaIoBaseDownload
import csv

SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file','https://www.googleapis.com/auth/drive.readonly']

creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
	with open('token.pickle', 'rb') as token:
		creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
	if creds and creds.expired and creds.refresh_token:
		creds.refresh(Request())
	else:
		flow = InstalledAppFlow.from_client_secrets_file(
			'credentials.json', SCOPES)
		creds = flow.run_local_server()
	# Save the credentials for the next run
	with open('token.pickle', 'wb') as token:
		pickle.dump(creds, token)

drive_service = build('drive', 'v3', credentials=creds)	
	
file_id = '12os_T3UqgOYsIjrelcq9VyIz7gAiT3uwV2h5zaTUa74'
request = drive_service.files().export_media(fileId=file_id, mimeType='text/csv')
# AS File
fh = io.FileIO('cards.csv', 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
	status, done = downloader.next_chunk()
	print ("Download %d%%." % int(status.progress() * 100))

# AS BytesIO
#fh = io.BytesIO()
#downloader = MediaIoBaseDownload(fh, request)
#done = False
#while done is False:
#    status, done = downloader.next_chunk()
#    print ("Download %d%%." % int(status.progress() * 100))

transaction = []

with open('cards.csv', 'r',encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)