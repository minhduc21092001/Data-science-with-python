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