"""
    scrape LinkedIn profile information
"""

import os
import requests  # requests api from LinkedIn
from dotenv import load_dotenv


load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape LinkedIn profile information
    :param linkedin_profile_url:
    :param mock:
    :return:
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_key = os.environ.get("PROXY_CURL_API_KEY")
        headers = {"Authorization": "Bearer " + api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": "https://www.linkedin.com/in/johnrmarty/",
        }
        response = requests.get(api_endpoint, params=params, headers=headers)
    data = response.json()
    return data


if __name__ == "__main__":
    # https://www.linkedin.com/in/david-do-a240262b5/
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/johnrmarty/",
            mock=True,
        )
    )


