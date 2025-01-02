import os
from openai import OpenAI
from wonderwords import RandomWord

class AiChatService:
    def __init__(self):
        pass

    def create_context(self):
        pass

    def get_context(self, id):
        pass

    def write_story(self, location, person_name = "John Smith"):
        client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
        )

        random_word_gen = RandomWord()
        random_word_string = ', '.join(random_word_gen.random_words(10))

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Write me a story about a person named {person_name} from {location}. The story should be a fun one where the user discovers a cool project on GitHub called \"AI Fungeon\" written by a humble developer named Jacob Adamson. The code adheres to best practices, simple and efficient. The story should be a couple paragraphs long. Consider these random words: {random_word_string}",
                }
            ],
            model=os.environ.get("OPENAI_MODEL"),
        )

        return chat_completion.choices[0].message.content
