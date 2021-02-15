# Flask-Github-OAuth
### Acquire Client ID and Secret
```bash
Sign in your GitHub account.
Go to settings > Developer settings > OAuth apps
Create new OAuth
Set homepage URL as : http://127.0.0.1:5000/
Set authorization callback URL as : http://127.0.0.1:5000/github_login/
Note down your Client ID and Secret
```
### To run the script
```bash
pip install -r requirements.txt
Edit The GithubOAuth.py file > edit the client_id and client_secret as you got from above steps
For Linux/macOS
    export OAUTHLIB_INSECURE_TRANSPORT=1
For Windows
    set OAUTHLIB_INSECURE_TRANSPORT=1

python GithubOAuth.py

```
