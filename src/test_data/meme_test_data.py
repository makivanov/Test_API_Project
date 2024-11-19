one_meme_test_data = [
    {
        "text": "Meme_____1",
        "url": "https://url.com/ujglklkgk0l/i.jpg",
        "tags": [1, 3, 7, 5],
        "info": {
            "color": [],
            "size": {}
        }
    },
]

one_change_mem_test_data = [
    {
        "text": "Мем 1",
        "url": "https://урл.ру/ujglklkgk0l/i.jpg",
        "tags": ["one", "two"],
        "info": {
            "color": ["blue", "red"],
            "size": {"big": "big"}
        }
    },
]

meme_positive_test_data = [
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
        "info": {

        }
    },
    {
        "text": "Meme 1",  # noqa: F601
        "text": "Meme 2",  # noqa: F601
        "url": "l",
        "tags": [1, 3],
        "info": {
            "id": 11,  # noqa: F601
            "id": 12  # noqa: F601
        },
        "error": 7
    },
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkiuiybiop87bbtguyuytbbtboub/ljghyubtboton7blgnlytytyno76nlntgytlyuygkl/jfguytbyuty"
               "ytyontyo8ty7n7o78m87o8888m8kl;jjhnmpuymh8ouympoo8u9m,9u87p[,8lkjg786/oh.jpg",
        "tags": [1, 3],
        "info": {
            "id": 11,
        },
        "error": 7,
        "field": ["field"]
    }

]

meme_negative_test_data = [
    {
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
        "object": {}
    },
    {
        "text": "Meme 1",
        "tags": [1, 3],
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkgkl",
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
    },
    {
        "text": 22,
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": 22,
        "tags": [1, 3],
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkgkl",
        "tags": 1,
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
        "object": 1
    },
    {
        "text": ["Meme 1"],
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": ["https://url.com/ujgkgkl"],
        "tags": [1, 3],
        "object": {}
    },
    {
        "text": "Meme 1",
        "url": "https://url.com/ujgkgkl",
        "tags": [1, 3],
        "object": ()
    },
    {}
]

incorrect_id_test_data = [
    0,
    -1,
    1.5,
    None,
    "1",
    "a"
]
