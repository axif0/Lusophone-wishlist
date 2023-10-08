# Wikimedia Initial Tasks

This repository contains solutions for two tasks for the [Wikimedia projects](https://phabricator.wikimedia.org/T347259).

## Task 1: [Display Article Creation Dates](https://phabricator.wikimedia.org/T347737)

### Description

The HTML file in this project displays information about articles from a dataset. It uses JavaScript to iterate over the dataset and create paragraphs with the article details, such as the title, page ID, and creation date.

### Usage

To view the results, open the `index.html` file in a web browser. The article details will be displayed in a section with the ID "results".

### Dataset

The dataset used in this project is stored in the JavaScript variable `data`. It is an array of objects, where each object represents an article and contains the following properties:

- `page_id`: The ID of the page.
- `creation_date`: The creation date of the article in the format "YYYY-MM-DD".
- `title`: The title of the article.

## Task 2: [Check Status Codes of URLs](https://phabricator.wikimedia.org/T347784)

### Description

The Python script in this project reads a list of URLs from a CSV file and checks the status codes of each URL using concurrent requests. It saves the results to a text file.

### Usage

To run the script, make sure you have Python installed. Then, execute the following command in the terminal:

`python main.py`


The status code results will be saved to the file `output.txt`.

### CSV File

The CSV file containing the URLs is specified in the `csv_file` variable in the Python script. Make sure to provide a valid path to the CSV file.

## License

This project is licensed under the terms of the MIT license.
