
**Skeleton**

Connection is secure. A padlock. The **'S'** in HTTPS. For decades, these have been the signals we trust when browsing the web. 
I trusted them too, but I never stopped to ask what was actually happening beneath that padlock. 
One afternoon, staring at a padlock icon on my browser, a question hit me: IS HTTPS REALLY SAFE? 
I went down the rabbit hole. What I found shocked me. The padlock is not a promise about where you are going. It is only a promise about how you get there. After weeks of research, one thing became clear: the tunnel is safe, but the destination isn't. To understand why, we need to start with the layer that runs this whole thing: HTTP.

Hypertext Transfer Protocol (HTTP) is a foundational rule system that governs how information is exchanged between client and server on the internet. It defines how data is formatted and transmitted, and how web browsers and servers respond to various commands.
HTTP is the core language of the World Wide Web. With HTTP, a client, typically a web browser, requests a resource from a server, and the server responds with a status code and the requested resource. This is what we call the request-response system.
Though HTTP forms the foundation for the World Wide Web, transferring data in plaintext poses a huge security risk. With the right tool and technical know-how, anyone on the same network could intercept data in transit. This is called a Man-In-The-Middle(MITM) attack. 
Think of it like delivering an unsealed letter through a delivery agency to a friend. The delivery man can see the contents of the letter and also tamper with it before it gets to your friend. 
This is exactly how a MITM happens over HTTP.
To prove this, I conducted a lab using testfire.net as our case study.

Url: http://testfire.net

![Wireshark test](HTTP_test.png)

> From the capture, we can observe the complete HTTP login transaction. The browser first requests the login page (GET /login.jsp), then submits the login form through a POST /doLogin request. Because HTTP transmits data without encryption, Wireshark is able to decode the request body and display the submitted form fields in plaintext. The username (ArticleUser) and password (InsecurePassword) are clearly visible in the packet details, demonstrating that sensitive information can be exposed to anyone capable of intercepting the network traffic.

As the World Wide Web grew, this vulnerability was exploited by many, and so the need for a secure type of HTTP was necessitated. HTTPS was the solution to this.

**What Is HTTPS?**

Hypertext Transfer Protocol Secure(HTTPS) is simply HTTP over a security layer. This security layer is called the **Transport Layer Security(TLS)**: a security or cryptographic protocol that encrypts data sent over the internet to keep it private and safe. During data transfer over HTTPS, there's a key share which grants data privacy by encrypting it. This help improve Confidentiality and Intergrity over the internet. In other words, HTTPS is HTTP over TLS. 

To understand this better, a lab was conducted over HTTPS using testfire.net as a case study and the same login credentials.

URL: https://testfire.net

![Wireshark test](HTTPS_test.png)

> The capture above shows the same login activity performed over HTTPS. Unlike the previous HTTP capture, Wireshark is unable to reveal the contents of the communication. Instead of displaying HTTP requests such as GET and POST, the packets appear as TLS Application Data, indicating that the application-layer data has been encrypted before transmission. The packet payload consists only of encrypted bytes, making the username, password, and other sensitive information unreadable to anyone intercepting the traffic. Although an attacker can still observe metadata such as the communicating IP addresses, the use of TLS prevents them from viewing or modifying the data exchanged between the client and the server.

The difference between HTTP and HTTPS is now visible. In the HTTP capture, the login credentials were exposed becaused data is transferred in plaintext. In the HTTPS capture, the same type of communication appears only as encrypted TLS application data, preventing anyone intercepting the traffic from reading the contents.

The current the version of the Transport Layer Security(TLS) running the web is version 1.3(v1.3). Initially, the Secure Socket Layer(SSL) was the protocol powering web security. Created in 1994 by Netscape, SSL 1.0  was never released to the public due to the severe security and design flaws revealed by internal testing. SSL 2.0 was released to the public in 1995 and succeeded by SSL 3.0 in 1996. SSL used weak Message Authentication Codes(MAC) and Algorithms like MD5, which could be exploited easily. Also, as the web grew, the industry needed an open vendor protocol to enhance web security rather than a sole proprietary Netscape product; hence, the Internet Engineering Task Force(IETF), an international open standard organization introduced TLS to standardize internet encryption and fix critical cryptographic vulnerabilities inherent to Netscape's proprietary code
