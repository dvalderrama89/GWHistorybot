"""
Version 1.0.0 (1/28/2014)
-works for all reddits

Known Issues:
-no known @ 1/28/2014
"""

import praw
import time
import datetime
import random

#User_ID
userA = ('History checker bot(only checks to see if someone posted to gonewild) by /u/epimetheusincarnate')

r = praw.Reddit(user_agent=userA)

#account that the agent logs in with the bot
r.login('YOUR_USERNAME_HERE', 'YOUR_PASSWORD_HERE')


#vars
already_done = set()
str_comment = ""
match_found = False
d = {}

print "GWHistory Detection bot started"
while True:

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    try:
        all_comments = r.get_comments('all', limit=1000)

        for comment in all_comments:
            if comment.body == "+summon gwbot" and comment.id not in already_done:
                print "I've been summoned! @ %s" % st
                parent = r.get_info(thing_id=comment.parent_id)
                
                if not comment.is_root:
                    user_submitted = parent.author.get_submitted(sort='top', time='all', limit='none')
                    str_comment += "Scraping user " + parent.author.name + "'s history for gonewild posts...\n\n"
                    for submission in user_submitted:
                        sub_name = submission.subreddit.display_name
                        if sub_name == "gonewild":
                            str_comment += "Found a match, here's the link: " + submission.short_link + "\n\n"
                            match_found = True
                    if match_found:
                        comment.reply(str_comment)
                        match_found = False
                    else:
                        str_comment += "No matches found.\n\n"
                        str_comment += "_________________________________________________________\n\n"
                        str_comment += "This comment was posted by a bot.\n"
                        comment.reply(str_comment)
                        
                else:
                    #The comment was a top level comment so do a query on submission author
                    submissionAuthor = comment.submission.author.get_submitted(sort='top', time='all', limit='none')
                    str_comment += "Scraping user " + comment.submission.author.name + "'s history for gonewild posts...\n\n"
                    for submission in submissionAuthor:
                        sub_name = submission.subreddit.display_name
                        if sub_name == "gonewild":
                            str_comment += "Found a match, here's the link: " + submission.short_link + "\n\n"
                            match_found = True
                    if match_found:
                        comment.reply(str_comment)
                        match_found = False
                    else:
                        str_comment += "No matches found.\n\n"
                        str_comment += "_________________________________________________________\n\n"
                        str_comment += "This comment was posted by a bot.\n"
                        comment.reply(str_comment)

                str_comment = ""
                already_done.add(comment.id)
            #endif
        #end for loop
            
    except:
        print "network error or summoned too much"
    
    #search new entries every 50 seconds
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print "BOT GO TO SLEEP NOW %s" % st
    time.sleep(50)
    
    
#end while

