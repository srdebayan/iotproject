Video link: https://www.youtube.com/watch?v=SRvRYIv8SwA&t=211s&ab_channel=DebayanBhattacharya





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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#credentials">Credentials</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

The core objectives of the project include resource monitoring. Through the meticulous analysis of collected data, farmers can optimize resource usage, leading to increased efficiency and reduced operational costs. The system will show the data which is collected through various IOT sensors in a dashboard. The essence of the project is in the fact that how MQTT, Nodered, InfluxDB, and Grafana have been combined to make a data pipeline and show the results graphically.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This project is built with the following technologies.


* [Python](Python-url)
* [Paho-MQTT](Paho-MQTT-url)
* [MQTT](MQTT-url)
* [Node-RED](Node-RED-url)
* [InfluxDB](InfluxDB-url)
* [Grafana](Grafana-url)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is project for Smart Farming Monitoring System using python simulator, mqtt, nodered, influxdb and grafana.

### Prerequisites

Install paho-mqtt in your system: how to install this:
* npm
  ```sh
  pip install paho-mqtt
  ```

### Installation

Instruction for installation of this projectate doesn't rely on any external dependencies or services._

1. Clone the repo
 *nmp
   ```sh
   git clone  https://github.com/srdebayan/iotproject.git
   ```
3. Docker compose up: go to the terminal, (having docker demon turned on)
*nmp
```sh
  docker-compose up
```
4. Grafana dashboard: dashboard "farming_dashboard"
*nmp
   ```sh
   localhost:3000
   ```
6. Influxdb:
*nmp
  ```sh
   localhost:8086
  ```
6. Nodered:
*nmp
    ```sh
   localhost:1880
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Usage of this project is described in the documentation mentioned here,please refer to the [Documentation](/docs.google.com/document/d/1OEeDvpzonv0mm_RzSJyPqbeKO3b86FiS9NGWq9lIYKY/edit?usp=sharing )_

<p align="right">(<a href="#readme-top">back to top</a>)</p>












<!-- CONTACT -->
## Contact

Your Name - [@kabta](https://github.com/kabta]) - kabitaad85@gmail.com
Your Name - [@srdebayan](https://github.com/srdebayan) - srdebayan@gmail.com


<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- Credentials -->
## Credentials
Influxdb token: Ga4G4JVwcf2-5ERDGp_rMiwA1PWQv14y7IjLSzGzrVlR15Cad-uhsmRbInJXuTPhRUDFCVnEDllb4x9ghi9tEw==


1. Influxdb
 ```sh
  Influxdb username: admin 
  Influxdb password: admin123
  Influxdb bucket: iot
  Influxdb organization: univaq
```
2. Grafana
```sh
grafana username: admin 
grafana password: admin123
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>




