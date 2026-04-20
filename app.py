from flask import Flask, render_template

app = Flask(__name__)

# 샘플 데이터
posts = [
    {"id": 1, "title": "첫 번째 글", "content": "Flask 블로그 시작!"},
    {"id": 2, "title": "두 번째 글", "content": "Vercel 배포 테스트"}
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)

# 로컬 실행용
if __name__ == "__main__":
    app.run(debug=True)
