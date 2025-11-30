**Statement**
Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?
https://ctfg-cookie-monster.vercel.app 

**Points** 50

**FLAG** IDC{7h3_wInn3r_Tak3s_I7_4ll}

**SOLUTION**
	- Head to the site using link provided in the challenge.
	- Use Inspect element to view the source of web page.
	- Click on storage tab.
	- Click on cookies to find the cookie file named 'secret_recipe' and copy its value.
	- Convert the value from base64 to obtain the flag.
	
**Core concpet** Web cookies
