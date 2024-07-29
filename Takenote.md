# SQL
---
## SQL là gì?

SQL là viết tắt của **Structured Query Language**, dịch sang tiếng Việt là **Ngôn ngữ Truy vấn Có Cấu trúc**. Đây là một ngôn ngữ lập trình tiêu chuẩn, được sử dụng rộng rãi để **tương tác với các cơ sở dữ liệu quan hệ** (Relational Database Management System - RDBMS).

Vai trò của SQL:
+ Tạo, sửa đổi và xóa cơ sở dữ liệu: Bạn có thể tạo các bảng, cột, chỉ mục (index) và các đối tượng khác trong cơ sở dữ liệu bằng SQL.
+ Truy vấn dữ liệu: SQL cho phép bạn tìm kiếm, lọc và sắp xếp dữ liệu từ các bảng khác nhau.
+ Cập nhật dữ liệu: Bạn có thể thêm, sửa hoặc xóa dữ liệu trong các bảng hiện có.
+ Kiểm soát quyền truy cập: SQL giúp bạn xác định ai có thể truy cập vào dữ liệu và thực hiện các hoạt động nào.

Ví dụ về câu lệnh SQL:

```SQL
SQL
SELECT * FROM Customers;  -- Lấy tất cả dữ liệu từ bảng Customers
INSERT INTO Customers (CustomerName, ContactName) VALUES ('Alfreds Futterkiste', 'Maria Anders');  -- Thêm một bản ghi mới vào bảng Customers
```

## Các loại SQL

Mặc dù SQL là một ngôn ngữ chuẩn, nhưng có một số loại SQL khác nhau tùy thuộc vào hệ quản trị cơ sở dữ liệu cụ thể mà bạn sử dụng. Tuy nhiên, tất cả các loại SQL đều dựa trên các tiêu chuẩn cơ bản giống nhau.

Các loại SQL phổ biến:

+ SQL tiêu chuẩn: Đây là tập hợp các câu lệnh SQL được định nghĩa bởi **ANSI** (American National Standards Institute) và **ISO** (International Organization for Standardization).
+ SQL mở rộng: Các hệ quản trị cơ sở dữ liệu khác nhau có thể cung cấp các mở rộng riêng cho ngôn ngữ SQL để đáp ứng các nhu cầu cụ thể. Ví dụ:
  + PL/SQL: Một ngôn ngữ lập trình thủ tục được phát triển bởi Oracle.
  + T-SQL: Một ngôn ngữ lập trình thủ tục được phát triển bởi Microsoft SQL Server.
  + MySQL: Một hệ quản trị cơ sở dữ liệu mã nguồn mở cũng có các mở rộng riêng của SQL.

## Các loại câu lệnh SQL

+ DDL (Data Definition Language): Các câu lệnh dùng để định nghĩa cấu trúc của cơ sở dữ liệu, ví dụ: CREATE, ALTER, DROP.
+ DML (Data Manipulation Language): Các câu lệnh dùng để thao tác với dữ liệu, ví dụ: SELECT, INSERT, UPDATE, DELETE.
+ DQL (Data Query Language): Một tập hợp con của DML, chuyên dùng để truy vấn dữ liệu.
+ DCL (Data Control Language): Các câu lệnh dùng để kiểm soát quyền truy cập vào dữ liệu, ví dụ: GRANT, REVOKE.
+ TCL (Transaction Control Language): Các câu lệnh dùng để kiểm soát các giao dịch, ví dụ: COMMIT, ROLLBACK.

## Tại sao nên học SQL?

SQL là một kỹ năng rất quan trọng cho bất kỳ ai làm việc với dữ liệu. Việc nắm vững SQL sẽ giúp bạn:
+ Truy xuất và phân tích dữ liệu hiệu quả: Bạn có thể dễ dàng trích xuất thông tin hữu ích từ các cơ sở dữ liệu lớn.
+ Tự động hóa các tác vụ lặp đi lặp lại: SQL giúp bạn viết các script để thực hiện các tác vụ một cách tự động.
+ Cải thiện hiệu suất làm việc: Viết các truy vấn SQL hiệu quả giúp bạn tiết kiệm thời gian và tài nguyên.

## Hệ quản trị cơ sở dữ liệu

+ Các hệ quản trị cơ sở dữ liệu quan hệ phổ biến: MySQL, PostgreSQL, SQL Server, Oracle
+ Các khái niệm cơ bản về cơ sở dữ liệu: bảng, cột, hàng, khóa chính, khóa ngoại
+ Các phép toán quan hệ: JOIN, UNION, INTERSECT, EXCEPT
+ Các hàm và biểu thức trong SQL: hàm toán học, hàm chuỗi, hàm ngày tháng

## Cơ sở dữ liệu được tạo ra ntn
Quá trình tạo một cơ sở dữ liệu (CSDL) bao gồm nhiều giai đoạn, từ việc lên ý tưởng đến triển khai thực tế.
1. Xác định mục tiêu và yêu cầu:
+ Mục tiêu: CSDL sẽ được sử dụng để làm gì? Lưu trữ thông tin gì? Phục vụ cho đối tượng nào?
+ Yêu cầu: CSDL cần đáp ứng những yêu cầu nào về dung lượng, tốc độ truy xuất, bảo mật, khả năng mở rộng?
2. Thiết kế cấu trúc CSDL:
+ Xác định các thực thể: Nhận dạng các đối tượng cần lưu trữ (ví dụ: khách hàng, sản phẩm, đơn hàng).
+ Xác định các thuộc tính: Xác định các đặc tính của mỗi thực thể (ví dụ: tên khách hàng, giá sản phẩm, ngày đặt hàng).
+ Xây dựng mối quan hệ: Xác định mối liên hệ giữa các thực thể (ví dụ: một khách hàng có thể đặt nhiều đơn hàng).
+ Chọn mô hình dữ liệu: Lựa chọn mô hình phù hợp (quan hệ, đồ thị, NoSQL,...) dựa trên yêu cầu của hệ thống.
3. Chọn hệ quản trị CSDL (DBMS):
+ Đánh giá các DBMS: So sánh các DBMS khác nhau về tính năng, hiệu suất, chi phí, và khả năng tương thích với hệ thống hiện có.
+ Các DBMS phổ biến: MySQL, PostgreSQL, Oracle, SQL Server, MongoDB,...
4. Viết các câu lệnh SQL:
+ Tạo bảng: Sử dụng câu lệnh CREATE TABLE để tạo các bảng tương ứng với các thực thể.
+ Xác định khóa chính: Xác định cột hoặc nhóm cột duy nhất xác định một hàng trong bảng.
+ Tạo mối quan hệ: Sử dụng khóa ngoại để tạo liên kết giữa các bảng.
+ Tạo chỉ mục: Tạo chỉ mục để tăng tốc độ truy vấn.
5. Nhập dữ liệu:
+ Nhập thủ công: Nhập dữ liệu trực tiếp vào các bảng.
+ Nhập từ file: Nhập dữ liệu từ các file có định dạng như CSV, Excel.
+ Kết nối với các nguồn dữ liệu khác: Kết nối với các hệ thống khác để lấy dữ liệu.
6. Kiểm thử và tối ưu hóa:
+ Kiểm tra tính toàn vẹn: Đảm bảo dữ liệu được nhập chính xác và không có xung đột.
+ Kiểm tra hiệu suất: Đo lường thời gian thực hiện các truy vấn và tối ưu hóa nếu cần.
+ Điều chỉnh cấu hình: Điều chỉnh các thông số cấu hình của DBMS để đạt hiệu suất tốt nhất.
7. Triển khai và bảo trì:
+ Cài đặt: Cài đặt CSDL lên máy chủ.
+ Sao lưu: Thực hiện sao lưu thường xuyên để phòng ngừa mất dữ liệu.
+ Bảo mật: Đặt các biện pháp bảo mật để bảo vệ dữ liệu khỏi truy cập trái phép.
+ Cập nhật: Cập nhật CSDL khi có thay đổi về yêu cầu hoặc cấu trúc dữ liệu.
+ 
Các công cụ hỗ trợ:
+ Các phần mềm vẽ ER diagram: Visio, Lucidchart,...
+ Các IDE: MySQL Workbench, Visual Studio Code,...

Ví dụ đơn giản:
Giả sử bạn muốn tạo một CSDL để quản lý thông tin khách hàng của một cửa hàng. Bạn sẽ có các bảng như:

+ Khách hàng: Mã khách hàng, tên, địa chỉ, số điện thoại.
+ Đơn hàng: Mã đơn hàng, ngày đặt hàng, tổng tiền, mã khách hàng.
+ Sản phẩm: Mã sản phẩm, tên sản phẩm, giá.

```SQL
CREATE TABLE KhachHang (
    MaKH INT PRIMARY KEY,
    TenKH VARCHAR(50),
    DiaChi VARCHAR(100),
    SDT VARCHAR(20)
);

CREATE TABLE DonHang (
    MaDH INT PRIMARY KEY,
    NgayDatHang DATE,
    TongTien DECIMAL(10,2),
    MaKH INT,
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH)
);
```



