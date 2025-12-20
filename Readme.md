## Development:

### Start all services:
`docker-compose -f docker-compose.dev.yml up -d`

### View logs:
`docker-compose -f docker-compose.dev.yml logs -f`

### Stop services:
`docker-compose -f docker-compose.dev.yml down`

### To run specific services
`docker-compose -f docker-compose.dev.yml up backend pgadmin`


### Access:
* Frontend: http://localhost:5173
* Backend API: http://localhost:8000
* Backend Docs: http://localhost:8000/api/docs
* pgAdmin: http://localhost:5050
* Redis: http://localhost:6379
```
