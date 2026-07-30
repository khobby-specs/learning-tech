**Skeleton**

Connection is secure. A padlock. The 'S' in HTTPS. For decades, these have been the signals we trust when browsing the web. I trusted them too, but I never stopped to ask what was actually happening beneath that padlock. One afternoon, staring at a padlock icon on my browser, a question hit me: IS HTTPS REALLY SAFE? I went down the rabbit hole. What I found shocked me. The padlock is not a promise about where you are going. It is only a promise about how you get there. After weeks of research, one thing became clear: the tunnel is safe, but the destination isn't. To understand why, we need to start with the layer that runs this whole thing: HTTP.
Hypertext Transfer Protocol (HTTP) is a foundational rule system that facilitates how information is exchanged between client and server on the internet. It defines how data is formatted and transmitted, and how web browsers and servers respond to various commands.
HTTP is the core language of the World Wide Web. With HTTP, a client, typically a web browser, requests a resource from a server(web server), and the server responds to the request with a status code and the requested resource. This is what we call the request - response system.
Though HTTP forms the foundation for the World Wide Web, transferring data in plaintext poses a huge security risk. With the right tool and technical know-how, anyone on the same network could intercept data in transit. This is termed as a Man-In-The-Middle(MITM) attack. 
Think of it like delivering an unsealed letter through a delivery agency to a friend. The delivery man can see the contents of the letter and also tamper with it before it gets to your friend. 
This is exactly what happens during MITM in HTTP.
To prove this, I conducted a lab using testfire.net as our case study.

Url: http://testfire.net

![Wireshark test](HTTP_test.png)

From the image:
- An HTTP request was made to the server to get the home page.
- The server responded to the request with a status code and the page.
- Another request was made to get the login page, which was responded to with a status code, 200 and the page.
- I then attempted a login with username: 'ArticleUser' and password: 'InsecurePassword' which were captured in plaintext as seen in the image.

As the World Wide Web grew, this vulnerability was exploited by many, and so the need for a secure type of HTTP was necessitated. HTTPS was the solution to this.

**What Is HTTPS?**

Hypertext Transfer Protocol Secure(HTTPS) is simply HTTP with security. HTTPS gains its security from the Transport Layer Security (TLS). In other words, HTTPS is HTTP over TLS. HTTPS protects data in transit by encrypting it. The data is encrypted into ciphertext using an encryption key, which is only accessible to the client and server.
