{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\"  />\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Hands-on Lab : Web Scraping**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Estimated time needed: **30 to 45** minutes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Objectives\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this lab you will perform the following:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* Extract information from a given web site \n",
    "* Write the scraped data into a csv file.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Extract information from the given web site\n",
    "You will extract the data from the below web site: <br> \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#this url contains the data you need to scrape\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Import the required libraries\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Your code here\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Download the webpage at the url\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Webpage downloaded and saved as 'Programming_Languages.html'\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# URL of the HTML file\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Check if the request was successful\n",
    "if response.status_code == 200:\n",
    "    # Save the content to an HTML file\n",
    "    with open('Programming_Languages.html', 'wb') as file:\n",
    "        file.write(response.content)\n",
    "    print(\"Webpage downloaded and saved as 'Programming_Languages.html'\")\n",
    "else:\n",
    "    print(f\"Failed to download the webpage. Status code: {response.status_code}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a soup object\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<html lang=\"en\">\n",
      " <head>\n",
      "  <title>\n",
      "   Salary survey results of programming languages\n",
      "  </title>\n",
      "  <style>\n",
      "   table, th, td {\n",
      "  border: 1px solid black;\n",
      "}\n",
      "  </style>\n",
      " </head>\n",
      " <body>\n",
      "  <hr/>\n",
      "  <h2>\n",
      "   Popular Programming Languages\n",
      "  </h2>\n",
      "  <hr/>\n",
      "  <p>\n",
      "   Finding out which is the best language is a tough task. A programming language is created to solve a specific problem. A language which is good for task A may not be able to properly handle task B. Comparing programming language \n"
     ]
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# Path to the downloaded HTML file\n",
    "file_path = 'Programming_Languages.html'\n",
    "\n",
    "# Read the content of the HTML file\n",
    "with open(file_path, 'r', encoding='utf-8') as file:\n",
    "    html_content = file.read()\n",
    "\n",
    "# Create a BeautifulSoup object\n",
    "soup = BeautifulSoup(html_content, 'html.parser')\n",
    "\n",
    "# Print the first 500 characters of the parsed HTML to verify\n",
    "print(soup.prettify()[:500])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Scrape the `Language name` and `annual average salary`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data saved to 'github-job-postings.xlsx'\n"
     ]
    }
   ],
   "source": [
    "#your code goes here\n",
    "\n",
    "# Find the table in the HTML\n",
    "table = soup.find('table')\n",
    "\n",
    "# Extract headers and rows from the table\n",
    "headers = [header.text.strip() for header in table.find_all('th')]\n",
    "rows = table.find_all('tr')\n",
    "\n",
    "# Extract the data from each row\n",
    "data = []\n",
    "for row in rows[1:]:  # Skip the header row\n",
    "    cells = row.find_all('td')\n",
    "    if len(cells) > 1:\n",
    "        language = cells[0].text.strip()\n",
    "        salary = cells[1].text.strip()\n",
    "        data.append([language, salary])\n",
    "\n",
    "# Create a DataFrame from the extracted data\n",
    "df = pd.DataFrame(data, columns=['Programming Language', 'Average Annual Salary'])\n",
    "\n",
    "# Save the DataFrame to an Excel file\n",
    "df.to_excel('github-job-postings.xlsx', index=False)\n",
    "\n",
    "print(\"Data saved to 'github-job-postings.xlsx'\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Save the scrapped data into a file named *popular-languages.csv*\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data saved to 'popular-languages.csv'\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "\n",
    "# Save the DataFrame to a CSV file\n",
    "df.to_csv('popular-languages.csv', index=False)\n",
    "\n",
    "print(\"Data saved to 'popular-languages.csv'\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Authors\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Ramesh Sannareddy\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Other Contributors\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Rav Ahuja\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change Log\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "|  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |\n",
    "|---|---|---|---|\n",
    "| 2020-10-17  | 0.1  | Ramesh Sannareddy  |  Created initial version of the lab |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Copyright &copy; 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01).\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python",
   "language": "python",
   "name": "conda-env-python-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
