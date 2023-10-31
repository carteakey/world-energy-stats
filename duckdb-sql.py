import duckdb
con = duckdb.connect("energy.db")
con.sql("CREATE TABLE ontime AS SELECT * FROM 'energy-data/owid-energy-data.csv'")
