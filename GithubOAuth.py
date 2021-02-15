#set/export OAUTHLIB_INSECURE_TRANSPORT=1

try:
    from flask import Flask,render_template,url_for,request,redirect, make_response
    import secrets
    import string
    import json
    from time import time
    from flask_dance.contrib.github import make_github_blueprint, github
except Exception as e:
    print("Some Modules are Missings {}".format(e))


app = Flask(__name__)
res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10))
app.config["SECRET_KEY"]=res

github_blueprint = make_github_blueprint(client_id='Enter Key Here',
                                         client_secret='Enter Secret Here')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            #return format(account_info_json['login'])
            username =  format(account_info_json['login'])
            return redirect('https://github.com/'+username)

    return '<h1>Request failed!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
