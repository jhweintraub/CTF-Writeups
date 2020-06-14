```
Prompt - This year, I resolve to not use old and deprecated nameserver technologies!

There is nothing running on port 80. This is an OSINT challenge.

Connect here: jh2i.com
```

This challenge was very annoying because while it's simple enough to use dig, the trick comes from knowing which record type to use. I ended up using the `digwebinterface.com` site and selecting `any` from the types and input the domain `jh2i.com` into the search box and the flag came out for record type `SPF`

`flag{next_year_i_wont_use_spf}`