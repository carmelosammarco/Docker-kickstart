## Project setup
This app contains both the backend and the frontend in a single repository.
```	
├── PIC
├── Readme.md
├── backend
├── docker-compose.yml
└── frontend
```

Navigate to the root directory.

```bash
$ cd ToDoS
```

### Start app containers

Start the `frontend`, `backend` and `db` containers using docker-compose

```	bash
$ docker-compose up -d 
```

Access the app from your browser at http://localhost:8080: 

![PIC](PIC/Screen.png)
