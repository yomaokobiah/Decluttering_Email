"""This program sends emails to the trash"""

import imaplib
import getpass

user_name =  input("Enter the email address: ")
pass_word = getpass.getpass("Enter password: ")
server_name = "imap.gmail.com"

response = eval(input("Enter 1 if you want to trash all unread emails \nEnter 2 if you want to trash emails with a particular subject \nEnter 3 if you want to trash all emails from a sender: "))


def trash_unread(server, username, password):
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select("INBOX")
    results, messages = mail.search(None, 'UNSEEN')
    messages = messages[0].split()
    digit = len(messages)
    for x in messages:
        mail.store(x, '+X-GM-LABELS', '\\Trash')
    mail.close()
    mail.logout()
    print(f"All {digit} unread emails have been trashed.")

def trash_subject(server, username, password):
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select("INBOX")
    subject = input("Enter the desired subject: ")
    subject = subject.encode("utf-8")
    mail.literal = subject
    results, messages = mail.search("utf-8", "SUBJECT")
    messages = messages[0].split()
    digit = len(messages)
    for x in messages:
        mail.store(x, '+X-GM-LABELS', '\\Trash')
    mail.close()
    mail.logout()
    print(f"All {digit} emails with the subject {subject} have been trashed.")

def trash_sender(server, username, password):
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select("INBOX")
    sender = input("Enter the senders email address: ")
    sender = sender.encode("utf-8")
    mail.literal = sender
    results, messages = mail.search("utf-8", "FROM")
    messages = messages[0].split()
    digit = len(messages)
    for x in messages:
        mail.store(x, '+X-GM-LABELS', '\\Trash')
    mail.close()
    mail.logout()
    print(f"All {digit} emails from {sender} have been trashed.")


if response == 3:
    trash_sender(server_name, user_name, pass_word)
if response == 2:
    trash_subject(server_name, user_name, pass_word)
if response == 1:
    trash_unread(server_name, user_name, pass_word)