# The Tunnel Is Safe, Not The Destination: HTTPS Demystified 

![cover picture](cover1.png)

## The Illusion of Safety

**Connection is secure. A padlock. The "S" in HTTPS. For decades, these have been signals we trust when browsing the web. I trusted them too, but I never stopped to ask what was actually happening beneath that padlock. One afternoon, staring at a padlock icon on my browser, a question hit me: IS HTTPS REALLY SAFE?**

I went down the rabbit hole. What I found shocked me.

It turns out I wasn't alone in misunderstanding what the padlock meant. When PhishLabs surveyed internet users, 80% of respondents believed the padlock indicated that a website was legitimate, safe, or secure. Google's own research found that 74% of participants said the icon meant that the website was secure, while more than half believed it meant they could safely enter their information. The CA Security Council found another side of the problem: only 3% of users said they would enter credit card information on a website without a padlock.

These numbers reveal something important about how we interpret the padlock. We don't simply see it as a technical indicator of an encrypted connection. We often interpret it as a broader signal of safety and trust.

But the padlock is not a promise about where you are going. **It is only a promise about how you get there**.

After weeks of research, one thing became clear: the tunnel is safe, but the destination isn't.

To understand why, we need to start with the layer that runs this whole thing: **HTTP**.

## The Open Road: Traveling in Broad Daylight with HTTP

**Hypertext Transfer Protocol (HTTP)** is a foundational rule system that governs how information is exchanged between a client and a server on the internet. It defines how data is formatted and transmitted, and how web browsers and servers respond to various commands.
HTTP is the core language of the World Wide Web. With HTTP, a client, typically a web browser, requests a resource from a server, and the server responds with a status code and the requested resource. This is what we call the request-response system.
Although HTTP forms the foundation of the World Wide Web, transferring data in plaintext poses a significant security risk. With the right tool and technical know-how, anyone on the same network could intercept data in transit. This is called a Man-In-The-Middle(MITM) attack. 
Think of it like delivering an unsealed letter through a delivery agency to a friend. The delivery man can see the contents of the letter and also tamper with it before it gets to your friend. 
This is exactly how a MITM happens over HTTP.
To prove this, I conducted a lab using testfire.net as our case study.

URL: http://testfire.net

![Wireshark test](HTTP_test.png)

> From the capture, we can observe the complete HTTP login transaction. The browser first requests the login page (GET /login.jsp), then submits the login form through a POST /doLogin request. Because HTTP transmits data without encryption, Wireshark is able to decode the request body and display the submitted form fields in plaintext. The username (ArticleUser) and password (InsecurePassword) are clearly visible in the packet details, demonstrating that sensitive information can be exposed to anyone capable of intercepting the network traffic.

As the World Wide Web grew, this vulnerability was exploited by many, and so the need for a secure type of HTTP was necessitated. **HTTPS** was the solution to this.

## Building the Tunnel: Enter HTTPS and the TLS Handshake
### What Is HTTPS?

Hypertext Transfer Protocol Secure(HTTPS) is simply HTTP over a security layer. This security layer is called the **Transport Layer Security(TLS)**: a security or cryptographic protocol that encrypts data sent over the internet to keep it private and safe. During data transfer over HTTPS, there's a key share that grants data privacy by encrypting it. This helps improve Confidentiality and integrity over the internet. In other words, HTTPS is HTTP over TLS. 

To understand this better, a lab was conducted over HTTPS using testfire.net as a case study and the same login credentials.

URL: https://testfire.net

![Wireshark test](HTTPS_test.png)

> The capture above shows the same login activity performed over HTTPS. Unlike the previous HTTP capture, Wireshark is unable to reveal the contents of the communication. Instead of displaying HTTP requests such as GET and POST, the packets appear as TLS Application Data, indicating that the application-layer data has been encrypted before transmission. The packet payload consists only of encrypted bytes, making the username, password, and other sensitive information unreadable to anyone intercepting the traffic. Although an attacker can still observe metadata such as the communicating IP addresses, the use of TLS prevents them from viewing or modifying the data exchanged between the client and the server.

The difference between HTTP and HTTPS is now visible. In the HTTP capture, the login credentials were exposed because data is transferred in plaintext. In the HTTPS capture, the same type of communication appears only as encrypted TLS application data, preventing anyone intercepting the traffic from reading the contents.

Today's web primarily uses **TLS 1.3**, the latest and most secure version of the protocol. However, web encryption did not begin with TLS. It began with its predecessor, the **Secure Sockets Layer (SSL)**.

Developed by Netscape in 1994, **SSL 1.0** was never released publicly because internal testing uncovered serious security and design flaws. **SSL 2.0**, released in 1995, became the first public version, but it was later found to contain multiple vulnerabilities, including weak cryptographic protections and susceptibility to several attacks. Netscape responded by releasing **SSL 3.0** in 1996, which significantly improved the protocol. Nevertheless, researchers continued to discover weaknesses as cryptographic research advanced and the web evolved.

Recognizing the need for a stronger, vendor-neutral security standard, the **Internet Engineering Task Force (IETF)** developed **Transport Layer Security (TLS)** as the successor to SSL. Although TLS was based on SSL 3.0, it introduced stronger cryptography, improved protocol design, and an open standard that could evolve through community review rather than relying on a single company's implementation.

Over the years, TLS has continued to evolve. **TLS 1.0, 1.1**, and **1.2** gradually addressed newly discovered attacks and strengthened encryption. Today, **TLS 1.3** is the recommended standard, having removed obsolete algorithms, simplified the handshake process, and improved both security and performance.

However, before any encrypted data is exchanged, the client and server must first establish trust and agree on how they will communicate securely. This process is known as the **TLS handshake**.
#### What is TLS handshake?
**TLS handshake** is a communication process that initiates a secure connection between a client and a server. This handshake is also responsible for key creation. Unlike SSL and earlier TLS versions, TLS 1.3 typically establishes a secure connection in One Round Trip Time (1-RTT), meaning the client can send its initial handshake message and receive the server's response in a single network round trip before encrypted application data can begin. This reduces connection latency while improving security.

#### How the TLS handshake occurs
During a TLS 1.3 handshake, the client begins by sending a **ClientHello**, a message containing information about the cryptographic capabilities it supports:
- **Supported versions**: The TLS protocol versions supported by the client, allowing the server to select a mutually supported version.
- **Cipher suites**: The cryptographic suites the client supports for protecting the connection. In TLS 1.3, these specify the symmetric encryption and authentication algorithms, such as **AES-128-GCM**, **AES-256-GCM**, and **ChaCha20-Poly1305**.
- **Key share**: The client sends its public key share for one or more supported key-exchange groups, commonly using **Elliptic Curve Diffie-Hellman Ephemeral (ECDHE)**. The corresponding private key never leaves the client.

ECDHE allows the client and server to independently derive the same shared secret without transmitting that secret across the network. An eavesdropper can observe the public information exchanged during the process, but recovering the private values from that information would require solving the underlying **elliptic-curve discrete logarithm problem**, which is computationally infeasible with currently known classical methods.

The server then responds with a **ServerHello**, containing:

- Selected protocol version: The TLS version selected from those supported by the client, typically TLS 1.3.
- Selected cipher suite: The cryptographic suite selected from the client's offered options.
- Server key share: The server's public key share for the selected key-exchange group.

Using their own private key and the other party's public key, both sides can independently arrive at the same shared secret. **The secret itself is never transmitted over the network**.

That shared secret then enters the TLS 1.3 key schedule, which derives the symmetric traffic keys used to protect subsequent communication. TLS 1.3 uses an [Authenticated Encryption with Associated Data(AEAD) symmetric encryption](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data) cipher, such as AES-GCM or ChaCha20-Poly1305, to provide both confidentiality and integrity for the encrypted data.

After ServerHello, the server sends additional handshake messages that authenticate itself to the client and establish the parameters needed to complete the handshake. These include:
- Certificate: Sends the server's digital certificate to prove its identity. A digital certificate is an electronic file that proves the identity of a user, computer, or website. It is issued by a Certificate Authority(CA): a trusted group that signs the file to ensure its legitimacy
- CertificateVerify: A digital signature proving the server owns the private key linked to that certificate.
- Finished: A cryptographic verification that confirms the handshake messages exchanged so far have not been altered and that both sides possess the necessary handshake secrets.

The client then responds with a client-to-server message, which is a final confirmation saying:
- The client verifies the server’s certificate and signature.
- The client derives the same shared secret using its private key and the server's public key share.
- The client sends its own Finished message, providing final cryptographic confirmation that it has successfully completed the handshake.

After a successful TLS handshake and verification of the server's certificate by the browser, the browser can indicate that the connection is secure. 
This is where the problem begins.
We instinctively associate the padlock with safety. But the padlock is not a declaration that the website is safe, legitimate, or trustworthy. It tells us something much narrower: the connection to the authenticated domain is protected by HTTPS.

It tells us that the **journey is protected**.

It says nothing about the **destination**.

A website can have a valid TLS certificate, establish a perfectly secure encrypted connection, and still be designed to steal your password, deceive you, sell fraudulent products, distribute malware, or manipulate you into giving away sensitive information.

That is the central idea of this article:

> **The Tunnel Is Safe, But the Destination Isn't**.

## The Limits of the Walls: What the Tunnel Cannot Protect
The cryptographic handshake ensures that your data is perfectly sealed while in transit. However, a secure pipe does not guarantee a safe destination. The tunnel only protects the journey; it cannot validate the intent or integrity of what lies at either end. 
- **HTTPS does not protect us from phishing and scams**. Unlike the early and mid 2000s where HTTPS signaled more trust than it does now due to the cost of setup, verification process, and technical setup then. Today, a malicious site, like a phishing site or fake bank site, with the help of free automated Certificate Authorities(CAs) like Let's Encrypt and ZeroSSL, can gain a valid digital certificate for its malicious purposes at no cost, with just proof of domain control as the requirement for verification. This is termed domain validation. HTTPS doesn't guarantee who runs the site beyond the domain name. It only encrypts your data and proves the site controls that web address. That's why a report by [NOS](https://nos.nl/artikel/2234720-duizenden-sites-met-groen-slotje-onveilig), after an examination of 1,000s of blacklisted sites, found out that 4,300 of them had a valid certificate. Though we see the padlock or connection is secure, it says nothing about the destination. This is not because HTTPS is broken; rather, we trust the signals without understanding what it means. 

- **HTTPS does not protect data from attacks at its destination**. Hypertext **Transfer Protocol** Secure, as the name suggests, is a **transfer protocol**. It protects data while it is being transferred between the client and server, not what happens to that data after it reaches the server. Once the encrypted data reaches the server, TLS decrypts it so the application can process it. The data may then be stored in databases, files, logs, sessions, or other parts of the server's infrastructure. If the application or server is compromised, an attacker may gain access to that data. This is also why HTTPS does not prevent attacks such as **SQL injection** or **Cross-Site Scripting (XSS)**. SQL injection targets how an application processes database queries, while XSS targets how an application handles and renders untrusted input. Neither attack requires HTTPS itself to be broken. HTTPS can successfully secure the journey while the application at the destination remains vulnerable. **The tunnel is secure, but the destination isn't**.

In short, HTTPS is designed to prevent unauthorized parties from reading or modifying your data while it is travelling through the tunnel. But what happens when an attacker forces you out of the tunnel entirely, taps into it with permission, or exploits a weakness in the very mechanisms keeping it secure?

## Sabotaging the Journey: How the Tunnel is Intercepted, Stripped, and Cracked
Up to this point, we have assumed that a secure TLS connection successfully connects the user to the server. In reality, the journey between client and destination is rarely a straight, untouched path. Attackers, network administrators, and even outdated cryptographic standards can interfere with the connection. Sometimes the secure tunnel is secretly dismantled before it can even form; other times, it is monitored by a third party with permission; and occasionally, the very mathematical bricks used to build the tunnel crumble under modern analysis. To understand the illusion of web security, we must look at the specific ways this safe tunnel is manipulated, bypassed, and broken.

### Collapsing the Tunnel: Downgrade Attacks and Trust Failures
More often than not, when visiting websites, we tend to ignore the protocol when typing out the web address in the address bar. We mostly use the site's name and its Top-Level Domain (TLD). 
> Eg. `example.com` or `www.example.com` instead of `https://example.com`

In such cases, an attacker can easily perform an MITM technique that downgrades a secure HTTPS connection to an unencrypted HTTP connection. This is termed **SSL stripping.**

During SSL stripping, an attacker uses MITM techniques, such as a fake Wi-Fi hotspot or [ARP spoofing](https://en.wikipedia.org/wiki/ARP_spoofing), to intercept network traffic. When a user tries to visit a secure site, the browser sends the initial request over HTTP before getting redirected to HTTPS. The attacker blocks this redirect upgrade. The attacker maintains a secure HTTPS connection with the actual website server, but talks to the user's browser over plain, unencrypted HTTP. The user sees a normal page (and sometimes even a fake lock icon generated by the tool), unaware that all typed credentials are exposed to the attacker.

#### The Step-by-Step Breakdown
1. **The Normal Flow (No Attacker)**
   - You type bank.com into your browser.
   - Your browser sends a plain request: `http://bank.com`.
   - The bank's server receives it and replies: "Hey, use our secure site instead!" It sends a 301 Redirect to `https://bank.com`.Your browser establishes a secure, encrypted HTTPS connection.
2. **The SSL Stripping Flow (With Attacker)**
   - You type bank.com. Your browser sends the initial plain request: `http://bank.com`.
   - The attacker intercepts this initial request and forwards it to the bank's server.
   - The bank's server replies to the attacker with the secure 301 Redirect (`https://bank.com`).
   - The Strip: The attacker establishes a secure HTTPS connection with the bank on your behalf, but strips the "S" out of the response they send back to you.
   - The attacker sends you plain `http://bank.com`. Your browser thinks the website just doesn't support HTTPS, so it loads the page without encryption.

This is exactly what Moxie Marlinspike, a security researcher, introduced in his February 2009 demonstration titled **New Tricks for Defeating SSL in Practice**  at the Black Hat DC conference. He introduced SSL stripping, a man-in-the-middle technique and released his tool sslstrip, showing how web traffic could be silently downgraded from HTTPS to HTTP.
This was feasible because, during the time of its introduction, browsers could not differentiate between a website that lacked HTTPS entirely and a malicious man-in-the-middle actively stripping an encrypted link away. To solve this critical vulnerability exposed by Marlinspike's attack, where browsers blindly trusted initial unencrypted connections, the security community developed **HTTP Strict Transport Security (HSTS)**

**HTTP Strict Transport Security(HSTS)** is a security policy that tells web browsers to load and communicate with websites strictly over HTTPS and block insecure HTTP. Once the browser knows that a domain is an HSTS domain, it upgrades HTTP URLs to HTTPS before making the connection and refuses insecure HTTP connections.

 On the modern web, over 95% of web traffic is encrypted by default, and browsers feature built-in **HTTPS-First** modes alongside the **HSTS Preload List**. However, the attack still succeeds in narrow, niche scenarios where operational gaps persist. Examples of where SSL will still succeed are:
 - **Misconfigured or Incomplete HSTS**: Smaller websites, corporate internal web apps, or IoT admin panels that redirect to HTTPS via a loose script but lack a strict max-age HSTS header—can still leak an initial plaintext request.
 - **Local Network Compromise**: On unsecured public or corporate Wi-Fi spots, an attacker running ARP poisoning or rogue access points can still trick legacy clients, unpatched software, or poorly configured mobile apps into crossing an unencrypted bridge

The history of HTTPS is not just a story of encryption working; it is also a story of researchers, attackers, and even compromised authorities finding ways around it. SSL stripping, together with HSTS, is one of those stories. It brings to light the measures security researchers and engineers take to create a safe tunnel when attackers try to downgrade or prevent the tunnel from being established. But what happens when the tunnel is safely built, yet your web browser is tricked into trusting the wrong server?

### When Trust Breaks: The DigiNotar Incident
In 2011, this wasn't merely a theoretical possibility. A Certificate Authority trusted by major browsers was compromised, and fraudulent certificates were issued for major websites, including Google. The incident became known as the **DigiNotar breach**.
#### What is DigiNotar
DigiNotar was a Dutch Certificate Authority, one of the trusted organizations responsible for issuing the digital certificates that browsers use to verify a server's identity. When a browser encounters a certificate, it checks whether a trusted CA signed it. If yes, the padlock appears. If no, the browser throws a warning. DigiNotar was one of those trusted signers, recognized by all major browsers including Chrome, Firefox, and Internet Explorer.

#### How the Breach Unfolded

In June 2011, an attacker compromised DigiNotar's internal systems. The attacker did not need to break TLS or defeat encryption. They went around all of it by going straight to the source: the CA itself. Once inside, they issued over 500 fraudulent certificates, including a wildcard certificate for `.google.com`. A wildcard certificate covers every subdomain of a domain, meaning the attacker could impersonate mail.google.com, accounts.google.com, or any other Google service.

With a fraudulent but technically valid certificate issued by a trusted CA, the attacker could perform a MITM attack that browsers would not flag. The padlock appeared. The connection looked secure. The certificate chain checked out. But the server on the other end was not Google. The breach primarily targeted Iranian internet users, with hundreds of thousands of Gmail accounts exposed to traffic surveillance through this attack.

#### The Fallout and What Changed

When the breach was publicly disclosed in August 2011, browser vendors responded by revoking trust in DigiNotar entirely. Every certificate DigiNotar had ever issued became untrusted overnight. DigiNotar filed for bankruptcy within weeks.

But the deeper problem the breach exposed was structural. There was no public, auditable record of what certificates any CA had issued. An attacker could compromise a CA, issue fraudulent certificates, and nobody would know until someone happened to notice something suspicious. This directly led to the creation of Certificate Transparency (CT), a system that requires every publicly trusted CA to log every certificate they issue to a public, append-only ledger. Browsers now require that certificates appear in a CT log before trusting them. If a CA issues a fraudulent certificate, it must be logged publicly, making it detectable.

DigiNotar showed that the padlock is only as trustworthy as the CA that issued the certificate behind it. Break the CA, and you break the padlock without touching the encryption itself.

SSL stripping tries to prevent the tunnel from forming. DigiNotar showed that even a perfectly formed tunnel can lead to the wrong destination if the authority that vouched for it cannot be trusted. The tunnel was safe. The certificate authority was not.

### The Transparent Tunnel: Middleboxes and the Mirage of Privacy

From the beginning, we've established that HTTPS builds a secure connection to protect data in transit. But what happens when this tunnel is intruded upon by third parties we have given our full consent to, sometimes without fully understanding what they can see? Well, this is what corporate networks, firewalls, antivirus software, and other middleboxes can do.

Most often, in the name of security, we connect to networks and install software that can inspect our HTTPS traffic, and this is only the beginning of the problem. These third-party systems can act as an MITM between the client and the server. Instead of establishing one end-to-end secure connection between the web browser and the destination server, the middlebox terminates the TLS connection from the browser and establishes a separate TLS connection with the server. In other words, it builds one tunnel from the browser to itself and another from itself to the server.

When this happens, encrypted messages from the browser are decrypted by the middlebox, inspected, and then encrypted again before being sent to the destination. **The padlock is not necessarily missing, but the connection is no longer end-to-end** between the browser and the destination. The middlebox can see the plaintext because the browser has been configured to trust a certificate authority controlled by the organization or software performing the interception. The browser therefore sees the middlebox's certificate as trusted rather than treating it as an untrusted attacker.

In a research paper titled [The Security Impact of HTTPS Interceptions](https://jhalderm.com/pub/papers/interception-ndss17.pdf), researchers found that HTTPS interception by middleboxes breaks end-to-end encryption, allowing third parties to decrypt and inspect traffic, which degrades security in 32% to 97% of cases. These systems introduce significant risks, including cryptographic downgrading to weaker ciphers, failure to validate server certificates, and potential exposure of sensitive data


### Cracks in the Architecture (Tunnel): When the HTTPS Breaks Itself
From the beginning of the article, we've looked at attacks that do not break the tunnel itself. Aside from the question, **"Is HTTPS really safe?"** that led me to these findings, one question also remained prevalent throughout my research: **Has HTTPS (the tunnel) itself ever been broken?**
Though there might not be a simple yes-or-no answer to this question, one thing remained clear through my findings: ***The tunnel is only as strong as the mechanisms behind it***. And this is exactly what the POODLE and BEAST attacks are about.

#### What is the Beast attack?
The **BEAST (Browser Exploit Against SSL/TLS)** is an attack targeting a vulnerability in the way TLS 1.0 uses block ciphers with **[Cipher Block Chaining (CBC)](https://www.hexnode.com/blogs/explained/what-is-cipher-block-chaining/)**. The vulnerability was known theoretically earlier, but the attack was practically demonstrated against HTTPS in 2011. BEAST exploited the predictable way initialization vectors (IVs) were used between TLS 1.0 records. By controlling or influencing part of the data sent by the browser and observing the resulting encrypted blocks, an attacker could make repeated guesses and gradually recover sensitive information, such as authentication cookies, byte by byte.

The important thing to understand is that BEAST did not break the underlying encryption algorithm. Instead, it exploited a weakness in how the encryption mechanism was implemented within TLS 1.0. The tunnel was safe, but the mechanism behind it caused a crack.

#### What is the POODLE attack?

The **POODLE (Padding Oracle On Downgraded Legacy Encryption)** attack was discovered in 2014 and targeted a weakness in the way SSL 3.0 handled padding in **Cipher Block Chaining (CBC)** encryption. Unlike BEAST, which exploited predictable initialization vectors in TLS 1.0, POODLE exploited the way SSL 3.0 failed to properly verify the contents of padding bytes.

An attacker positioned between the browser and server could manipulate encrypted traffic and observe how the server responded. By repeating this process, the attacker could gradually recover sensitive information, such as authentication cookies.

What made POODLE particularly dangerous was not only the weakness in SSL 3.0, but the fact that browsers and servers could fall back to SSL 3.0 when a connection using a newer version of TLS failed. An attacker could deliberately interfere with the connection and force this downgrade to the vulnerable protocol. The attacker did not need to break the encryption directly; they manipulated the connection until the browser and server used an older protocol with a known weakness.

*POODLE, like BEAST, did not prove that encryption is useless. It showed that the security of the tunnel depends on the mechanisms used to build and maintain it. BEAST exploited a weakness in how CBC was used in TLS 1.0, while POODLE exploited a weakness in SSL 3.0's handling of CBC padding and the ability to fall back to that outdated protocol. The tunnel is only as strong as the mechanisms behind it.

The lessons from BEAST and POODLE are not limited to the history of HTTPS. They reveal a problem that still matters today: having HTTPS enabled does not automatically mean that HTTPS has been configured securely. A website can display the padlock while still supporting deprecated protocols, using weak cryptographic configurations, or mishandling the data once it reaches the server.

## Leaving the Back Door Wide Open: Common Configuration Blunders
Leaving the Back Door Wide Open: Common Configuration Blunders

When talking about the tunnel, organizations like the IETF can try their best to make sure the tunnel is safe. This includes deprecating older versions of TLS and SSL, introducing stronger cryptographic protocols, and establishing standards for secure communication. But all of this can amount to nothing when the people responsible for deploying and maintaining these systems get it wrong.

These key players include web developers, system administrators, and other people responsible for configuring web servers and applications. They can make practices that do not conform to modern security standards, affecting both the tunnel and the destination. These practices can leave the back door wide open. Some of these practices are:
- **Running HTTPS but storing passwords in plaintext**. While HTTPS successfully encrypts the password as it travels from the user's browser to the server, the security completely breaks down once it arrives. Storing passwords in plaintext in a database, configuration file, or internal log is a severe security vulnerability. This is because once data reaches the server, it gets unencrypted. In this case, when an attacker breaches the database, they get clean usernames and passwords. This also causes credential stuffing, insider threats and compliance violations. Regardless of the safety the tunnel gives, credentials are never safe. In this case, the protocols put in place by organizations like IETF were never the but practices by the key players. ***The tunnel was safe, but the destination wasn't.***
- **Running HTTPS with deprecated versions of cryptographic protocols enabled**. Though TLS 1.3 is the current standard for web encryption, some web developers, system administrators, and others still deploy services with deprecated versions such as TLS 1.0 or TLS 1.1 enabled. We might have the assurance of security, which is the padlock, but these deprecated protocols create a severe security gap and break compliance. This is because these protocols enable downgrade attacks. An attacker can intercept the handshake and force the connection to use TLS 1.0 or TLS 1.1, bypassing the security of TLS 1.3. This eventually leads to attacks like BEAST and POODLE, which exploit the vulnerable cryptography used by these protocols. Our assurance of safety will still be visible, but our journey won't be smooth. **The tunnel was initially secured but was not configure well**.
- **Running HTTPS on login pages but HTTPS on other pages**. While securing the login page encrypts credentials during transmission, the security completely breaks down once the user logs in. Redirecting users back to unencrypted HTTP pages means their session tokens or authentication cookies travel in plaintext. In this case, an attacker on a shared network can easily sniff the session cookie, clone it, and hijack the user's logged-in session. This also exposes the site to active mixed content blocking by browsers and insecure form action exploits. Regardless of the safety of the initial login, the user's continuous session is never safe. In this case, the protocols are selectively applied instead of being enforced site-wide. **The tunnel door was locked, but the rest of the journey was left wide open**. 
- **Running HTTPS but with a self-signed certificate that browsers flag as untrusted.**
While a self-signed certificate successfully encrypts the data passing between the user and the server, the security completely breaks down regarding identity verification. Browsers cannot verify the authenticity of a self-signed certificate, triggering severe, full-screen security warnings for visitors. In this case, when users are trained to click through these warnings, they become highly vulnerable to Man-in-the-Middle (MitM) attacks. This also destroys user trust and completely tanks site traffic, as modern browsers actively discourage users from proceeding. Regardless of the cryptographic strength of the encryption, the connection is never truly safe from interception. In this case, the implementation lacks the trusted foundation required by modern web standards. **The tunnel was strongly built, but nobody trusted where it led.**
- **Running HTTPS but with HTTP fallback enabled and no HSTS.**
While configuring an SSL/TLS certificate allows your server to handle secure traffic, the security completely breaks down if you leave the unencrypted fallback open. Without implementing HTTP Strict Transport Security (HSTS), the browser will default to a standard HTTP connection unless a user explicitly types https:// in the address bar. In this case, an attacker can exploit this window of vulnerability through a protocol downgrade attack (like SSL Stripping). By intercepting the initial unencrypted request, they can force the user to stay on a plain text version of the site while proxying the secure connection back to the server. This also leaves users completely blind to the fact that their data is being intercepted, as the browser padlock simply disappears. Regardless of your server supporting high-level encryption, users are never safe if they can be silently downgraded. In this case, the safety of the connection is left entirely up to chance. **The tunnel was available, but there was no signpost forcing anyone to use it.**
* **Using HTTPS but with weak cipher suites still negotiable.**
While having a valid SSL/TLS certificate establishes an encrypted connection, the security completely breaks down if the server agrees to use weak encryption algorithms. If your server is configured to negotiate outdated cipher suites—like those using 3DES, RC4, or weak Diffie-Hellman parameters—it opens the door to severe cryptographic exploits. In this case, an attacker can intercept the initial TLS handshake and force the server and browser to agree on the weakest mutually supported cipher. This enables advanced Man-in-the-Middle (MitM) attacks like SWEET32, allowing the attacker to decrypt sensitive traffic and session tokens in transit. This also means that despite seeing a green padlock or secure status in the browser, the underlying encryption is practically useless against modern computing power. Regardless of your certificate being valid, the connection is never truly secure if the lock can be easily picked. In this case, the illusion of security is maintained while the mathematical foundation is broken. **The tunnel was securely built, but the lock on the gate was rusted and weak.**

We have seen that HTTPS can be weakened by outdated protocols, poor configurations, broken trust, and insecure practices at the destination. This brings us back to the symbol that started this journey: the padlock. If the padlock does not tell us everything about the security of a website, then what should we actually look for? How do we look beyond the symbol and examine the tunnel itself?

## Beyond the Padlock: How to Audit the Journey and Ask the Right Questions
Throughout this article, we have seen that the padlock is only one small part of the security story. We have looked at how HTTPS establishes the tunnel, how certificates establish trust, how attackers can interfere with the journey, and how poor configurations can weaken protections that are already available. So, how do we know what is actually happening behind that padlock?

**The answer is to look beyond the symbol**. A security practitioner does not simply ask whether a website uses HTTPS. They examine which TLS versions it supports, which cryptographic mechanisms it uses, whether its certificate is valid and properly trusted, whether HSTS is enabled, and whether the overall configuration follows modern security standards.

The good news is that you do not need to be a cryptographer to perform some of these checks. Tools such as SSL Labs' SSL Server Test can expose many of the details hidden behind the simple "Connection is secure" message in your browser.

### How to check the TLS configuration of any website using SSL Labs
Go to [SSL Labs](https://www.ssllabs.com/ssltest/) and enter the domain name of the website you want to examine. For example:
> `example.com`

After starting the test, SSL Labs performs an extensive analysis of the server's TLS configuration and provides an overall grade.
Below is a table containing a list of SSL Labs result grade and what they mean.

| SSL Labs result                  | What it means                                                 | What you do as a visitor                                                                                                              |
| -------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **A / A+**                       | Strong, modern TLS configuration                              | No TLS-related concern from the report                                                                                                |
| **B**                            | Some configuration weaknesses or outdated settings            | Be aware; the site may still be legitimate and usable                                                                                 |
| **C**                            | Significant weaknesses                                        | Exercise caution, especially before entering sensitive information                                                                    |
| **D / E / F**                    | Serious TLS/configuration problems                            | Avoid entering passwords, payment information, or other sensitive data; for a site handling sensitive information, use an alternative |
| **Certificate/identity failure** | The browser cannot properly establish trusted server identity | **Do not proceed through the warning** unless you independently understand and trust the environment                                  |

These grades are very important and matter because they tell us why the website received those grades. 
The difference between the padlock and this report is that the padlock tell us the **connection is secure**, but SSL Labs tells us **what makes this connection secure, and how well has it been configured?** 

### What does a security practitioner check beyond HTTPS?

A security practitioner does not stop after seeing `https://` in the address bar. They look beyond the existence of HTTPS and examine the mechanisms behind it.

They ask:
- Which TLS versions are supported?
- Which cipher suites and cryptographic mechanisms are being used?
- Is the certificate valid and does it cover the correct domain?
- Is the certificate chain trusted?
- Is HSTS enabled?
- Are obsolete protocols and weak cryptographic mechanisms disabled?
- How is the server establishing session keys?
- Are security-related browser controls such as secure cookie attributes properly configured?
- What happens to the user's data after it reaches the server?

The last question takes us beyond TLS itself. HTTPS can successfully encrypt a password while it travels from the browser to the server, but it cannot prevent the application from storing that password in plaintext. It can protect the journey while SQL injection, XSS, broken access control, or a compromised server threatens the destination.

This is why the presence of HTTPS should be treated as the **beginning of a security assessment, not the end of one**.

### What does the padlock actually tell you?

After everything we have uncovered, we can finally answer the question that started this journey: **What does the padlock actually mean?**

The padlock means that your browser has successfully established a **TLS-protected connection** to the domain you are visiting and that the certificate presented by the server passed the browser's relevant trust and validation checks. The data travelling through that connection is encrypted, helping prevent someone who merely intercepts the traffic from reading or modifying it.

But the padlock does **not** mean that the website itself is safe.

It does not tell you that:

* the website is legitimate rather than a phishing site;
* the organization behind the website is trustworthy;
* the application contains no vulnerabilities;
* the server has not been compromised;
* your data will be stored securely;
* the website is free from SQL injection or XSS;
* your connection is not being inspected by an authorized middlebox;
* the website is using the strongest possible TLS configuration.

This brings us back to the distinction that has followed us throughout this article:

> **HTTPS can secure the journey without securing the destination.**

A certificate can establish that the server controls the domain for which the certificate was issued. TLS can encrypt the communication between your browser and that server. But neither one can tell you what the server will do with your data after it arrives.

### The One Question the Padlock Cannot Answer

The padlock can tell you:

> **"Is my connection to this domain protected by TLS?"**

But it cannot answer the question that matters beyond the tunnel:

> **"Can I trust the destination?"**

That is the limitation we often overlook.

A phishing website can have HTTPS. A vulnerable application can have HTTPS. A compromised server can have HTTPS. A website storing your password insecurely can have HTTPS.

The padlock was never a guarantee that the destination was safe.

**It was only ever a guarantee about the tunnel.**

And that is why:

> **The tunnel is safe, but the destination isn't.**
