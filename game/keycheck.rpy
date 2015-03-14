label keycheck:
#How to make activation keys:
#1 - Upload a .txt file to a host. This must have a static url, or it wont work.
#2 - Once someone gets a key by any means you want, be it purchasing or asking nicely, add that key to the .txt file.
#3 - Key is compared to the ones in the server by a simple python script, could be something like this:


#key = renpy.input("Key: ")
#import urllib2
#python:
#    try:
#        for line in urllib2.urlopen('http://mykeyserver.com/keys.txt'):
#            if key in line:
#                activated = 1
#    except:
#        activated = 0
        
        
        
#python:
#    email_message = "Key "+key+" has been redeemed."
#    import smtplib
#    server = smtplib.SMTP('localhost')
#    # This line is configured like this: server.sendmail('from', 'to', 'message')
#    server.sendmail('yourclientemailaccount@example.com', 'youremailaccount@example.com', email_variable)
#    server.quit()
        
        
#5 - Edit the .txt file and remove the key so it can't be redeemed again. You can also place a button in the client that once the key has been activated requests a new key. That would ask for the person's email and use it as the 'yourclientemailaccount@example.com' to send the message to you. You send them a new key if you find their email on a list which you should keep and send them their key again. Once you send the key be sure to add it to the .txt file so it can be redeemed once more.


#renpy.full_restart()