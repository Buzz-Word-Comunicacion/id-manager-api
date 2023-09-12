<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/marturojt/id-manager-api">
    <img src="images/logo-ai-id-manager.png" alt="Logo" width="180" height="180">
  </a>

  <h1 align="center">Identity manager API [Fast API]</h1>

  <p align="justify">
    <strong>ID Image Processor API</strong> is a powerful tool designed to streamline and enhance your ID image processing tasks. Leveraging the latest in web technologies, this API is built using FastAPI and employs JWT for secure authentication. With it, you can effortlessly perform two key image processing tasks: background removal from a physical ID photo and face comparison.
    <br />
    <br />
    <a href="https://github.com/marturojt/id-manager-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/marturojt/id-manager-api">View Demo</a> -->
    <!-- · -->
    <a href="https://github.com/marturojt/id-manager-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/marturojt/id-manager-api/issues">Request Feature</a>
  </p>
</div>

<h2>Backgroud removal</h2>

<div>
    <p>
        The Background Removal feature is designed to take a photo of a physical ID and perform two critical tasks:
    </p>
    <ul>
        <li><strong>Background Removal:</strong>It will meticulously remove the background from the input image, leaving you with a clean and isolated image of the physical ID.</li>
        <li><strong>Perspective Correction:</strong>The API will also correct the perspective of the ID, ensuring that the output image is not only background-free but also properly aligned.</li>
    </ul>
    <p>
      This is immensely useful for various applications such as document scanning, fraud prevention, and data extraction from identification documents.
    </p>
</div>

<h2>Face Comparison (Face ID)</h2>

<div>
    <p>
        The Face Comparison functionality enables you to compare two photos and determine whether they belong to the same person.
    </p>
    <ul>
        <li><strong>Face Detection:</strong> The API will first detect and extract faces from both input photos.</li>
        <li><strong>Face Comparison:</strong>After detecting the faces, it will employ sophisticated algorithms to compare the faces and provide you with a percentage indicating the similarity between the two.</li>
    </ul>
    <p>
      This capability can be vital for identity verification, access control, and authentication processes, providing an added layer of security and reliability.
    </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The ID Image Processor API project was created to address the growing need for efficient and reliable image processing tools in today's fast-paced digital world. We recognized the challenges faced by businesses and developers when dealing with physical identification documents and the need for accurate face comparison capabilities.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python.org]][Python-url]
[![Love][LoveBadge]][Python-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

The project is made ready to go, so you only need the following:

- A local python environment
- An instance of MySQL server
- Basic knowledge of Python
- A bit of patience

In the project its a file named config.py.dist, you will need to rename or copy to config.py and fill the file with your MySQL credentials and your JWT configurations.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/marturojt/id-manager-api
   ```

2. Install NPM packages
   Before install the packages create a virtual environment `python -m venv venv_id_manager` and then activate it `venv_id_manager/Scripts/activate`

   Once the virutal environment is active, run the following command to install all the dependencies:
  
   ```sh
   pip install -r pip_requirements.txt
   ```

   IMPORTANT: To use the face-recognition pip package, you will need `dlib` which is not easy to install in a windows environment. This is the oficial documentation, and it is recommended to read it to make it work in windows:
   - [https://github.com/ageitgey/face_recognition/issues/175](https://github.com/ageitgey/face_recognition/issues/175)
  
3. Copy `config.py.dist` to `config.py` and enter your api keys and the database credentials
   ```python
    class DBOptions:
        """
        Database connection options class
        """

        def __init__(self, user: str, password: str, host: str, database: str):
            self.user = user
            self.password = password
            self.host = host
            self.database = database


    # Database connection options definitions
    db_options = DBOptions(
                            user='XXXX YOUR USERNAME XXXX',
                            password='XXXX YOUR PASSWORD XXXX',
                            host='XXXX YOUR HOST XXXX',
                            database='XXXX YOUR DATABASE XXXX'
                            )


    class OptionsKeys:
        """
        Keys used by main script details class
        """

        def __init__(self, secret_jwt: str, algorithm_jwt: str, access_token_expiration: int):
            self.secret_jwt = secret_jwt
            self.algorithm_jwt = algorithm_jwt
            self.access_token_expiration = access_token_expiration


    # Optioons keys
    options_keys = OptionsKeys(
                            secret_jwt='XXXX YOUR SECRET KEY XXXX',
                            algorithm_jwt='HS256',
                            access_token_expiration=5
                            )
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Create a basic fastapi app with authorization via JWT
- [x] Add the ID background removal method
- [x] Add the Face ID (face comparition) method
- [ ] Refactor the code to remove dependencies



See the [open issues](https://github.com/marturojt/id-manager-api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

**Arturo Jiménez:**
 - Twitter => [@_systemctl](https://twitter.com/_systemctl)
 - Mail => okami@freejolitos.com
 - Github => [@marturojt](https://github.com/marturojt)


**Diego Rodríguez:**
 - Twitter => [@diegoderf](https://twitter.com/diegoderf)
 - Mail => diego.rodriguez.ferreira@gmail.com
 - Github => [@derftech](https://github.com/derftech)



### Repo URL
id-manager-api: [https://github.com/marturojt/id-manager-api](https://github.com/marturojt/id-manager-api)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/marturojt/id-manager-api?style=for-the-badge
[contributors-url]: https://github.com/marturojt/id-manager-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/marturojt/id-manager-api?style=for-the-badge
[forks-url]: https://github.com/marturojt/id-manager-api/network/members
[stars-shield]: https://img.shields.io/github/stars/marturojt/id-manager-api?style=for-the-badge
[stars-url]: https://github.com/marturojt/id-manager-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/marturojt/id-manager-api?style=for-the-badge
[issues-url]: https://github.com/marturojt/id-manager-api/issues
[license-shield]: https://img.shields.io/github/license/marturojt/id-manager-api?style=for-the-badge
[license-url]: https://github.com/marturojt/id-manager-api/blob/dev/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/marturojt
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/
[LoveBadge]: https://img.shields.io/static/v1?label=❤️&message=Love&style=for-the-badge&color=red
[Love-url]: https://freejolitos.com