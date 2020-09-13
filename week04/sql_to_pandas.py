"""
作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等
方式进行数据的清洗和处理工作。因此需要你能够掌握基本的 SQL 语句和 pandas 等价的
语句，利用 Python 的函数高效地做聚合等操作。
作业要求：请将以下的 SQL 语句翻译成 pandas 语句：
1. SELECT * FROM data;
2. SELECT * FROM data LIMIT 10;
3. SELECT id FROM data;  //id 是 data 表的特定一列
4. SELECT COUNT(id) FROM data;
5. SELECT * FROM data WHERE id<1000 AND age>30;
6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
8. SELECT * FROM table1 UNION SELECT * FROM table2;
9. DELETE FROM table1 WHERE id=10;
10. ALTER TABLE table1 DROP COLUMN column_name;
"""
import pandas as pd
import pymysql

if __name__ == '__main__':\

    sql = "select * from dept_manager;"
    conn = pymysql.connect('127.0.0.1', 'root', 'rj123', 'employees')
    df = pd.read_sql(sql, conn)

    # 1. SELECT * FROM data;
    print("1. select * from dept_manager;")
    print(df)
    print()

    # 2. SELECT * FROM data LIMIT 10;
    print("2. select * from dept_manager limit 10;")
    print(df.head(10))
    print()

    # 3. SELECT id FROM data;  //id 是 data 表的特定一列
    print("3. select emp_no from dept_manager;")
    print(df['emp_no'])
    print()

    # 4.SELECT COUNT(id) FROM data;
    print("4. select count(emp_no) from dept_manager;")
    print(df['emp_no'].count())
    print()

    # 5. SELECT * FROM data WHERE id<1000 AND age>30;
    print("5. select * from dept_manager where emp_no <111000 "
          "and from_date < '1990-01-01';")
    df['from_date'] = pd.to_datetime(df['from_date'])
    print(df[(df['emp_no'] < 111000)
             & (df['from_date'] < pd.to_datetime('1990-01-01'))])
    print()

    # 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
    print("6. select dept_no, count(distinct(emp_no)) from dept_manager "
          "group by dept_no;")
    print(df.groupby('dept_no')['emp_no'].count())
    print()

    # 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
    print("7. select * from dept_manager t1 inner join departments t2 "
          "on t1.dept_no = t2.dept_no;")
    dept_manager = pd.read_sql('select * from dept_manager;', conn)
    departments = pd.read_sql('select * from departments;', conn)
    print(pd.merge(dept_manager, departments, on='dept_no'))
    print()

    # 8. SELECT * FROM table1 UNION SELECT * FROM table2;
    print("8. select dept_no from departments "
          "union select dept_no from dept_manager;")
    dept_manager = pd.read_sql('select dept_no from dept_manager;', conn)
    departments = pd.read_sql('select dept_no from departments;', conn)
    print(pd.concat([departments, dept_manager]).drop_duplicates())
    print()

    # 9. DELETE FROM table1 WHERE id=10;
    print("9. delete from departments where dept_no='d100';")
    departments = pd.read_sql('select * from departments;', conn)
    print(departments)
    dropdone = departments.drop(
        departments[departments['dept_no'] == 'd100'].index)
    print(dropdone)
    print()

    # 10. ALTER TABLE table1 DROP COLUMN column_name;
    print("10. alter table departments drop column dept_name;")
    departments = pd.read_sql('select * from departments;', conn)
    print(departments)
    dropdone = departments.drop('dept_name', 1)
    print(dropdone)
    print()
