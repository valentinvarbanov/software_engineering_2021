# Input sanitization

Input sanitization is needed in order to avoid some common attacks. 

## SQL injection 

A SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.

Resources:

* https://www.w3schools.com/sql/sql_injection.asp
* https://www.youtube.com/watch?v=ciNHn38EyRc
* https://owasp.org/www-community/attacks/SQL_Injection

## Cross Site Scripting - XSS

Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

Resources:

* https://owasp.org/www-community/attacks/xss/


## Cross Frame Scripting - XFS

Cross-Frame Scripting (XFS) is an attack that combines malicious JavaScript with an iframe that loads a legitimate page in an effort to steal data from an unsuspecting user. This attack is usually only successful when combined with social engineering. An example would consist of an attacker convincing the user to navigate to a web page the attacker controls. The attacker’s page then loads malicious JavaScript and an HTML iframe pointing to a legitimate site. Once the user enters credentials into the legitimate site within the iframe, the malicious JavaScript steals the keystrokes.

Resources:

* https://owasp.org/www-community/attacks/Cross_Frame_Scripting