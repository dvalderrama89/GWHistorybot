GWHistorybot
============

Reddit bot that searches a users history for gonewild posts and provides links to any matches found.

Getting Started
----------------

Replace the fields in r.login() on line 20 in history_checker_bot.py with the login credentials of the Reddit account you wish to use as a commenter on any [Intro] submissions posted. Then run the bot with:

        $ python history_checker_bot.py 
        
Requires PRAW (Python Reddit API Wrapper) installation to work correctly.

Usage
---------------

GWHistorybot can be requested in all subreddits by submitting a comment with the following body: +summon gwbot

If the comment is a top-level comment then the bot will check the submission author's history.
If the comment is a child comment, then the parent's history will be checked.

Regardless of whether a match was found, the bot will submit output as a comment reply to the comment that requested the search.
