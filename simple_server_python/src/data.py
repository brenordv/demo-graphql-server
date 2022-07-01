# -*- coding: utf-8 -*-
from datetime import datetime

PRODUCTS = [
    {
        "id": 1,
        "name": "USB Type-C cable - 3m",
        "price": 14.22,
    },
    {
        "id": 2,
        "name": "Red Tomato",
        "price": 4.14,
    },
    {
        "id": 3,
        "name": "Generic Beer",
        "price": 2.99,
    },
    {
        "id": 4,
        "name": "Cell phone charger",
        "price": 30.00,
    },
    {
        "id": 5,
        "name": "Replica of Obiwan Kenobi Lightsaber",
        "price": 99.50,
    },
    {
        "id": 6,
        "name": "Mouse Gamer",
        "price": 78.55,
    },
    {
        "id": 7,
        "name": "Gamer girl bath water",
        "price": 200.12,
    },
]

REVIEWS = [
    {
        "id": 1,
        "product_id": 5,
        "author": "starWarsFan321",
        "content": "Great product! Excellent build quality!",
        "grade": 4,
        "date_added": datetime.utcnow()
    },
    {
        "id": 2,
        "product_id": 5,
        "author": "darthSider11",
        "content": "This replica of Obiwan Kenobi's lightsaber is terrible! The blade is flimsy and the hilt feels cheap. I would not recommend this product to anyone.",
        "grade": 1,
        "date_added": datetime.utcnow()
    },
    {
        "id": 3,
        "product_id": 5,
        "author": "warOfTheStars99",
        "content": "This is the best replica of an Obiwan Kenobi lightsaber that I have ever seen! It is so realistic and looks just like the real thing!",
        "grade": 5,
        "date_added": datetime.utcnow()
    },
    {
        "id": 4,
        "product_id": 3,
        "author": "beerGourmetPerson",
        "content": "This beer is pretty generic. It's not great, but it's not terrible. It's just kind of... there. If you're looking for a beer that won't offend anyone and will just get the job done, this is the one for you. But if you're looking for!",
        "grade": 3,
        "date_added": datetime.utcnow()
    },
    {
        "id": 5,
        "product_id": 3,
        "author": "drunk33",
        "content": "If you're looking for a cheap, generic beer, then this is the one for you! It's watery and tasteless, but it'll get the job done.",
        "grade": 4,
        "date_added": datetime.utcnow()
    },
    {
        "id": 6,
        "product_id": 7,
        "author": "simpLePerson123",
        "content": "I don't know what all the fuss is about. It's just water.",
        "grade": 3,
        "date_added": datetime.utcnow()
    },
    {
        "id": 7,
        "product_id": 7,
        "author": "superFan",
        "content": "smells amazing! <3",
        "grade": 5,
        "date_added": datetime.utcnow()
    },
    {
        "id": 8,
        "product_id": 7,
        "author": "ultraFan",
        "content": "nice smell... tastes a little funky, though.",
        "grade": 5,
        "date_added": datetime.utcnow()
    },
    {
        "id": 8,
        "product_id": 7,
        "author": "GamerGirrrl",
        "content": "I'm a gamer girl and I completely misunderstood this product. DO. NOT. RECOMMEND.",
        "grade": 1,
        "date_added": datetime.utcnow()
    },
    {
        "id": 9,
        "product_id": 7,
        "author": "ai44",
        "content": "This gamergirl bath water is terrible! It's just a bunch of dirty water that smells like gamer sweat. Do not bother buying it.",
        "grade": 5,
        "date_added": datetime.utcnow()
    },
]
