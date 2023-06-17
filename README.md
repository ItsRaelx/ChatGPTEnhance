## Text Processing with OpenAI GPT-3

This Python script performs automated cleanup and enhancement of text files using OpenAI's GPT-3. 

## Description

The script reads text files from the `./docs` directory, performs necessary cleanup (removal of unnecessary spaces and dates), and enhances readability using OpenAI's GPT-3 model. It splits the text files into chunks and sends them to the GPT-3 model. After processing, it combines the chunks and writes the processed text to a new file in the `./done` directory. If the `./done` directory does not exist, the script will create it.

## Usage

Before running the script, ensure that you have set your OpenAI API key in the `openai.api_key` variable. 

Then, simply run the script with `python main.py`.

This script works with text files (.txt extension) in the `./docs` directory.

After running the script, check the `./done` directory for the processed files.

## Dependencies

This script requires the `openai` Python package. You can install it using pip:

```bash
pip install openai
```

## Notes

This script has been developed to work with utf-8 encoded text files. Other file encodings may not work correctly.

The script uses regex to find and remove dates in the DD-MM-YYYY format. It will not remove dates in other formats.

The OpenAI API has a limit on the maximum size of the text that can be processed in a single API call. Therefore, the script splits the text into chunks of a size that can be processed by the API. After receiving the processed chunks from the API, it combines them to create the processed file.

## Disclaimer

The quality of the processed text depends on the performance of the GPT-3 model. This script merely facilitates the use of the OpenAI GPT-3 API for processing text files.
