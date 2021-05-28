"""This program permanently deletes emails."""
from imapclient import IMAPClient
import getpass

user_name =  input("Enter the email address: ")
pass_word = getpass.getpass("Enter password: ")
server_name = "imap.gmail.com"


response = eval(input("Enter 1 if you want to trash all unread emails \nEnter 2 if you want to trash emails with a particular subject \nEnter 3 if you want to trash all emails from a sender: "))


def trash_unread(mail, username, password):
    server = IMAPClient(mail, use_uid=True)
    server.login(username, password)
    server.select_folder("INBOX")
    messages = server.search("UNSEEN")
    digit = len(messages)
    for x in messages:
        server.delete_messages(x)
    server.logout()
    print(f"All {digit} unread emails have been deleted.")

def trash_subject(mail, username, password):
    server = IMAPClient(mail, use_uid=True)
    server.login(username, password)
    server.select_folder("INBOX")
    subject = input("Enter the desired subject: ")
    messages = server.search(['SUBJECT', subject])
    digit = len(messages)
    for x in messages:
        server.delete_messages(x)
    server.logout()
    print(f"All {digit} emails with the subject {subject} have been deleted.")

def trash_sender(mail, username, password):
    server = IMAPClient(mail, use_uid=True)
    server.login(username, password)
    server.select_folder("INBOX")
    sender = input("Enter the senders email address: ")
    messages = server.search(['FROM', sender])
    digit = len(messages)
    for x in messages:
        server.delete_messages(x)
    server.logout()
    print(f"All {digit} emails from {sender} have been deleted.")

if response == 1:
    trash_unread(server_name, user_name, pass_word)
if response == 2:
    trash_subject(server_name, user_name, pass_word)
if response == 3:
    trash_sender(server_name, user_name, pass_word)
