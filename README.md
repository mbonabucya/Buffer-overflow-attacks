# Buffer-overflow-attacks
Applications that have BOF vulnerabilities SLmail, vulnserver and Brainpan

### Requirements

1. Victim window Machine
2. Attacking box , I have used Kali linux 
3. SLmail.exe installer
4. Immunity debugger running on your Windows Machine(victim)

#### Objectives

1. Evaluate the buffer overflow in the Slmail application
2. Determine number of the Bytes that can crash program
3. Find the offset value
4. Get EIP address
5. Create the Unique Pattern that can crash the program rather than sending A characters.
6. Find the Bad characters
7. Develop exploit and the shellcode for the reverse shell.
8. Execute the exploit for the reverse shell connection.

### SLMAIL Buffer overflow steps

1. Download the SLmail.exe file ,install it on the Victim Machine
2. Run the slmail as Administrator from the target Machine
3. Attach it to the Immunity debugger
4. Execute the script "spiking.py"
5. Follow my walkthrough


