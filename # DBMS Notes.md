# DBMS Notes
<style>
    .hidden{
    display:none;
    }
</style>

## Create Table
```sql 

-- create
CREATE TABLE product_categories (
  id INTEGER NOT NULL AUTO_INCREMENT,
  product_cat varchar(255) NOT NULL,
  short_code varchar(20) NOT NULL,
  PRIMARY KEY (id)
);


create TABLE products(
id int NOT NULL AUTO_INCREMENT,
product varchar(255) NOT NULL,
product_cat_id int NOT NULL,
short_code varchar(20) NOT NULL,
primary KEY (id),
foreign KEY(product_cat_id) references product_categories(id)
);
```

## Insert Statements
``hidden``

*refer raw markdown*

<textarea class="hidden">
insert into product_categories(product_cat,short_code) values ("smart phones","SP");
insert into product_categories(product_cat,short_code) values ("Laptops","LP");
insert into product_categories(product_cat,short_code) values ("smart watches","SW");
insert into product_categories(product_cat,short_code) values ("Head phones","HP");
insert into product_categories(product_cat,short_code) values ("Pendrive","PD");
insert into product_categories(product_cat,short_code) values ("cell phone","CP");
insert into product_categories(product_cat,short_code) values ("hard disk","HD");
insert into product_categories(product_cat,short_code) values ("power bank","PB");
insert into product_categories(product_cat,short_code) values ("hard disk","HD");
insert into product_categories(product_cat,short_code) values ("power bank","PB");

insert  into products (product, product_cat_id, short_code) values ("iPhone",1,"IP");
insert  into products (product, product_cat_id, short_code) values ("Galaxy Phone",1,"GP");
insert  into products (product, product_cat_id, short_code) values ("Nothing",1,"NP");
insert  into products (product, product_cat_id, short_code) values ("MacBook",2,"MB");
insert  into products (product, product_cat_id, short_code) values ("Dell",2,"DL");
</textarea>


## BASIC Queries

```sql
alter table products
add ratings decimal(4,2);

select * from product_categories;

SELECT product_cat, COUNT(*) AS duplicate_count
FROM product_categories
GROUP BY product_cat
HAVING COUNT(*) >1;
```
## Join Tables

```sql
SELECT products.product,product_categories.product_cat
FROM products INNER join product_categories
ON products.product_cat_id=product_categories.id;


SELECT product_cat,count(*) 
FROM products inner join product_categories
on products.product_cat_id=product_categories.id
Group BY product_cat
```
## RIGHT JOIN
(INCLUDE NULL VALUES FROM RIGHT TABLE)
```sql 

SELECT 
    COALESCE(product_categories.product_cat, 'Uncategorized') AS "Product Category",
    COUNT(products.id) AS "Number of products"
FROM products 
right JOIN product_categories 
    ON products.product_cat_id = product_categories.id
GROUP BY product_categories.product_cat;
```

#### NEW TABLE 
`hidden`
<div style="display:none">
CREATE TABLE suppliers(
id int not NULL AUTO_INCREMENT,
supplier_name varchar(255) NOT NULL,
supplier_city varchar(30) NOT NULL,
PRIMARY KEY(id),
);
INSERT INTO suppliers (supplier_name,supplier_city) 
VALUES ("APPLE","Mysore");

INSERT INTO suppliers (supplier_name,supplier_city) 
VALUES ("Software Engineers","Banglore");

INSERT INTO suppliers (supplier_name,supplier_city) 
VALUES ("Cheap Quality Products","China");

INSERT INTO suppliers (supplier_name,supplier_city) 
VALUES ("Terrorists","Pakisthan");

create table stocks(
id int not NULL AUTO_INCREMENT,
product_id int not NULL,
supplier_id int not NULL,
purchase_qty int not NULL,
purchase price decimal(15,2) not NULL,
PRIMARY KEY(id),
foreign KEY(supplier_id) references suppliers(id),
foreign KEY(product_id) references products(id),
);
</div>

### 3 TABLE JOIN
```sql
SELECT products.product,suppliers.supplier_name,(purchase_qty*purchase_price) as "Value in Stock"
FROM stocks INNER JOIN products 
on products.id=stocks.product_id 
INNER JOIN suppliers
ON stocks.supplier_id=suppliers.id;
```

#### Aggregate on 3 table join 

```sql
select product_categories.product_cat, sum(stocks.purchase_qty) As "Total Quantity"
from product_categories left join products
on products.id = product_categories.id
inner join stocks 
on stocks.product_id = products.id
group by product_categories.product_cat;
```

### Storing Output as Intermediate Table
```sql
with discount_table as (
    select 
    products.product, 
    purchase_price, 
    case 
        when purchase_price > 60000 then 10 
        when purchase_price >= 40000 then 5
        when purchase_price < 40000 then 2 
        else 0 
    end as discount 
from stocks 
inner join products on stocks.product_id = products.id
)

select product,purchase_price,discount,(purchase_price-(purchase_price*discount*0.01)) as "Discounted Price"
from discount_table;
```
### Category with maximum purchased products
```sql
with temp as (
select product_categories.product_cat,sum(stocks.purchase_qty) as pq
from product_categories LEFT JOIN products 
ON product_categories.id = products.product_cat_id 
INNER JOIN stocks 
on stocks.product_id=products.id 
group by product_categories.product_cat
)
select product_cat from temp where pq=(select max(pq) from temp);
--OR
select product_cat from temp order by pq desc limit 1;
```
### Join and Where
```sql
select sum(purchase_qty*purchase_price) as TOTAL_PURCHASES
from stocks LEFT JOIN suppliers 
ON stocks.supplier_id=suppliers.id
WHERE supplier_city like "Ba%"
```

### Display For Each City
```sql
select supplier_city,sum(purchase_qty*purchase_price)
from stocks LEFT JOIN suppliers 
ON stocks.supplier_id=suppliers.id
group BY supplier_city;

```
### Some more create Statements `hidden`
<div class="hidden">
create table customers(
id int not null AUTO_INCREMENT,
customer varchar(20) not null,
customer_city varchar(20) not null,
primary key(id)
);
insert into customers(customer,customer_city) values ("Vishwa","Mysore");
insert into customers(customer,customer_city) values ("Tejas","Mysore");
insert into customers(customer,customer_city) values ("Dhanush","Mangalore");
insert into customers(customer,customer_city) values ("Sumana","Bengaluru");
create table sales(
id int not null AUTO_INCREMENT,
customer_id int,
product_id int not null,
order_date date not null,
order_qty int not null,
order_price float(15,2) not null,
primary key(id),
foreign key(customer_id) references customers(id),
foreign key(product_id) references products(id)
);
insert into sales(customer_id,product_id,order_date,order_qty,order_price) values (1,1,"2026-03-10",1,96000);
insert into sales(customer_id,product_id,order_date,order_qty,order_price) values (2,1,"2026-03-12",1,96000);
insert into sales(customer_id,product_id,order_date,order_qty,order_price) values (3,2,"2026-03-15",1,75000);
insert into sales(customer_id,product_id,order_date,order_qty,order_price) values (4,2,"2026-04-06",2,75000);
insert into sales(customer_id,product_id,order_date,order_qty,order_price) values (1,2,"2026-04-07",1,70000);
select * from customers;
select * from sales;
</div>

### Dates
```sql
select CONCAT("$",sum(order_price)) As "Total Sales Of Iphone" from sales
where order_date between "2026-03-01" and "2026-03-31" and product_id=
(select id from products where product="iphone");
```

