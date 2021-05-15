import csv
import os

from google_drive_downloader import GoogleDriveDownloader as gdd


def normalize_string(string):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in replacements:
        string = string.replace(a, b).replace(a.upper(), b.upper())
    return string.lower()


def check_file(path):
    if os.path.isfile(path):
        return True
    return False


def get_topic(string_topic):
    topics = [
        "Blockchain",
        "Computer Vision",
        "Data Science",
        "Scientific Computing",
        "Artifial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "DevOps",
        "IoT",
        "Web",
        "Python Core",
        "Video Games",
        "Infrastructure",
        "Performance",
        "Community",
        "Other",
    ]

    if string_topic in topics:
        return string_topic
    return "Other"


def fcount(path, map={}):
    count = 0
    for f in os.listdir(path):
        child = os.path.join(path, f)
        if os.path.isdir(child):
            child_count = fcount(child, map)
            count += child_count + 1  # unless include self
    map[path] = count
    return count


def get_country(country):
    choices = [
        "af",
        "ax",
        "al",
        "dz",
        "as",
        "ad",
        "ao",
        "ai",
        "aq",
        "ag",
        "ar",
        "am",
        "aw",
        "au",
        "at",
        "az",
        "bh",
        "bs",
        "bd",
        "bb",
        "by",
        "be",
        "bz",
        "bj",
        "bm",
        "bt",
        "bo",
        "bq",
        "ba",
        "bw",
        "bv",
        "br",
        "io",
        "bn",
        "bg",
        "bf",
        "bi",
        "kh",
        "cm",
        "ca",
        "cv",
        "ky",
        "cf",
        "td",
        "cl",
        "cn",
        "cx",
        "cc",
        "co",
        "km",
        "cg",
        "cd",
        "ck",
        "cr",
        "ci",
        "hr",
        "cu",
        "cw",
        "cy",
        "cz",
        "dk",
        "dj",
        "dm",
        "do",
        "ec",
        "eg",
        "sv",
        "gq",
        "er",
        "ee",
        "et",
        "fk",
        "fo",
        "fj",
        "fi",
        "fr",
        "gf",
        "pf",
        "tf",
        "ga",
        "gm",
        "ge",
        "de",
        "gh",
        "gi",
        "gr",
        "gl",
        "gd",
        "gp",
        "gu",
        "gt",
        "gg",
        "gn",
        "gw",
        "gy",
        "ht",
        "hm",
        "va",
        "hn",
        "hk",
        "hu",
        "is",
        "in",
        "id",
        "ir",
        "iq",
        "ie",
        "im",
        "il",
        "it",
        "jm",
        "jp",
        "je",
        "jo",
        "kz",
        "ke",
        "ki",
        "kp",
        "kr",
        "kw",
        "kg",
        "la",
        "lv",
        "lb",
        "ls",
        "lr",
        "ly",
        "li",
        "lt",
        "lu",
        "mo",
        "mk",
        "mg",
        "mw",
        "my",
        "mv",
        "ml",
        "mt",
        "mh",
        "mq",
        "mr",
        "mu",
        "yt",
        "mx",
        "fm",
        "md",
        "mc",
        "mn",
        "me",
        "ms",
        "ma",
        "mz",
        "mm",
        "na",
        "nr",
        "np",
        "nl",
        "nc",
        "nz",
        "ni",
        "ne",
        "ng",
        "nu",
        "nf",
        "mp",
        "no",
        "om",
        "pk",
        "pw",
        "ps",
        "pa",
        "pg",
        "py",
        "pe",
        "ph",
        "pn",
        "pl",
        "pt",
        "pr",
        "qa",
        "re",
        "ro",
        "ru",
        "rw",
        "bl",
        "sh",
        "kn",
        "lc",
        "mf",
        "pm",
        "vc",
        "ws",
        "sm",
        "st",
        "sa",
        "sn",
        "rs",
        "sc",
        "sl",
        "sg",
        "sx",
        "sk",
        "si",
        "sb",
        "so",
        "za",
        "gs",
        "ss",
        "es",
        "lk",
        "sd",
        "sr",
        "sj",
        "sz",
        "se",
        "ch",
        "sy",
        "tw",
        "tj",
        "tz",
        "th",
        "tl",
        "tg",
        "tk",
        "to",
        "tt",
        "tn",
        "tr",
        "tm",
        "tc",
        "tv",
        "ug",
        "ua",
        "ae",
        "gb",
        "us",
        "um",
        "uy",
        "uz",
        "vu",
        "ve",
        "vn",
        "vg",
        "vi",
        "wf",
        "eh",
        "ye",
        "zm",
        "zw",
    ]

    choice_labels = [
        "Afghanistan",
        "Åland Islands",
        "Albania",
        "Algeria",
        "American Samoa",
        "Andorra",
        "Angola",
        "Anguilla",
        "Antarctica",
        "Antigua and Barbuda",
        "Argentina",
        "Armenia",
        "Aruba",
        "Australia",
        "Austria",
        "Azerbaijan",
        "Bahrain",
        "Bahamas",
        "Bangladesh",
        "Barbados",
        "Belarus",
        "Belgium",
        "Belize",
        "Benin",
        "Bermuda",
        "Bhutan",
        "Bolivia. Plurinational State of",
        "Bonaire. Sint Eustatius and Saba",
        "Bosnia and Herzegovina",
        "Botswana",
        "Bouvet Island",
        "Brazil",
        "British Indian Ocean Territory",
        "Brunei Darussalam",
        "Bulgaria",
        "Burkina Faso",
        "Burundi",
        "Cambodia",
        "Cameroon",
        "Canada",
        "Cape Verde",
        "Cayman Islands",
        "Central African Republic",
        "Chad",
        "Chile",
        "China",
        "Christmas Island",
        "Cocos(Keeling) Islands",
        "Colombia",
        "Comoros",
        "Congo",
        "Congo. the Democratic Republic of the",
        "Cook Islands",
        "Costa Rica",
        "Côte dIvoire",
        "Croatia",
        "Cuba",
        "Curaçao",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Djibouti",
        "Dominica",
        "Dominican Republic",
        "Ecuador",
        "Egypt",
        "El Salvador",
        "Equatorial Guinea",
        "Eritrea",
        "Estonia",
        "Ethiopia",
        "Falkland Islands(Malvinas)",
        "Faroe Islands",
        "Fiji",
        "Finland",
        "France",
        "French Guiana",
        "French Polynesia",
        "French Southern Territories",
        "Gabon",
        "Gambia",
        "Georgia",
        "Germany",
        "Ghana",
        "Gibraltar",
        "Greece",
        "Greenland",
        "Grenada",
        "Guadeloupe",
        "Guam",
        "Guatemala",
        "Guernsey",
        "Guinea",
        "Guinea-Bissau",
        "Guyana",
        "Haiti",
        "Heard Island and McDonald Islands",
        "Holy See(Vatican City State)",
        "Honduras",
        "Hong Kong",
        "Hungary",
        "Iceland",
        "India",
        "Indonesia",
        "Iran. Islamic Republic of",
        "Iraq",
        "Ireland",
        "Isle of Man",
        "Israel",
        "Italy",
        "Jamaica",
        "Japan",
        "Jersey",
        "Jordan",
        "Kazakhstan",
        "Kenya",
        "Kiribati",
        "Korea. Democratic Peoples Republic of",
        "Korea. Republic of",
        "Kuwait",
        "Kyrgyzstan",
        "Lao Peoples Democratic Republic",
        "Latvia",
        "Lebanon",
        "Lesotho",
        "Liberia",
        "Libya",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Macao",
        "Macedonia. the Former Yugoslav Republic of",
        "Madagascar",
        "Malawi",
        "Malaysia",
        "Maldives",
        "Mali",
        "Malta",
        "Marshall Islands",
        "Martinique",
        "Mauritania",
        "Mauritius",
        "Mayotte",
        "Mexico",
        "Micronesia. Federated States of",
        "Moldova. Republic of",
        "Monaco",
        "Mongolia",
        "Montenegro",
        "Montserrat",
        "Morocco",
        "Mozambique",
        "Myanmar",
        "Namibia",
        "Nauru",
        "Nepal",
        "Netherlands",
        "New Caledonia",
        "New Zealand",
        "Nicaragua",
        "Niger",
        "Nigeria",
        "Niue",
        "Norfolk Island",
        "Northern Mariana Islands",
        "Norway",
        "Oman",
        "Pakistan",
        "Palau",
        "Palestine. State of",
        "Panama",
        "Papua New Guinea",
        "Paraguay",
        "Peru",
        "Philippines",
        "Pitcairn",
        "Poland",
        "Portugal",
        "Puerto Rico",
        "Qatar",
        "Réunion",
        "Romania",
        "Russian Federation",
        "Rwanda",
        "Saint Barthélemy",
        "Saint Helena. Ascension and Tristan da Cunha",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Martin(French part)",
        "Saint Pierre and Miquelon",
        "Saint Vincent and the Grenadines",
        "Samoa",
        "San Marino",
        "Sao Tome and Principe",
        "Saudi Arabia",
        "Senegal",
        "Serbia",
        "Seychelles",
        "Sierra Leone",
        "Singapore",
        "Sint Maarten(Dutch part)",
        "Slovakia",
        "Slovenia",
        "Solomon Islands",
        "Somalia",
        "South Africa",
        "South Georgia and the South Sandwich Islands",
        "South Sudan",
        "Spain",
        "Sri Lanka",
        "Sudan",
        "Suriname",
        "Svalbard and Jan Mayen",
        "Swaziland",
        "Sweden",
        "Switzerland",
        "Syrian Arab Republic",
        "Taiwan. Province of China",
        "Tajikistan",
        "Tanzania. United Republic of",
        "Thailand",
        "Timor-Leste",
        "Togo",
        "Tokelau",
        "Tonga",
        "Trinidad and Tobago",
        "Tunisia",
        "Turkey",
        "Turkmenistan",
        "Turks and Caicos Islands",
        "Tuvalu",
        "Uganda",
        "Ukraine",
        "United Arab Emirates",
        "United Kingdom",
        "United States",
        "United States Minor Outlying Islands",
        "Uruguay",
        "Uzbekistan",
        "Vanuatu",
        "Venezuela. Bolivarian Republic of",
        "Viet Nam",
        "Virgin Islands. British",
        "Virgin Islands. U.S.",
        "Wallis and Futuna",
        "Western Sahara",
        "Yemen",
        "Zambia",
        "Zimbabwe",
    ]

    position = 0

    if country in choice_labels:
        for country_label in choice_labels:
            if country_label == country:
                return choices[position]
            position += 1
    return ""


def create_folder(path, username):
    if not os.path.exists(path + username):
        os.makedirs(path + username)


def create_info_file(
    path,
    name,
    country_residence,
    email,
    facebook_handle,
    github_handle,
    information,
    last_name,
    linkedin_handle,
    position_1,
    twitter_handle,
):
    info = """name: {0}
---
country_residence: {1}
---
email: {2}
---
facebook_handle: {3}
---
github_handle: {4}
---
information: {5}
---
last_name: {6}
---
linkedin_handle: {7}
---
position_1: {8}
---
publish: yes
---
twitter_handle: {9}
---
image: profile.png
    """.format(
        name,
        country_residence,
        email,
        facebook_handle,
        github_handle,
        information,
        last_name,
        linkedin_handle,
        position_1,
        twitter_handle,
    )

    file = open(path, "w")
    file.write(info)
    file.close()


def create_talk_file(path, title, authors, description, language, summary, topic, type):
    topic = ", ".join(topic)

    info = """name: {0}
---
authors: {1}
---
description: {2}
---
language: {3}
---
summary: {4}
---
topic: {5}
---
type: {6}
---
    """.format(
        title, authors, description, language, summary, topic, type
    )

    file = open(path, "w")
    file.write(info)
    file.close()


def get_file_id(drive_url):
    url_splitted = drive_url.split("id=")
    return url_splitted[1]


def download_photo(id, path):
    gdd.download_file_from_google_drive(file_id=id, dest_path=path)


def get_username(string_to_search):
    username = ""
    if string_to_search:
        string_splitted = string_to_search.split("/")
        username = string_splitted[len(string_splitted) - 1]
    return username


def get_language(string_language):
    language = {"Spanish / Español": "es", "English / Inglés": "en"}
    return language[string_language]


def process_csv(path, talk_type):
    total_talks = fcount("../content/ponencias") + 1

    with open(path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            # Social Networks
            facebook_handle = get_username(row["Facebook"])
            github_handle = get_username(row["Git"])
            linkedin_handle = get_username(row["Linkedin"])
            twitter_handle = get_username(row["Twitter"])

            name = row["First_name"]
            last_name = row["Last_name"]
            username = (
                normalize_string(name.replace(" ", "-"))
                + "-"
                + normalize_string(last_name.replace(" ", "-"))
            )
            country_residence = get_country(row["Country_residence"])
            email = row["Email"]
            information = row["Biography"]
            position_1 = row["Affiliation"]
            photo_url = row["Photo"]

            create_folder("../content/ponentes/", username)

            # Create Speakers
            create_info_file(
                "../content/ponentes/" + username + "/contents.lr",
                name,
                country_residence,
                email,
                facebook_handle,
                github_handle,
                information,
                last_name,
                linkedin_handle,
                position_1,
                twitter_handle,
            )
            if not check_file("../content/ponentes/" + username + "/profile.png"):
                download_photo(
                    get_file_id(photo_url),
                    "../content/ponentes/" + username + "/profile.png",
                )

            # Create Talks
            create_folder("../content/ponencias/", str(total_talks))
            title = row["Title"]
            description = row["Description"]
            language = get_language(row["Spoken_language"])
            topics_form = row["Tags"].split(", ")
            topics = []

            for topic in topics_form:
                topic = get_topic(topic)

                if topic not in topics:
                    topics.append(topic)

            create_talk_file(
                "../content/ponencias/" + str(total_talks) + "/contents.lr",
                title,
                username,
                description,
                language,
                "",
                topics,
                talk_type,
            )

            total_talks += 1

            line_count += 1
        print("Processed {} lines.".format(line_count))


def main():
    process_csv("./talks.csv", "talk")


if __name__ == "__main__":
    main()
