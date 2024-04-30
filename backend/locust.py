from locust import HttpUser, TaskSet, task, between

TOKEN = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6Inc0ZW1acjZQdUc1b3lNdUtfNm1oVE83SmtWUkJnRGM3UmtISTZMcExwSzQifQ.eyJleHAiOjE3MTIyODcyODcsImlhdCI6MTcxMjI1MTI4NywianRpIjoiY2VlYzlkNDUtMzQ3OS00MWUxLTgyMGMtOTUxMjFlY2I2ZWEzIiwic3ViIjoiNWRkYWQ2YzgtNDc0YS00YWUyLWI1MDktMmJjNmFhZGY3MDU1IiwidHlwIjoiQmVhcmVyIiwic2Vzc2lvbl9zdGF0ZSI6IjE1NzAzODJkLTQ5ZGEtNDEzZi04MWFhLTJhY2E4ZDY1ZjNmNyIsInNjb3BlIjoib3BlbmlkIHJvbGVzIiwic2lkIjoiMTU3MDM4MmQtNDlkYS00MTNmLTgxYWEtMmFjYThkNjVmM2Y3IiwiZW1haWwiOiJhcHBfbWFycyBhcHBfbWFycyIsImdyb3VwcyI6WyIvTUFSU19VU0VSIl0sInByZWZlcnJlZF91c2VybmFtZSI6ImFwcF9tYXJzIiwiZ2l2ZW5fbmFtZSI6ImFwcF9tYXJzIiwiZmFtaWx5X25hbWUiOiJhcHBfbWFycyJ9.vkXuw_HG5rPMQa_jSTAoZEkm8ezwL8w2SQ6qopRtSgM49issC90KXip5jj0kydAbne-AMeLK5ha_SiMLRbmRYw"

class UserBehavior(TaskSet):

    @task
    def get_or_create_user(self):
        headers = {'Authorization': TOKEN}
        self.client.post("/user", headers=headers)

    @task
    def search_books(self):
        headers = {'Authorization': TOKEN}
        self.client.get("/search_books", params={"name": "To Kill a Mockingbird", "author": "Harper Lee", "page": "1", "size": "1"},
                        headers=headers)

    @task
    def get_book_by_id(self):
        headers = {'Authorization': TOKEN}
        self.client.get("/book/OL22819394M", headers=headers)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 15)  # time an simulated user waits between executing each task