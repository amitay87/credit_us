import yagmail
from git import Repo
import smtplib
from email.mime.text import MIMEText
import json
import sys
import trace

def send_email(receiver): # sender, receiver, subject, body):
    with open('credentials.json') as fp:
        credentials = json.load(fp)

    username = credentials['username']
    password = credentials['password']

    yag = yagmail.SMTP(username, password)
    yag.send(receiver, 'Thank you for your contribution', 'Thank you!')



def say_hi():
    print("Hi!")
    filepath = 'C:\\Users\\USER\\Documents\\credit_us\\main.py'
    repo = Repo('C:\\Users\\USER\\Documents\\credit_us')
    for commit, lines in repo.blame('HEAD', filepath):
        # send_email(commit.committer.email, 'Thanks!')
        print("%s changed these lines: %s" % (commit, lines))

if __name__ == '__main__':
    say_hi()
    # send_email()



# # create a Trace object, telling it what to ignore, and whether to
# # do tracing or line-counting or both.
# tracer = trace.Trace(
#     ignoredirs=[sys.prefix, sys.exec_prefix],
#     trace=0,
#     count=1)
#
# # run the new command using the given tracer
# tracer.run('say_hi()')
#
# # make a report, placing output in the current directory
# r = tracer.results()
# r.write_results(show_missing=True, coverdir="cover")