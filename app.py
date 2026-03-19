from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    
    my_name= "Thang"
    my_bio = "best chamber"
    contact_email = "nhanminhthang4a1@gmail.com"
   
    
    my_skills = [
        {
            "skill_name": "Lập trình Scratch",
            "description": "Lập trình Scratch là một ngôn ngữ lập trình trực quan được thiết kế để giúp trẻ em và người mới bắt đầu học lập trình.",
            "percentage": 80,
            "certificate": ''
        },
        {
            "skill_name": "Lập trình Python cơ bản",
            "description": "Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.",
            "percentage": 70,
            "certificate": ''
        },
        {
            "skill_name": "Lập trình Python nâng cao",
            "description": "Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.",
            "percentage": 850,
            "certificate": ''
        },
        {
            "skill_name": "Lập trình Web",
            "description": "Lập trình Web là quá trình tạo ra các trang web và ứng dụng web tương tác.",
            "percentage": 90,
            "certificate": 'docs/thang.pdf'
        }
    ]
    return render_template("index.html", name=my_name, title = my_bio, email = contact_email, skills = my_skills)
# @app.route('/projects')
# def projects():
#     return 'This is the projects page.'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == ('__main__'):
    app.run(debug= True)
