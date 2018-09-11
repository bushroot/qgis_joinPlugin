# README  

## Resources
- [PYQGIS API documenations](https://qgis.org/pyqgis/3.0/)

## Order of the scripting to be done  

1) Create function to append new lines with values in the junction table of the many-to-many relationship. -> done: 02_appendRow.py 

2) Create button that triggers the append action

3) Create function that gets the selected features from the two required layers and create a key pair with all possible combinations

4) Update the button, so that it appends the key pairs generated from the selected features (cf. step 3)

5) Create a interface that allows to select the two layers that are joined as well as the junction table.