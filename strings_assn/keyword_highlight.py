#TASK 1
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

for i in reviews:
    my_word = ["good", "excellent", "bad", "poor", "average"]
    for j in my_word:
        if j in i:
            new_reviews = i.replace(j, j.upper())
            print(new_reviews)


#TASK 2
def tally(list):
    for i in list:
        positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
        for p in positive_words:
            if p in i:
                print(p, i.count(p))
                
        negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
        for n in negative_words:
            if n in i:
                print(n, i.count(n))

tally(reviews)


#TASK 3
for i in reviews:
    print(i[:32] + "...")