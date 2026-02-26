import os
import base64
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes define karte hain ke humein sirf read-only access chahiye
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    # token.json mein aapki login details save hongi pehli baar ke baad
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    return build('gmail', 'v1', credentials=creds)

def fetch_unread_emails():
    service = get_gmail_service()
    # Sirf unread emails uthayega jo inbox mein hain
    results = service.users().messages().list(userId='me', q='is:unread label:inbox').execute()
    messages = results.get('messages', [])

    if not messages:
        print("Koi naye unread emails nahi mile.")
        return

    print(f"{len(messages)} naye emails mile hain. Processing dates and content...")

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data.get('payload', {}).get('headers', [])
        
        # Headers se info nikaalna
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
        sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")
        date = next((h['value'] for h in headers if h['name'] == 'Date'), "No Date")
        
        # Email ki body nikaalna
        body = "No text content found."
        payload = msg_data.get('payload', {})
        
        def get_body(payload):
            if 'parts' in payload:
                for part in payload['parts']:
                    if part['mimeType'] == 'text/plain':
                        data = part.get('body', {}).get('data')
                        if data:
                            return base64.urlsafe_b64decode(data).decode('utf-8')
                # Agar text/plain nahi mila toh depth mein check karein
                for part in payload['parts']:
                    res = get_body(part)
                    if res: return res
            else:
                data = payload.get('body', {}).get('data')
                if data:
                    return base64.urlsafe_b64decode(data).decode('utf-8')
            return None

        body = get_body(payload) or "No text content found."

        # Inbox folder mein file save karna
        file_path = f"Inbox/Email_{msg['id']}.md"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"--- DATE: {date} ---\n") # Ab date bhi save hogi
            f.write(f"--- SENDER: {sender} ---\n")
            f.write(f"--- SUBJECT: {subject} ---\n\n")
            f.write(body)
        
        print(f"Saved: {file_path} | Date: {date}")

if __name__ == '__main__':
    # Ensure Inbox folder exists
    if not os.path.exists('Inbox'):
        os.makedirs('Inbox')
    
    # Optional: Purani files delete karna taake sirf fresh unread emails rahein
    # for file in os.listdir('Inbox'): os.remove(os.path.join('Inbox', file))
    
    fetch_unread_emails()