## 🧩 Solution to the Challenge  
I had already checked for a page `/admin` because I’d done CTFs before, and I saw an `/admin` page. I thought there were probably other unprotected paths on the site, and I came across the vulnerability via `robots.txt`. By typing the path from `robots.txt` into my browser’s address bar I was able to access a page where there was a folder `/whatever -> .htpasswd` containing a password in MD5 prefixed by the word `root` : `root:437394baff5aa33daa618be47b75cb49` I decoded the MD5 and it gave the password `qwerty123@`. Using `root` and that password on the admin page I found the flag.

![image](https://github.com/user-attachments/assets/ba53746e-4166-4aea-8068-90d7ea81d01e)


<img width="416" height="154" alt="image (1)" src="https://github.com/user-attachments/assets/77e5c692-cbc8-49f8-b2b2-587dd33b1624" />

robots.txt is a public file used to tell search engines which parts of a website to ignore. However, relying on it to hide sensitive directories is insecure because it publicly exposes these paths, making it easy for attackers to discover and access admin pages, backups, or confidential files. Proper security requires implementing real access controls and not depending on robots.txt for protection.

## 🔐 Result / FLAG:  
`FLAG: d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466`

## 🏁 Conclusion:  
`robots.txt` revealed sensitive paths; an accessible `.htpasswd` contained an MD5 password which I decoded to log into the admin and obtain the flag.

source : https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/01-Information_Gathering/03-Review_Webserver_Metafiles_for_Information_Leakage
