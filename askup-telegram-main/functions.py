functions = [
    {
        "name": "get_search_info",
        "description": "If it is difficult to answer, select a keyword from the question and make it search.",
        "parameters": {
            "type": "object",
            "properties": {
                "keyword": {
                    "type": "string",
                    "description": "The keyword to use for the information search",
                },
            },
            "required": ["keyword"],
        },
    }
]