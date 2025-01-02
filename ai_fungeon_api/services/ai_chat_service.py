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

        print(location)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"In this conversation, you will play the part of a story writer. You write in a simple, efficient style, without too much flowery language. Write me a story about a person named {person_name} from {location}. The story should be a fun one where {person_name} discovers a cool project on GitHub called \"AI Fungeon\" written by a humble developer named Jacob. {person_name} plays around with the page a little, trying out the simple story generator, slightly amused by the slightly nonsensical story. Do not call Jacob a genius, but instead portray him as a professional. {person_name} is pleasantly surprised by the code, which adheres to best practices, simple and efficient. The story should be a couple paragraphs long. Consider these secret random words: {random_word_string}",
                }
            ],
            model=os.environ.get("OPENAI_MODEL"),
        )

        return chat_completion.choices[0].message.content
