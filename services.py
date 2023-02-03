import cohere
api_key ="Enter your API key here"



co = cohere.Client(api_key)
def generate_text_cohere(prompt):
    response = co.generate(  
        model='medium',  
        prompt = prompt,  
        max_tokens=100,  
        temperature=0.5,  
        presence_penalty = 0.3,
        stop_sequences=["--"])
    co_gen = response.generations[0].text
    return co_gen

