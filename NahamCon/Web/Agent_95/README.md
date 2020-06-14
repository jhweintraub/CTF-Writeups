`Prompt - They've given you a number, and taken away your name~`

The web page has only the following text 
```
You don't look like our agent!
We will only give our flag to our Agent 95! He is still running an old version of Windows...
```

The thing that sticks out to me is the repeated use of the word `agent`, meaning user-agent in an HTTP request, but we need to know what the correct user-agent is. the `95` and `windows` sticks out to me as windows 95, so I googled what that was and find the following

`Mozilla/4.0 (compatible; MSIE 5.5; Windows 95; BCD2000)`

Replace that as the header in your http request with burp and we get the flag in return


`flag{user_agents_undercover}`