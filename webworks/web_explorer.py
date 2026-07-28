import requests  # The HTTP library you installed in Module 4

# --- GET Request: Fetching data ---
# This is exactly what your browser does when you visit a URL
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# The status code tells us if the request succeeded
print(f"Status Code: {response.status_code}")  # Should print 200

# Response headers contain metadata about the response
print(f"Content-Type: {response.headers['Content-Type']}")

# The response body contains the actual data
data = response.json()  # Parse the JSON response into a Python dictionary
print(f"Post Title: {data['title']}")
print(f"Post Body: {data['body'][:80]}...")  # First 80 characters


# Request a post that doesn't exist
response_404 = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
print(f"\nBad Post Status: {response_404.status_code}")  # 404 — Not Found

# Request a URL that doesn't exist at all
try:
    response_bad = requests.get("https://jsonplaceholder.typicode.com/nonexistent")
    print(f"Bad URL Status: {response_bad.status_code}")  # Still returns a status code
except requests.exceptions.ConnectionError:
    # This happens when the server can't be reached at all
    print("Could not connect to the server!")


# --- POST Request: Sending data ---
# This is what happens when you submit a form or create a new record
new_post = {
    "title": "My First Post from Python",
    "body": "This was sent using the requests library!",
    "userId": 1  # Required by this API
}

response_post = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post  # 'json=' automatically sets Content-Type header
)

print(f"\nPOST Status: {response_post.status_code}")  # 201 — Created
print(f"Created Post: {response_post.json()}")
