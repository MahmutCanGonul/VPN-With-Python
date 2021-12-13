def Vpn():
    codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W",
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
    enter_time = datetime.datatime.now()
    print("' q' --> Disconnect Vpn")
    print(" 'v' --> Change Vpn Location")
    code = random.choice(codeList)
    try:
        os.system("windscribe connect")
        while True:
            
            if 0xFF == ord("q"):  #When you click 'q'  exit the system and disconnect to VPN
                os.system("windscribe disconnect")
                print("Disconnected the VPN!")
                exit_time = datetime.datetime.now() - enter_time
                print(f"Passed Time {exit_time}")
                break
            elif 0xFF == ord("v"): #When you click 'v'  change the vpn location
                code = random.choice(codeList)
                print("Changing the IP Address.....")
            
            
            os.system("windscribe connect "+code)
                
            
            
            
    except Exception as ex:
        os.system("windscribe disconnect")
        print("Disconnected the VPN!")
        print(f"Error --> {ex}")
        
