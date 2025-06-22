MODEL_CHOICES = ["Groq", "OpenAI", "Both"]
DEFAULT_TOPIC = "Science"
DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

VARIETY_PROFILES = {
    "Standard": {"temp": 0.7, "diversity": 1},
    "High": {"temp": 0.9, "diversity": 2},
    "Extreme": {"temp": 1.1, "diversity": 3}
}

BANNED_QUESTIONS = {
    "Science": [
        "What is the term for the process by which water moves through a plant",
        "What is transpiration",
        "What is photosynthesis",
        "What is the powerhouse of the cell",
        "What is Newton's first law"
    ],
    "History": [
        "Who was the first president",
        "When was World War II",
        "Who discovered America"
    ]
}

TOPIC_EXPANDERS = {
    "Science": [
        "Focus on recent discoveries (2020-2025) and unusual phenomena",
        "Cover cutting-edge research and surprising applications",
        "Include lesser-known scientists and accidental discoveries"
    ],
    "History": [
        "Highlight overlooked historical figures and cultural impacts",
        "Explore strange historical events and everyday life in different eras",
        "Cover misunderstood events and alternate history possibilities"
    ]
}
