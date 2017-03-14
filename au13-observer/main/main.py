from news.publisher import Publisher
from subscribe.subscriber import Subscriber

p1 = Publisher("Die Tagespresse")
p2 = Publisher("Der Postillion")

s1 = Subscriber()
s2 = Subscriber()
s3 = Subscriber()

p1.register(s1)
p1.register(s2)
p2.register(s3)
