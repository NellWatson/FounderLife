init python:
    import renpy.store as store
    
    

    class Mail(store.object):
        def __init__(self, subject, sender, body, reply_label, view=True, status=True):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.reply_label = reply_label
            self.view = view
            self.status = status
            mail.insert(0, self)
            if reply_label:
                self.can_reply = True
            else:
                self.can_reply = False
            global new_messages
            new_messages = new_messages + 1

        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)
            reply_screen = False

        def delete(self):
            self.view = False

        def restore(self):
            self.view = True

        def mark_read(self):
            self.status = False

    def restore_all():
        deleted_messages = [x for x in mail if x.view == False]
        for x in deleted_messages:
            x.restore()
        renpy.restart_interaction()

    def mark_all_read():
        unread_messages = [x for x in mail if x.status]
        for x in unread_messages:
            x.mark_read()

    def add_message(subject, sender, body, reply_label=False):
        renpy.sound.play("mail.wav")
        message = Mail(subject, sender, body, reply_label)
        renpy.show_screen("mailbox_overlay")
        
    def add_later(subject, sender, body, reply_label=False):
        mail_later.append([subject, sender, body, reply_label])
        
    def add_now():
        for element in mail_later:
            add_message(element[0], element[1], element[2], element[3])
        global mail_later
        mail_later = []
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.status:
                    return False #message is marked as unread
                else:
                    return True # message is marked as read

screen mailbox_overlay:
    hbox:
        xalign 1.0 yalign 0.0
        if new_messages > 0:
            textbutton "Mailbox ([new_messages] New)" text_color "#000000" # action Show("mailbox")
        else:
            textbutton "Mailbox"# action Show("mailbox")

screen mailbox:
    tag menu
    modal True
    default current_message = None
    $ visible_messages = [i for i in mail if i.view]
    frame:
        style_group "mailbox"
        vbox:
            label "Inbox"
            if new_messages > 0:
                text ("Messages: " + str(len(visible_messages)) + " ([new_messages] unread)")
            else:
                text ("Messages: " + str(len(visible_messages)))
            side "c r":
                area (0,0,1280,200)
                viewport id "message_list":
                    draggable True mousewheel True
                    vbox:
                        for i in mail:
                            if i.view:
                                if i.status:
                                    textbutton ("{size=-5}*{/s}NEW{size=-5}*{/s} " + i.sender + " - " + i.subject) action [SetScreenVariable("current_message",i), i.mark_read, SetVariable("new_messages",new_messages-1)] xfill True
                                else:
                                    textbutton (i.sender + " - " + i.subject) action SetScreenVariable("current_message",i) xfill True
                vbar value YScrollValue("message_list")
            hbox:
                null height 50
            side "c r":
                area (0,0,1280,380)
                viewport id "view_message":
                    draggable True mousewheel True
                    vbox:
                        if current_message:
                            text ("From: " + current_message.sender)
                            text ("Subject: " + current_message.subject)
                            text current_message.body
                vbar value YScrollValue("view_message")
            use mailbox_commands

screen mailbox_commands:
    hbox:
        if current_message and current_message.can_reply:
            textbutton "Reply" action current_message.reply
        else:
            textbutton "Reply" action None
        if current_message:
            textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)]
        else:
            textbutton "Delete" action None
        if new_messages > 0:
            textbutton "Mark All Read" action [mark_all_read, SetVariable("new_messages",0)]
        else:
            textbutton "Mark All Read" action None
        textbutton "Restore Trash" action restore_all
        textbutton "Exit" action Hide("mailbox")

init -2 python:
    style.mailbox = Style(style.default)
    style.mailbox_vbox.xalign = 0.5
    style.mailbox_vbox.xfill = True
    style.mailbox_hbox.xalign = 0.5
    style.mailbox_label_text.size = 30
    style.mailbox_label_text.xalign = 0.5
    style.mailbox_label.xfill = True
    style.mailbox_frame.xalign = 0.5
    style.mailbox_frame.yalign = 0.5