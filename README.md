# API Configuration 

## run the api locally  

### Install the required modules
``` pip3 install requiremets.text ```
<br>

### Start the API 
```python app.py ```   
<br>
### to view the database
``` http://127.0.0.1:5000/ ```
### to add chef to the database
``` http://127.0.0.1:5000/addChef?chef=<chef> ```
### to add/update new food under chef
``` http://127.0.0.1:5000/addFood?chef=<chef>&name=<food_name>&price=<price> ```
