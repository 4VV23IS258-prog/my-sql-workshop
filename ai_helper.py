import pyperclip
input()
TEXT=r"""

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

create table suppliers(
id int nOt null AUTO_INCREMENT,
supplier_name varchar (255) not null,
supplier_city varchar(255)  not null,
primary key (id)
);

create table stocks (
id int not null AUTO_INCREMENT,
product_id int not null,
supplier_id int not null,
purchase_qty int not null,
purchase_price decimal(15,2) not null,
primary key (id),
foreign key (product_id) references products(id),
foreign key (supplier_id) references suppliers(id)
);

insert into product_categories(product_cat,short_code) values ("smart phones","SP");
insert into product_categories(product_cat,short_code) values ("Laptops","LP");
insert into product_categories(product_cat,short_code) values ("smart watches","SW");
insert into product_categories(product_cat,short_code) values ("Head phones","HP");
insert into product_categories(product_cat,short_code) values ("Pendrive","PD");
insert into product_categories(product_cat,short_code) values ("cell phone","CP");
insert into product_categories(product_cat,short_code) values ("hard disk","HD");
insert into product_categories(product_cat,short_code) values ("power bank","PB");

insert  into products (product, product_cat_id, short_code) values ("iPhone",1,"IP");
insert  into products (product, product_cat_id, short_code) values ("Galaxy Phone",1,"GP");
insert  into products (product, product_cat_id, short_code) values ("Nothing",1,"NP");
insert  into products (product, product_cat_id, short_code) values ("MacBook",2,"MB");
insert  into products (product, product_cat_id, short_code) values ("Dell",2,"DL");

insert into suppliers(supplier_name, supplier_city) values ("Apple", "Mysore");
insert into suppliers(supplier_name, supplier_city) values ("Samsung", "Bangalore");
insert into suppliers(supplier_name, supplier_city) values ("CMF", "Bangalore");
insert into suppliers(supplier_name, supplier_city) values ("HP", "Managalore");

insert into stocks (product_id, supplier_id, purchase_qty, purchase_price) values (1,1,12,75000);
insert into stocks (product_id, supplier_id, purchase_qty, purchase_price) values (2,2,20,45000);
insert into stocks (product_id, supplier_id, purchase_qty, purchase_price) values (3,3,40,23000);
insert into stocks (product_id, supplier_id, purchase_qty, purchase_price) values (4,4,25,39000);


alter table products
add ratings decimal(4,2);

select * from product_categories;
select * from products;
select * from suppliers; 
select * from stocks;

select product_categories.product_cat, sum(stocks.purchase_qty) As "Total Quantity"
from product_categories left join products
on products.id = product_categories.id
inner join stocks 
on stocks.product_id = products.id
group by product_categories.product_cat;

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


with temp as (
select product_categories.product_cat,sum(stocks.purchase_qty) as pq
from product_categories LEFT JOIN products 
ON product_categories.id = products.product_cat_id 
INNER JOIN stocks 
on stocks.product_id=products.id 
group by product_categories.product_cat
)
select product_cat from temp where pq=(select max(pq) from temp);
with temp as (
select product_categories.product_cat,sum(stocks.purchase_qty) as pq
from product_categories LEFT JOIN products 
ON product_categories.id = products.product_cat_id 
INNER JOIN stocks 
on stocks.product_id=products.id 
group by product_categories.product_cat
)
select product_cat from temp order by pq desc limit 1;

select sum(purchase_qty*purchase_price) as TOTAL_PURCHASES
from stocks LEFT JOIN suppliers 
ON stocks.supplier_id=suppliers.id
WHERE supplier_city like "Ba%";

select supplier_city,sum(purchase_qty*purchase_price) as "Purchased Value"
from stocks LEFT JOIN suppliers 
ON stocks.supplier_id=suppliers.id
group BY supplier_city;











"""

print("Dont worry I have copied It to your clipboard")
pyperclip.copy(TEXT)
