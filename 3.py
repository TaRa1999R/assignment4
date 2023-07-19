print (" 📱📱 INSTAGRAM FOLLOW & UNFOLLOW FINDERS 📱📱 ")

import instaloader
import getpass

f = open ( "3-followers.txt", "r" )                                      #gereftan list follower hae qadimi az file
old_followers = []
for line in f :
    old_followers.append ( line )
f.close ()

L = instaloader.Instaloader ()

username = print (" Please enter your instagram username : ")
password = getpass.getpass (" Please enter your instagram password : ")

L.login ( username, password )
print (" 🎉 Successfully logged in 🎉 ")

profile = instaloader.Profile.from_username ( L.context, username)        #vurud be account

Followers = []                                                            #gereftan follower ha
for follower in profile.get_followers :
    Followers.append ( follower )


for old_follower in old_followers :                                       #unfollow finder
    if old_follower not in Followers :
        print ( old_follower )


for new_follower in Followers :                                           #new follower finder 
    if new_follower not in old_followers :
        print ( new_follower )


f = open ( "3-followers.txt", "w" )                                       #zakhire follower ha dar file
for follower in Followers : 
    f.write ( follower, "\n" )
f.close ()
