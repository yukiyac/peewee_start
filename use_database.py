from database import Thread

Thread.create(name="Keisuke", title="Title", body="Body")

thread01 = Thread(name="Keisuke01", title="Title01", body="Body01")
thread01.save()
