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
    "# **Survey Dataset Exploration Lab**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Estimated time needed: **30** minutes\n"
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
    "After completing this lab you will be able to:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "-   Load the dataset that will used thru the capstone project.\n",
    "-   Explore the dataset.\n",
    "-   Get familier with the data types.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Load the dataset\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Import the required libraries.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The dataset is available on the IBM Cloud at the below url.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset_url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load the data available at dataset_url into a dataframe.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Respondent                      MainBranch Hobbyist  \\\n",
      "0           4  I am a developer by profession       No   \n",
      "1           9  I am a developer by profession      Yes   \n",
      "2          13  I am a developer by profession      Yes   \n",
      "3          16  I am a developer by profession      Yes   \n",
      "4          17  I am a developer by profession      Yes   \n",
      "\n",
      "                                         OpenSourcer  \\\n",
      "0                                              Never   \n",
      "1                         Once a month or more often   \n",
      "2  Less than once a month but more than once per ...   \n",
      "3                                              Never   \n",
      "4  Less than once a month but more than once per ...   \n",
      "\n",
      "                                          OpenSource          Employment  \\\n",
      "0  The quality of OSS and closed source software ...  Employed full-time   \n",
      "1  The quality of OSS and closed source software ...  Employed full-time   \n",
      "2  OSS is, on average, of HIGHER quality than pro...  Employed full-time   \n",
      "3  The quality of OSS and closed source software ...  Employed full-time   \n",
      "4  The quality of OSS and closed source software ...  Employed full-time   \n",
      "\n",
      "          Country Student                                            EdLevel  \\\n",
      "0   United States      No           Bachelor’s degree (BA, BS, B.Eng., etc.)   \n",
      "1     New Zealand      No  Some college/university study without earning ...   \n",
      "2   United States      No        Master’s degree (MA, MS, M.Eng., MBA, etc.)   \n",
      "3  United Kingdom      No        Master’s degree (MA, MS, M.Eng., MBA, etc.)   \n",
      "4       Australia      No           Bachelor’s degree (BA, BS, B.Eng., etc.)   \n",
      "\n",
      "                                      UndergradMajor  ...  \\\n",
      "0  Computer science, computer engineering, or sof...  ...   \n",
      "1  Computer science, computer engineering, or sof...  ...   \n",
      "2  Computer science, computer engineering, or sof...  ...   \n",
      "3                                                NaN  ...   \n",
      "4  Computer science, computer engineering, or sof...  ...   \n",
      "\n",
      "                              WelcomeChange  \\\n",
      "0   Just as welcome now as I felt last year   \n",
      "1   Just as welcome now as I felt last year   \n",
      "2  Somewhat more welcome now than last year   \n",
      "3   Just as welcome now as I felt last year   \n",
      "4   Just as welcome now as I felt last year   \n",
      "\n",
      "                                        SONewContent   Age Gender Trans  \\\n",
      "0  Tech articles written by other developers;Indu...  22.0    Man    No   \n",
      "1                                                NaN  23.0    Man    No   \n",
      "2  Tech articles written by other developers;Cour...  28.0    Man    No   \n",
      "3  Tech articles written by other developers;Indu...  26.0    Man    No   \n",
      "4  Tech articles written by other developers;Indu...  29.0    Man    No   \n",
      "\n",
      "                 Sexuality                              Ethnicity Dependents  \\\n",
      "0  Straight / Heterosexual           White or of European descent         No   \n",
      "1                 Bisexual           White or of European descent         No   \n",
      "2  Straight / Heterosexual           White or of European descent        Yes   \n",
      "3  Straight / Heterosexual           White or of European descent         No   \n",
      "4  Straight / Heterosexual  Hispanic or Latino/Latina;Multiracial         No   \n",
      "\n",
      "            SurveyLength                  SurveyEase  \n",
      "0  Appropriate in length                        Easy  \n",
      "1  Appropriate in length  Neither easy nor difficult  \n",
      "2  Appropriate in length                        Easy  \n",
      "3  Appropriate in length  Neither easy nor difficult  \n",
      "4  Appropriate in length                        Easy  \n",
      "\n",
      "[5 rows x 85 columns]\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "\n",
    "import pandas as pd\n",
    "\n",
    "# URL of the dataset\n",
    "dataset_url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv\"\n",
    "\n",
    "# Load the CSV data into a DataFrame\n",
    "df = pd.read_csv(dataset_url)\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Explore the data set\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is a good idea to print the top 5 rows of the dataset to get a feel of how the dataset will look.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the top 5 rows and columns from your dataset.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Top 5 rows of the dataset:\n",
      "   Respondent                      MainBranch Hobbyist  \\\n",
      "0           4  I am a developer by profession       No   \n",
      "1           9  I am a developer by profession      Yes   \n",
      "2          13  I am a developer by profession      Yes   \n",
      "3          16  I am a developer by profession      Yes   \n",
      "4          17  I am a developer by profession      Yes   \n",
      "\n",
      "                                         OpenSourcer  \\\n",
      "0                                              Never   \n",
      "1                         Once a month or more often   \n",
      "2  Less than once a month but more than once per ...   \n",
      "3                                              Never   \n",
      "4  Less than once a month but more than once per ...   \n",
      "\n",
      "                                          OpenSource          Employment  \\\n",
      "0  The quality of OSS and closed source software ...  Employed full-time   \n",
      "1  The quality of OSS and closed source software ...  Employed full-time   \n",
      "2  OSS is, on average, of HIGHER quality than pro...  Employed full-time   \n",
      "3  The quality of OSS and closed source software ...  Employed full-time   \n",
      "4  The quality of OSS and closed source software ...  Employed full-time   \n",
      "\n",
      "          Country Student                                            EdLevel  \\\n",
      "0   United States      No           Bachelor’s degree (BA, BS, B.Eng., etc.)   \n",
      "1     New Zealand      No  Some college/university study without earning ...   \n",
      "2   United States      No        Master’s degree (MA, MS, M.Eng., MBA, etc.)   \n",
      "3  United Kingdom      No        Master’s degree (MA, MS, M.Eng., MBA, etc.)   \n",
      "4       Australia      No           Bachelor’s degree (BA, BS, B.Eng., etc.)   \n",
      "\n",
      "                                      UndergradMajor  ...  \\\n",
      "0  Computer science, computer engineering, or sof...  ...   \n",
      "1  Computer science, computer engineering, or sof...  ...   \n",
      "2  Computer science, computer engineering, or sof...  ...   \n",
      "3                                                NaN  ...   \n",
      "4  Computer science, computer engineering, or sof...  ...   \n",
      "\n",
      "                              WelcomeChange  \\\n",
      "0   Just as welcome now as I felt last year   \n",
      "1   Just as welcome now as I felt last year   \n",
      "2  Somewhat more welcome now than last year   \n",
      "3   Just as welcome now as I felt last year   \n",
      "4   Just as welcome now as I felt last year   \n",
      "\n",
      "                                        SONewContent   Age Gender Trans  \\\n",
      "0  Tech articles written by other developers;Indu...  22.0    Man    No   \n",
      "1                                                NaN  23.0    Man    No   \n",
      "2  Tech articles written by other developers;Cour...  28.0    Man    No   \n",
      "3  Tech articles written by other developers;Indu...  26.0    Man    No   \n",
      "4  Tech articles written by other developers;Indu...  29.0    Man    No   \n",
      "\n",
      "                 Sexuality                              Ethnicity Dependents  \\\n",
      "0  Straight / Heterosexual           White or of European descent         No   \n",
      "1                 Bisexual           White or of European descent         No   \n",
      "2  Straight / Heterosexual           White or of European descent        Yes   \n",
      "3  Straight / Heterosexual           White or of European descent         No   \n",
      "4  Straight / Heterosexual  Hispanic or Latino/Latina;Multiracial         No   \n",
      "\n",
      "            SurveyLength                  SurveyEase  \n",
      "0  Appropriate in length                        Easy  \n",
      "1  Appropriate in length  Neither easy nor difficult  \n",
      "2  Appropriate in length                        Easy  \n",
      "3  Appropriate in length  Neither easy nor difficult  \n",
      "4  Appropriate in length                        Easy  \n",
      "\n",
      "[5 rows x 85 columns]\n",
      "\n",
      "Top 5 columns of the dataset:\n",
      "   Respondent                      MainBranch Hobbyist  \\\n",
      "0           4  I am a developer by profession       No   \n",
      "1           9  I am a developer by profession      Yes   \n",
      "2          13  I am a developer by profession      Yes   \n",
      "3          16  I am a developer by profession      Yes   \n",
      "4          17  I am a developer by profession      Yes   \n",
      "\n",
      "                                         OpenSourcer  \\\n",
      "0                                              Never   \n",
      "1                         Once a month or more often   \n",
      "2  Less than once a month but more than once per ...   \n",
      "3                                              Never   \n",
      "4  Less than once a month but more than once per ...   \n",
      "\n",
      "                                          OpenSource  \n",
      "0  The quality of OSS and closed source software ...  \n",
      "1  The quality of OSS and closed source software ...  \n",
      "2  OSS is, on average, of HIGHER quality than pro...  \n",
      "3  The quality of OSS and closed source software ...  \n",
      "4  The quality of OSS and closed source software ...  \n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "\n",
    "# Display the first 5 rows of the DataFrame\n",
    "print(\"Top 5 rows of the dataset:\")\n",
    "print(df.head())\n",
    "\n",
    "# Display the first 5 columns of the DataFrame\n",
    "print(\"\\nTop 5 columns of the dataset:\")\n",
    "print(df.iloc[:, :5].head())  # Displaying the first 5 columns for the first 5 rows"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Find out the number of rows and columns\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Start by exploring the numbers of rows and columns of data in the dataset.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print the number of rows in the dataset.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of rows in the dataset: 11552\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "\n",
    "# Get the number of rows in the DataFrame\n",
    "num_rows = df.shape[0]\n",
    "\n",
    "# Print the number of rows\n",
    "print(f\"Number of rows in the dataset: {num_rows}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print the number of columns in the dataset.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of columns in the dataset: 85\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "\n",
    "# Get the number of columns in the DataFrame\n",
    "num_columns = df.shape[1]\n",
    "\n",
    "# Print the number of columns\n",
    "print(f\"Number of columns in the dataset: {num_columns}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Identify the data types of each column\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Explore the dataset and identify the data types of each column.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print the datatype of all columns.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data types of all columns:\n",
      "Respondent       int64\n",
      "MainBranch      object\n",
      "Hobbyist        object\n",
      "OpenSourcer     object\n",
      "OpenSource      object\n",
      "                 ...  \n",
      "Sexuality       object\n",
      "Ethnicity       object\n",
      "Dependents      object\n",
      "SurveyLength    object\n",
      "SurveyEase      object\n",
      "Length: 85, dtype: object\n"
     ]
    }
   ],
   "source": [
    "# your code goes here\n",
    "\n",
    "# Print the data types of all columns\n",
    "print(\"Data types of all columns:\")\n",
    "print(df.dtypes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Print the mean age of the survey participants.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# your code goes here\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The dataset is the result of a world wide survey. Print how many unique countries are there in the Country column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# your code goes here"
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
    "| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |\n",
    "| ----------------- | ------- | ----------------- | ---------------------------------- |\n",
    "| 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).\n"
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
