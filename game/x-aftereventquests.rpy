label AfterEventQuestOne:
    if dianaGoodRelations == False:
        if jeremy_message_event_one == False:
            show screen NotificationScreen
            $ Jeremy_Text_Unread = True
    else:

        $ newQuest = True
        call notificationShow from _call_notificationShow_46
        $ calendar.AddTime(1)
        if BenjaminContent == True:
            $ benjamin_event_one = True
        else:
            $ benjamin_var_two = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
