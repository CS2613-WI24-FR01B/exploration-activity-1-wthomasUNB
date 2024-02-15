#Exploration Activity 1

For the first activity, I chose to use the Seaborn Python library.

#Instructions For Runing This Program
Seaborn can be installed using the installation instructions provided on the [Seaborn Info Page](https://seaborn.pydata.org/installing.html).</br>
**NOTE**: For this application, I used a tool called Jupyter to display the graphs. This isn't mandatory for Seaborn, however, if you are not using this, you will need to uncomment the "plt.show()" line in order to view the graph.</br>
If you want to use Jupyter for this, feel free to follow the [installation instructions](https://jupyter.org/install) found on Jupyter's website.
#Purpose Of This Application
This application uses data which is collected by Environment Canada to plot out the Max Temperature's recorded at a given station over the course of a year. This focuses on stations which provide a daily output, rather than monthly. (The files generated use different column names in them depending on if it's monthly or daily). To learn more or to test out a different CSV than what's provided here, visit the [Environment and Natural Resources Canada Historical Climate Data](https://climate.weather.gc.ca/index_e.html) page.

#Input
As mentioned before, this program uses historic weather information provided by Environment and Natural Resources Canada. This is through the use of CSV files which are generated from each station. Essentially, the only user input in this program is a prompt for the CSV file's name. Once that is given, the program will then attempt to open the file using Pandas. If successful, Seaborn will then take the Pandas object as input and plot the data based on parameters given in its plot-type function call (There are multiple types of plots, however, for the purpose of this program, I chose to use the lineplot)