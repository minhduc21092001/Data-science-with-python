### Udacity
# Programming for data science nanodegree
---
## Looking ahead
Why we need programming for analysis?
2 điều quan trọng trong phân tích dữ liệu là thống kê và lập trình.
Lập trình quan trọng ntn?
Điều đầu tiên là programming cho phép bạn làm việc với các tập dữ liệu lớn/dataset hơn là làm việc với excel, gg sheet vô cùng thủ công.
Làm sao mà gg có thể xử lý hàng tỉ tỉ queries mỗi năm? Cũng như các nền tảng khác làm sao để xử lý lượng traffic khổng lồ từ khắp nơi trên thế giới?
Điều thứ 2 là programming cho phép tự động hóa các processes, điều mà trước đây phải được thực hiện một cách thủ công và tốn thời gian.

## Projects
Học phải đi đôi với hành! Learning by doing!
Project 1: Sử dụng SQL với cơ sở dữ liệu quan hệ về online DVD rentals.
Project 2: Sử dụng Python để phân tích bike share data được thu thập từ 3 cities.
Project 3: Build Github profile để share về các project khác.

## Projects and progress
Không nhất thiết phải xem hết các videos nhưng phải làm hết các projects.
Xong projects là xong khóa học, tuy nhiên xem videos để học kiến thức chứ không phải vô bổ.

## Integrity and mindset
Không lấy bài của người khác để nộp, tự mình làm thì sẽ học được nhiều hơn. Hãy tin vào khả năng của mình, mở rộng giới hạn của bản thân.

## Leaning strategies
1. Space your learning, học trải đều hàng ngày chứ đừng học dồn một lúc.
2. Write notes, don't type note, mục đích để có thời gian ngấm thông tin, não bộ và tay làm việc với nhau.
3. Recall, don't just read your notes, hãy cố nhớ chứ đừng đọc lại, giống việc cô giáo kiểm tra thuộc bài cũ.
4. Connect the concepts, những cái đã học liên quan tới nhau ntn, giống nhau ntn, khác nhau ntn, tại sao chúng lại như thế?
5. Mistakes are learning opportunities, thất bại là mẹ thành công, học từ thất bại.

## Basic SQL
### Lesson Overview
In this lesson, we will cover and you will be able to:

+ Describe why SQL is important
+ Explain how SQL data is stored and structured
+ Create SQL queries using proper syntax including
    + SELECT & FROM
    + LIMIT
    + ORDER BY
    + WHERE
    + Basic arithmetic operations
    + LIKE
    + IN
    + NOT
    + AND & BETWEEN & OR

There is a lot to cover so let's get started!

### The Parch & Posey Database
In this course, we will mostly be using the Parch & Posey database for our queries. Whenever we use a different database, we will let you know.

Parch & Posey (not a real company) is a paper company and the database includes sales data for their paper.

Using the sales data, you'll be able to put your SQL skills to work with data you would find in the real world.

### Entity relationship diagrams (ERD)
An entity-relationship diagram (ERD) is a common way to view data in a database. Below is the ERD for the database we will use from Parch & Posey. These diagrams help you visualize the data you are analyzing including:

1. The names of the tables.
2. The columns in each table.
3. The way the tables work together.

You can think of each of the boxes below as a spreadsheet.

**Parch & Posey Database ERD**
**web_events**
![alt text](image-1.png)
Relationship:

account_id in the web_events table is a foreign key linked to the id (primary key) in the accounts table.
![alt text](image-2.png)
Relationship:

sales_rep_id in the accounts table is a foreign key linked to the id (primary key) in the sales_reps table.
![alt text](image-3.png)
Relationship:

account_id in the orders table is a foreign key linked to the id (primary key) in the accounts table.
![alt text](image-4.png)
Relationship:

region_id in the sales_reps table is a foreign key linked to the id (primary key) in the region table.
![alt text](image-5.png)
**What to Notice**
In the Parch & Posey database there are five tables (essentially 5 spreadsheets):

1. web_events
2. accounts
3. orders
4. sales_reps
5. region

You can think of each of these tables as an individual spreadsheet. Then the columns in each spreadsheet are listed below the table name. For example, the region table has two columns: id and name. Alternatively, the web_events table has four columns.

![alt text](image-6.png)
The "crow's foot" that connects the tables together shows us how the columns in one table relate to the columns in another table. In this first lesson, you will be learning the basics of how to work with SQL to interact with a single table. In the next lesson, you will learn more about why these connections are so important for working with SQL and relational databases.

Quiz 1:
![alt text](image-7.png)

### Why SQL is Important
**Introduction**

Before we dive into writing Structured Query Language (SQL) queries, let's take a look at what makes SQL and the databases that utilize SQL so popular.

I think it is an important distinction to say that SQL is a language. Hence, the last word of SQL being language. SQL is used all over the place beyond the databases we will utilize in this class. With that being said, SQL is most popular for its interaction with databases. For this class, you can think of a database as a bunch of excel spreadsheets all sitting in one place. Not all databases are a bunch of excel spreadsheets sitting in one place, but it is a reasonable idea for this class.

**Why Do Data Analysts Use SQL?**
Tại sao lại sử dụng SQL?
Có từ lâu đời.
Là ngôn ngữ tiêu chuẩn.
![alt text](image-9.png)
Với SQL ta có thể phân tích sâu hơn, ví dụ so sánh với gg analytics
![alt text](image-10.png)
There are some major advantages to using traditional relational databases, which we interact with using SQL. The five most apparent are:

+ SQL is easy to understand.
+ Traditional databases allow us to access data directly.
+ Traditional databases allow us to audit and replicate our data.
+ SQL is a great tool for analyzing multiple tables at once.
+ SQL allows you to analyze more complex questions than dashboard tools like Google Analytics.

You will experience these advantages first hand, as we learn to write SQL to interact with data.

I realize you might be getting a little nervous or anxious to start writing code. This might even be the first time you have written in any sort of programming language. I assure you, we will work through examples to help assure you feel supported the whole time to take on this new challenge!

**SQL vs. NoSQL**
You may have heard of NoSQL, which stands for not only SQL. Databases using NoSQL allow you to write code that interacts with the data a bit differently than what we will do in this course. These NoSQL environments tend to be particularly popular for web-based data, but less popular for data that lives in spreadsheets the way we have been analyzing data up to this point. One of the most popular NoSQL languages is called MongoDB(opens in a new tab). Udacity has a full course on MongoDB that you can take for free here(opens in a new tab), but these will not be a focus of this program.

NoSQL is not a focus for this course, but you might see it referenced in the real world!

**Code from the Video**
Throughout the course, you can copy and paste the code from the video walkthroughs into the workspaces to try things out yourself. Even better you can practice writing the queries to help build muscle memory for writing SQL commands.

```SQL
SELECT account_id,
       occurred_at,
       standard_qty,
       gloss_qty,
       poster_qty
FROM orders
WHERE (standard_qty = 0 OR gloss_qty = 0 OR poster_qty = 0)
AND occurred_at = '2016-10-01'
```
Below is the workspace where you can write your queries. Once you write your queries against the above mentioned questions, you can click on the EVALUATE button at the bottom of the workspace.

Hầu hết các ứng dụng đều cần lưu trữ data để có thể lấy ra sử dụng sau này. Ví dụ như Twitter, mỗi bài đăng cần được lưu trữ để mọi người có thể xem được.
![alt text](image-8.png)
Twitter sẽ lưu hàng tá thông tin về bài Tweet, như là ai là tác giả, thời gian viết, bao nhiêu tym, có nhắc đến ai không, ... rất rất nhiều thứ.
Tất cả thông tin được sử dụng để xác định ai sẽ nhìn được bài Tweet và khi nào họ sẽ nhìn thấy nó, ...
Data integrity?
Make sure that the data entered is consistent.
Vd: số người con của tôi thì chắc chắn phải là số nguyên, không thể là số thập phân kiểu 1.8 người con?
Database tối ưu tốc độ xử lý/phản hồi, phân quyền truy cập

**Why Businesses Like Databases**
1. Data integrity is ensured - only the data you want to be entered is entered, and only certain users are able to enter data into the database.
2. Data can be accessed quickly - SQL allows you to obtain results very quickly from the data stored in a database. Code can be optimized to quickly pull results.
3. Data is easily shared - multiple individuals can access data stored in a database, and the data is the same for all users allowing for consistent results for anyone with access to your database.

### Why SQL is Important
![alt text](image-11.png)
Database lưu dữ liệu thành các bảng, mỗi bảng gồm nhiều cột, tên các cột là duy nhất, kiểu dữ liệu được lưu trong các cột là giống nhau, text là text mà số là số.
A few key points about data stored in SQL databases:

1. **Data in databases is stored in tables that can be thought of just like Excel spreadsheets**. For the most part, you can think of a database as a bunch of Excel spreadsheets. Each spreadsheet has rows and columns. Where each row holds data on a transaction, a person, a company, etc., while each column holds data pertaining to a particular aspect of one of the rows you care about like a name, location, a unique id, etc.

2. **All the data in the same column must match in terms of data type**.
An entire column is considered quantitative, discrete, or as some sort of string. This means if you have one row with a string in a particular column, the entire column might change to a text data type. This can be very bad if you want to do math with this column!

3. **Consistent column types are one of the main reasons working with databases is fast**. Often databases hold a LOT of data. So, knowing that the columns are all of the same types of data means that obtaining data from a database can still be fast.

### Types of Databases
**SQL Databases**
There are many different types of SQL databases designed for different purposes. In this course, we will use Postgres(opens in a new tab) within the classroom, which is a popular open-source database with a very complete library of analytical functions. (Note: You do not need to install PostgreSQL on your computer unless you really want to. We provide SQL environments in the classroom for you to work in.)

Some of the most popular databases include:

1. MySQL
2. Access
3. Oracle
4. Microsoft SQL Server
5. Postgres

You can also write SQL within other programming frameworks like Python, Scala, and Hadoop.

**Small Differences**
Each of these SQL databases may have subtle differences in syntax and available functions -- for example, MySQL doesn’t have some of the functions for modifying dates as Postgres. Most of what you see with Postgres will be directly applicable to using SQL in other frameworks and database environments. For the differences that do exist, you should check the documentation. Most SQL environments have great documentation online that you can easily access with a quick Google search.

The article on relational databases(opens in a new tab) compares three of the most common types of SQL: SQLite, PostgreSQL, and MySQL. Again, once you have learned how to write SQL in one environment, the skills are mostly transferable.

So with that, let's jump in!

### Types of Statements
The key to SQL is understanding statements. A few statements include:

1. CREATE TABLE is a statement that creates a new table in a database.
2. DROP TABLE is a statement that removes a table in a database.
3. SELECT allows you to read data and display it. This is called a query.

The SELECT statement is the common statement used by analysts, and you will be learning all about them throughout this course!

Là 1 data analyst chúng ta ít khi cập nhật thêm sửa xóa dữ liệu mà thay vào đó là đọc và tận dụng dữ liệu.
Quiz
![alt text](image-12.png)

### SELECT & FROM
Here you were introduced to the SQL command that will be used in every query you write: SELECT ... FROM ....

1. **SELECT** indicates which column(s) you want to be given the data for.

2. **FROM** specifies from which table(s) you want to select the columns. Notice the columns need to exist in this table.

If you want to be provided with the data from all columns in the table, you use "*", like so:

> SELECT * FROM orders

Note that using SELECT does not create a new table with these columns in the database, it just provides the data to you as the results, or output, of this command.

You will use this SQL SELECT statement in every query in this course, but you will be learning a few additional statements and operators that can be used along with them to ask more advanced questions of your data.

### Formatting Best Practices
![alt text](image-13.png)
However, you may have noticed that we have been capitalizing SELECT and FROM, while we leave table and column names in lower case. This is because even though SQL is case-insensitive, **it is common and best practice to capitalize all SQL commands, like SELECT and FROM, and keep everything else in your query lower case.**

Capitalizing command words makes queries easier to read, which will matter more as you write more complex queries. For now, it is just a good habit to start getting into, to make your SQL queries more readable.

One other note: The text data stored in SQL tables can be either upper or lower case, and SQL **is case-sensitive in regard to this text data.**

**Avoid Spaces in Table and Variable Names**
It is common to use **underscores** and avoid spaces in column names. It is a bit annoying to work with spaces in SQL. In Postgres, if you have spaces in column or table names, you need to refer to these columns/tables with double quotes around them (Ex: FROM "Table Name" as opposed to FROM table_name). In other environments, you might see this as square brackets instead (Ex: FROM [Table Name]).
![alt text](image-14.png)
![alt text](image-15.png)
Phew!!! That was a lot of rules. Let's just write some queries. You will make mistakes, but that is part of the learning process!

# LIMIT
We have already seen the SELECT (to choose columns) and FROM (to choose tables) statements. The LIMIT statement is useful when you want to see just the first few rows of a table. This can be much faster for loading than if we load the entire dataset.

The LIMIT command is always the very last part of a query. An example of showing just the first 10 rows of the orders table with all of the columns might look like the following:
![alt text](image-16.png)
![alt text](image-17.png)

### ORDER BY
The ORDER BY statement allows us to sort our results using the data in any column. If you are familiar with Excel or Google Sheets, using ORDER BY is similar to sorting a sheet using a column. **A key difference, however, is that using ORDER BY in a SQL query only has temporary effects, for the results of that query, unlike sorting a sheet by column in Excel or Sheets.**

In other words, when you use ORDER BY in a SQL query, your output will be sorted that way, but then the next query you run will encounter the unsorted data again. It's important to keep in mind that this is different than using common spreadsheet software, where sorting the spreadsheet by column actually alters the data in that sheet until you undo or change that sorting. This highlights the meaning and function of a SQL "query."

The ORDER BY statement always comes in a query after the SELECT and FROM statements, but before the LIMIT statement. If you are using the LIMIT statement, **it will always appear last. As you learn additional commands, the order of these statements will matter more.**

**Pro-Tip**
Remember **DESC** can be added after the column in your ORDER BY statement to sort in descending order, as the default is to sort in ascending order.
![alt text](image-18.png)

### ORDER BY Part II
Here, we saw that we can ORDER BY more than one column at a time. When you provide a list of columns in an ORDER BY command, the sorting occurs using **the leftmost column in your list first**, then the next column from the left, and so on. We still have the ability to flip the way we order using DESC.
![alt text](image-19.png)
This query selected account_id and total_amt_usd from the orders table, and orders the results first by total_amt_usd in descending order and then account_id.
**Solutions to previous ORDER BY Questions**
1. Write a query that displays the order ID, account ID, and total dollar amount for all the orders, sorted first by the account ID (in ascending order), and then by the total dollar amount (in descending order).
```SQL
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY account_id, total_amt_usd DESC;
```
2. Now write a query that again displays order ID, account ID, and total dollar amount for each order, but this time sorted first by total dollar amount (in descending order), and then by account ID (in ascending order).
```SQL
SELECT id, account_id, total_amt_usd
FROM orders
ORDER BY total_amt_usd DESC, account_id;
```
Compare the results of these two queries above. How are the results different when you switch the column you sort on first? **In query #1, all of the orders for each account ID are grouped together, and then within each of those groupings, the orders appear from the greatest order amount to the least. In query #2, since you sorted by the total dollar amount first, the orders appear from greatest to least regardless of which account ID they were from. Then they are sorted by account ID next. (The secondary sorting by account ID is difficult to see here since only if there were two orders with equal total dollar amounts would there need to be any sorting by account ID.)**

### WHERE
Using the WHERE statement, we can display subsets of tables based on conditions that must be met. You can also think of the WHERE command as filtering the data.

This video above shows how this can be used, and in the upcoming concepts, you will learn some common operators that are useful with the WHERE statement.

Common symbols used in WHERE statements include:

1. \> (greater than)

2. < (less than)

3. \>= (greater than or equal to)

4. <= (less than or equal to)

5. = (equal to)

6. != (not equal to)

![alt text](image-20.png)

![alt text](image-21.png)

![alt text](image-22.png)

### WHERE with Non-Numeric Data
The WHERE statement can also be used with non-numeric data. We can use the = and != operators here. You need to be sure to use single quotes (just be careful if you have quotes in the original text) with the text data, not double quotes.

Commonly when we are using WHERE with non-numeric data fields, we use the LIKE, NOT, or IN operators. We will see those before the end of this lesson!
![alt text](image-23.png)
![alt text](image-24.png)
![alt text](image-25.png)
**Note: If you received an error message when executing your query, remember that SQL requires single-quotes, not double-quotes, around text values like 'Exxon Mobil.'**

### Arithmetic Operators
**Derived Columns**
Creating a new column that is a combination of existing columns is known as a derived column (or "calculated" or "computed" column). Usually, you want to give a name, or "alias," to your new column using the **AS** keyword.

This derived column, and its alias, are generally only temporary, existing just for the duration of your query. The next time you run a query and access this table, the new column will not be there.

If you are deriving the new column from existing columns using a mathematical expression, then these familiar mathematical operators will be useful:

```
1. * (Multiplication)
2. + (Addition)
3. - (Subtraction)
4. / (Division)
```

Consider this example:

```SQL
SELECT id, (standard_amt_usd/total_amt_usd)*100 AS std_percent, total_amt_usd
FROM orders
LIMIT 10;
```
Here we divide the standard paper dollar amount by the total order amount to find the standard paper percent for the order, and use the **AS** keyword to name this new column "std_percent." You can run this query on the next page if you'd like, to see the output.
![alt text](image-26.png)
![alt text](image-27.png)
![alt text](image-28.png)
![alt text](image-29.png)

### Introduction to Logical Operators
In the next concepts, you will be learning about Logical Operators. Logical Operators include:

1. LIKE This allows you to perform operations similar to using WHERE and =, but for cases when you might not know exactly what you are looking for.
2. IN This allows you to perform operations similar to using WHERE and =, but for more than one condition.
3. NOT This is used with IN and LIKE to select all of the rows NOT LIKE or NOT IN a certain condition.
4. AND & BETWEEN These allow you to combine operations where all combined conditions must be true.
5. OR This allows you to combine op

### LIKE
The LIKE operator is extremely useful for working with text. You will use LIKE within a WHERE clause. The LIKE operator is frequently used with %. The % tells us that we might want any number of characters leading up to a particular set of characters or following a certain set of characters, as we saw with the google syntax above. Remember you will need to use single quotes for the text you pass to the LIKE operator because these lower and uppercase letters are not the same within the string. Searching for 'T' is not the same as searching for 't'. In other SQL environments (outside the classroom), you can use either single or double-quotes.

Hopefully, you are starting to get more comfortable with SQL, as we are starting to move toward operations that have more applications, but this also means we can't show you every use case. Hopefully, you can start to think about how you might use these types of applications to identify phone numbers from a certain region or an individual where you can't quite remember the full name.
![alt text](image-30.png)
*Note: wild card % mang ý nghĩa là nó có thể đại diện cho bất kỳ chuỗi kí tự nào đó vd: xy46google78yzwr.
![alt text](image-31.png)
![alt text](image-32.png)

### IN
The IN operator is useful for working with both numeric and text columns. This operator allows you to use an =, but for more than one item of that particular column. We can check one, two, or many column values for which we want to pull data, but all within the same query. In the upcoming concepts, you will see the OR operator that would also allow us to perform these tasks, but the IN operator is a cleaner way to write these queries.
![alt text](image-33.png)
**Expert Tip**
In most SQL environments, although not in our Udacity's classroom, you can use single or double quotation marks - and you may NEED to use double quotation marks if you have an apostrophe within the text you are attempting to pull.

In our Udacity SQL workspaces, note you can include an apostrophe by putting two single quotes together. For example, Macy's in our workspace would be 'Macy''s'.
![alt text](image-34.png)
![alt text](image-35.png)
![alt text](image-36.png)
![alt text](image-37.png)

### NOT
The NOT operator is an extremely useful operator for working with the previous two operators we introduced: IN and LIKE. By specifying NOT LIKE or NOT IN, we can grab all of the rows that do not meet particular criteria.
![alt text](image-38.png)
![alt text](image-39.png)
![alt text](image-40.png)
![alt text](image-41.png)

### AND and BETWEEN
![alt text](image-42.png)
**BETWEEN Operator**
Sometimes we can make a cleaner statement using **BETWEEN** than we can use **AND**. Particularly this is true when we are using the same column for different parts of our **AND** statement. In the previous video, we probably should have used **BETWEEN**.
![alt text](image-43.png)
![alt text](image-44.png)
![alt text](image-45.png)
![alt text](image-46.png)
![alt text](image-47.png)
```SQL
SELECT *
FROM web_events
WHERE channel IN ('organic', 'adwords') AND occurred_at BETWEEN '2016-01-01' AND '2017-01-01'
ORDER BY occurred_at DESC;
```

### OR
![alt text](image-48.png)
Sử dụng ngoặc để kết hợp AND với OR
![alt text](image-49.png)
![alt text](image-50.png)
![alt text](image-51.png)

### Lession recap

**Commands**
You have already learned a lot about writing code in SQL! Let's take a moment to recap all that we have covered before moving on:
![alt text](image-52.png)
*Note: BETWEEN và IN có lấy điều kiện biên

![alt text](image-53.png)
![alt text](image-54.png)
![alt text](image-55.png)

## SQL Join
![alt text](image-56.png)
So above, we understand that all of the information related to an account is not in the orders table, but why not? Watch the below video to find out!
![alt text](image-57.png)
![alt text](image-58.png)
![alt text](image-60.png)
![alt text](image-59.png)
Có thể thấy 1 bảng thì thông thường chỉ cần thay đổi thông tin, số lượng hàng không thay đổi, còn 1 bảng thì cần thêm hàng liên tục khi người dùng mua thêm nhiều đơn mới, nên cần thiết tách thành bảng riêng để dễ dàng quản lý.
![alt text](image-61.png)
![alt text](image-62.png)
*Note: Nếu gộp bảng một cách không khoa học, thì khi thông tin của 1 người dùng bị thay đổi, cần cập nhật ở rất nhiều hàng, dẫn tới việc tốn kém xử lý

### JOIN
![alt text](image-63.png)
![alt text](image-64.png)
![alt text](image-65.png)
![alt text](image-66.png)
![alt text](image-67.png)
![alt text](image-68.png)
Joining tables allows you access to each of the tables in the SELECT statement through the table name, and the columns will always follow a . after the table name.

Now it's your turn.
![alt text](image-69.png)
![alt text](image-70.png)
![alt text](image-72.png)
![alt text](image-73.png)
![alt text](image-74.png)
![alt text](image-75.png)
![alt text](image-76.png)
![alt text](image-77.png)
![alt text](image-78.png)
![alt text](image-79.png)
![alt text](image-80.png)
![alt text](image-81.png)
![alt text](image-82.png)
![alt text](image-83.png)
![alt text](image-84.png)
![alt text](image-85.png)
![alt text](image-86.png)
![alt text](image-87.png)
![alt text](image-88.png)
![alt text](image-89.png)
![alt text](image-90.png)
![alt text](image-91.png)
![alt text](image-92.png)
![alt text](image-93.png)
![alt text](image-94.png)
![alt text](image-95.png)
![alt text](image-96.png)
![alt text](image-97.png)
![alt text](image-98.png)
![alt text](image-99.png)
![alt text](image-100.png)
![alt text](image-101.png)
![alt text](image-102.png)
![alt text](image-103.png)
![alt text](image-104.png)
![alt text](image-105.png)

### JOIN AND FILTER
![alt text](image-106.png)
![alt text](image-107.png)
![alt text](image-108.png)
![alt text](image-109.png)
![alt text](image-110.png)
![alt text](image-111.png)
![alt text](image-112.png)
![alt text](image-113.png)
![alt text](image-114.png)
![alt text](image-115.png)
![alt text](image-116.png)
![alt text](image-117.png)
![alt text](image-118.png)
![alt text](image-119.png)
![alt text](image-120.png)
![alt text](image-121.png)

## Aggregation
![alt text](image-122.png)
![alt text](image-123.png)
![alt text](image-124.png)
Không có dữ liệu, bị xóa hoặc thiếu thông tin, khi cần liên lạc thì không có thông tin để liên hệ
![alt text](image-125.png)
![alt text](image-126.png)
![alt text](image-127.png)
![alt text](image-128.png)
![alt text](image-129.png)
![alt text](image-130.png)
![alt text](image-131.png)
![alt text](image-132.png)
![alt text](image-133.png)
![alt text](image-134.png)
![alt text](image-135.png)
![alt text](image-136.png)
![alt text](image-137.png)
![alt text](image-138.png)
![alt text](image-139.png)
![alt text](image-140.png)
![alt text](image-141.png)
![alt text](image-142.png)
![alt text](image-143.png)
![alt text](image-144.png)
![alt text](image-145.png)
![alt text](image-146.png)
![alt text](image-147.png)
![alt text](image-148.png)
![alt text](image-149.png)
![alt text](image-150.png)
![alt text](image-151.png)
![alt text](image-152.png)
![alt text](image-154.png)
![alt text](image-153.png)
![alt text](image-155.png)
![alt text](image-156.png)
![alt text](image-157.png)
![alt text](image-158.png)
![alt text](image-159.png)
![alt text](image-160.png)
![alt text](image-161.png)
![alt text](image-162.png)
![alt text](image-163.png)
![alt text](image-164.png)
![alt text](image-165.png)
![alt text](image-166.png)
![alt text](image-167.png)
![alt text](image-168.png)
![alt text](image-169.png)
![alt text](image-170.png)
![alt text](image-171.png)
![alt text](image-172.png)
![alt text](image-173.png)
![alt text](image-174.png)
![alt text](image-175.png)
![alt text](image-176.png)
![alt text](image-177.png)
![alt text](image-178.png)
Day of the week
![alt text](image-179.png)
![alt text](image-180.png)
![alt text](image-181.png)
![alt text](image-182.png)
![alt text](image-183.png)
![alt text](image-184.png)
![alt text](image-185.png)
![alt text](image-186.png)
![alt text](image-187.png)
![alt text](image-188.png)
![alt text](image-189.png)
Mô tả lại sẽ clear hơn và giống với lable hơn
![alt text](image-190.png)
![alt text](image-191.png)
![alt text](image-192.png)
![alt text](image-193.png)
![alt text](image-194.png)
![alt text](image-195.png)
![alt text](image-196.png)
![alt text](image-197.png)
![alt text](image-198.png)
![alt text](image-199.png)
![alt text](image-200.png)
![alt text](image-201.png)
![alt text](image-202.png)

## Subqueries
![alt text](image-203.png)
![alt text](image-204.png)
![alt text](image-205.png)
![alt text](image-206.png)
![alt text](image-207.png)
![alt text](image-209.png)
take a stab at this quiz: hãy đâm 1 nhát vào bài quiz này haha
![alt text](image-210.png)
![alt text](image-211.png)
![alt text](image-212.png)
![alt text](image-213.png)
![alt text](image-214.png)
caveat -> cảnh báo
![alt text](image-215.png)
![alt text](image-216.png)
![alt text](image-217.png)
![alt text](image-218.png)
![alt text](image-219.png)
![alt text](image-220.png)
![alt text](image-221.png)
![alt text](image-222.png)
![alt text](image-223.png)
![alt text](image-224.png)
![alt text](image-225.png)
![alt text](image-226.png)
![alt text](image-227.png)
![alt text](image-228.png)
![alt text](image-229.png)
![alt text](image-230.png)
![alt text](image-231.png)
![alt text](image-232.png)
![alt text](image-233.png)
