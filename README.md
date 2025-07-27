
# Đây chỉ là khung code hãy đọc kĩ và hoàn thiện code mới tự đăng kí cho cá nhân
# Tool đăng kí học phần dành cho sinh viên

# I. Mở đầu
đây là công cụ tiện lợi giúp cho sinh viên đăng kí học phần nhanh chóng chỉ cần bấm chạy và chờ đến khi đăng kí thành công môn học.
- ưu điểm: bỏ qua bước chờ load danh sách học phần rồi chọn lớp, không cần phải thức đêm để tranh slot đăng 
- nhược điểm: gửi nhiều request liên tục có thể bị chặn IP (khắc phục: hạn chế bấm chạy liên tục, chờ 1 xíu rồi bấm chạy tiếp), chưa có cơ chế để biết đã đăng kí thành công chưa (phải tự kiểm tra)

# II. Hướng dẫn cài đặt 
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
  <img src="https://sf-static.upanhlaylink.com/img/image_202507274acb1fb08a08f2eb32c7f4d6861e9ae4.jpg" alt="Screenshot 2025-07-26 150009.png">       

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

# III. Hướng dẫn dùng tool:
- Sau khi cài đặt IDE và hoàn thiện code bạn có thể bấm chạy code để thử xem tool đã hoạt động chưa 
<img src="https://sf-static.upanhlaylink.com/img/image_202507277e925ae4e4ce2188aab6a36017a47d33.jpg" alt="Screenshot 2025-07-27 184105.png">         

###### nếu terminal hiện giống như này thì tool của bạn đã hoạt động và chỉ chờ đến ngày đăng kí học phần thôi

<img src="https://sf-static.upanhlaylink.com/img/image_20250727fab787a05636c928482d150b1eb691c4.jpg" alt="Screenshot 2025-07-27 184803.png">

###### ảnh minh họa nếu như đã đăng kí môn học thành công

# IV. Một số cần lưu ý:
### 1. Tính tương thích với mọi Website của trường:
- Đây là tool được phát triển bởi sinh viên Học Viện Hàng Không Việt Nam dựa trên website của trường nên có thể sẽ khác cách thức đăng kí dẫn đến tool không hoạt động được trên website trường của bạn. Bạn hãy tìm hiểu kĩ hoặc có thể tự phát triển tool cho phù hợp với website trường 
### 2. Dùng tool hợp lý:
- Vì cách hoạt động của  tool sẽ spam đăng kí nên web trường sẽ chặn IP của bạn nên tôi khuyên nên để `MAX_REQUESTS` là 1 đồng thời dừng khoảng 1-2 phút rồi bấm chạy tool tiếp
- Nếu bạn cho tool đăng kí 6 môn cùng 1 lúc sẽ rất dễ bị phát hiện nên tôi khuyên bạn hãy đăng kí từng môn cho đến khi môn đó đã đăng kí xong
  - những dòng của các môn còn lại bạn có thể thêm dấu `#` ở phía trước để `Comment` đoạn đó lại khi nào đến lượt đăng kí môn đó hãy xóa dấu `#` đi sẽ tiết kiệm thời gian của bạn hơn
  - Lưu ý dòng cuối cùng trong danh sách môn học sẽ không có dấu `,` vì vậy nếu bạn đăng kí theo từng môn thì có thể xóa dấu `,` đi
### 3. Hỗ trợ cài đặt tool:
- Nếu bạn có vấn đề gì trong quá trình cài đặt bạn có thể nhắn tin trực tiếp qua [Facebook](https://www.facebook.com/Longpogba06) của tôi với phụ phí nho nhỏ khoảng 20k
- Hoặc bạn muốn tôi setup cho bạn từ A-Z tôi sẽ làm cho bạn qua `UltraViewer` với phí 50k
- Nếu bạn học trường khác muốn mình hỗ trợ setup tool thì tôi không chắc tool sẽ hoạt động nhưng sẽ vẫn mất phí nhé!
### 4. Cảnh báo về tính trách nhiệm:
- Vì tôi cũng là sinh viên nên tôi không chắc dùng tool có bị cấm hay không nên bạn có thể tìm hiểu kĩ hoặc cân nhắc trước khi dùng 
- Đây chỉ là Tool tôi muốn chia sẻ để cho bạn tham khảo, việc sử dụng để đăng kí là do bạn quyết định nên nếu dùng tool mà bạn bị nhà trường phát hiện và bị xử lí với nhiều hình thức như hủy kết quả đăng kí hoặc bị cảnh bảo học vụ... thì tôi sẽ **không chịu trách nhiệm** cho những việc đó

#
##### Cuối cùng nếu bạn thấy hay có thể ủng hộ cho tôi để tôi có thể phát triển tool nhé!
<img src="https://sf-static.upanhlaylink.com/img/image_202507271165dc209b7d5c9e5edb3822acf1fcbc.jpg" alt="SmartSelect_20250727_193724_Gallery.jpg"> 