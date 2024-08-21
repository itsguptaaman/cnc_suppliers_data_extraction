# Aerospace CNC Manufacturing Supplier Data

This repository contains data extracted from various sources to support the analysis of CNC manufacturing suppliers specializing in aerospace parts. The data includes detailed information on each supplier, such as their location, description, and social media links, as well as additional contact details for certain suppliers.

## Table of Contents
- [Dataset Overview](#dataset-overview)
- [Data Structure](#data-structure)
- [Sources](#sources)
- [Data Preparation](#data-preparation)
- [Usage](#usage)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Dataset Overview
The dataset consists of supplier information relevant to aerospace CNC manufacturing. It was collected to analyze the capabilities of suppliers in this field, including their experience, certifications, and specializations.

## Data Structure
The dataset is structured as a JSON file with the following fields:

### Supplier Data Fields:
- **Supplier Name**: The name of the supplier.
- **Supplier Link**: The URL to the supplier's website or profile.
- **Location**: The location of the supplier (City, State).
- **Description**: A brief description of the supplier and their capabilities.
- **Social Media Links**: A list of social media links associated with the supplier.
- **Phone Number**: Contact phone number of the supplier (if available).
- **Company Profile Link**: Additional company profile link (if available).

### Sample Entry:
```json
{
    "Supplier Name": "Aaero Swiss",
    "supplier_link": "https://aaeroswiss.com/",
    "Location": "Anaheim, CA",
    "phone_number": "714-575-8990",
    "Description": "Aaero Swiss supplies precision CNC machining services with a quick turn-around for high or low volume orders in the Los Angeles, California area. Our dedicated and skilled employees are backed by their many years of combined CNC machining experience. We are well-known for our innovation in medical components machining and for our equipment being the cutting edge and top of the line.",
    "company_profile_link": "https://www.iqsdirectory.com/profile/aaero-swiss-54206/",
    "social_media_links": [
        "https://www.linkedin.com/company/1factory/",
        "https://twitter.com/1factoryinc?lang=en",
        "https://www.instagram.com/5thaxis/",
        "https://www.youtube.com/@1factory"
    ]
}
```

## Data Preparation
The dataset has been manually curated, with data extracted from various web sources. Any missing or incomplete fields were left as null. The data has been stored in a JSON format to allow for easy parsing and analysis.

**Note**:
This dataset does not include standardization or preprocessing steps. It is recommended to perform data cleaning and standardization before analysis, especially for fields such as location, phone numbers, and descriptions.

## Usage
The dataset is intended for use in analyzing aerospace CNC manufacturing suppliers, including but not limited to:

- Supplier cohort analysis based on capabilities and certifications.
- Geographic distribution analysis of suppliers.
- Social media presence analysis.

## Limitations
- **Data Completeness**: Some suppliers may have incomplete information due to limitations in available data.
- **Manual Entry**: The data was manually curated, so there may be human errors in data entry.
- **Standardization**: The data is not standardized; for example, location and phone number formats may vary.

## Contributing
If you find any errors in the data or would like to contribute additional supplier information, please feel free to submit a pull request or open an issue.
