import pandas as pd
db={"s1":{"rollno":1,"name":"jig","ssc marks":69,"inter marks":79,"cgpa":6.9,"preferred lang":"python","career option":"data scientist"},
    "s2":{"rollno":2,"name":"nihal","ssc marks":49,"inter marks":69,"cgpa":9.9,"preferred lang":"python","career option":"analyst"},
    "s3":{"rollno":3,"name":"rohan","ssc marks":99,"inter marks":89,"cgpa":9.1,"preferred lang":"python","career option":"ml engg"}}
cf=pd.DataFrame(db)
print(cf)
