# Oddcrk

Tool to perform dictionary attacks on emails in the SMTP protocol. It has two functions, the first
is to create word dictionaries through Heap's algorithm, indicating the words to use. The second
functionality allows you to perform dictionary attacks by indicating the parameters established in the script.

## Requeriments

If you want to use this tool you must have a python version greater than or equal to 3.
If you do not have python installed on your system you can download it from the following link.

https://www.python.org/downloads/

## Running oddcrk

When running the tool you will have the possibility of two options, generate a dictionary and perform the dictionary attack.

![imagen](https://user-images.githubusercontent.com/106930530/235549827-1772014c-027a-4911-8968-6c934e4a0082.png)


### Generate dictionary

This option will allow you to generate a dictionary according to the words that you assign to it by parameter.

The syntax to run this function is as follows:

`python3 oddcrk.py -list [LISTNAME] -add password 1 2 3 `

#### Example

`python3 oddcrk.py -list numbers.txt -add 0 1 2 3 4 5 6 7 8 9`

![imagen](https://user-images.githubusercontent.com/106930530/235550350-f1b75b85-813b-46d9-8f61-5d6aa5aadee8.png)

### Dictionary attack
This part of the tool is a bit more extensive, it consists of assigning three parameters to it, which work as follows:

- First, it receives the IP address of the host on which the attack will be carried out. In the tool's options menu
you will see a section where it indicates some of the most common IP addresses. 

- Second, it receives the name of the user to whom the dictionary attack will be carried out.

- Third, it receives the name of the file which contains the possible passwords to use in the dictionary attack.

The first parameter which receives the IP address of the host is used to verify that the host is listening for requests.

the full command syntax would be as follows:

`python3 oddcrk.py -ip [IP] -usr [USERNAME] -psw [LISTNAME]`

The command will start to execute, then it will only be time to find the password, if it is found in the file that we
pass to it by parameter.

#### Example

`python3 oddcrk.py -ip 52.96.189.34 -usr email@hotmail.com -psw numbers.txt`

![imagen](https://user-images.githubusercontent.com/106930530/235551739-1e788470-0c42-447a-9683-d13a050929fe.png)

### Proxy

This tool allows you to use proxyhains to send the requests. The syntax for running the tool with proxychains is as follows:

`proxychains python3 oddcrk.py -ip [IP] -usr [USERNAME] -psw [LISTNAME]`

## Support

The tool will be constantly updated as many times as necessary, the tool is still under development, if you find faults in its
operation, do not hesitate to contact me, that will help to solve your problem and improve the tool.

## Legal disclaimer

This tool is designed for educational purposes, the person who decides to use it assumes responsibility for their own actions 
according to the use they decide to give it.

## Glosary

If you are someone new to the world of cybersecurity and hacking, you may come across some unfamiliar terms.

- *Dictionary attack:* The technique consists of consecutively trying many real words collected in the dictionaries of
the different languages, and also the most used passwords

- *SMTP:* Simple Mail Transfer Protocol (SMTP) is a TCP/IP protocol used to send and receive email.

- *Ip:* An IP address is a unique address that identifies a device on the Internet or on a local network.

- *Server:* It is a set of computers capable of meeting the requests of a client and returning a response accordingly.

### References
- https://www.bbva.com/es/innovacion/que-es-un-ataque-de-diccionario-si-no-se-refiere-a-arrojar-un-libro-a-alguien/
- https://www.ibm.com/docs/es/i/7.3?topic=information-smtp
- https://latam.kaspersky.com/resource-center/definitions/what-is-an-ip-address
- https://es.wikipedia.org/wiki/Servidor

## License

oddcrk is [MIT Licensed](https://github.com/odindaza/oddcrk/blob/main/LICENSE)




