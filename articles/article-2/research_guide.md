# Research Guide and Question Bank for HTTPS Article
## Section 1 – What HTTPS Actually Is
What is HTTP and what does it do. The request response cycle at a basic level
What problem did HTTP have that created the need for HTTPS
What is SSL and how did it evolve into TLS
What version of TLS is current and why did the earlier versions get deprecated
What does the TLS handshake actually do step by step — what gets negotiated, what keys get exchanged, what gets verified
What is a digital certificate and what information does it contain
What is a Certificate Authority and what does it actually verify before issuing a certificate
What does it mean to trust a certificate — where does that trust ultimately come from
What is the chain of trust and what happens if a link in that chain is compromised
What does the padlock icon in a browser actually verify and what does it not verify
## Section 2 – What HTTPS Does Not Protect
Does HTTPS protect data once it reaches the server — why not
Does HTTPS prevent SQL injection on the server — why not
Does HTTPS prevent XSS — why not
Can a phishing site have a valid HTTPS certificate — how and how commonly
Does HTTPS guarantee the identity of who runs the site beyond the domain name
What is the difference between domain validation, organization validation, and extended validation certificates
Has the green padlock ever genuinely signaled more trust than it does now and what changed
## Section 3 - Real Attacks and Breaks
What is SSL stripping and how does it work — Moxie Marlinspike's 2009 demonstration
What is HSTS and how does it defend against SSL stripping
What were POODLE and BEAST attacks and what did they exploit specifically
What is the BEAST attack and what CBC cipher weakness did it exploit
What is the POODLE attack and why did it target SSL 3.0 specifically
What is the DigiNotar incident — what happened, who was affected, what it revealed about CA trust
What is certificate transparency and why was it introduced after DigiNotar and similar incidents
What is a man-in-the-middle attack in the context of HTTPS and what conditions make it possible
What is HPKP (HTTP Public Key Pinning) and why was it eventually deprecated despite being a security improvement
## Section 4 — Middleboxes
Middleboxes are one of the most interesting and underwritten aspects of the HTTPS trust discussion and they connect directly to your thesis that the tunnel being safe does not mean the journey is private.
What is a middlebox — define it clearly, give examples: corporate firewalls, DPI devices, content filters, antivirus proxies
How do corporate HTTPS inspection middleboxes work — they terminate the TLS connection, inspect the plaintext, re-encrypt to the destination. The user sees a padlock but the traffic is being decrypted in the middle
Is corporate HTTPS inspection a man-in-the-middle attack technically — yes, a legitimate authorized one
What are the security implications of middlebox inspection — the middlebox becomes a new attack surface, if compromised all "secure" traffic through it is exposed
What is deep packet inspection and when does it interact with HTTPS
ISP-level HTTPS interception — is it legal, where, and what does it enable
The middlebox section is particularly powerful in the context of your thesis because it shows that even when HTTPS is working perfectly as designed, the tunnel can still be opened mid-journey by entities the user never consented to and often does not know exist.
## Section 5 — What Website Owners Get Wrong
Running HTTPS but storing passwords in plaintext on the server
Running HTTPS but with TLS 1.0 or 1.1 still enabled — deprecated versions
Running HTTPS on login pages but HTTP on other pages — mixed content
Running HTTPS but with a self-signed certificate that browsers flag as untrusted
Running HTTPS but with HTTP fallback enabled and no HSTS
Using HTTPS but with weak cipher suites still negotiable
## Section 6 — Practical Takeaways
How to check the TLS configuration of any website using SSL Labs at ssllabs.com/ssltest
What a security practitioner checks beyond whether HTTPS is present
What the padlock actually tells you and the one question you should ask that it cannot answer
