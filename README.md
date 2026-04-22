
# Tool đăng kí học phần dành cho sinh viên

## Menu
[I. Mở đầu ](#i-mở-đầu) 

[II. Hướng dẫn cài đặt](#ii-hướng-dẫn-cài-đặt)
- [1. Cài đặt tool](#1-cài-đặt-tool)
- [2. Cấu hình tool để sử dụng](#2-cấu-hình-tool-để-sử-dụng)

[III. Hướng dẫn dùng tool](#iii-hướng-dẫn-dùng-tool)

[IV. Một số cần lưu ý](#iv-một-số-cần-lưu-ý)
- [1. Thu phí khi dùng tool](#1-thu-phí-khi-dùng-tool)
- [2. Chống lạm dụng tool](#2-chống-lạm-dụng-tool)
- [3. Bảo mật của tool](#3-bảo-mật-của-tool)
- [4. Giải đáp](#4-giải-đáp)
- [5. Cảnh báo khi dùng tool](#5-cảnh-báo-khi-dùng-tool)

===========================================================================

# I. Mở đầu
đây là công cụ tiện lợi giúp cho sinh viên đăng kí học phần nhanh chóng chỉ cần bấm chạy và chờ đến khi đăng kí thành công môn học.
- ưu điểm: 
    - bỏ qua bước chờ load danh sách học phần rồi chọn lớp, không cần phải thức đêm để tranh slot đăng kí.
    - giảm được số request đến server nhà trường giúp giảm tải, tránh sập website.

- nhược điểm: 
    - nếu dùng không đúng cách có thể bị nhà trường phát hiện và hủy kết quả học phần.

# II. Hướng dẫn cài đặt 
### 1. Cài đặt tool
- Nhấn vào `Releases` chọn file `Tool_ĐKHP.exe` để tải về hoặc nhấp vào [đây](https://github.com/ChrisDemon0811/Tool_dang_ki_hoc_phan/releases/tag/Tool_%C4%90KHP?)
- tìm đến file vừa tải về và giải nén ra 
- truy cập vào thư mục vừa giải nến double click vào file `Tool_ĐKHP` có logo VAA để dùng

### 2. Cấu hình tool để sử dụng
- sau khi cài đặt tool xong bạn cứ đăng nhập/đăng kí như bình thường
<img src="https://cdn.phototourl.com/free/2026-04-22-f2c32349-3cba-4c97-809f-9893376c56a1.png?" alt="Giao diện khi đăng nhập thành công">

###### giao diện khi đăng nhập thành công

- để sử dụng các chức năng trong tool trước tiên bạn phải lấy được cookies ASC.AUTH:
    - Đăng nhập vào trang sinh viên bấm phím `F12` => chọn tab `Application` 
  <img src="https://cdn.phototourl.com/free/2026-04-22-1db97a62-77bf-4e93-9233-538d0f43272c.png?" alt="Lấy cookies ASC.AUTH">       

  - chọn mục `Cookies` và chọn vào link trang sinh viên trường => nhấp vào dòng ASC.AUTH copy hết mã Cookies và dán vào `ASC.AUTH` trong tool
  - **Lưu ý:** 
    - vì cookies liên quan đến tài khoảng nên không được share cho bất kì ai, bạn có thể bị đánh cắp thông tin cá nhân nếu làm lộ cookies 
    - vì cookies có thể bị reset liên tục nên bạn phải cập nhật cookies mới trước giờ đăng kí khoảng 10-30 phút và phải đảm bảo bạn phải luôn mở trang sinh viên trong trình duyệt mà bạn lấy cookies để nó vẫn hoạt động tốt

  - sau khi lấy cookies xong bạn có thể chuyển qua tab thông tin cá nhân để check xem có đúng tài khoảng của mình chưa hoặc nếu không hiện thông tin thì bạn đã copy sai cookies hoặc cookies đã hết hạn, hãy kiên nhẫn làm lại.

# III. Hướng dẫn dùng tool
- Khi đã lấy đúng cookies rồi thì bạn có thể cấu hình sẵn các môn học bạn dự định học:
    - truy cập vô tab `lấy mã` hệ thống sẽ truy vấn tất cả các môn được hiển thị trong trang đăng ký học phần
    - bạn chỉ cần thao tác giống như website nhà trường
    - khi bạn chọn được lớp học phần của môn đó hệ thống sẽ trả về bạn bạn `mã GUID` hãy bấm vào nút `gán` và gán vào các ô môn học (hiện tại tool chỉ cho phép đăng kí tối đa 6 môn cùng 1 lúc)  
    - sau khi gán xong bạn có thể quay lại tab nhập mã để kiểm tra đủ số lượng môn học chưa
    - **Lưu ý:**
        - ở ô kết quả có hiển thị ID đợt đăng kí, mỗi đợt đăng ký học phần sẽ có ID khác nhau (thường là +1 so với đợt trước) bạn hãy chú ý để nhập ở ô ID đợt đăng ký cho đúng.

- sau khi bạn chọn được các lớp học phần bạn có thể đặt hẹn giờ đến ngày, giờ đăng kí của khoa mình để hệ thống tự đăng kí (**Lưu ý:** nếu đặt hẹn giờ thì không được tắt tool và trang sinh viên), bạn có thể bật delay giữa các môn tránh việc tất cả các môn đều được đăng kí cùng 1 lúc để không bị phát hiện
- bạn có thể chạy tool để test thử tool đã hoạt động tốt chưa






<img src="https://sf-static.upanhlaylink.com/img/image_202507277e925ae4e4ce2188aab6a36017a47d33.jpg" alt="Screenshot 2025-07-27 184105.png">         

###### nếu ô kết quả hiện giống như này thì tool của bạn đã hoạt động và chỉ chờ đến ngày đăng kí học phần thôi

<img src="https://sf-static.upanhlaylink.com/img/image_20250727fab787a05636c928482d150b1eb691c4.jpg" alt="Screenshot 2025-07-27 184803.png">

###### ảnh minh họa nếu như đã đăng kí môn học thành công

# IV. Một số cần lưu ý
### 1. Thu phí khi dùng tool
- Để giảm tải cho hệ thống mỗi giờ cao điểm cũng như tránh việc tận dụng lỗ hổng của tool để làm sập website trường, mình xin phép thu phí 5k/môn đăng kí thành công (nếu chạy tool mà đăng ký thành công 1 môn bất kì, hệ thống sẽ trừ đi 1 lượt đăng kí của bạn và sẽ dừng lại khi bạn hết lượt).
### 2. Chống lạm dụng tool
- Để tránh việc mọi người spam request mình đã có 1 số giải pháp để khắc phục như:
    - Khi bấm đăng khi mỗi môn chỉ gửi request 1 lần khi chạy xong sẽ dừng lại.
    - tính năng khóa tài khoảng tự động trong 5p nếu cố tình spam nút đăng ký quá 5 lần trong 1p.
    - giới hạn số lượt đăng ký bằng cách thu phí .
- Mình đã cố gắng để thu hẹp khoảng cách giữa người đăng kí trên website và người dùng tool để đăng kí để các bạn đăng kí trên website vẫn có nhiều cơ hội để đăng ký được lớp học phần mà mình muốn.

### 3. Bảo mật của tool
- Nhiều bạn thắc mắc liệu tool có thu thập thông tin người dùng không? thì mình trả lời luôn là **Không** và mình không có nhu cầu lấy thông tin của các bạn. Trong hệ thống cơ sở dữ liệu của tool mình chỉ quản lý các tài khoảng mà các bạn tạo để đăng nhập tool và các chức năng phụ của tool thôi. Các cookies, mã môn học đều được lưu trên thiết bị của bạn hết.
### 4. Giải đáp 
- Sẽ có bạn thắc mắc ở mục mở đầu vì sao mình lại bảo tool có ưu điểm là giảm được số request đến server nhà trường giúp giảm tải, tránh sập website thì mình sẽ giải thích như sau:
    - Nếu bạn đăng kí trên website sẽ gồm các bước như sau: truy cập trang đăng kí học phần -> load học kỳ -> chọn môn muốn đăng kí -> chọn lớp muốn học -> bấm nút đăng kí. Tổng cộng 5 request/môn gửi đến server của trường.
    - Nếu bạn đăng kí bằng tool: việc bạn gán GUID của từng môn học thì khi bấm đăng kí hệ thống sẽ bỏ qua các bước kia và trỏ thẳng đến nút đăng kí của lớp học phần đó và bấm đăng kí. Tổng cộng 1 request/môn gửi đến server của trường.
- Điều này sẽ làm giảm tải 1 lượng lớn request đến server nhà trường tránh bị sập website.
### 5. Cảnh báo khi dùng tool
- Vì tôi cũng là sinh viên nên tôi không chắc dùng tool có bị cấm hay không mặc dù đã có các biện pháp chống lạm dụng tool vì mục đích xấu nhưng bạn vẫn nên cân nhắc trước khi dùng. Và tôi cũng không khuyến khích bạn xử dụng.
- Đây chỉ là Tool tôi muốn chia sẻ để cho bạn tham khảo, việc sử dụng để đăng kí là do bạn quyết định nên nếu dùng tool mà bạn bị nhà trường phát hiện và bị xử lí với nhiều hình thức như hủy kết quả đăng kí hoặc bị cảnh bảo học vụ... thì mình sẽ **không chịu trách nhiệm** cho những việc đó.

#
