# 042020_HCM_NguyenThanhLoc_SE

1.Trang Admin và phân quyền:
- Công nghệ/framework: Odoo. Nền tảng Odoo hỗ trợ xây dựng menu, models. Phần phân quyền dựa trên Group và Access Rule.
- Phân quyền:
  + Mỗi user sẽ được gán những Group có quyền CRUD trên models tương ứng. Ví dụ: Đối với Phim, Loại Phim, ta có 3 loại Group là Movie Manager(CRUD), Movie User(CRU) vaf Movie Viewer(R). User vận hành nội dung sẽ có quyền Movie Manager để có đầy đủ quyền với các models Phim. Loại Phim. User Bán Vé chỉ có quyền Movie Viewer có nghĩa là chỉ có quyền xem và không có quyền thao tác Create, Update, Delete dữ liệu.
  + Access Rule: mỗi Group sẽ có thêm Access Rule riêng nhằm để phân tách quyền trên model mà User chỉ được thao tác theo Rule quyết định. Ví dụ: Đối với User Bán Vé chỉ có thể xem được thông tin Phim mà rạp hiện tại đang chiếu, như vậy có nghĩa là trong hệ thống có 3 bộ phim Ironman, Thor, Hulk nhưng rạp mà nhân viên bán vé chỉ đang chiếu Thor và Hulk nên lúc này nhân viên bán vé không thể thấy được thông tin bán vé của Ironman.

2. API
- Công nghệ/framework: Sử dụng Flask. Sử dụng api_key để xác định request của ví điện tử nào. api_key được thêm vào Header khi request. Demo api key cho Momo: 2d4278333671cd4b6b06a74742ebbca1.
- Export Postman trong file Flask API.postman_collection.json
- Các Restful API:
```
 + Rạp:
  + /api/cinema: method GET, lấy danh sách các rạp chiếu phim.
  + /api/cinema/<id>: method GET, thông tin rạp chiếu phim theo id.
  + /api/cinema/<name>: method GET, thông tin rạp chiếu phim theo tên rạp.
 + Phim:
  + /api/movie: method GET, lấy danh sách các phim.
  + /api/movie/<id>: method GET, thông tin phim theo id.
  + /api/movie/<name>: method GET, thông tin phim theo tên phim.
  + /api/movie/cinema/<cinema_id>: method GET, danh sách thông tin phim theo rạp id.
 + Lịch chiếu:
  + /api/showtime/movie/<movie_id>: method GET, lấy danh sách lịch chiếu theo phim.
  + /api/showtime/cinema/<cinema_id>: method GET, lấy danh sách lịch chiếu theo cinema.
  + /api/showtime/<cinema_id>/<movie_id>: method GET, lấy danh sách lịch chiếu theo cinema và phim.
 + Ghế ngồi:
    + api/sheets/<int:showtime_id>: lấy danh sách các ghế ngồi trong giờ chiếu, gái trị trả về là dạng object với thông tin mã ghế, số ghế ngồi, tình trạng đặt, số tiền.
 + Đặt vé:
   + api/sheet/booking: method POST, PUT. Dữ liệu cần truyền gồm mã ghế và tình trạng đặt. Trả về lỗi khi:
    - Nếu ghế không tồn tại.
    - Nếu ghế đã được đặt và tình trạng truyền là True.
    - Nếu ghế chưa được đặt và trạng thái truyền là False.
```


3. Report đế thống kê:
- TODO

4. Setup Docker:
- Dockerfile:
  - Tạo Dockerfile từ image pyhon version3.6,
  - Copy thư mục source code vào /app trong docker.
  - Cài đặt các libraries trong requirements.txt
  - chạy file app.py để start Flask
- Docker compose:
  - Tạo service flask build từ Dockerfile trong cùng thư mục.
  - Chỉnh port 5000

5. Setup CD/CD
- Sử dụng Python Application CI của github, chạy pytest cho file test_app.py
