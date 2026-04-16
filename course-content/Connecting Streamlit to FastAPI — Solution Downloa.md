# Connecting Streamlit to FastAPI — Solution Download

**GitHub:** `module-06-web-streamlit/solutions/exercises/streamlit-fastapi-connect/`

Compare your solution to the reference. Key things to check:

- Does the login form store the JWT in `st.session_state`?
- Does the sidebar show the logged-in user and have a working logout?
- Do API calls include the `Authorization: Bearer <token>` header?
- Does the app show a helpful error when the backend is not running?
- Does a 401 response redirect to the login form?

Differences in layout, styling, and which metrics you chose are fine. The critical pattern is: auth gate → authenticated API calls → error handling.