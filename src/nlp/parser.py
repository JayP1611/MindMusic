# def parsing_output(text: str) -> str:
#     '''Parse the GPT-2 generated output for the prompt'''
#     text = text.split("###")[0]
#     return text

def parsing_output(text: str) -> dict:
    '''Parse the GPT-2 generated output for the prompt'''
    text = text.split("###")[0]
    result = {
        "title": None,
        "tags": [],
        "description": None
    }

    for line in text.splitlines():
        line = line.strip()

        if line.lower().startswith("title:"):
            result['title'] = line.replace("Title: ", "").strip()
        elif line.lower().startswith("tags:"):
            tags = line.replace("Tags: ", "").strip()
            result['tags'] = [t.strip() for t in tags.split(",")]
        elif line.lower().startswith("description:"):
            result['description'] = line.replace("Description: ", "").strip()

    return result

if __name__ == "__main__":
    sample = '''
    Title: Study Preparation
    Tags: study, calm, hopeful, focus
    Description: Gentle melodies and steady rhythms to support study sessions.
    ###
    '''

    print(parsing_output(sample))