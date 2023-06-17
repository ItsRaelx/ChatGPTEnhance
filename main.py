import os
import openai
import re
import time

# Set your API key
openai.api_key = "YOUR_API_KEY"


def split_into_chunks(text, max_length):
    # Podziel tekst na chunki o maksymalnej długości
    chunks = []
    current_chunk = ''
    for word in text.split(' '):
        if len(current_chunk) + len(word) < max_length:
            current_chunk += ' ' + word
        else:
            chunks.append(current_chunk)
            current_chunk = word
    chunks.append(current_chunk)
    return chunks

def cleanup_text(text):
    # Usuń zbędne spacje
    text = re.sub(' +', ' ', text)
    # Usuń daty (format DD-MM-YYYY)
    text = re.sub('\d{2}-\d{2}-\d{4}', '', text)
    return text

def clean_and_edit_file(file_path):
    # Otwórz plik do odczytu z kodowaniem 'utf-8'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Wyczyść tekst
    text = cleanup_text(text)

    # Podziel tekst na chunki
    chunks = split_into_chunks(text, 3000)

    # Wywołaj API dla każdego chunka
    edited_chunks = []
    for chunk in chunks:
        while True:
            try:
                response = openai.Edit.create(
                    model="text-davinci-edit-001",
                    input=chunk,
                    instruction="Ułatw czytelność tego tekstu, użyj formatowania Markdown. (Dla przykładu: dodaj nagłówki, listy, pogrubienia, fragmenty kodu itp.) usuń daty w formacie DD-MM-YYYY.",
                    temperature=1,
                    top_p=1
                )
                edited_chunks.append(response['choices'][0]['text'])
                break
            except Exception as e:
                print(e)
                print("Waiting for 10 seconds before trying again.")
                time.sleep(10)

    # Zapisz wynik do pliku
    with open(f"./done/{os.path.basename(file_path)}", 'w', encoding='utf-8') as file:
        for text in edited_chunks:
            file.write(text)

# Get a list of all files in the 'docs' directory
files = os.listdir('./docs')


# For each file in the directory
for file_name in files:
    # If the file is a text file
    if file_name.endswith('.txt'):
        print(f"Processing {file_name}...")
        # Clean and edit the file
        clean_and_edit_file(f"./docs/{file_name}")
        print(f"Finished processing {file_name}!")
