db          = 'test';
user        = 'yuanquan';
password    = 'yuanquan';
dbConnect   = database(db,user,password,'org.postgresql.Driver','jdbc:postgresql://localhost:5432/test');
sqlcommand  = 'select * from test_try;';
cursor      = exec(dbConnect,sqlcommand);
row         = fetch(cursor,4)

