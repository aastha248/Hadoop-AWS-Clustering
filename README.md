# Hadoop Clustering on Amazon Web Services

Name : Aastha Gupta <br>
Email : aastha.gupta@mavs.uta.edu <br>
Affiliation : University of Texas at Arlington <br>
Website URL :  <br>

## Project Description : <br>

Configured a small Hadoop cluster. Implemented Hadoop MapReduce to examine different causes for airline delay. The results from MapReduce can be visualized using D3.js on flask application in python <br>

1. Get, install, try Hadoop. (downloads: http://www.apache.org/dyn/closer.cgi/hadoop/common/, more at: http://hadoop.apache.org/) Or, use a prebuilt image or, use the AWS service But, you will need to use Hadoop on a cloud service provider (Google, AWS) <br>
2. Interesting data sets have at least 100 thousand tuples up to a few million tuples. At these web-sites there are schema/meta-data describing the data. <br>
3. Using airline delay causes as an example data, we would like to know: the number of flights on time (arr_del15 <15 min) and number late seperated by carrier and also by airport. <br>
4. Tried with different numbers of mappers and reducers. (1 mapper, 1 reducer (1,1), then: (2,1), (2,2), (10,1), (10,2) Run with 1, 2, and 3 instances.
5. Show time to run and results on a AWS web page. <br>

### Visualization

1. Using D3.JS (or similar) packages. <br>
2. Import the output from the clustering above, and show bar charts with annotated color, through your web browser on your screen.


### Run the application on hadoop <br>

1. [Install Python][] <br>
2. Load the data file to Hadoop DFS using the command "hadoop dfs -copyFromLocal /home/ubuntu/application/Input_data/data.csv  /temp/data.csv" <br>
3. Run Mapper.py and Reducer.py using the command "hadoop jar contrib/streaming/hadoop-streaming-1.2.1.jar -D mapred.map.tasks=1 -D mapred.reduce.tasks=1 -mapper mapper.py -file ./application/mapper.py -reducer reducer.py -file ./application/reducer.py -input /temp/data.csv -output /temp/output1" <br>
4. Get output file from Hadoop DFS to EC2 instance using the command "hadoop dfs -copyToLocal /temp/output1/part-00000  /home/ubuntu/application/output/test.csv" <br>
5. Run flask app in a browser at the public DNS of Master Node <br>

[Install Python]: https://www.python.org/downloads/