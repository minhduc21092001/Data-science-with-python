# Project1
---
## Project Overview
![alt text](image-234.png)
## Project Details
![alt text](image-235.png)
![alt text](image-236.png)
## Workspace vs. Local environment
![alt text](image-237.png)
![alt text](image-238.png)
## Set Up Your Local Environment

## Composite Key
![alt text](image-239.png)
![alt text](image-240.png)
![alt text](image-241.png)
![alt text](image-242.png)
## Workspace: DVD Rental Database
![alt text](image-243.png)
## Practice Solution #1
![alt text](image-244.png)
Dấu ``` bị thừa
![alt text](image-245.png)
![alt text](image-246.png)
## Practice Solution #2
![alt text](image-247.png)
![alt text](image-248.png)
```SQL
SELECT    DISTINCT(filmlen_groups),
          COUNT(title) OVER (PARTITION BY filmlen_groups) AS filmcount_bylencat
FROM  
         (SELECT title,length,
      	CASE WHEN length <= 60 THEN '1 hour or less'
      	WHEN length > 60 AND length <= 120 THEN 'Between 1-2 hours'
      	WHEN length > 120 AND length <= 180 THEN 'Between 2-3 hours'
      	ELSE 'More than 3 hours' END AS filmlen_groups
          FROM film ) t1
ORDER BY  filmlen_groups
```
## Workspace + Question Set #1
![alt text](image-249.png)
![alt text](image-250.png)
![alt text](image-251.png)
![alt text](image-252.png)
## Workspace + Question Set #2
![alt text](image-253.png)
![alt text](image-254.png)
![alt text](image-255.png)
![alt text](image-256.png)
## Template for Project Submission
![alt text](image-257.png)
![alt text](image-258.png)
![alt text](image-259.png)
![alt text](image-260.png)
![alt text](image-261.png)
![alt text](image-262.png)
![alt text](image-263.png)
![alt text](image-264.png)
## Common Mistakes
![alt text](image-265.png)
```SQL
SELECT count(film_id)
FROM inventory```

- This returns 1 row, with the count of film_id in the table.

If a column in the select statement is not in the Group By statement your results will be something you are not expecting. Please be careful of this!

### Subqueries
Subqueries are awesome but you should not use one if you do not need it to answer the question you asked. Many times the first question that is thought of does not require one. You may need to think of a few more to find a complex question that necessitates a subquery. 

 **Think of using a subquery when a SQL query is nested within another query. You need it to further restrict the returned data, so give careful thought to where.** 



### Window Functions
Window Functions are extremely  **useful for creating an aggregation or doing any other calculation across a subset of rows.** Once you have completed the calculation across the subset of rows, you can then reference the calculation as a new column in the query. You are required to use a window function in your query for this project. 

Think about when you need to aggregate across a subset of rows within a larger data table resulting from a query.
 


### Joins
Joins in general should be from a Primary Key to its corresponding Foreign Key.

Correct:
```ON inventory.inventory_id = rental.inventory_id```
- Here, Inventory PrimaryKey = Inventory ForeignKey
___
Incorrect: 
```ON inventory.inventory_id = rental.rental_id```
- Here, Inventory PrimaryKey does not equal Rental PrimaryKey


### Understanding the data
The Rentals table captures the rental history of the inventory of movie titles. Keep this in mind in case you are trying to show which movie has the most rentals. You would have to show which movie has the most copies or inventory rented out.
```
## Helpful strategies
![alt text](image-266.png)
# Project Rubric (tiêu chí dự án)
![alt text](image-267.png)
![alt text](image-268.png)
![alt text](image-269.png)

## Knowledge
![alt text](image-434.png)
![alt text](image-435.png)