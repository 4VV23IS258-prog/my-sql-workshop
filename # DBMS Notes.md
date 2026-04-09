# DBMS Notes
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

<textarea style="display:none;">
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