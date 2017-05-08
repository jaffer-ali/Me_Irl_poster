from imgurpython import ImgurClient
import time
import random
import praw

client_id       = 'id_here'
client_secret   = 'scecret_here'
client          = ImgurClient(client_id, client_secret)
reddit          = praw.Reddit(user_agent='agent_here',
                     client_id='id_here',
                     client_secret="secret_here",
                     username='user_here',
                     password='pass_here')
subreddit       = reddit.subreddit("me_irl")

items           = client.subreddit_gallery("dankmemes", "hour")
postfolder      = []



def refresh(): #get some more memes for the folder
    for item in items:
        link = item.link
        if not link.endswith("gif"): #make sure its not a gif
            postfolder.append(item)


refresh()

def runposter():
    if len(postfolder) == 1:
        refresh()

    iterand = random.randrange(1,len(postfolder))
    link = postfolder[iterand]
    print(link.link)
    subreddit.submit(title="me irl", url=link.link, send_replies=False)
    del postfolder[iterand]
    time.sleep(5)
    runposter()

runposter()