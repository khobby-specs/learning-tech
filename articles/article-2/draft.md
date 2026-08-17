
**Skeleton**

# The Tunnel Is Safe, Not The Destination: HTTPS Demystified 

![cover picture](cover1.png)

## The Illusion of Safety

Connection is secure. A padlock. The **'S'** in HTTPS. For decades, these have been the signals we trust when browsing the web. 
I trusted them too, but I never stopped to ask what was actually happening beneath that padlock. 
One afternoon, staring at a padlock icon on my browser, a question hit me: IS HTTPS REALLY SAFE? 
I went down the rabbit hole. What I found shocked me. The padlock is not a promise about where you are going. It is only a promise about how you get there. After weeks of research, one thing became clear: the tunnel is safe, but the destination isn't. To understand why, we need to start with the layer that runs this whole thing: **HTTP**.

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

The current version of the Transport Layer Security(TLS) running the web is version 1.3(v1.3). Initially, the Secure Sockets Layer(SSL) was the protocol powering web security. Created in 1994 by Netscape, SSL 1.0  was never released to the public due to the severe security and design flaws revealed by internal testing. SSL 2.0 was released to the public in 1995 and was succeeded by SSL 3.0 in 1996. SSL used weak Message Authentication Codes(MAC) and Algorithms like MD5, which could be exploited easily. Also, as the web grew, the industry needed an open vendor protocol to enhance web security rather than a sole proprietary Netscape product; hence, the Internet Engineering Task Force(IETF), an international open standard organization, introduced TLS to standardize internet encryption and fix critical cryptographic vulnerabilities inherent to Netscape's proprietary code.

For TLS to work effectively, thus protecting data in transit, the client and server go through a process to establish trust and secure communication methods before encrypted data is transferred. This process is known as **TLS Handshake**

TLS handshake is a communication process that initiates a secure connection between a client and a server. This handshake is also responsible for key creation. Unlike SSL and earlier versions of TLS, TLS 1.3 uses 1 Round Trip Time(1RTT) to establish a secure connection between the client and server. 

### How the TLS handshake occurs
During a TLS handshake, the client sends a **ClientHello**, which is a single message containing:
- Supported versions: the client sends its supported protocol version
- Cipher suites: a list of all the encryption algorithms
- Key shares: the client shares its secret key using an Elliptic Curve Diffie-Hellman(ECDHE): a modern protocol that lets two people make a secret code over a public network. The secret code is never sent out on the network, but both the client and the sever ends up with the same secret. This protocol works together with the [Authenticated Encryption with Associated Data(AEAD) symmetric encryption](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data) like AES-GCM to generate keys. With the help of the discrete logarithm problem, the secret can never be accessed via an attacker sniffing packets.

The server, after processing the client's request, responds with a **ServerHello**: a single message which contains:
- Protocol version: Confirms TLS 1.3 protocol usage
- Cipher suite: the specific encryption algorithm selected by the server from the list the client provided
- Server key share: Sends its own half of the cryptographic key material.

After sending the server hello, the server sends a server-to-client message that proves identity in one flight. The message contains:
- Certificate: Sends the server's digital certificate to prove its identity. A digital certificate is an electronic file that proves the identity of a user, computer, or website. It is issued by a Certificate Authority(CA): a trusted group that signs the file to ensure its legitimacy
- CertificateVerify: A digital signature proving the server owns the private key linked to that certificate.
- Finished: A cryptographic check verifying that a third party did not alter the handshake messages.

The client then responds with a client-to-server message, which is a final confirmation saying:
- The client verifies the server’s certificate and signature.
- The client generates the same shared secret key using the two key shares.
- The client sends its own Finished message, encrypted with the new keys.

After a successful TLS handshake, that is when the client displays the padlock. This is where all problems begin, because we instinctively associate safety with the padlock. The displayed padlock tells you that the server has been verified and also that your data in transit is protected, and nothing about the site, what it does, and others. All it screams is safety about the journey, not the destination. This is what I term as: ***The Tunnel is Safe, but The Destination Isn't***

### The Limits of the Walls: What the Tunnel Cannot Protect
The cryptographic handshake ensures that your data is perfectly sealed while in transit. However, a secure pipe does not guarantee a safe destination. The tunnel only protects the journey; it cannot validate the intent or integrity of what lies at either end. 
- HTTPS does not protect us from phishing and scams. Unlike the early and mid 2000s where HTTPS signaled more trust than it does now due to the cost of setup, verification process, and technical setup then. Today, a malicious site, like a phishing site or fake bank site, with the help of free automated Certificate Authorities(CAs) like Let's Encrypt and ZeroSSL, can gain a valid digital certificate for its malicious purposes at no cost, with just proof of domain control as the requirement for verification. This is termed domain validation. HTTPS doesn't guarantee who runs the site beyond the domain name. It only encrypts your data and proves the site controls that web address. That's why a report by [NOS](https://nos.nl/artikel/2234720-duizenden-sites-met-groen-slotje-onveilig), after an examination of 1,000s of blacklisted site found out that 4,300 of them had a valid certificate. Though we see the padlock or connection is secure, it says nothing about the destination. This is not because HTTPS is broken; rather, we trust the signals without understanding what it means. 

- Hypertext **Transfer Protocol** Secure, like the name says: a **transfer protocol**, is a protocol that protects data in transit, not data at its destination. As soon as data reaches the server, HTTPS no longer protects it. The data gets decrypted and stored somewhere in the server's database, logs, or files. When the server gets compromised or attacked, all your data in its database is accessible to the attacker. This is also why HTTPS does not prevent attacks such as SQL injection or Cross-Site Scripting (XSS). SQL injection targets how an application processes database queries, while XSS targets how an application handles and renders untrusted input. Neither attack requires HTTPS itself to be broken. HTTPS can successfully secure the journey while the application at the destination remains vulnerable. The tunnel is secure, but the destination isn't.

In short, HTTPS guarantees that nobody can look inside the pipe while your data is moving. But what happens when an attacker forces you out of the tunnel entirely, taps into it with permission, or cracks the very math keeping it shut?

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
The BEAST (Browser Exploit Against SSL/TLS) is an attack targeting a vulnerability in the way TLS 1.0 uses block ciphers with Cipher Block Chaining (CBC). The vulnerability was known theoretically earlier, but the attack was practically demonstrated against HTTPS in 2011. BEAST exploited the predictable way initialization vectors (IVs) were used between TLS 1.0 records. By controlling or influencing part of the data sent by the browser and observing the resulting encrypted blocks, an attacker could make repeated guesses and gradually recover sensitive information, such as authentication cookies, byte by byte.

The important thing to understand is that BEAST did not break the underlying encryption algorithm. Instead, it exploited a weakness in how the encryption mechanism was implemented within TLS 1.0. The tunnel was safe, but the mechanism behind it caused a crack.

#### What is the POODLE attack
The POODLE (Padding Oracle On Downgraded Legacy Encryption) attack was discovered in 2014 and targeted a weakness in the way SSL 3.0 handled padding in Cipher Block Chaining (CBC) encryption. Unlike BEAST, which exploited predictable initialization vectors in TLS 1.0, POODLE exploited the way SSL 3.0 failed to properly verify the contents of padding bytes. An attacker positioned between the browser and server could manipulate encrypted traffic and observe how the server responded to determine whether their guesses about the plaintext were correct. By repeating this process, the attacker could gradually recover sensitive information, such as authentication cookies.
What made POODLE particularly dangerous was not only the weakness in SSL 3.0, but the fact that browsers and servers could fall back to SSL 3.0 when a connection using a newer version of TLS failed. An attacker could deliberately interfere with the connection and force this downgrade to the vulnerable protocol. The attacker did not need to break the encryption directly; they manipulated the connection until the browser and server used an older protocol with a known weakness.
POODLE therefore exposed another weakness in the tunnel: even when stronger cryptographic protocols are available, keeping an obsolete protocol as a fallback can create a path back to a vulnerable mechanism. The tunnel may have newer and stronger walls, but if an attacker can force you through an older entrance, those protections no longer matter.

POODLE, like BEAST, did not prove that encryption is useless. It showed that the security of the tunnel depends on the mechanisms used to build and maintain it. BEAST exploited a weakness in how CBC was used in TLS 1.0, while POODLE exploited a weakness in SSL 3.0's handling of CBC padding and the ability to fall back to that outdated protocol. The tunnel is only as strong as the mechanisms behind it.
