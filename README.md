# wifi-SSID-searcher-web-app 
<tr>
    <td align="center"><a href="https://skillicons.dev/" target="_blank"><img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python Skill Light Icon"></a></td>
  </tr>Project for Neishabur Science and Technology Park

![wifi searcher](https://github.com/saeidsaadatigero/wifi-SSID-searcher-web-app/assets/121683582/467e97f2-d421-4b79-87ba-53329a84e304)
## 🚀 Getting Started 

**Requirements**

* Python: 3.10+
* Package manager or container runtime: `pip` or `docker` recommended.
* Run on Docker port:
Your application will be available at http://localhost:8000.
* Run on Django port:
http://127.0.0.1:8000/

  ### ⚙️ Installation
  Connecting to real Wi-Fi networks from a web application is not a common or recommended practice due to security concerns. However, I can guide you on how to display available Wi-Fi networks (SSIDs) using Python and Django. Keep in mind that this will only work on your local development machine, and connecting to Wi-Fi networks will not be possible through a web application in a secure way.

First, you need to install the wifi library:

#### Using `pip`

>
> ```sh
> pip install wifi
> ```

#### Using `django`

>
> ```sh
> pip install django
> ```

#### Using `Terminal`

>
> ```sh
> sudo ifconfig wlan0
> ```

> ```sh
> ip link show
> ```

change altname wlp0s20f3 to views.py

>python manage.py runserver

