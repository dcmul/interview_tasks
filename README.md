# Integration Engineer Challenge

Submission for solution for the challenge

## Installation

The solution Djangos application that is placed in the folder named solution



## Usage

Usage instructions will be coming soon


Step 1: 
Git clone the repo
```bash
git clone repo
```

Step 2
run docker compose to setup application
```bash
 docker-compose up --build -d

```

Step 3: 


To start cli service run python manage genreadings and provide the smartmeter id and date of reading. That date format should be like 2021-03-03
```bash
 docker exec -it <web container> python manage.py genreadings 34 2021-03-03

```

Step 4:

For the rest api service. In docker-compose the container will be bound to port 8750. Becuase of URL encodeing issues the data will have to be taken as yyyy-mm-dd_hh:min. such as example below.
```bash
 http://localhost:8750/232/2021-05-10_00:00/2021-05-10_02:03

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)