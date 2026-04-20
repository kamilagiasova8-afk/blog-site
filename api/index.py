from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# 샘플 블로그 데이터
posts = [
    {
        "id": 1,
        "title": "첫 번째 블로그 글",
        "content": "안녕하세요. Flask와 Vercel로 만든 블로그입니다."
    },
    {
        "id": 2,
        "title": "두 번째 글",
        "content": "HTML 템플릿과 CSS를 적용한 예제입니다."
    }
]


@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    selected_post = next((p for p in posts if p["id"] == post_id), None)

    if not selected_post:
        return "Post not found", 404

    return render_template("post.html", post=selected_post)


# Vercel에서 Flask app 인식용
app = app
