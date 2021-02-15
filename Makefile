postgres_run:
	docker run --name postgres1 -v /home/vadim/docker_data:/var/lib/postgresql/data -p 127.0.0.1:5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres

postgres_start:
	docker start postgres1







