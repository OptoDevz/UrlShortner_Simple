import os
import easygui

msg = "Loading.."
title = "URL SHORTENER"
choice = ["urlshortener", "exit", "troll"]
reply = easygui.buttonbox(msg, title, choice)
if reply == "urlshortener":
    os.startfile("D:\\Downloads\\Datasets & yes\\proj\\urlshor\\urlshor.py")
elif reply == exit:
    os.system("Exiting..")
    os._exit
elif reply == "troll":
    easygui.msgbox("You got big time trolled")