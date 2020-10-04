# Books

#### Author: [Peris Oduol](https://github.com/PerisOduol618)

* Github repository: https://programmingbooks.herokuapp.com/books

* Link to live site: https://programmingbooks.herokuapp.com/

## Description

The Best General Programming Books.where teh user cann also have a orevier of the  book.

### Prerequisites
* python3.6
* virtual environment
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/PerisOduol618/Books.git
        $ cd books

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` from `development` to `production`
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py server
       


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|To display various books| Click the available books|Redirected to a page with a list of programming books |
|Display the preview of the books| Book review| Redirected to the the news preview|



## Built With

* [Python3.6](https://docs.python.org/3/)
* Flask
* Boostrap
* HTML
* CSS




## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :oduolpepe618@gmail.com

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
