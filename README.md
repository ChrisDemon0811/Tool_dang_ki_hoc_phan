
# Đây chỉ là khung code hãy đọc kĩ và hoàn thiện code mới tự đăng kí cho cá nhân
# Tool đăng kí học phần dành cho sinh viên

# I. Mở đầu
đây là công cụ tiện lợi giúp cho sinh viên đăng kí học phần nhanh chóng chỉ cần bấm chạy và chờ đến khi đăng kí thành công môn học.
- ưu điểm: bỏ qua bước chờ load danh sách học phần rồi chọn lớp, không cần phải thức đêm để tranh slot đăng 
- nhược điểm: gửi nhiều request liên tục có thể bị chặn IP (khắc phục: hạn chế bấm chạy liên tục, chờ 1 xíu rồi bấm chạy tiếp), chưa có cơ chế để biết đã đăng kí thành công chưa (phải tự kiểm tra)

# II. Hướng dẫn dùng tool 
### 1. Cài môi trường chạy code (IDE):
Tool dùng ngôn ngữ `Python` nên bạn có khá nhiều sự lựa chọn IDE để chạy chương trình như `Pycharm`, `Visual Studio Code`, `Sublime Text`,.... Tôi khuyên bạn nên dùng `Visual Studio Code` vì nó khá tiện và dễ dùng        
Cài đặt và chạy `Python` trên `Visual Studio Code` ở [đây](https://youtu.be/yZFG5ktaZtU?si=Tj3DBs7wEL33M2xb)

### 2. Tải code và cài thư viện:
- Tải code:  
  - Bạn có thể nhập vào file `tool.py` ở phía trên và tải/copy code về hoặc nhấp vào [đây](https://github.com/ChrisDemon0811/Tool_dang_ki_hoc_phan/blob/main/tool.py)
- cài thư viện:
  - Trong đoạn code của tôi có 2 thư viện nhưng thư viện đầu đã được tích hợp sẵn trong `Python` chỉ cần cài thêm thư viện `aiohttp` 
  - Các bước cài thư viện `aiohttp`:
    - bấm phím `Windows` nhập `cmd` rồi bấm chạy
    - nhập dòng lệnh này vào `terminal`
    ```sh
    pip install aiohttp
    ```
    Hoặc  
    ```sh 
    python -m pip install aiohttp
    ```
    Hoặc  
    ```sh
    py -3 -m pip install aiohttp
    ```
    Hãy thử 1 trong 3 cho đến khi cài đặt thành công

### 3. Nhập URL
- Vào trang sinh viên chọn đăng kí học phần => chọn học kì mà mình muốn đăng kí sau đó copy link dán vào link đăng kí hp trường
### 4. Lấy Cookies và mã môn học 
- Lấy Cookies ASC.AUTH:
  - Vào trang sinh viên bấm phím `F12` => chọn tab `Application` 
  <img src="https://sf-static.upanhlaylink.com/img/image_202507264ee99a24c918129790ceafcf281a794a.jpg" alt="Screenshot 2025-07-26 150009.png">        

  - chọn mục `Cookies` và chọn vào link trang sinh viên trường của bạn => nhấp vào dòng ASC.AUTH copy hết mã Cookies và dán vào `your cookies` trong 
  - **Lưu ý:** vì cookies liên quan đến tài khoảng nên không được share cho bất kì ai, bạn có thể bị đánh cắp tài khoảng nếu làm lộ cookies 

- lấy mã môn học
  - Vào trang đăng kí học phần chọn lớp học phần muốn học bấm phím `F12` => chọn tab `Network` rồi bấm tổ hợp phím Ctrl + L
  - Bấm vào nút đăng kí của lớp học phần sẽ hiện dòng này 
  <img src="https://sf-static.upanhlaylink.com/img/image_2025072670de2e831817308dae7150bd551b20aa.jpg" alt="Screenshot 2025-07-26 152050.png">        

  - click vào dòng đó và lấy mã
  - **Lưu ý:** dòng `param[IDDotDangKy]` và `param[IDLoaiDangKy]` có thể sẽ thay đổi theo từng đợt đăng kí nên hãy xem kĩ và sửa lại
  - Copy đoạn mã ở dòng `param[GuidIDLopHocPhan]` và dán vào mã môn học
  - đây là cách lấy mã của 1 môn các môn còn lại cũng làm tương tự 
  - tôi đã để sẵn 6 mục tượng trung cho 6 môn học bạn có thể thêm bớt tùy ý miễn là đúng bố cục. **Lưu ý dòng cuối không có dấu phẩy**



