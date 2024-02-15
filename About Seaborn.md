#What Is This Package
This exploration activity uses the Seaborn library for Python.</br>
#What Is Seaborn?
Seaborn is a library that makes visualizing data simple. It provides numerous tools which work for all sorts of data. Using MatPlotLib, it then displays the data in graph form.</br></br>
There are many different types of graphs that Seaborn can create with given data [as can be seen here](https://seaborn.pydata.org/tutorial/function_overview.html) on Seaborn's official documentation page. Not to mention that you can also combine different graph types to make complex and detailed visualizations of data.</br></br>
Additionally, while by default, the axis names will match the column name, this can be modified to enhance the readability of the graph.</br></br>
For my application, this simply uses a lineplot with data given by a CSV file to create a simple line graph of the average daily highs reported in the CSV file for a given time period.</br>
#Functionalities
As stated previously, this library which is built on top of MatPlotLib is primaraly to make generating graphs simpler. There are multiple types of plots which can be used.</br>
lineplot(data, x="value", y="value"). </br>
Here, value refers to columns inside of the CSV file. Data is a Pandas object containing the CSV file.</br>
scatterplot(data) generates a scatter plot, and so on.</br></br>
The data parameter is generally the only one that **needs** to exist in order to generate a graph, however, specifying x and y parameters is highly recomended.

#When Was Seaborn Created?
The earliest seaborn build was released to [PyPi](https://pypi.org/project/seaborn/0.1/) on October 28th, 2013.

#Why Did I Choose This Library?
Simply because I remembered using the historic weather data files for an assignment from my CS1083 class and wanted to do something else with them. I decided that using a library to plot out certain aspects of the data contained in the file sounded interesting to me, so I went looking for a library that would make this simple, and stumbled upon this.

#How Did Learning This Library Influence My Learning Of Python?
I knew beforehand that Python was good for data analysis, however, I didn't know just how many libraries existed in Python for this sort of thing. Learning this library has made me want to explore Python more outside of class for some smaller projects that I have in mind.

#My Overall Experience With Seaborn
Overall, Seaborn looks very daunting at first, however, it is actually quite simple to understand. I would definitely recomend this library to anyone who needs to create a program to generate graphs from pre-compiled data. I'll likely continue to use this library going forward if I have another project which could utilize it.
