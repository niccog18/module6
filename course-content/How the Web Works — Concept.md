# How the Web Works — Concept

**Module 6 — Web Essentials & Streamlit**

**Estimated time: 30 minutes**

---

### Learning Objectives

By the end of this lesson, you will be able to:

1. Explain what happens step-by-step when you type a URL into a browser and hit Enter
2. Describe the roles of client, server, DNS, and HTTP in the request/response cycle
3. Identify common HTTP status codes and what they mean
4. Explain why understanding the web matters for building AI-powered applications

---

`[VIDEO PLACEHOLDER: 5 min — "How the Web Works: Trace a URL from browser to server and back. DNS lookup, HTTP request, server response, browser rendering — the 30-second version of what happens when you hit Enter."]`

You use the web every single day. You type something into a browser, hit Enter, and a page appears. It feels instant and almost magical — like flipping a light switch.

But here's the thing: when you flip a light switch, a remarkable chain of events happens behind the wall. Electricity flows from a power plant through miles of wire, gets stepped down by transformers, routes through your home's circuit breaker, and finally reaches that one bulb. You don't need to understand all of that to turn on a light. But if you're training to become an *electrician*, you absolutely do.

That's where you are right now. You're not just using the web anymore — you're about to *build things on it*. In Module 5, you built a FastAPI backend. In this module, you'll build the other half: the part users actually see and interact with. To do that well, you need to understand how the web actually works under the hood.

Let's trace exactly what happens when you type `https://www.google.com` into your browser and press Enter.

---

## Step 1: Your Browser Looks Up the Address (DNS)

Your browser doesn't actually know where "[google.com](http://google.com)" lives. Domain names like "[google.com](http://google.com)" are for humans — computers communicate using **IP addresses**, which are numerical identifiers like `142.250.80.46`.

So the very first thing your browser does is ask: "What's the IP address for [google.com](http://google.com)?" It sends this question to a **DNS server** (Domain Name System). Think of DNS as the internet's phone book — you give it a name, it gives you a number.

![image.png](How%20the%20Web%20Works%20%E2%80%94%20Concept/image.png)

Your computer usually knows which DNS server to ask because your internet provider (or your Wi-Fi router) configured it automatically. The DNS server looks up the name and responds with the IP address. This usually takes milliseconds.

---

## Step 2: Your Browser Connects and Sends a Request (HTTP)

Now that your browser knows the IP address, it connects to that server and sends an **HTTP request**. You already know about HTTP from Module 4 — it's the protocol (the set of rules) that browsers and servers use to communicate.

The request includes several pieces of information: the **method** (GET — because you want to *get* a page), the **path** (/ — the root page), **headers** (metadata like what browser you're using, what language you prefer, and whether you accept compressed data), and sometimes a **body** (not for GET requests, but for POST requests when you're sending data).

Your Browser Connects and Sends a Request (HTTP)

![image.png](How%20the%20Web%20Works%20%E2%80%94%20Concept/image%201.png)

This is the exact same structure you worked with when building API endpoints in FastAPI. The web isn't using some different system for websites versus APIs — it's all HTTP, all the way down.

---

## Step 3: The Server Responds

Google's server receives your request, processes it (figures out what page to show you), and sends back an **HTTP response**. This response contains a **status code** (200 OK — success), **headers** (content type, cache rules, security settings), and a **body** (the actual HTML, CSS, and JavaScript that make up the page).

![image.png](How%20the%20Web%20Works%20%E2%80%94%20Concept/image%202.png)

You remember status codes from Module 4:

- **200** — Everything worked
- **301** — This page moved permanently (the server tells your browser the new address)
- **404** — Not found (the thing you asked for doesn't exist)
- **500** — Server error (something broke on their end)

These codes aren't just API concepts. Every single webpage you've ever loaded returned one of these codes. Your browser just handles them silently — redirecting on 301s, showing error pages on 404s.

---

## Step 4: Your Browser Renders the Page

The response body contains three types of content: **HTML** (the structure — headings, paragraphs, images, links), **CSS** (the styling — colors, fonts, spacing, layout), and **JavaScript** (the behavior — what happens when you click a button, type in a search box, or scroll down).

Your browser reads the HTML first to build the structure, applies the CSS to make it look right, then runs the JavaScript to make it interactive. This entire process — from DNS lookup to rendered page — typically takes under a second.

![image.png](How%20the%20Web%20Works%20%E2%80%94%20Concept/image%203.png)

---

## HTTPS: The Secure Version

You probably noticed the "https://" at the start of the URL. The "s" stands for **secure**. HTTPS encrypts the communication between your browser and the server so that nobody in between (your Wi-Fi provider, a hacker on the same coffee shop network, your ISP) can read the data being exchanged.

For AI applications that handle user data, API keys, or any sensitive information, HTTPS is not optional — it's essential. Every modern browser warns users when a site uses plain HTTP instead of HTTPS.

---

## Why This Matters for AI Engineers

You might be wondering: "I'm building AI applications, not websites. Why do I need to know this?"

Because every AI application has a user interface, and that interface communicates with your backend over HTTP. When you build a Streamlit app in Week 2 that connects to your FastAPI backend, here's what's actually happening: your user's browser loads the Streamlit interface, the interface sends HTTP requests to your FastAPI server, your server processes the request (maybe queries a database, maybe calls an AI model), and the response flows back to the browser to display the result.

Understanding this cycle means you can debug problems. When something doesn't work, you'll know how to check: Is it a DNS issue? A connection problem? A wrong status code? A malformed response? The DevTools Network tab — which you'll use in the Guided Example — makes all of this visible.

You're not just a user of the web anymore. You're a builder. And builders understand their medium.