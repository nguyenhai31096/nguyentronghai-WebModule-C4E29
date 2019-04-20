from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about_me')
def favorite_quotes():
    return "Không phải Tào tháo ta mặt dầy, mà là ta sớm không còn để những cương thường luân lý, dung tục trên thế gian ở trong lòng rồi. Thế nhân nói ta là gian hùng, nhưng lại không làm gì được một kẻ gian hùng như ta. Bọn người các ngươi tự cho mình quân tử cũng đều bại trong tay kẻ gian hùng là ta đây. Nếu cái giá làm quân tử phải trả là bị lăng nhục, bị chà đạp, bị tiêu diệt, thậm chí là giết chết, ta thà là một gian hùng có thể thực hiện được hoài bão của mình. Từ cổ đến nay, “đại gian như trung, đại giả như thật”, trung nghĩa và gian ác không thể nhìn bề ngoài có thể nhận ra được. Có thể các người trước đây đã nhìn lầm tào tháo ta, bây giờ lại cũng nhìn lầm ta, nhưng ta vẫn là ta, ta chưa hề sợ người khác nhìn lầm ta"



@app.route('/school')
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run( debug=True)