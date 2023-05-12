# SparkMongo Environment
## Install Spark
Clone this github files, which already installed neccessary .jars for mongo connectors.

## Install Mongo

Mongo Community Editor [download here](https://www.mongodb.com/try/download/community)

Host local server for Mongo [here](https://l.messenger.com/l.php?u=https%3A%2F%2Fwww.mongodb.com%2Fdocs%2Fmanual%2Ftutorial%2Finstall-mongodb-on-windows%2F&h=AT2ME2Zyyxgi55Wd1hq80CpGOrrnNBNp7IC95YCS3x9GZpryuOW_O5hYWk7a9LDiIm2XXWcK28Y-7M3Fq_8_6R24_-LziQU2fkFgyIuFiMCzk1bzcv8v7SpyfglQgRwqOg2QfjeoHC2rlO4)

## Install python libraries
``` command prompt
>> pip install pyspark
>> pip install pymongo
>> pip install findspark
```

## Setting up environment
``` python
import os
os.environ['HADOOP_HOME'] = '/path/to/pyspark'
os.environ['SPARK_HOME'] = '/path/to/pyspark'
os.environ['JAVA_HOME'] = '/path/to/java'
os.environ['MONGO_HOME'] = '/path/to/mongo'
```

## Adding EnvPath

![Untitled](https://github.com/thinhsuy/SparkMongo_Environment/assets/81562297/b4650185-40b5-489c-bb3e-741c14ccba6a)

## Note
Make sure the version of `pyspark` and `python` must be as same.
