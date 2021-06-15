'''Made by Leafy-Pro ¯\_(ツ)_/¯'''

import webbrowser # Used for working with browser
import winapps  # Used for working with installed apps
from termcolor import colored # Just for colouring ツ
from os import remove # Used in -appsLocation command

for item in winapps.search_installed("chrome"): # Stores  correct chrome's location in windows in most of the cases
    string = f"\n\n {item} \n\n"
string = string.replace("'", "")
string = string.replace(",", "")
string = string.split("WindowsPath")
string = str(string[1])
string = string.split("install_source")
string = str(string[0])
string = string.replace("(", "")
string = string.replace(")", "")
string = string.strip()
string = f"{string}/chrome.exe"
            
print(colored("'''Know location of your chrome by -chromeLocation command'''", "magenta"))

try:
    inp = input(colored("Enter Your Query (--help to list commands or just Enter Query To Search): ", "cyan"))

    if inp != "--help" and inp != "-setup" and inp != "-chromeLocation" and inp != "-appsLocation": # To execute rather than commands
        query_list = inp.replace(" ", "+")
        url = f"https://www.google.com/search?q={query_list}"
        with open("setup.txt") as se:
            location = se.read()
        chrome_path = f"{location} %s" # %s is important after location
        webbrowser.get(chrome_path).open(url)

    else: # To execute commands
        if inp == "--help":
            with open("help.txt") as h:
                help = h.read()
                print(help)

        elif inp == "-chromeLocation":
            print(string)

        elif inp == "-setup":
            try:
                setup = string
            except:
                with open("setup.txt", "w") as s:
                    setup = input("Enter Path Of Chrome Or Any Web Browser (Like C:/Program Files/Google/Chrome/Application/chrome.exe): ")
                    s.write(setup)
                    print("Done! Restart the program to implement changes.")

        elif inp == "-appsLocation":
            for item in winapps.list_installed():
                one_app_info_at_a_time = str(item)

                with open("temporary.txt", "a+") as t:
                    t.write(one_app_info_at_a_time + "\n")

            with open("installed_apps.txt", "w") as ins:
                with open("temporary.txt") as t:
                    temp_read = t.read()
                ins.write(temp_read)

            remove("temporary.txt")

            # Colouring the texts

            apps_info = temp_read.split("\n")
            apps_info_len = len(apps_info)

            for i in range(apps_info_len):
                if i%2 == 0:
                        print("\n" + colored(apps_info[i], "yellow") + "\n")
                else:
                    print("\n" + colored(apps_info[i], "green") + "\n")

except KeyboardInterrupt:
    print(colored("\nProgram Exited Successfully!", "red"))

except:
    print("Something Went Wrong. Please Contact The Creator On GitHub Page.")