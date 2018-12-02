# IDC Cancer Classifier

## Requirements

* **Language:** Python 3.6
* **Package manager:** pip

## Execution instructions	

1. Set the environment variables
    ##### For Linux and Mac:
    `export FLASK_APP=IDC_Cancer_Classifier` <br/>
    `export FLASK_ENV=development` <br/>

    #### For Windows cmd, use set instead of export:
    `set FLASK_APP=IDC_Cancer_Classifier` <br/>
    `set FLASK_ENV=development` <br/>    

    #### For Windows PowerShell, use $env: instead of export:
    `$env:FLASK_APP = "IDC_Cancer_Classifier"` <br/>
    `$env:FLASK_ENV = "development"` <br/>    
   
2. Create / restart the database    
    `flask init-db`
    
3. Run the application    
    `flask run`