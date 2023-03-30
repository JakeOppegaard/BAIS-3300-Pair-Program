from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friends_dict = [
    {"title": "Harry Potter", "author": "J.K Rowling", "pages": "345", "genre": "Mystery", "details":"I own this book", "how_got": "I purchased it"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )

@app.route('/add', methods=['POST'])
def add():
    if request.method == "POST":
        form = request.form

        title = form['fname']
        author = form['lname']
        pages = form['pages']
        genre = form['genre']
        details = form.getlist('details')
        how_got = ['how_got']

        print(title)
        print(author)
        print(pages)
        print(genre)
        print(details)
        print(how_got)

        details_string = ", ".join(details)

        friend_dict = {
            'title': title,
            'author': author,
            'pages': pages,
            'genre': genre,
            'details': details,
            'how_got': how_got
        }

        print(friend_dict)
        friends_dict.append(friend_dict)
        print(friends_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", pageTitle="About")

if __name__ == "__main__":
    app.run(debug=True)
