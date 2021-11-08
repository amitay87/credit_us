from git import Repo

def say_hi():
    print("Hi!")
    filepath = 'C:\\Users\\USER\\Documents\\credit_us\\main.py'
    repo = Repo('C:\\Users\\USER\\Documents\\credit_us')
    for commit, lines in repo.blame('HEAD', filepath):
        print("%s changed these lines: %s" % (commit, lines))

if __name__ == '__main__':
    say_hi()