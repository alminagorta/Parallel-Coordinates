Code come from :https://bl.ocks.org/syntagmatic/482706e0638c67836d94b20f0cb37122

from the original the data : Cabin Version3

This sheet is ready to input in the plot
- I deleted all NaN from "Type" column
- I filter only Ontario in column "Province",conside present only rivers (because EPT does not make sense in lakes), 
-I deleteade count macroinvertebarets and LogCount to make less heavy 
-Deleated EcoregionNumber
-Deleted Julian day
- Deleated some outlier .eg. Conductivity (negative)
-Eliminate higher DO (like 90 rows)

I modified using the output from python , all orange columns is what I added


Data come from 
https://gist.github.com/syntagmatic/482706e0638c67836d94b20f0cb37122#file-planets-csv

To modify
Change the csv and the code of the html CHANGE THE VAR DIMENSIONS as shown below
var dimensions = [
  {
    key: "pl_rade",// OA-this is the heading in the csv file  
    description: "Planet Radius in Earth Radii",// label- axes of the II_coord
    type: types["Number"]


In the columns with strings I need to inlcude in the domain the options

 .domain(["Rosita dame la pa", ..."Transit", "Transit Timing Variations"]) // This is what is i the input of the column


Things to correct:

High number use logarithms 
Explore extrem values or outlier [like -99] and reemplaze with NaN
In count column => what is 0 I put 0.01 because I am using logaritm
But now considering NaN will be represented as disconnected lines
Example : General-Conductivity, phosphorus 

I guess the approach is instead of NaN just leave empty cells like in the original excel file

Updated October 9, 2019
Some Changes in The Html code:

Add Units:
Temperature (C)
- ph (0-14), where 0 is acidic and 14 is alkaline-pure water =7 
- Conductivity (uS/cm)-microSiemens/cm- pure water 0uS/cm, sea water 56,000 uS/cm
-Dissolved Oxygen (mg/L)-  