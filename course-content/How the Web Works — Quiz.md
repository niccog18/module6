# How the Web Works — Quiz

**Module 6 — Web Essentials & Streamlit**

---

**Question 1:** When you type `https://www.example.com` into your browser, what is the very first thing that happens?

- A) Your browser sends an HTTP request to [example.com](http://example.com)
- B) Your browser asks a DNS server for the IP address of [example.com](http://example.com)
- C) Your browser downloads the HTML, CSS, and JavaScript files
- D) Your browser checks if the site uses HTTPS

> **Answer: B** — Before your browser can communicate with a server, it needs to know *where* that server is. Domain names like "[example.com](http://example.com)" are human-readable labels — computers use IP addresses (like 93.184.216.34). DNS translates the domain name into an IP address. Only after getting the IP address can the browser send an HTTP request. If you picked A, you skipped the crucial first step — the browser can't send a request to a server it can't find.
> 

---

**Question 2:** In the client/server model, which is the "client" and which is the "server"?

- A) The client is the database; the server is the API
- B) The client is your browser (or app) making requests; the server is the computer responding to those requests
- C) The client is the person using the computer; the server is the web developer
- D) The client and server are always on the same computer

> **Answer: B** — In web communication, the *client* is the software that initiates a request (your browser, a mobile app, or even a Python script using the `requests` library). The *server* is the software that receives and responds to those requests (like the FastAPI applications you built in Module 5). They are almost always on different computers connected over a network.
> 

---

**Question 3:** You make an HTTP request and receive a status code of `404`. What does this mean?

- A) The server is down and can't respond
- B) Your request was malformed or invalid
- C) The resource you requested was not found on the server
- D) You don't have permission to access this resource

> **Answer: C** — A 404 means "Not Found" — the server is running and received your request just fine, but the specific thing you asked for (a page, an API endpoint, a file) doesn't exist at that URL. This is different from a 500 (server error — something crashed), a 400 (bad request — your request was malformed), or a 403 (forbidden — the resource exists but you don't have permission).
> 

---

**Question 4:** Why is HTTPS important for AI applications?

- A) It makes the website load faster
- B) It encrypts communication between the browser and server, protecting sensitive data like API keys and user information
- C) It's required for all Python applications
- D) It prevents hallucinations in AI models

> **Answer: B** — HTTPS encrypts data in transit, preventing anyone between the client and server (internet providers, hackers on public Wi-Fi, etc.) from reading the data being exchanged. For AI applications that handle user data, authentication tokens, and API keys, this protection is essential. If you chose A, HTTPS actually adds a tiny bit of overhead due to encryption — it's about security, not speed.
>