import requests


class DataStructure:
    title: str = None
    city: str = None
    country_code: str = None
    workplace_type: str = None
    company_name: str = None
    company_url: str = None
    company_size: str = None
    experience_level: str = None
    published_at: str = None
    remote_interview: bool = None
    employment_types: str = None
    skills: str = None
    remote: bool = None

    def __init__(self):
        pass


class JustJoinScrapper:
    def __init__(self, job_name: str):
        self.url = "https://justjoin.it/api/offers"
        self.job_name = job_name

    def __str__(self):
        return self.job_name

    def get_url(self) -> list:
        req = requests.get(self.url)
        data = req.json()
        print(f"Ilosc ogloszen: {len(data)}")
        return data

    def parse_json(self):
        data = self.get_url()
        offer_info = DataStructure()
        for offer in data:
            offer_info.title = offer['title']
            offer_info.city = offer['city']
            offer_info.country_code = offer['country_code']
            offer_info.workplace_type = offer['workplace_type']
            offer_info.company_name = offer['company_name']
            offer_info.company_url = offer['company_url']
            offer_info.company_size = offer['company_size']
            offer_info.experience_level = offer['experience_level']
            offer_info.published_at = offer['published_at']
            offer_info.remote_interview = offer['remote_interview']
            offer_info.employment_types = offer['employment_types']
            offer_info.skills = offer['skills']
            offer_info.remote = offer['remote']

            if self.job_name.lower() in offer_info.title.lower():
                print(offer_info.__dict__)


def main():
    obj = JustJoinScrapper('Big Data')
    print(obj.__str__())
    obj.parse_json()


if __name__ == '__main__':
    main()
