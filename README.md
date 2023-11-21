<!-- Inspired by https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md -->

<a name="readme-top"></a>

<!-- SHIELDS HEADER -->
<div align="center">

[![Current Release][release-shield]][release-url] [![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url] [![LinkedIn][linkedin-shield]][linkedin-url]

![PyPI - Python Version][pypi-python-shield]
![PyPi - Package Version][pypi-version-shield]

[![PyPi - License][pypi-license-shield]][license-url]

[release-shield]:https://img.shields.io/github/release/EJOOSTEROP/crewcal.svg
[release-url]:https://github.com/EJOOSTEROP/crewcal/releases

[contributors-shield]: https://img.shields.io/github/contributors/EJOOSTEROP/crewcal.svg?logo=github
[contributors-url]: https://github.com/EJOOSTEROP/crewcal/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/EJOOSTEROP/crewcal.svg?logo=github
[forks-url]: https://github.com/EJOOSTEROP/crewcal/network/members

[stars-shield]: https://img.shields.io/github/stars/EJOOSTEROP/crewcal.svg?logo=github
[stars-url]: https://github.com/EJOOSTEROP/crewcal/stargazers

[issues-shield]: https://img.shields.io/github/issues/EJOOSTEROP/crewcal.svg?logo=github
[issues-url]: https://github.com/EJOOSTEROP/crewcal/issues

[license-shield]: https://img.shields.io/github/license/EJOOSTEROP/crewcal.svg
[license-url]: https://github.com/EJOOSTEROP/crewcal/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/erik-oosterop-9505a21

[pypi-python-shield]: https://img.shields.io/pypi/pyversions/crewcal?logo=python
[pypi-version-shield]: https://img.shields.io/pypi/v/crewcal?logo=python
[pypi-license-shield]: https://img.shields.io/pypi/l/crewcal?logo=python
</div>


<!-- PROJECT SUMMARY AND LOGO -->
<div align="center">
  <a href="https://github.com/EJOOSTEROP/crewcal">
    <img src="https://github.com/EJOOSTEROP/crewcal/blob/main/etc/logo.png?raw=true" alt="Logo" width="180" height="180">
  </a>

<h3 align="center">crewcal</h3>

  <p align="center">
    Convert an airline crew schedule pdf into iCalendar format using a machine learning Large Language Model.
    <br />
    <a href="https://github.com/EJOOSTEROP/crewcal"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!--
    <a href="https://github.com/EJOOSTEROP/crewcal">View Demo</a>
    ·
    -->
    <a href="https://github.com/EJOOSTEROP/crewcal/issues">Report Bug</a>
    ·
    <a href="https://github.com/EJOOSTEROP/crewcal/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<br />
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
      <!-- <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul> -->
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ABOUT THE PROJECT -->
## About the Project

<div  align="center">
  <a href="https://github.com/EJOOSTEROP/crewcal">
    <img src="https://github.com/EJOOSTEROP/crewcal/blob/main/etc/intro_image.jpg?raw=true" alt="intro_image" width="75%" height="75%">
  </a>
</div>

<div>

  Convert an airline crew schedule pdf into iCalendar format using a machine learning Large Language Model. An LLM (Large Language Model, specifically OpenAI's gpt-3.5-turbo) is used to extract the schedule information. iCalender files are recognized by most calendar systems (iOS, Android, Google, ++) and will create the flights on your phone/device calendar.

  The PDF schedule does not need to follow a very prescribed structured format.

  Development performed mostly using AIMS eCrew pdf schedules.

</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- BUILT WITH -->
<!--
### Built With

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- GETTING STARTED -->
## Getting Started

<!--To get a local copy up and running follow these simple example steps.
-->

### Prerequisites

Obtain an OpenAI API key.

Make this available as an environment variable:
```shell
export OPENAI_API_KEY=YOUR_KEY
```
Alternatively specify the API Key in a .env file.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation
Strongly consider using pipx or a virtual environment depending on your needs.
```shell
pip install crewcal
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
### CLI
To create the calendar file (schedule.ics) from a pdf schedule file (schedule.pdf):
```shell
crewcal extract schedule.pdf schedule.ics
```

`crewcal --help` shows a brief manual page.


### Python Package
The following sript extracts the schedule from `schedule.pdf` and stores the icalendar file in `schedule.ics` file.

```python
from crewcal.llm_extract import OpenAISchedule

sched = OpenAISchedule(schedule_path='schedule.pdf', to_icalendar_file='schedule.ics')
```

The resulting .ics file can be read by most calendar software.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [ ] None (feel free to suggest)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

<!-- Contributions are what make the open source community such an amazing place to learn, inspire, and create. -->
Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also [open](https://github.com/EJOOSTEROP/crewcal/issues/new/choose) a feature request or bug report.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
<!--
## License

Distributed under the MIT License. See `LICENSE.txt` for more information. The tools and the sample data are subject to their own respective licenses.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->


<!-- CONTACT -->
## Contact

<!--
Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com
-->

Project Link: [crewcal](https://github.com/EJOOSTEROP/crewcal)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
<!--
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>

-->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
