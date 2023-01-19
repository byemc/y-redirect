from flask import Flask, redirect, request
from requests import get

app = Flask(__name__)

checkheaders = {'User-Agent': 'ByeBot for the web v1.0 :: y.omg.lol'} 

@app.errorhandler(404)
def page_not_found(e):

    print(f"https://exit.the-y.lol{request.path}")

    if len(request.path.split("/")) != 2:
        return redirect(f"https://read.the-y.lol{request.path}")
    purlcheck = get(f"https://exit.the-y.lol{request.path}", allow_redirects=False, headers=checkheaders)
    print(purlcheck.status_code)
    if purlcheck.status_code == 302:
        return redirect(f"https://exit.the-y.lol{request.path}")
    else:
        return redirect(f"https://read.the-y.lol{request.path}")

    return f"Sorry, something went wrong with the redirector. Somehow. Try visiting <a href='https://read.the-y.lol{request.path}'>https://read.the-y.lol{request.path}</a>"


if __name__ == "__main__":
    app.run(debug=True)
